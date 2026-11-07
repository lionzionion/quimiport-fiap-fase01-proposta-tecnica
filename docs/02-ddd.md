# 02 — Modelagem DDD do QuimiPort

## Contexto delimitado

O núcleo é o *bounded context* **Gestão Portuária de Cargas Químicas**. A linguagem ubíqua do [documento de domínio](01-contexto-e-domínio.md) deve ser preservada na modelagem.

## Entidades e responsabilidades

| Entidade | Atributos | Regra e relacionamento |
|---|---|---|
| `ProdutoQuimico` | id, código, nome, classificaçãoRisco, ativo | Nome e classe obrigatórios; referenciado por cargas |
| `CargaQuimica` | id, código, produtoId, quantidade, unidade, responsavelId, status, versão | Raiz do agregado; controla invariantes e transições |
| `ResponsavelTecnico` | id, nome, registroProfissional | Identificação presente no registro; pode responder por N cargas |
| `DocumentoCarga` | id, tipo, referência, situação, validade, validador | Pertence a uma carga; avaliado por política documental |
| `Inspecao` | id, status, parecer, solicitadaEm, concluidaEm, inspetorId | Pertence à carga; reprovação impede liberação |
| `EventoHistorico` | id, tipo, autorId, dataHora, anterior, novo, motivo | Pertence à carga; somente acrescenta eventos |
| `AreaArmazenamento` | id, descrição, capacidade, restrições | Entidade **futura**, fora do núcleo obrigatório |

## Objetos de valor

- `ClassificacaoRisco`: código/edição da classificação; sem identidade própria.
- `QuantidadePositiva`: número finito maior que zero + unidade.
- `CodigoCarga`: identificador de negócio normalizado.
- `ReferenciaDocumento`: tipo e código/referência não vazios.
- `StatusCarga`: conjunto fechado de estados válidos.
- `MotivoBloqueio`: justificativa obrigatória.

**Diferença:** entidade mantém identidade ao longo do tempo; objeto de valor é comparado pelo valor e validado como uma unidade.

## Agregados

**`CargaQuimica` — raiz principal:** contém/coordena `DocumentoCarga`, `Inspecao` e `EventoHistorico`. Ninguém deve alterar `status` diretamente; os métodos de domínio validam pré-condições.

**`ProdutoQuimico` — agregado de catálogo:** é independente; a carga o referencia por `produtoId` e valida existência/atividade ao registrar. `ResponsavelTecnico` é referência externa por ID.

## Invariantes da carga

1. Produto precisa existir, estar ativo e possuir classificação.
2. Quantidade precisa ser positiva e responsável informado.
3. Ausência de política documental ou de documento obrigatório validado impede liberação.
4. Carga bloqueada não inicia movimentação; cancelada não é liberada.
5. Inspeção pendente/desfavorável impede liberação conforme política.
6. Não há finalização sem liberação e movimentação.
7. Toda transição gera `EventoHistorico` com responsável e momento.
8. Mudança documental relevante após liberação exige reavaliação conforme política.

## Serviços e casos de uso

`RegistrarCarga` consulta o catálogo e cria agregado válido; `ValidarDocumentacao` coordena política; `LiberarCarga` obtém carga/política/parecer e solicita transição à raiz; `BloquearCarga` exige motivo e registra evento. Os casos de uso **orquestram**, o domínio **protege regras** e repositórios **persistem**.

## Multiplicidades conceituais

- ProdutoQuimico **1** ↔ **0..N** CargaQuimica.
- CargaQuimica **1** ↔ **0..N** DocumentoCarga e **0..N** Inspecao.
- CargaQuimica **1** ↔ **1..N** EventoHistorico (incluindo registro).
- ResponsavelTecnico **1** ↔ **0..N** CargaQuimica.

Essas associações não impõem um esquema físico de banco na Fase 01. Consulte o [diagrama de domínio](../diagramas/dominio.mmd).
