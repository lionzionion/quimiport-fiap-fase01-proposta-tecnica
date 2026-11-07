# 07 — Planejamento de qualidade de software

## Estratégia de testes por nível

| Nível | Responsabilidade | Exemplo |
|---|---|---|
| Unitário | Funções puras, VOs e invariantes do agregado | Zero ou `NaN` não é quantidade válida |
| Unitário de caso de uso | Orquestração com repositório fake/mock | Produto inativo impede cadastro da carga |
| Integração | Casos de uso + banco/transações futuros | Status e histórico salvos atomicamente |
| Contrato/API | Entradas, saídas, erros estáveis | Documento inválido retorna erro de domínio mapeado |
| End-to-end futuro | Fluxo completo da UI | Registrar→validar→inspecionar→liberar |

## Prioridades de risco

**Críticas:** liberação indevida; movimentação com bloqueio; cancelamento reativado; classificação ausente; histórico inconsistente; duplicidade de código. **Altas:** vencimento documental, identificação de responsável, concorrência de atualizações. **Médias:** filtros e consulta paginada.

## Cenários planejados

1. Produto sem nome ou classe de risco → erro.
2. Produto inativo → impedir nova carga.
3. Quantidade zero, negativa, infinita ou `NaN` → erro.
4. Responsável técnico ausente → erro.
5. Documento obrigatório ausente → não liberar.
6. Documento exigido expirado → não liberar.
7. Carga bloqueada → não movimentar.
8. Carga cancelada → não liberar.
9. `REGISTRADA` → `FINALIZADA` diretamente → erro.
10. Carga elegível → liberar e gerar histórico com status anterior e novo.
11. Duas requisições simultâneas → não perder atualização (futura integração).
12. Evento de histórico não pode ser omitido em mudança de estado.

## Mocks e dados simulados

Usar `MemoryCargaRepository`, `FakeProdutoRepository`, `FakeClock` e `FakeActorIdentity`, injetados nos casos de uso. Fixtures fictícias devem incluir produto ativo, produto inativo, documentação em dia, documentos ausentes, carga bloqueada e cancelada. **Não usar registros reais de produção ou documentos sensíveis.**

## Critérios de aceite e automação futura

Executar `npm test` no pipeline quando houver código, bloquear merge de testes críticos falhos, medir cobertura das regras mais relevantes e manter testes por comportamento. Cobertura alta sem cenários críticos adequados não garante qualidade. A Fase 01 solicita **plano** de qualidade; testes executáveis são material complementar, não condição obrigatória.

## Pirâmide de testes proposta

| Nível | Alvo | Exemplos |
|---|---|---|
| Unidade | Objetos de valor, entidades e máquina de estados | RN01–RN13; transições válidas e proibidas |
| Aplicação | Orquestração de caso de uso, interfaces e erros | `LiberarCarga` verifica pendências e persiste evento |
| Integração (futura) | Repositório, transações, API e persistência | Concorrência, códigos únicos, consistência de histórico |
| E2E (futura) | Fluxo completo de usuário | Criar produto → carga → documentação → inspeção → liberação |

## Critérios de conclusão de cada regra

- Caso positivo e pelo menos um negativo descritos em formato Dado / Quando / Então.
- Resultado esperado e mensagem de rejeição definidos.
- Regra vinculada a UC e responsável na arquitetura.
- Mudança de estado acompanhada de histórico previsto.
- Massa de teste fictícia identificada e sem dependência de serviço real.

## Exemplo de BDD

**Cenário:** impedir liberação sem documento obrigatório.

**Dado** que a carga `CQ-2026-001` está `EM_ANALISE` e o documento de demonstração `DOC-A` está ausente; **quando** um ator autorizado solicita liberação; **então** o sistema rejeita a transição, informa a pendência, mantém a carga em `EM_ANALISE` e não registra um evento de liberação bem-sucedida.

**Cenário:** liberar carga apta.

**Dado** que a carga está em análise, com política atendida e inspeção favorável quando aplicável; **quando** ocorre a decisão por ator autorizado; **então** o domínio permite `LIBERADA`, gera evento e solicita persistência conjunta.

Os critérios são planejamento de testes. Se houver protótipo local, resultados executados devem ser relatados separadamente e não confundidos com cobertura real de um produto de produção.

## Matriz adicional de testes para a banca

| Cenário | Dado | Quando | Então | Tipo futuro |
|---|---|---|---|---|
| QA01 | Produto sem classificação | Cadastrar produto | Rejeitar e manter catálogo inalterado | Unidade |
| QA02 | Produto inativo | Registrar carga | Não criar carga | Caso de uso com fake |
| QA03 | Carga com documento ausente | Liberar | Manter EM_ANALISE e informar pendência | Domínio + aplicação |
| QA04 | Inspeção desfavorável | Emitir parecer | Alterar para BLOQUEADA com evento | Domínio |
| QA05 | Carga BLOQUEADA | Iniciar movimentação | Rejeitar transição | Unidade |
| QA06 | Carga CANCELADA | Liberar | Rejeitar transição | Unidade |
| QA07 | Carga REGISTRADA | Finalizar | Rejeitar transição | Unidade |
| QA08 | Carga apta e em análise | Liberar | LIBERADA com evento e autor | Caso de uso + integração futura |
| QA09 | Duas versões concorrentes | Salvar a segunda | Sinalizar conflito sem perder histórico | Integração futura |

**Distinção importante:** esta é uma **estratégia planejada** exigida pela Fase 01. Não corresponde a testes executados no repositório de documentação. Os testes do aplicativo-laboratório foram executados separadamente e não equivalem a validação industrial ou portuária.


## Um teste que conecta pesquisa, regra e caso de uso

**Cenário C-001:** [pré-conferência de uma carga com documento pendente](16-estudo-de-caso.md).

```gherkin
Funcionalidade: Pré-conferência documental de carga perigosa
  Cenário: Rejeitar tentativa de liberação com pendência
    Dado que a carga CQ-2026-001 está EM_ANALISE
    E que existe uma política documental P-01 configurada para o cenário
    E que um requisito da política está pendente
    Quando um responsável autorizado solicitar liberação
    Então o sistema rejeita a solicitação informando a pendência
    E a carga permanece EM_ANALISE
    E nenhuma autorização operacional é emitida pelo QuimiPort
```

**Mock necessário:** repositório de carga, provedor da política P-01, identidade do usuário autorizado e relógio. São componentes **planejados**, não evidências de testes executados num porto. Para conferir a origem da política e o que ainda depende de especialistas, leia [Fontes e evidências](17-fontes-e-evidencias.md).
