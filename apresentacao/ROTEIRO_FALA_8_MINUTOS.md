# Roteiro de fala — cerca de 8 minutos

**Importante:** use como guia e explique com suas palavras; ajuste após cronometrar a gravação.

## Slide 1 — Abertura e objetivo (0:00–0:30)

Meu projeto é o QuimiPort, uma proposta técnica para gestão de cargas químicas portuárias, inspirada no Porto de Santos. Nesta fase o foco é documentação, DDD, arquitetura, TypeScript e qualidade.

## Slide 2 — Contexto e problema (0:30–1:15)

O cenário envolve dados dispersos sobre produto, risco, documentos, inspeções e autorizações. O QuimiPort busca centralizar informações e rastrear decisões sem presumir critérios regulamentares não fornecidos.

## Slide 3 — Usuários e linguagem (1:15–2:00)

Os atores são operador, analista documental, inspetor, responsável técnico, gestor e administrador. Definimos termos comuns: carga, produto, bloqueio, liberação, movimentação e histórico.

## Slide 4 — Modelagem DDD (2:00–3:10)

A entidade principal e raiz de agregado é CargaQuimica. Ela protege quantidade, documentação, inspeção, status e eventos. ProdutoQuimico fica em catálogo independente. QuantidadePositiva, CodigoCarga e ClassificacaoRisco são objetos de valor propostos.

## Slide 5 — Casos de uso e regras (3:10–4:10)

Documentamos onze casos de uso, desde cadastrar produto até consultar histórico. As regras mais críticas proíbem quantidade inválida, produto inativo, liberação sem documentos e movimentação de carga bloqueada.

## Slide 6 — Diagramas obrigatórios (4:10–5:20)

No diagrama de domínio mostramos as fronteiras dos agregados e relações. No diagrama de status mostramos que a carga é registrada, analisada, eventualmente inspecionada, liberada e movimentada. Bloqueios e cancelamentos exigem transições explícitas.

## Slide 7 — Arquitetura e TypeScript (5:20–6:30)

A proposta utiliza monólito modular com apresentação, aplicação, domínio e infraestrutura. TypeScript auxilia na modelagem de tipos, interfaces, estados, funções puras e contratos. O domínio não depende de HTTP ou de banco de dados.

## Slide 8 — Planejamento de qualidade (6:30–7:25)

O plano prioriza testes unitários, casos de uso com repositórios falsos, transições, situações de erro e, depois, testes de integração e concorrência. Os testes são planejados para evolução, não exigidos como implementação completa nesta fase.

## Slide 9 — Roadmap e encerramento (7:25–8:10)

O roadmap prevê API, banco, frontend, autenticação, auditoria e validação das políticas reais. A integração industrial é uma extensão futura separada. Obrigado por acompanhar esta proposta de evolução do QuimiPort.
