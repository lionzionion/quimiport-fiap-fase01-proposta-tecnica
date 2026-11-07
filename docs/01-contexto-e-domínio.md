# 01 — Entendimento do domínio e contexto

## Situação-problema

**Recorte investigado:** pré-conferência documental e rastreabilidade de pendências antes da movimentação de uma carga perigosa. A operação portuária real possui processos oficiais — como o Porto Sem Papel — que **não serão substituídos**. [Levantamento e fontes](17-fontes-e-evidencias.md) · [Caso fictício C-001](16-estudo-de-caso.md).


Em um terminal portuário fictício inspirado no Porto de Santos, cargas químicas percorrem processos de cadastro, conferência documental, inspeção e decisão de movimentação. O controle descentralizado dificulta responder: *qual é o produto? qual o risco declarado? quem é o responsável? existem pendências? quem autorizou ou bloqueou?*

O QuimiPort propõe um registro único da **carga química** e de suas mudanças de estado, com regras de negócio explícitas que impeçam movimentos contraditórios. A decisão final, em operação real, dependeria de validações legais, ambientais, de segurança e de pessoas habilitadas; essas verificações **não** estão aqui implementadas nem presumidas.

## Perfis de usuários propostos

| Perfil | Responsabilidade no sistema proposto |
|---|---|
| Operador portuário | Cadastrar cargas e acompanhar status |
| Analista documental | Registrar e validar referências documentais |
| Analista de qualidade / inspetor | Solicitar ou emitir parecer de inspeção |
| Responsável técnico | Ser associado à carga e acompanhar restrições técnicas |
| Gestor operacional | Revisar bloqueios, acompanhar indicadores e decisões |
| Administrador | Gerenciar usuários, perfis e parâmetros futuramente |

Na Fase 01, **descrevemos** permissões previstas; não há necessidade de implementá-las.

## Informações controladas

Produto químico (código, nome, classe de risco, ativo), carga (código, produto, quantidade/unidade, responsável, situação), documentos exigidos e validados, inspeções e pareceres, motivos de bloqueio, eventos de histórico e data/hora de cada decisão.

## Linguagem ubíqua

| Termo | Definição usada em documentação e código futuro |
|---|---|
| Produto químico | Item do catálogo identificado e classificado quanto ao risco |
| Carga química | Unidade de controle operacional com produto, quantidade e status |
| Documento obrigatório | Exigência documental associada à política de validação da carga |
| Inspeção | Verificação registrada por analista autorizado, com parecer |
| Bloqueio | Restrição que impede a liberação/movimentação |
| Liberação | Decisão explícita de que condições **definidas pela política** foram atendidas |
| Movimentação | Etapa operacional posterior à liberação |
| Histórico | Registro temporal de ações e transições de status |
| Agregado | Conjunto de entidades protegido por invariantes transacionais |

## Decisões e riscos

- Não cadastrar carga sem produto associado ativo, classe de risco, quantidade positiva e responsável técnico.
- Não liberar carga com documentação pendente, situação bloqueada ou cancelada.
- Registrar autor, momento e justificativa das decisões; em produção, exigir identidade autenticada.
- Não supor que uma lista didática de documentos represente obrigações legais universais.
- Evitar uma classe de risco textual livre em produção; versionar catálogos e políticas aplicáveis.

## Evolução

O núcleo de cargas portuárias permanece separado de módulos futuros: fábrica, armazenamento industrial, estoque por lote, ordens de consumo, integrações externas e monitoramento de operações.

## Jornada portuária planejada (cenário fictício)

1. **Cadastro do produto:** catálogo registra identificação, classe de risco declarada e situação ativa/inativa.
2. **Registro da carga:** operador informa produto, quantidade/unidade e responsável técnico.
3. **Análise documental:** analista consulta política documental aplicável e registra referência e situação de cada documento exigido.
4. **Inspeção:** o setor de qualidade registra solicitação e parecer; ocorrência crítica leva a bloqueio.
5. **Decisão:** responsável autorizado libera a carga somente quando as validações planejadas forem satisfeitas.
6. **Movimentação e encerramento:** status é atualizado por transições válidas, com histórico da operação.

**Exemplo:** a carga fictícia `CQ-2026-001`, vinculada a um produto classificado, fica em `EM_ANALISE` enquanto faltar um documento exigido pela política de demonstração; a tentativa de `LIBERAR` é recusada e gera resultado de validação. A lista real de documentos, classes de risco e responsáveis habilitados será definida com especialistas e legislação pertinente em fase futura.

## Limites e premissas

- Operações, códigos, produtos e pessoas apresentados nos exemplos são fictícios.
- O sistema *planejado* não substitui licenças, procedimentos de segurança ou autorização de profissionais competentes.
- O enunciado define o **contexto portuário**. Controle de fábrica, estoque por lote e integração com ERP pertencem ao roadmap opcional.
- A decisão operacional de segurança não será automatizada apenas por uma flag `valido`; para uso real exigirá critérios e políticas verificáveis.
