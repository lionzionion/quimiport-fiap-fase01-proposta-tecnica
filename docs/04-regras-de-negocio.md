# 04 — Catálogo de regras de negócio

| ID | Regra projetada | Módulo responsável | Teste planejado |
|---|---|---|---|
| RN01 | Produto exige nome | Domínio/ProdutoQuimico | Nome vazio rejeitado |
| RN02 | Produto exige classificação de risco | Domínio/ProdutoQuimico | Classe vazia rejeitada |
| RN03 | Produto inativo não gera carga nova | Caso de uso + domínio | Produto inativo rejeitado |
| RN04 | Carga exige produto associado | Domínio/CargaQuimica | Sem produto rejeitado |
| RN05 | Quantidade deve ser finita e maior que zero | VO QuantidadePositiva | Zero, negativo, NaN rejeitados |
| RN06 | Carga exige responsável técnico | Domínio/CargaQuimica | Responsável vazio rejeitado |
| RN07 | Carga não pode ser liberada sem documentação exigida | Política documental + CargaQuimica | Documento faltante rejeitado |
| RN08 | Carga bloqueada não entra em movimentação | CargaQuimica | Movimentação bloqueada rejeitada |
| RN09 | Carga cancelada não pode ser liberada | CargaQuimica | Liberação cancelada rejeitada |
| RN10 | Carga em inspeção não pode ser finalizada sem liberação | CargaQuimica | Finalização em inspeção rejeitada |
| RN11 | Transições precisam obedecer estados permitidos | CargaQuimica | Salto REGISTRADA→FINALIZADA rejeitado |
| RN12 | Toda decisão de status registra histórico | CargaQuimica | Evento com status anterior/novo |
| RN13 | Motivo de bloqueio é obrigatório | VO MotivoBloqueio | Motivo vazio rejeitado |
| RN14 | Código de carga não pode duplicar | Caso de uso + repositório | Duplicata retorna conflito |
| RN15 | Inspeção desfavorável impede liberação no fluxo proposto | CargaQuimica + política de inspeção | Parecer reprovação causa BLOQUEADA |
| RN16 | Sem política documental aplicável definida, liberação não é autorizada | Caso de uso + PoliticaDocumental | Política ausente rejeita liberação |

## De onde surgiram as regras? 

As regras **RN01–RN11** correspondem a exigências e exemplos do enunciado acadêmico ou à explicitação dos estados planejados. **RN12–RN16** desenvolvem o modelo para garantir rastreabilidade, motivo, unicidade, inspeção e política configurável; são decisões de projeto que precisam ser justificadas e validadas. A pesquisa documental do Porto de Santos e do [Porto Sem Papel](17-fontes-e-evidencias.md) motivou a atenção à conferência, **mas não é prova** de que uma determinada lista de documentos ou máquina de estados seja legalmente obrigatória.

**Experimento conceitual C-001:** RN07 e RN16 impedem liberação com pendência ou sem política de referência; RN11 restringe transições; RN12 determina trilha de decisões. [Caso completo e critérios de aceite](16-estudo-de-caso.md).

## Localização das decisões

A API identifica requisições e traduz erros; **não** decide a validade do domínio. O caso de uso carrega referências e coordena persistência; a **entidade/agregado** protege transições. O repositório garante armazenamento e unicidade complementar quando houver banco. Esse desenho evita que uma interface diferente possa contornar a regra.

## Políticas a detalhar em fases futuras

O documento oficial da Fase 01 **não define** quais documentos são universalmente exigidos, nem o modelo exato de todas as transições. O projeto deve registrar essas hipóteses explicitamente. Em produção, política documental e classificação dependem de produto, operação e exigências legais aplicáveis; o exercício não presume validação normativa automática.

## Matriz de rastreabilidade para validação da entrega

| Regra | Caso(s) de uso | Elemento do domínio | Cenário de qualidade |
|---|---|---|---|
| RN01 / RN02 | UC01 | ProdutoQuimico / ClassificacaoRisco | Nome/classe em branco |
| RN03 | UC02, UC03 | ProdutoQuimico | Produto inativo no registro |
| RN04–RN06 | UC03 | CargaQuimica / QuantidadePositiva | Produto ausente, zero, negativo, sem responsável |
| RN07 | UC04, UC06 | DocumentoCarga / PoliticaDocumental | Falta ou invalidez documental |
| RN08–RN10 | UC05–UC09 | CargaQuimica / StatusCarga | Bloqueada/cancelada/inspeção não avançam |
| RN11–RN13 | UC06–UC09, UC11 | CargaQuimica / EventoHistorico | Transição inválida, falta de histórico/motivo |
| RN14 | UC03 | Registro de cargas / repositório | Código duplicado |
| RN15 | UC05, UC06, UC07 | Inspecao / CargaQuimica | Parecer desfavorável bloqueia |
| RN16 | UC04, UC06 | PoliticaDocumental / caso de uso | Política não definida impede liberação |

**Escopo do desafio:** as regras documentadas são a proposta do projeto; critérios de documentação e permissões de operação real são requisitos externos que deverão ser elicitados antes de qualquer adoção em ambiente portuário.

## Decisões revisadas após simulação da banca

- A inexistência de documento obrigatório gera pendência documental, **não muda automaticamente** a carga para `BLOQUEADA`. A saída `BLOQUEADA` exige evento e motivo.
- `CANCELADA` e `FINALIZADA` são terminais no desenho atual; UC09 restringe o cancelamento aos estados `REGISTRADA`, `EM_ANALISE` e `BLOQUEADA`.
- As regras RN15 e RN16 são **premissas propostas pela equipe** para completar o modelo, e não exigências regulatórias extraídas do PDF.
- É uma **pendência de evolução** definir qual ator pode interromper movimentação após o início, que ainda não possui transição explícita.
