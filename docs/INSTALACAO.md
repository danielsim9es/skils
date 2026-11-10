# Instalação e execução

## Claude Code — por projeto

Copie uma ou mais pastas de `skills/` para `.claude/skills/` na raiz do repositório onde deseja auditar:

```bash
mkdir -p .claude/skills
cp -R /caminho/skils/skills/* .claude/skills/
```

No Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force .claude/skills | Out-Null
Copy-Item -Recurse "C:\caminho\skils\skills\*" ".claude\skills\"
```

## Claude Code — instalação pessoal

Copie as pastas de `skills/` para `~/.claude/skills/`. Reinicie a sessão se seu agente não recarregar automaticamente. Invoque `/auditoria-juridica-br` (ou peça auditoria em linguagem natural, conforme suporte do cliente).

## Outras ferramentas compatíveis com Agent Skills

A estrutura usa a convenção `nome/SKILL.md` com frontmatter YAML. Cada cliente pode exigir um local de instalação diferente. Consulte a documentação da ferramenta; não é garantido que todo ambiente ofereça invocação por `/` ou acesso automático a outras skills.

## Scanner

```bash
python scripts/scan.py . --format md
python scripts/scan.py . --format json --saida /tmp/achados.json
python -m unittest discover -s tests -v
```

O scanner **não deve** operar com permissões irrestritas sobre segredos, nem exibir `.env`. Ele é um recurso de triagem, não um laudo de compliance ou teste dinâmico de consentimento.
