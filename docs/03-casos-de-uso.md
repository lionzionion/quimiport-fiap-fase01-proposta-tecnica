# 03 — Casos de uso planejados

Os 11 casos de uso abaixo são **comportamentos projetados**, não funções que a FIAP exija entregar implementadas. Cada um apresenta os seis elementos indicados pelo enunciado: objetivo, ator, entradas, saídas, regras e erros. O fluxo principal é uma proposta de design. **Fio condutor:** [caso fictício C-001 de pendência documental](16-estudo-de-caso.md), que exercita principalmente UC03 (registro), UC04 (conferência), UC06 (liberação) e UC11 (histórico).

| ID | Caso de uso | Ator principal | Resultado esperado |
|---|---|---|---|
| UC01 | Cadastrar produto químico | Administrador do catálogo | Produto ativo com ID e código |
| UC02 | Inativar produto químico | Gestor de catálogo | Produto marcado como inativo |
| UC03 | Registrar carga química | Operador portuário | Carga REGISTRADA e evento inicial |
| UC04 | Validar documentação | Analista documental | Lista de pendências e parecer de análise |
| UC05 | Solicitar inspeção | Analista de qualidade | Carga EM_INSPECAO e solicitação registrada |
| UC06 | Liberar carga química | Responsável autorizado | Carga LIBERADA, histórico e versão atualizada |
| UC07 | Bloquear carga química | Gestor ou analista autorizado | Carga BLOQUEADA + evento de bloqueio |
| UC08 | Atualizar status da carga | Operador autorizado para a operação | Novo status e histórico, se transição for permitida |
| UC09 | Cancelar carga química | Gestor operacional autorizado | CANCELADA + evento definitivo |
| UC10 | Consultar cargas por status | Operador ou gestor autorizado | Lista paginada de cargas |
| UC11 | Consultar histórico da carga | Gestor/analista autorizado | Eventos cronológicos com autor, data e transição |

## UC01 — Cadastrar produto químico

**Objetivo:** Registrar no catálogo um produto químico com identificação e classificação informadas.

**Ator:** Administrador do catálogo.  
**Entrada:** Código, nome e classificação de risco proposta.  
**Saída:** Produto ativo com ID e código.  
**Regra(s) central(is):** Nome e classe são obrigatórios; código único no catálogo.  
**Erros/exceções:** Nome/classe vazios; código duplicado; falta de permissão futura.  
**Fluxo principal:** Verificar dados → validar atributos → registrar produto → devolver identificação.

## UC02 — Inativar produto químico

**Objetivo:** Impedir a criação de novas cargas a partir de um produto descontinuado, mantendo o histórico anterior.

**Ator:** Gestor de catálogo.  
**Entrada:** ID do produto e motivo da mudança.  
**Saída:** Produto marcado como inativo.  
**Regra(s) central(is):** Produto inativo não poderá originar novas cargas; cargas anteriores permanecem rastreáveis.  
**Erros/exceções:** Produto não localizado; já inativo; falta de permissão.  
**Fluxo principal:** Buscar produto → verificar situação → inativar → guardar auditoria.

## UC03 — Registrar carga química

**Objetivo:** Criar uma carga rastreável com produto válido, quantidade positiva e responsável técnico.

**Ator:** Operador portuário.  
**Entrada:** Produto, quantidade/unidade, responsável técnico, código.  
**Saída:** Carga REGISTRADA e evento inicial.  
**Regra(s) central(is):** Produto existente/ativo/classificado, quantidade positiva e responsável informado.  
**Erros/exceções:** Produto ausente/inativo; classe ausente; quantidade inválida; código repetido.  
**Fluxo principal:** Consultar catálogo → validar → criar agregado → emitir evento → persistir.

## UC04 — Validar documentação

**Objetivo:** Identificar documentos exigidos, ausentes ou rejeitados antes de qualquer liberação.

**Ator:** Analista documental.  
**Entrada:** Carga, documentos apresentados, política aplicável.  
**Saída:** Lista de pendências e parecer de análise.  
**Regra(s) central(is):** Não liberar enquanto houver documento obrigatório ausente, vencido ou rejeitado.  
**Erros/exceções:** Documento inexistente; política desconhecida; carga cancelada/finalizada.  
**Fluxo principal:** Carregar política → confrontar exigências → registrar pendências → manter EM_ANALISE.

## UC05 — Solicitar inspeção

**Objetivo:** Abrir uma inspeção rastreável para uma carga em análise.

**Ator:** Analista de qualidade.  
**Entrada:** ID da carga, motivo e identificação do solicitante.  
**Saída:** Carga EM_INSPECAO e solicitação registrada.  
**Regra(s) central(is):** Somente carga em EM_ANALISE entra em inspeção; inspeção sem conclusão mantém o estado.  
**Erros/exceções:** Carga cancelada/bloqueada; estado divergente; motivo ausente.  
**Fluxo principal:** Validar situação → abrir inspeção → transitar → registrar histórico.

## UC06 — Liberar carga química

**Objetivo:** Autorizar a continuidade do processo somente após atender às condições de liberação propostas.

