# 06 — Diagramas técnicos

O enunciado exige **Diagrama de Domínio (agregados/entidades)** e **Fluxo de Transição de Status da Carga**. A arquitetura em camadas é complementar.

## Diagrama obrigatório 1 — Domínio e agregados

```mermaid
classDiagram
  direction LR
  class ProdutoQuimico {
    <<AgregadoCatalogo>>
    +id: UUID
    +nome: String
    +classificacaoRisco: String
    +ativo: Boolean
  }
  class CargaQuimica {
    <<RaizDeAgregado>>
    +id: UUID
    +codigo: String
    +quantidade: Decimal
    +status: StatusCarga
    +liberar()
    +bloquear()
  }
  class DocumentoCarga {
    +tipo: String
    +situacao: String
  }
  class Inspecao {
    +parecer: String
  }
  class EventoHistorico {
    +acao: String
    +dataHora: DateTime
  }
  class ResponsavelTecnico {
    +nome: String
    +registro: String
  }
  ProdutoQuimico "1" <-- "0..*" CargaQuimica : produtoId
  CargaQuimica "1" *-- "0..*" DocumentoCarga
  CargaQuimica "1" *-- "0..*" Inspecao
  CargaQuimica "1" *-- "1..*" EventoHistorico
  CargaQuimica "0..*" --> "1" ResponsavelTecnico
```

**Modelo:** `ProdutoQuimico` é agregado independente de catálogo; `CargaQuimica` é raiz do agregado transacional; documentos, inspeções e eventos pertencem a uma carga; responsável é referência. `ClassificacaoRisco` e `QuantidadePositiva` são objetos de valor candidatos.

## Diagrama obrigatório 2 — Transições de status

```mermaid
stateDiagram-v2
  [*] --> REGISTRADA
  REGISTRADA --> EM_ANALISE: iniciar análise
  EM_ANALISE --> EM_INSPECAO: solicitar inspeção
  EM_INSPECAO --> EM_ANALISE: parecer favorável
  EM_INSPECAO --> BLOQUEADA: parecer desfavorável
  EM_ANALISE --> LIBERADA: requisitos atendidos
  LIBERADA --> EM_MOVIMENTACAO: iniciar movimentação
  EM_MOVIMENTACAO --> FINALIZADA: concluir
  REGISTRADA --> BLOQUEADA: motivo técnico
  EM_ANALISE --> BLOQUEADA: ocorrência crítica
  LIBERADA --> BLOQUEADA: nova ocorrência
  BLOQUEADA --> EM_ANALISE: reabrir com justificativa
  REGISTRADA --> CANCELADA: cancelar
  EM_ANALISE --> CANCELADA: cancelar
  BLOQUEADA --> CANCELADA: cancelar
  FINALIZADA --> [*]
  CANCELADA --> [*]
```

**Nota de consistência:** parecer favorável não libera automaticamente; documento ausente cria pendência em análise. O cancelamento só parte dos estados indicados, e o tratamento de interrupção de movimentação em curso fica para levantamento futuro.

## Diagrama complementar — Camadas

```mermaid
flowchart TD
  UI[Apresentação web] --> HTTP[Controlador HTTP]
  HTTP --> APP[Aplicação / Casos de uso]
  APP --> DOM[Domínio e regras]
  APP --> PORT[Interfaces de repositório]
  INF[Infraestrutura / Adaptadores] -. implementa .-> PORT
```

**Fontes editáveis:** [domínio](../diagramas/dominio.mmd), [status](../diagramas/status.mmd) e [arquitetura](../diagramas/arquitetura.mmd). As visualizações representam um modelo **acadêmico**, não um fluxo regulamentar aprovado.
