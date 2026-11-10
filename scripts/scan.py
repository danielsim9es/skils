#!/usr/bin/env python3
"""Local static heuristic triage for Brazilian digital-product compliance.

No external network requests or third-party dependencies. Findings are clues,
NOT legal conclusions; review code and behavior manually before reporting.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

EXTENSIONS = {'.html', '.htm', '.js', '.jsx', '.ts', '.tsx', '.vue', '.svelte', '.astro', '.php', '.liquid'}
IGNORED_DIRS = {'node_modules', '.git', '.next', 'dist', 'build', 'coverage', '.venv', 'venv', '__pycache__', '.turbo', '.cache', 'vendor'}
MAX_FILE_SIZE = 400_000

# Each finding is a REASON TO CHECK, not an automatic violation.
RULES = [
    ('rastreador-encontrado', 'cookies-rastreamento', 'medio',
     r'(?:googletagmanager\.com|google-analytics\.com|connect\.facebook\.net|static\.hotjar\.com|clarity\.ms|analytics\.tiktok\.com)',
     'Rastreador identificado; verificar finalidade, base legal e ativação antes da escolha de cookies, quando aplicável.'),
    ('consentimento-tacito', 'cookies-rastreamento', 'medio',
     r'(?:ao continuar navegando|continuar (?:a )?navega[çc][ãa]o).{0,85}(?:cookies|consent|aceita)',
     'Texto sugere consentimento por continuidade; revisar mecanismo e transparência com a fonte oficial vigente.'),
    ('checkbox-pre-marcado', 'lgpd-privacidade', 'medio',
     r'<input\b(?=[^>]*\btype\s*=\s*[\"\']?checkbox)(?=[^>]*\bchecked(?:\s|=|\b))[^>]*>',
     'Checkbox pré-selecionado; confirmar finalidade e se consentimento específico é exigido.'),
    ('campo-cpf', 'lgpd-privacidade', 'baixo',
     r'(?:name|id)\s*=\s*[\"\']?cpf\b',
     'Campo CPF detectado; confirmar necessidade, finalidade, segurança e informação ao titular.'),
    ('imagem-sem-alt', 'acessibilidade-digital', 'medio',
     r'<img\b(?![^>]*\balt\s*=)[^>]*>',
     'Imagem sem atributo alt nesta marcação; verificar finalidade e alternativa textual.'),
    ('div-clicavel', 'acessibilidade-digital', 'medio',
     r'<div\b(?=[^>]*(?:onClick|onclick)\s*=)[^>]*>',
     'Elemento div com clique; verificar teclado, semântica, foco e interações acessíveis.'),
    ('zoom-desabilitado', 'acessibilidade-digital', 'medio',
     r'user-scalable\s*=\s*(?:no|0)|maximum-scale\s*=\s*1(?:\.0)?\b',
     'Indício de restrição de zoom; testar ampliação e reflow.'),
    ('promessa-forte', 'publicidade-direitos-autorais', 'medio',
     r'(?:resultado garantido|lucro garantido|cura garantida|100\s*%\s*(?:de )?garantia de resultado)',
     'Promessa objetiva identificada; exigir base probatória antes de uso publicitário.'),
    ('contador-aleatorio', 'publicidade-direitos-autorais', 'baixo',
     r'Math\.random\(\)',
     'Uso de aleatoriedade; verificar se afeta contadores, reviews, estoque ou escassez exibidos ao público.'),
]

def collect_files(base: Path):
    if base.is_file():
        if base.suffix.lower() in EXTENSIONS and base.stat().st_size <= MAX_FILE_SIZE:
            yield base
        return
    for folder, subdirs, files in __import__('os').walk(base):
        subdirs[:] = sorted(d for d in subdirs if d not in IGNORED_DIRS and not d.startswith('.'))
        for name in sorted(files):
            f = Path(folder) / name
            if f.suffix.lower() in EXTENSIONS and not f.is_symlink():
                try:
                    if f.stat().st_size <= MAX_FILE_SIZE:
                        yield f
                except OSError:
                    continue

def scan(base: Path) -> dict:
    if not base.exists():
        raise FileNotFoundError(f'Caminho não encontrado: {base}')
    findings = []
    files_scanned = 0
    for path in collect_files(base):
        try:
            content = path.read_text(encoding='utf-8', errors='replace')
        except OSError:
            continue
        files_scanned += 1
        try:
            rel = str(path.relative_to(base)) if base.is_dir() else path.name
        except ValueError:
            rel = path.name
        rel = rel.replace('\\', '/')
        for code, area, severity, expression, explanation in RULES:
            for match in re.finditer(expression, content, flags=re.IGNORECASE | re.DOTALL):
                line = content.count('\n', 0, match.start()) + 1
                findings.append({
                    'id': code,
                    'area': area,
                    'severity': severity,
                    'status': 'indicio',
                    'file': rel,
                    'line': line,
                    'location': f'{rel}:{line}',
                    'message': explanation,
                })
                # One indication per category and file is enough for initial triage.
                # Avoid thousands of reports on sites with recurring components.
                break
    findings.sort(key=lambda f: (f['file'], f['line'], f['id']))
    return {
        'tool': 'Skils static triage',
        'result': 'Indicadores técnicos. Não comprova infração legal nem conformidade.',
        'files_scanned': files_scanned,
        'finding_count': len(findings),
        'by_area': dict(sorted(Counter(f['area'] for f in findings).items())),
        'findings': findings,
    }

def to_markdown(data: dict) -> str:
    lines = [
        '# Triagem técnica — Skils', '',
        '> Indícios heurísticos; conferir manualmente. Não é parecer jurídico.', '',
        f"**Arquivos examinados:** {data['files_scanned']}  ",
        f"**Indícios:** {data['finding_count']}", '',
    ]
    if not data['findings']:
        lines.append('Nenhum indício encontrado pelas regras implementadas. Isto NÃO confirma conformidade.')
    for item in data['findings']:
        lines.extend([f"## {item['id']} — {item['location']}",
                      f"- Área: `{item['area']}` · Gravidade sugerida: `{item['severity']}` · Estado: **indício**",
                      f"- {item['message']}", ''])
    return '\n'.join(lines).rstrip() + '\n'

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description='Triagem local de riscos em produtos digitais brasileiros')
    ap.add_argument('path', type=Path, help='Diretório ou arquivo do projeto a analisar')
    ap.add_argument('--format', choices=['md', 'json'], default='md')
    ap.add_argument('--saida', type=Path, help='Gravar relatório neste arquivo')
    args = ap.parse_args(argv)
    try:
        result = scan(args.path)
        output = json.dumps(result, ensure_ascii=False, indent=2) + '\n' if args.format == 'json' else to_markdown(result)
        if args.saida:
            args.saida.parent.mkdir(parents=True, exist_ok=True)
            args.saida.write_text(output, encoding='utf-8')
        else:
            print(output, end='')
        return 0
    except (OSError, ValueError) as exc:
        print(f'Erro: {exc}', file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
