---
name: checklist-pre-lancamento
description: Organizar homologação de riscos jurídicos e técnicos antes de publicar sites, apps, lojas e SaaS no Brasil. Use em go-live, checklist de publicação, readiness, deploy final ou aprovação de release.
---

# Checklist de pré-lançamento

## Procedimento

1. Registrar versão/commit, ambiente, rotas públicas, donos de processos e data de publicação.
2. Consolidar auditorias temáticas de LGPD, cookies, CDC, acessibilidade, publicidade e direitos autorais, referenciando evidências.
3. Rodar testes automatizados e smoke de rotas; homologar rede e consentimento, cadastro, exclusão de conta, compra/cancelamento simulado e acessibilidade do fluxo crítico.
4. Classificar achados em **bloqueador confirmado**, **pendência que exige aceite responsável** e **melhoria planejada**.
5. Não aprovar automaticamente deploy regulado nem atestar conformidade legal; exigir revisão humana para lacunas materiais e contratos.
6. Criar plano de rollback, responsáveis por incidentes e checklist de publicação pós-deploy, sem armazenar segredos.

## Saída

Tabela de gates (resultado e evidência), riscos aceitos expressamente, impedimentos, testes concluídos/não executados e decisão de publicação atribuída ao responsável humano.
