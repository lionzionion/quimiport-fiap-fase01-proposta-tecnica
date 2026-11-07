# QuimiPort — Apresentação técnica FIAP Fase 01

Os slides abaixo são uma **versão textual navegável** para estudo e gravação. O PowerPoint/PDF editável pode ser usado localmente.

## 1. Abertura e objetivo

*Tempo sugerido: 0:00–0:30*

Meu projeto é o QuimiPort, uma proposta técnica para gestão de cargas químicas portuárias, inspirada no Porto de Santos. Nesta fase o foco é documentação, DDD, arquitetura, TypeScript e qualidade.

## 2. Contexto e problema

*Tempo sugerido: 0:30–1:15*

O cenário envolve dados dispersos sobre produto, risco, documentos, inspeções e autorizações. O QuimiPort busca centralizar informações e rastrear decisões sem presumir critérios regulamentares não fornecidos.

## 3. Usuários e linguagem

*Tempo sugerido: 1:15–2:00*

Os atores são operador, analista documental, inspetor, responsável técnico, gestor e administrador. Definimos termos comuns: carga, produto, bloqueio, liberação, movimentação e histórico.

## 4. Modelagem DDD

*Tempo sugerido: 2:00–3:10*

A entidade principal e raiz de agregado é CargaQuimica. Ela protege quantidade, documentação, inspeção, status e eventos. ProdutoQuimico fica em catálogo independente. QuantidadePositiva, CodigoCarga e ClassificacaoRisco são objetos de valor propostos.

## 5. Casos de uso e regras

*Tempo sugerido: 3:10–4:10*

Documentamos onze casos de uso, desde cadastrar produto até consultar histórico. As regras mais críticas proíbem quantidade inválida, produto inativo, liberação sem documentos e movimentação de carga bloqueada.

## 6. Diagramas obrigatórios

*Tempo sugerido: 4:10–5:20*

No diagrama de domínio mostramos as fronteiras dos agregados e relações. No diagrama de status mostramos que a carga é registrada, analisada, eventualmente inspecionada, liberada e movimentada. Bloqueios e cancelamentos exigem transições explícitas.

## 7. Arquitetura e TypeScript

*Tempo sugerido: 5:20–6:30*

A proposta utiliza monólito modular com apresentação, aplicação, domínio e infraestrutura. TypeScript auxilia na modelagem de tipos, interfaces, estados, funções puras e contratos. O domínio não depende de HTTP ou de banco de dados.

## 8. Planejamento de qualidade

*Tempo sugerido: 6:30–7:25*

O plano prioriza testes unitários, casos de uso com repositórios falsos, transições, situações de erro e, depois, testes de integração e concorrência. Os testes são planejados para evolução, não exigidos como implementação completa nesta fase.

## 9. Roadmap e encerramento

*Tempo sugerido: 7:25–8:10*

O roadmap prevê API, banco, frontend, autenticação, auditoria e validação das políticas reais. A integração industrial é uma extensão futura separada. Obrigado por acompanhar esta proposta de evolução do QuimiPort.
