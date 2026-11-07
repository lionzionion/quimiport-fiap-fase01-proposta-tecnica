# 03 — Casos de uso planejados

Os fluxos abaixo são **propostas**, não funcionalidades exigidas como código nesta fase. Para cada caso registramos os itens pedidos pela FIAP: objetivo, ator, entrada, saída, regra e erro.

| ID | Caso de uso | Ator |
|---|---|---|
| UC01 | Cadastrar produto químico | Administrador de catálogo |
| UC02 | Inativar produto | Gestor de catálogo |
| UC03 | Registrar carga química | Operador portuário |
| UC04 | Validar documentação | Analista documental |
| UC05 | Solicitar inspeção | Analista de qualidade |
| UC06 | Liberar carga química | Responsável autorizado |
| UC07 | Bloquear carga química | Gestor ou analista autorizado |
| UC08 | Atualizar status | Operador autorizado |
| UC09 | Cancelar carga | Gestor operacional autorizado |
| UC10 | Consultar cargas por status | Operador ou gestor |
| UC11 | Consultar histórico | Gestor/analista autorizado |

## UC01 — Cadastrar produto químico

**Objetivo:** Cadastrar produto químico de forma rastreável e consistente com o domínio.

**Ator:** Administrador de catálogo.

**Entrada:** Código, nome, classificação de risco.

**Saída:** Produto ativo identificado.

**Regras de negócio:** Nome e classe são obrigatórios, código deve ser único.

**Erros/exceções:** Nome/classe vazios, código duplicado, permissão insuficiente.

**Fluxo principal:** Validar entrada → conferir unicidade → criar produto → confirmar cadastro.

## UC02 — Inativar produto

**Objetivo:** Inativar produto de forma rastreável e consistente com o domínio.

**Ator:** Gestor de catálogo.

**Entrada:** Produto e justificativa.

**Saída:** Produto inativo, histórico preservado.

**Regras de negócio:** Produto inativo não origina novas cargas.

**Erros/exceções:** Produto inexistente, já inativo, permissão insuficiente.

**Fluxo principal:** Buscar produto → validar mudança → inativar → auditar.

## UC03 — Registrar carga química

**Objetivo:** Registrar carga química de forma rastreável e consistente com o domínio.

**Ator:** Operador portuário.

**Entrada:** Código, produto, quantidade/unidade e responsável técnico.

**Saída:** Carga REGISTRADA + evento inicial.

**Regras de negócio:** Produto existente, ativo e classificado; quantidade positiva; responsável obrigatório.

**Erros/exceções:** Produto ausente/inativo, quantidade inválida, código duplicado.

**Fluxo principal:** Consultar produto → validar invariantes → criar agregado → persistir.

## UC04 — Validar documentação

**Objetivo:** Validar documentação de forma rastreável e consistente com o domínio.

**Ator:** Analista documental.

**Entrada:** Carga, documentos e política aplicável.

**Saída:** Parecer e lista de pendências.

**Regras de negócio:** Documento obrigatório ausente ou rejeitado impede liberação.

**Erros/exceções:** Política indefinida, documento ausente, carga terminal.

**Fluxo principal:** Carregar política → avaliar exigências → registrar resultado.

## UC05 — Solicitar inspeção

**Objetivo:** Solicitar inspeção de forma rastreável e consistente com o domínio.

**Ator:** Analista de qualidade.

**Entrada:** Carga, motivo e solicitante.

**Saída:** Carga EM_INSPECAO e solicitação.

**Regras de negócio:** Somente EM_ANALISE entra em inspeção.

**Erros/exceções:** Estado incompatível, motivo ausente, carga cancelada.

**Fluxo principal:** Validar estado → abrir inspeção → registrar evento.

## UC06 — Liberar carga química

**Objetivo:** Liberar carga química de forma rastreável e consistente com o domínio.

**Ator:** Responsável autorizado.

**Entrada:** Carga, identidade e resultados de validação.

**Saída:** Carga LIBERADA + histórico.

**Regras de negócio:** Somente EM_ANALISE, política e documentos atendidos, parecer aplicável favorável, sem bloqueio.

**Erros/exceções:** Pendência, reprovação, estado inválido, concorrência.

**Fluxo principal:** Consultar agregado → validar política → liberar → persistir.

## UC07 — Bloquear carga química

**Objetivo:** Bloquear carga química de forma rastreável e consistente com o domínio.

**Ator:** Gestor ou analista autorizado.

**Entrada:** Carga, motivo e identidade.

**Saída:** BLOQUEADA e evento de bloqueio.

**Regras de negócio:** Motivo obrigatório; apenas estados previstos pelo diagrama.

**Erros/exceções:** Motivo vazio, CANCELADA/FINALIZADA, transição inválida.

**Fluxo principal:** Validar motivo/estado → bloquear → registrar evento.

## UC08 — Atualizar status

**Objetivo:** Atualizar status de forma rastreável e consistente com o domínio.

**Ator:** Operador autorizado.

**Entrada:** Carga, comando e identidade.

**Saída:** Novo status com histórico.

**Regras de negócio:** Transição específica permitida e pré-condições atendidas.

**Erros/exceções:** Salto indevido, bloqueio, versão desatualizada.

**Fluxo principal:** Carregar agregado → executar comando → validar → persistir.

## UC09 — Cancelar carga

**Objetivo:** Cancelar carga de forma rastreável e consistente com o domínio.

**Ator:** Gestor operacional autorizado.

**Entrada:** Carga e justificativa.

**Saída:** CANCELADA com evento final.

**Regras de negócio:** Permitido apenas desde REGISTRADA, EM_ANALISE ou BLOQUEADA.

**Erros/exceções:** Carga liberada/em movimento/finalizada/cancelada; motivo ausente.

**Fluxo principal:** Validar estado → cancelar → registrar histórico.

## UC10 — Consultar cargas por status

**Objetivo:** Consultar cargas por status de forma rastreável e consistente com o domínio.

**Ator:** Operador ou gestor.

**Entrada:** Status, período ou filtros.

**Saída:** Lista paginada.

**Regras de negócio:** Consulta não altera domínio; respeita acesso futuro.

**Erros/exceções:** Filtro inválido, usuário não autorizado.

**Fluxo principal:** Validar filtros → consultar visão de leitura → devolver lista.

## UC11 — Consultar histórico

**Objetivo:** Consultar histórico de forma rastreável e consistente com o domínio.

**Ator:** Gestor/analista autorizado.

**Entrada:** Identificador da carga.

**Saída:** Eventos cronológicos e autoria.

**Regras de negócio:** Não alterar/remover eventos em consulta.

**Erros/exceções:** Carga inexistente, acesso negado.

**Fluxo principal:** Carregar eventos → ordenar → apresentar.

## Decisões que precisam permanecer coerentes

- `EM_INSPECAO` volta a `EM_ANALISE` em parecer favorável; a liberação **não é automática**.
- Documento ausente gera pendência em análise, e não `BLOQUEADA` automaticamente.
- O cancelamento (UC09) não parte de `LIBERADA` nem `EM_MOVIMENTACAO` no modelo inicial.
- Interrupção de movimentação já iniciada é lacuna reconhecida para descoberta posterior.
- Permissões e catálogo de documentos regulamentares dependem de validação profissional posterior.
