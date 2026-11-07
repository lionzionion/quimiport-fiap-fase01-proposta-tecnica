# 16 — Estudo de caso: uma carga com pendência na pré-conferência

## Pergunta de projeto

**Como um terminal pode localizar uma pendência documental antes da movimentação de uma carga perigosa e explicar, posteriormente, por que ela não foi liberada?**

O caso é **fictício e elaborado para testar a proposta**. Não descreve um incidente, entrevista ou processo observado no Porto de Santos.

## O que sabemos a partir de fontes

- O [serviço oficial Porto Sem Papel](https://www.gov.br/pt-br/servicos/obter-autorizacao-para-movimentacao-de-cargas-perigosas-no-porto-sem-papel-psp?id=12324&origem=servico) informa que existe uma Declaração de Carga Perigosa e um processo de registro para embarque/desembarque. **O QuimiPort não emite nem substitui essa declaração**.
- O [Porto de Santos](https://www.portodesantos.com.br/informacoes-operacionais/normas-e-regulamentos/) mantém um conjunto de normas operacionais, inclusive norma de movimentação de mercadorias classificadas pelo IMDG.
- A [ANTAQ](https://www.gov.br/antaq/pt-br/assuntos/sustentabilidade/cargas-perigosas-1) destaca identificação, acondicionamento, documentação e cuidados no manuseio como elementos importantes da segurança.
- O [Código IMDG](https://www.imo.org/en/publications/pages/imdg%20code.aspx) é uma fonte de referência do modal marítimo, mas suas exigências detalhadas **não foram traduzidas integralmente em regras automáticas do projeto**.

**Inferência de design, ainda a validar:** uma equipe de terminal pode se beneficiar de uma trilha interna que agregue referências, pendências e decisões de uma carga. Essas fontes sustentam a relevância do contexto normativo, **não comprovam** perda de produtividade ou falhas em terminais específicos.

## Ficha de cenário — C-001

| Campo | Valor hipotético usado no estudo |
|---|---|
| Carga | `CQ-2026-001` |
| Operação | Movimentação portuária simulada |
| Produto | Produto demonstrativo P-001, identificado e classificado no cadastro |
| Quantidade | 2.000 kg (exemplo, não é dado operacional) |
| Responsável técnico | Referência `RT-001` fictícia |
| Situação inicial | `REGISTRADA` |
| Resultado da conferência interna | Um documento previsto na **política fictícia P-01** está pendente |
| Decisão esperada | Registrar pendência, manter `EM_ANALISE`, impedir `LIBERADA` |

Não nomeamos documentos como **universalmente obrigatórios**. A política P-01 é uma configuração inventada para o exercício; documentação real depende do modal, produto e operação, e deve ser revisada por responsáveis habilitados.

## Jornada do usuário antes e depois (hipótese de produto)

**Sem a ferramenta interna proposta:** o responsável precisa consolidar informações recebidas por múltiplos participantes. Não há demonstração de que esse seja o fluxo efetivo de todos os terminais; é uma hipótese de investigação.

**Com o QuimiPort planejado:**

1. Operador cadastra `CQ-2026-001` vinculando produto, quantidade e responsável.
2. Analista inicia conferência e vincula referências dos documentos apresentados.
3. Política P-01 aponta um requisito pendente. O sistema registra `DOC_PENDENTE` e não autoriza transição `EM_ANALISE → LIBERADA`.
4. O analista registra justificativa e pode consultar o histórico da carga.
5. Após regularização, o sistema **reavalia** os requisitos; não libera automaticamente.
6. Um responsável autorizado toma a decisão e registra o evento — se as condições do fluxo conceitual forem atendidas.

## Critérios de aceite propostos

| ID | Dado | Quando | Então |
|---|---|---|---|
| CA-01 | produto inativo | operador tenta registrar carga | cadastro é rejeitado com motivo |
| CA-02 | documento pendente | analista tenta liberar | retorna pendência, estado fica `EM_ANALISE` |
| CA-03 | carga `BLOQUEADA` | operador solicita movimentação | ação é rejeitada |
| CA-04 | regularização documental | documentação é aceita | carga fica **elegível à análise**, não é liberada automaticamente |
| CA-05 | qualquer mudança de status | ação autorizada é concluída | histórico contém quem, quando, estado anterior, novo estado e motivo |

## O que medir num futuro piloto (sem números inventados)

- Tempo entre registro e identificação da primeira pendência.
- Percentual de tentativas de liberação que retornam inconsistências documentais.
- Tempo médio de regularização por tipo de pendência.
- Percentual de decisões com trilha de auditoria completa.

**Nenhuma dessas métricas foi medida.** Devem ser comparadas com uma linha de base real apenas após autorização e acompanhamento de um terminal.

## Limites de responsabilidade

QuimiPort é um **sistema interno de apoio ao fluxo documental**, não substituto de Porto Sem Papel, IMDG, inspeção, profissionais legalmente responsáveis nem procedimentos do terminal. Não existe regra de segurança universal implementada neste trabalho.
