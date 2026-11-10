# Skils — Biblioteca de Skills Jurídicas para Produtos Digitais

Conjunto modular de **7 skills de Agent Skills** para orientar auditorias técnicas e jurídicas de sites, lojas, SaaS e aplicativos direcionados ao Brasil. Baseado nas áreas de verificação do projeto de referência [Kazualkun/Blindagemjuridica](https://github.com/Kazualkun/Blindagemjuridica), licenciado sob MIT.

> **Atenção:** Estas skills são ferramentas de triagem técnica, **não** emitem parecer jurídico, não comprovam conformidade e não substituem revisão por profissional habilitado. Verifique a versão vigente de normas e orientações oficiais. O scanner é heurístico e pode ter falsos positivos/negativos.

## Skills disponíveis

| Skill | Objetivo | Gatilhos usuais |
| --- | --- | --- |
| `auditoria-juridica-br` | Auditoria integral, triagem por evidência e plano de correções | auditar site, LGPD, riscos legais, conformidade |
| `lgpd-privacidade` | Inventário de dados, bases legais, transparência, direitos dos titulares | política de privacidade, mapa de dados, LGPD |
| `cookies-rastreamento` | Inventário de tags, consentimento e revogação | banner de cookies, GTM, Meta Pixel, GA4 |
| `consumidor-cdc` | Checkout, ofertas, cancelamento, reembolso e termos | e-commerce, assinaturas, direito de arrependimento |
| `acessibilidade-digital` | Testes de acessibilidade técnica e experiência inclusiva | WCAG, teclado, contraste, alt, formulários |
| `publicidade-direitos-autorais` | Alegações, provas, depoimentos e licenças de ativos | publicidade, testimonials, imagens, licenças |
| `checklist-pre-lancamento` | Gate de publicação orientado a riscos e bloqueadores | homologação, go-live, revisão final |

## Estrutura

```text
skils/
├── skills/
│   └── <nome-da-skill>/SKILL.md
├── scripts/scan.py          # triagem local; sem dependências externas
├── templates/relatorio.md  # formato de entrega da auditoria
├── docs/INSTALACAO.md
├── docs/METODOLOGIA.md
├── docs/FONTES-OFICIAIS.md
├── tests/
├── .github/workflows/testes.yml
├── NOTICE.md
└── LICENSE
```

## Instalação e uso

Para Claude Code, copie a pasta desejada de `skills/` para `.claude/skills/` no seu projeto ou para `~/.claude/skills/` no seu ambiente. Veja [INSTALACAO](docs/INSTALACAO.md) para comandos.

Solicite em linguagem natural: **"Audite minha aplicação para LGPD e CDC; apresente evidências e faça alterações somente após aprovação"**. Comece pela skill `auditoria-juridica-br`; ela direciona as demais por necessidade.

### Scanner local (triagem)

Requisito: **Python 3.9+**, biblioteca padrão.

```bash
python scripts/scan.py /caminho/do/site --format md
python scripts/scan.py /caminho/do/site --format json --saida achados.json
python -m unittest discover -s tests -v
```

Nenhum arquivo do projeto é enviado a serviços externos pelo scanner. Arquivos encontrados são lidos localmente e trechos de código são resumidos em achados. **Não cole relatórios com dados pessoais ou segredos em chats públicos.**

## Fluxo operacional

1. Ler o código e inventariar rotas, formulários, integrações e documentos existentes.
2. Executar scanner e validar cada achado manualmente.
3. Registrar a evidência como `arquivo:linha`, com severidade, escopo e hipótese normativa.
4. Buscar a fonte oficial vigente e distinguir obrigação, recomendação e questão dependente do negócio.
5. Propor correções técnicas preservando comportamento; pedir aprovação para alterações de conteúdo de negócio.
6. Executar testes/build conforme a stack e registrar limitações, pendências e validação profissional.

## Créditos e licença

Este pacote é uma **organização original de skills e ferramentas de triagem**, inspirada no escopo de [Blindagem Jurídica](https://github.com/Kazualkun/Blindagemjuridica) (MIT). Não se declara versão oficial nem afiliada ao projeto de origem. Consulte [NOTICE.md](NOTICE.md) e [LICENSE](LICENSE). Contribuições e correções são bem-vindas.
