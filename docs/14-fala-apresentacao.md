# 14 — Apresentação oral: use o caso C-001 como fio condutor

A gravação da Fase 01 deve demonstrar **a compreensão do problema e das escolhas técnicas**, não exibir um aplicativo pronto. Em vez de uma fala genérica, use o caso [CQ-2026-001](16-estudo-de-caso.md): uma carga fictícia chega com referência documental pendente e não pode ser liberada.

O roteiro principal desta versão é [Guia de vídeo — problema real e 8 minutos](../apresentacao/GUIA_VIDEO_CASO_REAL.md), que distribui o tempo e indica quais arquivos mostrar na tela.

## Cinco pontos que você precisa conseguir explicar sem ler

1. O que o [Porto Sem Papel](17-fontes-e-evidencias.md) já faz e por que QuimiPort **não o substitui**.
2. Por que a hipótese de pré-conferência é relevante, mas ainda **não foi validada em campo**.
3. Por que `CargaQuimica` é a raiz de agregado e por que `DocumentoCarga` não decide sozinho a liberação.
4. Por que `BLOQUEADA` não vai para `EM_MOVIMENTACAO` e o que acontece após parecer favorável de inspeção.
5. Como RN07 vira um caso de teste verificável e em que camada a regra será protegida.

**Ponto importante de autoria:** qualquer afirmação no vídeo sobre o que “eu desenvolvi” deve corresponder ao que você consegue reproduzir e justificar. Não diga que entrevistou operador, implementou sistema em porto ou mediu resultados; isso não ocorreu.
