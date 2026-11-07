# 07 — Plano de qualidade de software

## Objetivo

Definir como validar as regras críticas do QuimiPort **nas próximas fases**. O enunciado da Fase 01 exige estratégia e cenários planejados; não exige backend, testes de integração ou ambiente produtivo já implementados.

## Casos de uso prioritários

`RegistrarCarga`, `ValidarDocumentacao`, `SolicitarInspecao`, `LiberarCarga`, `BloquearCarga`, `CancelarCarga` e `AtualizarStatus`, pois erros nesses fluxos podem permitir decisões incoerentes de segurança.

## Pirâmide proposta

| Nível | Foco | Estratégia |
|---|---|---|
| Unitário | Entidades, VOs e funções puras | Testar entradas válidas e inválidas, sem dependência externa |
| Aplicação | Casos de uso e orquestração | Simular repositórios, políticas e usuário |
| Integração futura | Persistência, HTTP e transação | Banco isolado de teste; garantir gravação de carga e histórico |
| Fluxo principal futuro | Cadastro → análise → liberação → movimentação | Verificar estados, mensagens, registros e ações bloqueadas |
| Segurança futura | Acesso, permissões e concorrência | Tentar ações sem autorização e com versão desatualizada |

## Cenários de teste prioritários

| Cenário | Entrada | Esperado |
|---|---|---|
| Produto sem nome | Nome vazio | Rejeição RN01 |
| Produto sem classe | Classe vazia | Rejeição RN02 |
| Produto inativo | Registro de nova carga | Rejeição RN03 |
| Produto ausente | Carga sem produto | Rejeição RN04 |
| Quantidade zero ou negativa | 0, -10, NaN | Rejeição RN05 |
| Responsável ausente | Carga sem técnico | Rejeição RN06 |
| Documento exigido ausente | Liberar carga com pendência | Rejeição RN07 |
| Documento válido e política definida | Liberar após análise | LIBERADA, se demais condições atendidas |
| Carga bloqueada | Iniciar movimentação | Rejeição RN08 |
| Carga cancelada | Solicitar liberação | Rejeição RN09 |
| Carga em inspeção | Finalizar diretamente | Rejeição RN10 |
| Transição inválida | REGISTRADA → FINALIZADA | Rejeição RN11 |
| Bloqueio válido | Motivo e ator | Evento no histórico RN12 |
| Bloqueio sem motivo | Motivo vazio | Rejeição RN13 |
| Código duplicado | Mesmo código em duas cargas | Conflito RN14 |
| Inspeção reprovada | Solicitar liberação | Rejeição RN15 |
| Política inexistente | Solicitar liberação | Rejeição RN16 |

## Mocks, fixtures e dados simulados

Criar `CargaRepositoryFake`, `ProdutoRepositoryFake`, `PoliticaDocumentalFake` e `ClockFake` para isolamento. Manter cenários em `tests/fixtures/` com códigos, produtos e responsáveis **fictícios** e datas determinísticas. Evitar dependência de serviços externos para testes unitários.

## Estratégia de integração futura

Verificar que carga, mudança de status e evento sejam gravados de maneira atômica; testar rollback em falha e concorrência otimista com `versao`. Ao introduzir HTTP, validar contratos, erros padronizados e regras de autenticação. Em operações reais, exigir auditoria e controles adicionais.

## Critérios de aceite

As regras prioritárias são rastreáveis a cenários de teste, os estados do diagrama são coerentes com as respostas do domínio e alterações em políticas não permitem burlar a autorização. **A existência deste plano não comprova que testes de produção tenham sido executados.**
