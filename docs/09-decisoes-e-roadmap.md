# 09 — Decisões arquiteturais (ADRs) e roadmap

## ADR-001 — Monólito modular como ponto de partida

**Decisão:** uma aplicação modular no início, sem microsserviços. **Justificativa:** complexidade de domínio e requisitos ainda em evolução, com menor sobrecarga de infraestrutura e deploy. **Consequência:** definir módulos e interfaces claras desde o começo; extrair serviços somente se requisitos de escala e autonomia justificarem.

## ADR-002 — Agregado CargaQuimica protege liberação

**Decisão:** centralizar invariantes de documentação, transição e histórico na raiz `CargaQuimica`. **Justificativa:** impedir atualização direta de status e decisões inconsistentes. **Consequência:** operações passam por métodos do domínio/casos de uso, não por `UPDATE status` isolado.

## ADR-003 — TypeScript com tipagem explícita

**Decisão:** manter tipos compartilhados e contratos de interface. **Justificativa:** evitar estados inválidos e tornar comunicação entre módulos legível e testável. **Consequência:** custo inicial de modelagem e builds, compensado por manutenção mais segura.

## ADR-004 — Regras de documentos parametrizáveis

**Decisão:** evitar fixar uma lista universal de documentos no código. **Justificativa:** as exigências dependem da natureza da carga e da operação. **Consequência:** política de validação precisará ser definida, versionada e revisada por responsáveis competentes em uma futura implementação.

## Roadmap proposto

| Etapa | Evolução |
|---|---|
| Fase 01 | Modelagem de domínio, casos de uso, diagramas, plano de qualidade e decisões técnicas |
| Protótipo complementar | Testes das invariantes de domínio e fluxo didático local |
| Próxima fase técnica | API, banco persistente, autenticação por papéis e testes de integração |
| Evolução operacional | Anexos documentais, versão de política, auditoria, relatórios e observabilidade |
| Extensão opcional | Integração Porto → Fábrica; recebimento, quarentena e estoque por lote |

**Fase 01 não exige implementação do roadmap.** Os recursos são intenções de projeto condicionadas a requisitos futuros.

## ADR-005 — Fluxo conservador de cancelamento e inspeção

**Decisão:** permitir cancelamento somente de `REGISTRADA`, `EM_ANALISE` ou `BLOQUEADA`; tratar `CANCELADA` e `FINALIZADA` como terminais; exigir retorno de `EM_INSPECAO` a `EM_ANALISE` após parecer favorável. **Justificativa:** manter o comportamento documentado e legível sem criar autorização automática. **Consequência:** casos posteriores à liberação e interrupção de movimentação precisam ser detalhados em futuras entrevistas, sem alegar suporte no escopo inicial.

## ADR-006 — Não confundir protótipo com operação real

**Decisão:** documentação e diagramas representam decisões de produto para a Fase 01. **Justificativa:** não foi realizado levantamento jurídico/regulatório, nem validação por operação portuária real. **Consequência:** políticas documentais, permissões, auditoria e validação de risco precisam de especificação especializada antes da produção.

## ADR-007 — Pré-conferência interna em vez de substituir sistemas oficiais

**Contexto:** Porto Sem Papel já oferece procedimento formal de declaração de cargas perigosas, enquanto os operadores precisam lidar com referências e etapas da cadeia documental. **Hipótese não validada em campo:** há valor em consolidar pendências e decisões para a equipe do terminal.

**Decisão:** QuimiPort será uma ferramenta **interna de pré-conferência e rastreabilidade**; não emitirá autorizações oficiais nem afirmará conformidade automática com IMDG/autoridades.

**Alternativas consideradas:** (a) substituir PSP — descartada por competência e escopo; (b) painel apenas de cadastro — insuficiente para explicar decisões; (c) módulo de pré-conferência — selecionado como hipótese testável.

**Consequência:** necessidade de definir fonte confiável, responsável, política aplicável e status documental para cada processo. Evidência: [fontes](17-fontes-e-evidencias.md) e [caso C-001](16-estudo-de-caso.md).

**Risco não resolvido:** sem entrevistas, não sabemos se há demanda real por mais uma ferramenta ou se integrações existentes já atendem esse processo.
