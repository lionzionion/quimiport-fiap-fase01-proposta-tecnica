# 01 — Entendimento do domínio e contexto portuário

## Situação-problema

O QuimiPort é uma **proposta acadêmica** de gestão de cargas químicas em um terminal portuário fictício, inspirado no Porto de Santos. Atualmente, informações de identificação de produto, classificação de risco, documentação, inspeções e autorizações podem estar dispersas. Isso dificulta saber quem tomou uma decisão, com base em quais evidências e em qual momento.

**Objetivo:** centralizar o registro das cargas e definir regras verificáveis de análise, bloqueio, liberação e rastreabilidade, sem substituir exigências legais ou profissionais habilitados.

## Atores e responsabilidades propostas

| Perfil | Responsabilidade |
|---|---|
| Operador portuário | Cadastrar carga, consultar situação e solicitar avanço operacional |
| Analista documental | Conferir as exigências documentais da operação e registrar pendências |
| Inspetor / analista de qualidade | Solicitar e registrar parecer de inspeções |
| Responsável técnico | Vincular responsabilidade e acompanhar restrições técnicas |
| Gestor operacional | Decidir bloqueios, analisar exceções e acompanhar indicadores |
| Administrador | Gerenciar papéis, usuários e parâmetros em fase posterior |

Os papéis são **previstos**, não permissões implementadas.

## Informações a controlar

Produto químico (identificação, nome, classificação de risco, ativo/inativo); carga (código, produto associado, quantidade e unidade, responsável e status); referências documentais e seus resultados; inspeções; decisões de liberação/bloqueio; motivos e histórico temporal.

## Linguagem ubíqua

| Termo | Definição |
|---|---|
| Produto químico | Item identificado e classificado em catálogo |
| Carga química | Unidade operacional rastreável, vinculada a um produto |
| Documento obrigatório | Documento requerido por política aplicável à operação |
| Inspeção | Verificação formal com responsável, data e parecer |
| Pendência documental | Condição não atendida que impede liberação |
| Bloqueio | Restrição explícita com motivo registrado |
| Liberação | Decisão autorizada após verificações previstas |
| Movimentação | Ação operacional posterior à liberação |
| Histórico | Sequência de eventos de criação, decisões e transições |
| Agregado | Fronteira de consistência que protege invariantes de negócio |

## Jornada operacional proposta

1. Cadastrar produto identificado, classificado e ativo.
2. Registrar carga com produto, quantidade positiva e responsável.
3. Identificar política documental aplicável e avaliar documentos.
4. Solicitar inspeção quando prevista; registrar parecer.
5. Decidir por liberação ou bloqueio com justificativa e autoria.
6. Iniciar movimentação **apenas após liberação** e registrar encerramento e histórico.

**Cenário fictício:** a carga `CQ-2026-001` permanece `EM_ANALISE` porque um documento obrigatório não foi validado; `LiberarCarga` devolve a pendência. A ausência não implica automaticamente bloqueio formal. Somente um ator autorizado, diante de ocorrência crítica, gera `BLOQUEADA` com motivo.

## Riscos, limitações e hipóteses

- Exigências documentais reais dependem da operação, substância e legislação vigente; o PDF não define catálogo regulatório.
- A classificação de risco deve evoluir para referência versionada e validada.
- Em uso real, autenticação, autorização, segurança, auditoria, concorrência e especialistas são indispensáveis.
- Não há autorização legal ou operacional automática somente porque um atributo `valido` é verdadeiro.
- Armazenagem e estoque da fábrica são **extensões futuras fora do núcleo da Fase 01**.

## Próximas fases

Implementar persistência, API, interface, autenticação, integração documental, consultas operacionais e, somente como módulo separado, recebimento industrial e rastreabilidade de lotes.
