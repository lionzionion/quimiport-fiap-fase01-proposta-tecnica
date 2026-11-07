# 04 — Regras de negócio e rastreabilidade

| ID | Regra proposta | Localização arquitetural | Teste planejado |
|---|---|---|---|
| RN01 | Produto exige nome | Domínio/ProdutoQuimico | Rejeitar nome vazio |
| RN02 | Produto exige classe de risco | Domínio/ProdutoQuimico | Rejeitar classe vazia |
| RN03 | Produto inativo não origina carga nova | Aplicação + domínio | Rejeitar inativo |
| RN04 | Carga exige produto associado | Domínio/CargaQuimica | Rejeitar produto ausente |
| RN05 | Quantidade finita e maior que zero | VO QuantidadePositiva | Rejeitar zero, negativo, NaN |
| RN06 | Carga exige responsável técnico | Domínio/CargaQuimica | Rejeitar sem responsável |
| RN07 | Sem documentação obrigatória validada, não liberar | Política documental + agregado | Recusar pendência |
| RN08 | Bloqueada não entra em movimentação | Agregado | Recusar movimento |
| RN09 | Cancelada não é liberada | Agregado | Recusar liberação |
| RN10 | Inspeção não finaliza sem liberação | Agregado | Recusar finalização |
| RN11 | Transições obedecem à máquina de estados | Agregado | Recusar salto inválido |
| RN12 | Toda decisão de status cria histórico | Agregado | Conferir evento de transição |
| RN13 | Bloqueio exige justificativa | VO MotivoBloqueio | Rejeitar motivo vazio |
| RN14 | Código de carga não duplica | Caso de uso + repositório | Retornar conflito de duplicidade |
| RN15 | Inspeção desfavorável impede liberação | Agregado + política de inspeção | Rejeitar parecer desfavorável |
| RN16 | Sem política documental aplicável, não liberar | Aplicação + política | Rejeitar política ausente |

## Onde ficam as regras

**Apresentação:** valida formato, não decide liberação. **Aplicação:** coordena referências, transação e permissões. **Domínio:** protege invariantes de registro, status e bloqueio. **Infraestrutura:** aplica persistência, unicidade e integração. Uma interface diferente não poderá contornar as regras do domínio.

## Rastreabilidade

| Casos | Regras | Elementos |
|---|---|---|
| UC01–UC02 | RN01–RN03 | ProdutoQuimico, ClassificacaoRisco |
| UC03 | RN03–RN06, RN14 | CargaQuimica, QuantidadePositiva, repositório |
| UC04 e UC06 | RN07, RN15, RN16 | DocumentoCarga, Inspecao, PoliticaDocumental |
| UC05–UC09 | RN08–RN13 | CargaQuimica, StatusCarga, EventoHistorico |
| UC10–UC11 | RN12 e regras de acesso futuro | Repositórios, histórico |

**Premissas explícitas:** faltas documentais geram pendência, não bloqueio automático; `CANCELADA` e `FINALIZADA` são terminais; RN15 e RN16 são decisões de projeto, não leis extraídas do enunciado. Política documental, classificação e requisitos normativos deverão ser elicitados e validados para operação real.