**Ator:** Responsável autorizado.  
**Entrada:** Carga, identidade do decisor e confirmação da análise.  
**Saída:** Carga LIBERADA, histórico e versão atualizada.  
**Regra(s) central(is):** Somente a partir de EM_ANALISE, com política documental atendida, inspeção favorável se aplicável e sem bloqueios.  
**Erros/exceções:** Documentos pendentes; parecer desfavorável; bloqueada/cancelada; concorrência.  
**Fluxo principal:** Carregar agregado → verificar política/inspeção → liberar → salvar estado+evento.

## UC07 — Bloquear carga química

**Objetivo:** Impedir a continuidade de uma carga com ocorrência crítica, registrando o motivo.

**Ator:** Gestor ou analista autorizado.  
**Entrada:** ID da carga, motivo obrigatório, identidade.  
**Saída:** Carga BLOQUEADA + evento de bloqueio.  
**Regra(s) central(is):** Bloquear somente de REGISTRADA, EM_ANALISE, EM_INSPECAO ou LIBERADA no modelo inicial.  
**Erros/exceções:** Sem motivo; FINALIZADA/CANCELADA; tentativa fora de estado permitido.  
**Fluxo principal:** Verificar transição → validar motivo → bloquear → registrar evento.

## UC08 — Atualizar status da carga

**Objetivo:** Executar uma transição operacional autorizada e registrar seu histórico.

**Ator:** Operador autorizado para a operação.  
**Entrada:** ID da carga, comando específico e identidade.  
**Saída:** Novo status e histórico, se transição for permitida.  
**Regra(s) central(is):** Sem atualização direta; REGISTRADA→EM_ANALISE, LIBERADA→EM_MOVIMENTACAO e EM_MOVIMENTACAO→FINALIZADA têm pré-condições.  
**Erros/exceções:** REGISTRADA→FINALIZADA; movimentar bloqueada; versão desatualizada.  
**Fluxo principal:** Carregar agregado → validar comando/transição → registrar evento → persistir.

## UC09 — Cancelar carga química

**Objetivo:** Encerrar uma carga elegível antes da liberação, preservando o histórico.

**Ator:** Gestor operacional autorizado.  
**Entrada:** Carga e justificativa.  
**Saída:** CANCELADA + evento definitivo.  
**Regra(s) central(is):** No modelo inicial, cancelar apenas REGISTRADA, EM_ANALISE e BLOQUEADA; CANCELADA/FINALIZADA são terminais.  
**Erros/exceções:** Tentar cancelar LIBERADA, EM_MOVIMENTACAO, FINALIZADA ou CANCELADA; motivo vazio.  
**Fluxo principal:** Verificar estado → confirmar motivo → cancelar → persistir evento.

## UC10 — Consultar cargas por status

**Objetivo:** Permitir que operadores consultem cargas conforme sua situação e os filtros disponíveis.

**Ator:** Operador ou gestor autorizado.  
**Entrada:** Status, código ou filtros de período.  
**Saída:** Lista paginada de cargas.  
**Regra(s) central(is):** Retornar somente cargas acessíveis e sem alterar o domínio.  
**Erros/exceções:** Filtro inválido; ausência de resultados; acesso não autorizado (futuro).  
**Fluxo principal:** Interpretar filtros → consultar repositório → devolver dados de leitura.

## UC11 — Consultar histórico da carga

**Objetivo:** Exibir eventos, responsáveis e transições de uma carga sem alterar os registros.

**Ator:** Gestor/analista autorizado.  
**Entrada:** ID da carga.  
**Saída:** Eventos cronológicos com autor, data e transição.  
**Regra(s) central(is):** Eventos apenas de leitura; não permitir exclusão ou edição ordinária.  
**Erros/exceções:** Carga inexistente; permissão insuficiente (futura).  
**Fluxo principal:** Carregar carga → ordenar eventos → devolver trilha de auditoria.

## Exemplo verificável de encadeamento dos casos de uso

No caso C-001, o operador realiza **UC03** e a carga fica `REGISTRADA`. Um analista executa **UC04**, encontra um requisito pendente da política demonstrativa P-01 e informa `EM_ANALISE`. A tentativa de **UC06** devolve erro de pendência sem alterar o estado. A ação frustrada deve produzir resposta de validação e pode ser registrada em trilha de auditoria segundo a política futura; o **UC11** permite consultar a história das transições de estado bem-sucedidas. Somente depois de regularização e reavaliação poderá ocorrer decisão explícita de liberação.

Esse é o comportamento **planejado**, não um teste realizado em terminal real.

## Decisões explícitas e limites

- **UC09 e máquina de estados:** o cancelamento não é permitido a partir de `LIBERADA` ou `EM_MOVIMENTACAO` na versão conceitual atual. A ocorrência depois de liberação é tratada por bloqueio/revisão se o movimento ainda não iniciou; interrupção de movimento em curso é **lacuna operacional para futura descoberta**, não funcionalidade afirmada como pronta.
- **UC05:** solicitar e concluir inspeção são ações diferentes. O fluxo inicial prevê `EM_INSPECAO → EM_ANALISE` após parecer favorável e `EM_INSPECAO → BLOQUEADA` após parecer desfavorável; não há liberação automática após inspeção.
- **UC04:** documento ausente gera **pendência em análise**; bloqueio formal é reservado a decisão/ocorrência crítica com motivo.
- **Permissões e documentos oficiais:** os perfis e a política documental são hipóteses de arquitetura; exigem posterior validação em campo.
