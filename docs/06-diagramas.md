# 06 — Diagramas técnicos

Segundo o enunciado, o **Diagrama de Domínio** e o **Fluxo de Transição de Status da Carga** são obrigatórios. O diagrama de camadas é complementar.

## Diagrama 1 — Domínio e agregados (OBRIGATÓRIO)

```mermaid
classDiagram
  direction LR
  class ProdutoQuimico {
    <<AgregadoCatalogo>>
    +id: UUID
    +nome: String
    +risco: ClassificacaoRisco
    +ativo: Boolean
    +inativar()
  }
  class CargaQuimica {
    <<RaizDeAgregado>>
    +id: UUID
    +codigo: CodigoCarga
    +quantidade: QuantidadePositiva
    +status: StatusCarga
    +responsavelId: UUID
    +registrarDocumento()
    +liberar()
    +bloquear()
  }
  class DocumentoCarga {
    +id: UUID
    +tipo: String
    +referencia: String
    +valido: Boolean
  }
  class Inspecao {
    +id: UUID
    +parecer: String
    +situacao: String
  }
  class EventoHistorico {
    +id: UUID
    +acao: String
    +instante: DateTime
  }
  class ResponsavelTecnico {
    +id: UUID
    +nome: String
    +identificacao: String
  }
  class ClassificacaoRisco {
    +codigo: String
  }
  class QuantidadePositiva {
    +valor: Decimal
    +unidade: String
  }
  ProdutoQuimico "1" <-- "0..*" CargaQuimica : referencia por id
  CargaQuimica "1" *-- "0..*" DocumentoCarga
  CargaQuimica "1" *-- "0..*" Inspecao
  CargaQuimica "1" *-- "1..*" EventoHistorico
  CargaQuimica "0..*" --> "1" ResponsavelTecnico : referencia
  ProdutoQuimico --> ClassificacaoRisco
  CargaQuimica --> QuantidadePositiva
```

**Agregados:** `ProdutoQuimico` (catálogo) e `CargaQuimica` (raiz de documentos, inspeções e histórico). `ResponsavelTecnico` é referência externa. Os VOs não têm identidade própria.

## Diagrama 2 — Transições de status (OBRIGATÓRIO)

```mermaid
stateDiagram-v2
  [*] --> REGISTRADA
  REGISTRADA --> EM_ANALISE : iniciar análise documental
  EM_ANALISE --> EM_INSPECAO : solicitar inspeção
  EM_INSPECAO --> EM_ANALISE : parecer favorável
  EM_INSPECAO --> BLOQUEADA : parecer desfavorável
  EM_ANALISE --> LIBERADA : requisitos aprovados
  LIBERADA --> EM_MOVIMENTACAO : iniciar movimentação
  EM_MOVIMENTACAO --> FINALIZADA : concluir operação
  REGISTRADA --> BLOQUEADA : motivo técnico
  EM_ANALISE --> BLOQUEADA : pendência crítica
  LIBERADA --> BLOQUEADA : ocorrência nova
  BLOQUEADA --> EM_ANALISE : reabrir com justificativa
  REGISTRADA --> CANCELADA : cancelamento autorizado
  EM_ANALISE --> CANCELADA : cancelamento autorizado
  BLOQUEADA --> CANCELADA : cancelamento autorizado
  FINALIZADA --> [*]
  CANCELADA --> [*]
```

**Regras:** não há atalho de `REGISTRADA` a `FINALIZADA`; `BLOQUEADA` não inicia movimentação; `CANCELADA` não libera. A volta de `BLOQUEADA` a `EM_ANALISE` **não significa liberação automática**. Estados e retornos são **proposta** a validar com requisitos mais detalhados.

## Diagrama 3 — Arquitetura em camadas (COMPLEMENTAR)

```mermaid
flowchart TD
  UI[Apresentação: Web futura] --> API[Controladores HTTP]
  API --> APP[Aplicação: casos de uso]
  APP --> DOM[Domínio: regras e entidades]
  APP --> PORT[Interfaces de repositório]
  INF[Infraestrutura: banco e integrações] -. implementa .-> PORT
```

## Visualização imediata dos diagramas

Os arquivos `diagramas/dominio.svg` e `diagramas/status.svg` são versões vetoriais ampliáveis publicadas no GitHub. As fontes `.mmd` (Mermaid) e `.dot` (Graphviz) permitem conferir o modelo e gerar novas imagens. Veja o passo a passo em [Como os diagramas foram construídos](18-como-construi-os-diagramas.md).

> **Conferência:** as imagens e o Mermaid apresentam o mesmo modelo conceitual. Qualquer mudança de regra de status deve atualizar ambos para não gerar inconsistência entre código, diagrama e documentação.

## Processo e autoria verificável

Os SVGs foram gerados a partir de **Graphviz DOT** e não são apenas imagens decorativas. A modelagem também está descrita em Mermaid para permitir edição na web. O conjunto de decisões é proposto com apoio de IA; o estudante deve reproduzir e explicar os modelos antes da entrega. [Tutorial completo](18-como-construi-os-diagramas.md).

## Conferência de consistência da banca

1. `EM_INSPECAO` **não libera diretamente**. Com parecer favorável retorna a `EM_ANALISE` para decisão final.
2. O caso de uso de cancelamento só aceita os estados com seta explícita para `CANCELADA`.
3. Documento ausente mantém pendência em análise; apenas decisão de bloqueio gera `BLOQUEADA`.
4. Os dois diagramas obrigatórios contêm o modelo **proposto**, não um fluxo homologado para operação portuária.
5. A possibilidade de interromper movimentação em curso será analisada em fase futura e não é coberta pelo grafo inicial.
