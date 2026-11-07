# 14 — Texto-base para ensaio

Este roteiro é um material de estudo; deve ser explicado com palavras próprias e de acordo com a modelagem documentada.

## Abertura

Apresento o QuimiPort, uma proposta técnica e arquitetural para gestão de cargas químicas em contexto portuário inspirado no Porto de Santos. Na Fase 01, o foco é DDD, regras, TypeScript, arquitetura e qualidade, não a entrega do sistema full stack funcionando.

## Problema e atores

O registro descentralizado dificulta verificar identificação do produto, risco, documentos, inspeções, motivo de decisões e histórico. Os usuários previstos incluem operador, analista documental, inspetor, responsável técnico, gestor e administrador.

## DDD

O agregado central é `CargaQuimica`, responsável por controlar consistência entre produto, quantidade, documentos, inspeção, status e histórico. `ProdutoQuimico` pertence a um catálogo independente. Objetos de valor como `QuantidadePositiva` e `ClassificacaoRisco` evitam valores inválidos.

## Regras e transições

Uma carga precisa de produto ativo, classe de risco, quantidade positiva e responsável técnico. Para liberar, é necessário atender à política documental e às inspeções aplicáveis. Estados como `BLOQUEADA` e `CANCELADA` impedem movimentação ou liberação indevida. A máquina de estados formaliza as transições.

## Arquitetura e qualidade

Propomos monólito modular com apresentação, aplicação, domínio e infraestrutura. O domínio não conhece HTTP ou SQL. TypeScript ajuda a modelar contratos e estados. Testes unitários e de aplicação verificariam condições críticas com repositórios simulados, e testes de integração seriam acrescentados em fases futuras.

## Próximas fases

O plano prevê núcleo TypeScript, backend, banco, frontend, autenticação, auditoria e, separadamente, uma integração industrial opcional. As políticas legais e operacionais reais exigem levantamento com profissionais habilitados.
