---
name: cookies-rastreamento
description: Revisar tags e pixels em sites, Google Tag Manager, GA4, Meta Pixel, Clarity, Hotjar e banners de cookies, conferindo carga prévia, opções do usuário e revogação. Use em auditoria de cookies, rastreamento, consentimento e privacidade web.
---

# Auditoria de cookies e rastreamento

## Procedimento

1. Localizar scripts em HTML/JS/TS, tags do GTM, iframes, SDKs de anúncios, cookies, localStorage e ferramentas de analytics.
2. Construir inventário com **fornecedor**, **nome/função**, **finalidade**, **categoria proposta**, **origem**, **quando executa** e **base legal a confirmar**.
3. Testar com navegador **limpo**: antes da escolha, após rejeitar, após aceitar e após revogar. Observar rede, storage, cookies, pixels e iframes.
4. Conferir se a interface apresenta escolhas adequadas, opção clara de rejeitar quando aplicável, ausência de coerção e acesso posterior a preferências.
5. Examinar integrações com Consent Mode, CMP e carregamento dinâmico. Inspecionar a rede real; mera presença de um banner **não demonstra bloqueio**.
6. Não classificar automaticamente cookies estritamente necessários como sujeitos a consentimento; finalidade, base legal e orientações ANPD exigem análise contextual.
7. Se os testes de rede não forem possíveis, marcar como **não verificado** e solicitar homologação em ambiente publicado.

## Entrega

Tabela de rastreadores, sequência real de execução, achados `arquivo:linha` e roteiro de teste com resultados. Propor correções de código sem alterar campanhas e escolhas comerciais sem autorização.
