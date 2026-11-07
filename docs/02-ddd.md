# 02 — Modelagem com Domain-Driven Design

## Bounded context principal: Gestão Portuária de Cargas Químicas

A **CargaQuimica** é o agregado central. Suas regras de status, documentação, inspeção, autorização e histórico precisam ser consistentes ao mesmo tempo. Não é aceitável modificar `status = LIBERADA` diretamente em uma interface sem executar a verificação correspondente.

## Entidades candidatas

| Entidade | Atributos principais | Responsabilidade/relação |
|---|---|---|
| `ProdutoQuimico` | id, nome, classeRisco, ativo | Catálogo independente; uma carga referencia um produto |
| `CargaQuimica` | id, codigo, produtoId, quantidade, responsavelId, status | Raiz do agregado; mantém invariantes do fluxo |
| `DocumentoCarga` | id, tipo, referencia, valido, validade | Pertence a uma carga e compõe liberação |
| `Inspecao` | id, parecer, status, inspetorId, data | Pertence à carga; registra avaliação técnica |
| `EventoHistorico` | id, acao, ator, instante, statusAnterior, statusNovo | Auditabilidade lógica das alterações |
| `ResponsavelTecnico` | id, nome, identificacaoProfissional | Entidade de referência; exige validação futura de habilitação |
| `AreaArmazenamento` | id, descricao, capacidade, restricoes | Candidata para próxima fase; não cria controle de risco real |

## Objetos de valor (VO) candidatos

- `ClassificacaoRisco`: código de risco versionado, sem identidade própria.
- `QuantidadePositiva`: valor numérico finito positivo com unidade explícita.
- `CodigoCarga`: identificador de negócio normalizado.
- `ReferenciaDocumento`: tipo + referência não vazia; validade opcional conforme tipo.
- `StatusCarga`: conjunto fechado de estados permitidos.
- `MotivoBloqueio`: texto obrigatório de justificativa.

Um VO é comparado pelo **valor**, enquanto entidade mantém **identidade** ao longo do tempo.

## Agregados e fronteiras

`ProdutoQuimico` pode ser seu próprio agregado de catálogo. `CargaQuimica` protege e controla seu conjunto de `DocumentoCarga`, `Inspecao` e `EventoHistorico` como entidades internas. `ResponsavelTecnico` é referenciado por ID para evitar acoplamento a um cadastro externo.

## Invariantes do agregado CargaQuimica

1. Exige produto existente, ativo e classificado ao registrar.
2. Exige quantidade positiva e responsável técnico identificado.
3. Não permite liberação quando há pendência obrigatória.
4. Não permite movimentação quando bloqueada ou cancelada.
5. Não permite finalização antes de liberação e início de movimentação.
6. Toda transição guarda evento de histórico.
7. Mudança de documentação após liberação deve disparar nova avaliação conforme política definida.

## Domain services / casos de uso

- `RegistrarCarga` consulta catálogo e delega à raiz a criação válida.
- `ValidarDocumentacao` avalia documentação segundo política parametrizada.
- `SolicitarInspecao` abre verificação conforme estado.
- `LiberarCarga` faz pré-condições e gera evento.
- `BloquearCarga` registra motivação e restringe operações.

Os casos de uso orquestram. As invariantes vivem no domínio para não depender da UI ou da API.

## Ficha das entidades — atributos, regras e relacionamentos

