---
name: auditoria-juridica-br
description: Auditar tecnicamente sites, SaaS, lojas e aplicativos brasileiros quanto a riscos jurídicos (LGPD, CDC, cookies, acessibilidade, publicidade e direitos autorais). Ative em pedidos de auditoria jurídica de produto digital, revisar site antes de publicar, blindagem jurídica ou adequação legal.
---

# Auditoria jurídica brasileira — orquestrador

## Objetivo

Produzir auditoria **baseada em código e evidência**, coordenando as skills temáticas desta biblioteca. Não promete ausência de multas, processo ou conformidade integral. Não presta consultoria jurídica individual.

## Entradas

- Raiz do projeto e branch/commit; tipo de negócio; público e jurisdição; ambiente de teste.
- Stack, fluxos de cadastro e pagamento, fornecedores de dados e rastreamento.
- Informações confirmadas pela empresa, jamais presumidas.

## Processo obrigatório

1. Identificar stack, rotas, formulários, SDKs, banco, checkout, armazenamento, autenticação e políticas existentes.
2. Executar `python scripts/scan.py <raiz> --format md` **se** o scanner do pacote estiver disponível. O resultado é só triagem.
3. Escolher as skills específicas: `lgpd-privacidade`, `cookies-rastreamento`, `consumidor-cdc`, `acessibilidade-digital`, `publicidade-direitos-autorais`.
4. Confirmar cada achado em código, teste ou comportamento observado. Registrar `arquivo:linha`; separar **indício** de **não conformidade confirmada**.
5. Validar artigos, obrigações e normas em fontes oficiais atuais (`docs/FONTES-OFICIAIS.md` se disponível); especificar hipóteses e ressalvas.
6. Propor correções de menor risco. Solicitar aprovação para mudar preços, textos comerciais, dados coletados, depoimentos, licenças ou lógica de negócio.
7. Se alterações forem autorizadas, aplicar incrementos pequenos, executar testes/build e relatar o que NÃO foi testado.
8. Entregar `AUDITORIA-JURIDICA.md` usando o modelo `templates/relatorio.md` ou estrutura equivalente.

## Critérios mínimos

- Revisar inventário e transparência de dados, gestão de cookies, consumo e cancelamento, acessibilidade, alegações publicitárias, imagens e termos de licenças.
- Proteger credenciais e dados reais; não expor segredos no relatório.
- Nunca criar CNPJ, bases legais, prazos de exclusão, testemunhos ou licenças fictícias.
- Se houver pagamentos, menores ou setores regulados, elevar necessidade de revisão profissional.

## Saída

Resumo executivo, achados com severidade e evidência, mapa de dados, correções técnicas realizadas, itens pendentes de decisão, testes e recomendação de revisão jurídica profissional para alto risco.
