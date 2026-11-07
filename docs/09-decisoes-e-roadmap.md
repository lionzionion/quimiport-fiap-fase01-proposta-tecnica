# 09 — Decisões arquiteturais e evolução

## ADR-001: Monólito modular

**Contexto:** domínio em descoberta, time acadêmico pequeno e necessidade de testar transições atômicas.

**Decisão:** monólito modular com camadas e fronteiras explícitas.

**Consequências:** implantação inicialmente simples e maior consistência; exige disciplina para não criar acoplamento entre módulos. A adoção de microsserviços dependerá de métricas, escala e novas fronteiras de domínio.

## ADR-002: Domínio isolado

**Decisão:** entidades, VOs e regras não dependem de interface, HTTP, banco nem framework.

**Motivo:** as regras de liberação devem ser aplicadas independentemente de qual interface chame o caso de uso.

## ADR-003: TypeScript

**Decisão:** tipagem explícita para estados, entidades, contratos e operações.

**Motivo:** tornar relações e pré-condições mais visíveis, facilitar refatoração e reduzir erros de integração; tipagem estática não substitui validação em runtime.

## ADR-004: Política documental

**Decisão:** documentos obrigatórios serão definidos por política aplicável e versionada em fase futura, não fixados como uma lista universal.

**Motivo:** o enunciado não fornece uma matriz normativa completa; usar lista arbitrária como regra real seria inseguro.

## Roadmap

| Etapa | Evolução planejada |
|---|---|
| Fase 01 | Domínio, DDD, casos de uso, regras, arquitetura, diagramas e testes planejados |
| Próxima implementação | Núcleo TypeScript, testes unitários, armazenamento em memória e API |
| Evolução web | Frontend, autenticação, autorizações, documentos e histórico |
| Integração | Banco persistente, auditoria, políticas versionadas, observabilidade |
| Maturidade | Controle de concorrência, segurança ampliada, validação de requisitos legais |
| Extensão opcional | Recebimento industrial, quarentena, estoque por lote e consumo |
| Escala futura | Mobile e eventual separação em serviços se houver necessidade comprovada |

A extensão industrial **não integra a entrega oficial da Fase 01** e requer descoberta de regras próprias.