| Entidade | Identidade e atributos | Regra central | Relacionamentos |
|---|---|---|---|
| ProdutoQuimico | `produtoId`, `codigo`, `nome`, `classificacaoRisco`, `ativo` | Nome e classe obrigatórios; inativo não pode originar novas cargas | Referenciado pela CargaQuimica |
| CargaQuimica | `cargaId`, `codigo`, `produtoId`, `quantidade`, `unidade`, `responsavelTecnicoId`, `status`, `versao` | Protege registro, transições, bloqueio e liberação | 1 produto, 1 responsável, 0..N documentos, 0..N inspeções e 1..N eventos (incluindo criação) |
| ResponsavelTecnico | `responsavelId`, `nome`, `registroProfissional` | Identificação exigida no registro de carga | Pode ser referenciado por N cargas |
| DocumentoCarga | `documentoId`, `tipo`, `referencia`, `situacao`, `validade`, `validadoPor` | Política documental decide se é aceito | Pertence a 1 carga |
| Inspecao | `inspecaoId`, `status`, `parecer`, `solicitadaEm`, `concluidaEm`, `inspetorId` | Reprovação impede liberação conforme a política | Pertence a 1 carga |
| EventoHistorico | `eventoId`, `tipo`, `dataHora`, `autorId`, `anterior`, `novo`, `motivo` | Mudança de status gera evento imutável | Pertence a 1 carga |
| AreaArmazenamento | `areaId`, `descricao`, `capacidade`, `restricoes` | Modelo futuro; compatibilidade não inferida do nome | Associação futura com localização operacional |

A multiplicidade representa **associações conceituais** e não determina tabelas físicas nem o formato definitivo de APIs.

## Responsabilidades da raiz do agregado

A carga não aceita alterações diretas de `status`. Em vez disso, a raiz `CargaQuimica` expõe comportamentos (`registrarDocumento`, `solicitarInspecao`, `liberar`, `bloquear`, `iniciarMovimentacao`, `cancelar`) e valida as invariantes antes de gerar um evento de histórico. O serviço de aplicação consulta `ProdutoQuimico` e a política documental, mas a carga não conhece HTTP nem SQL.

## Fronteiras de domínio previstas

- **Catálogo químico:** manutenção de `ProdutoQuimico` e classificação declarada.
- **Operação portuária:** núcleo `CargaQuimica`, documentos, inspeção, liberação e histórico.
- **Identidade e acesso (futuro):** papéis, usuários e autenticação.
- **Armazenamento industrial (futuro):** gestão de lotes e quarentena após a operação portuária.

## Exemplo de linguagem ubíqua em uma conversa

Operador: "A carga CQ-2026-001 está registrada, mas ainda não foi liberada". Analista: "Há uma pendência documental; a carga permanecerá em análise". Gestor: "Registrar o motivo do bloqueio e o autor da decisão". Essas palavras devem ser usadas de forma consistente na documentação, nos testes e nos nomes de código.

## Decisões explícitas para defesa da modelagem

- **Identidade x valor:** dois registros de `CargaQuimica` com atributos iguais continuam sendo entidades diferentes, pois têm IDs próprios. Duas quantidades `100 kg` equivalem como valores; isso motiva `QuantidadePositiva` como VO.
- **Coesão transacional:** documentos, inspeções e eventos que participam de decisões de liberação são coordenados pela raiz `CargaQuimica`. O catálogo `ProdutoQuimico` possui ciclo de vida independente e é referenciado, não copiado como entidade interna da carga.
- **Histórico inicial:** a criação da carga gera o primeiro `EventoHistorico`; assim `1..N` eventos é coerente mesmo em uma carga apenas registrada.
- **Classificação e documentos:** os valores e as exigências são **modelos conceituais**, não comprovação regulatória para produtos químicos reais.
- **Fronteira proposta, não definitiva:** as decisões de composição e consistência devem ser validadas em futuras entrevistas com especialistas.


## Exemplo de fronteira de agregado com o caso C-001

No [cenário fictício CQ-2026-001](16-estudo-de-caso.md), a decisão de liberação consulta o conjunto formado por **status da carga, referências documentais, resultado de inspeção (se exigido) e histórico**. Se cada uma dessas partes pudesse alterar seu próprio status diretamente, existiria o risco de representar `LIBERADA` enquanto uma exigência continua pendente. Por isso, a proposta concentra a verificação na raiz `CargaQuimica` e utiliza casos de uso para consultar políticas e serviços externos.

**Essa modelagem é uma escolha de DDD**, não uma afirmação de que o Porto de Santos utiliza exatamente esses agregados. A diferença entre relação `referencia produto` e `contem documento` foi representada no [diagrama de domínio](../diagramas/dominio.mmd).
