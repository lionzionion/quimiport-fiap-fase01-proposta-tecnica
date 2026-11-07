# 17 — Fontes consultadas, inferências e limites da pesquisa

Este documento separa **o que a fonte realmente diz** do que é **hipótese ou decisão própria da proposta**. Links consultados para revisão documental em novembro de 2026. A validade legal deve ser verificada novamente antes de qualquer operação real.

| Fonte primária | O que sustenta | O que NÃO podemos concluir apenas dela |
|---|---|---|
| [Porto de Santos — Normas e regulamentos](https://www.portodesantos.com.br/informacoes-operacionais/normas-e-regulamentos/) | Existem normas locais para movimentação de mercadorias perigosas classificadas pelo IMDG (NAP de operação publicada na página). | Que o QuimiPort corresponde integralmente à norma ou que os terminais sofrem atraso operacional mensurado. |
| [Porto Sem Papel — autorização de cargas perigosas](https://www.gov.br/pt-br/servicos/obter-autorizacao-para-movimentacao-de-cargas-perigosas-no-porto-sem-papel-psp?id=12324&origem=servico) | Há procedimento formal envolvendo registro/declaração de carga perigosa. | Que um software independente possa emitir a autorização ou substituir o PSP. |
| [ANTAQ — Cargas perigosas](https://www.gov.br/antaq/pt-br/assuntos/sustentabilidade/cargas-perigosas-1) | Importância da identificação, acondicionamento, documentação e segurança no manuseio de cargas perigosas. | Exatamente quais documentos toda carga precisa apresentar. |
| [IMO — IMDG Code](https://www.imo.org/en/publications/pages/imdg%20code.aspx) | Código de referência do transporte marítimo de cargas perigosas; a edição 2024, emenda 42-24, é obrigatória desde 2026. | Regras específicas por produto sem consultar a edição integral aplicável. |
| [ANTT — Produtos perigosos](https://www.gov.br/antt/pt-br/assuntos/cargas/produtos-perigosos) | Exigências relacionadas ao transporte **rodoviário** de produtos perigosos; Resolução 5.998/2022 e alterações. | Que a regra rodoviária vale automaticamente para a movimentação marítima. A ficha de emergência não deve ser tratada como documento rodoviário universalmente obrigatório. |
| [FIAP — PDF Tech Challenge Fase 01](../docs/15-matriz-de-aderencia-pdf.md) | Requisitos acadêmicos de DDD, diagramas, arquitetura, qualidade e vídeo. | Que o trabalho de pesquisa ou a implementação estão homologados. |

## Como uma fonte se torna requisito de produto

**Exemplo de raciocínio:**

1. **Fato pesquisado:** Porto Sem Papel prevê declaração de carga perigosa.
2. **Pergunta levantada:** como o analista encontra, no acompanhamento interno, as referências e pendências que antecedem a movimentação?
3. **Hipótese:** uma fila de pendências e histórico de decisões poderiam facilitar a conferência interna.
4. **Requisito de produto proposto:** associar referências documentais a uma carga e impedir liberação na presença de pendências configuradas para o cenário.
5. **Modelagem DDD:** `CargaQuimica` é a raiz que controla transições e histórico; `DocumentoCarga` é associado a ela.
6. **Teste planejado:** tentar liberar carga com documento pendente e verificar rejeição.
7. **Validação ainda necessária:** entrevistas com operação, segurança e jurídico; definição da política documental real.

As etapas 2 a 6 são **raciocínio de projeto**. Não são exigências textuais de uma norma nem achados de pesquisa de campo.

## Decisões de escopo

- O foco acadêmico é o **porto**. A fábrica é uma extensão futura, não a solução do problema da Fase 01.
- A política documental não será uma lista universal codificada.
- Uma flag `documento.valido` não basta para validação jurídica; são necessárias referências, identidade, data, versão e critérios de avaliação.
- O cadastro de dados **não transforma** o sistema em fiscalizador ou órgão autorizador.

## Fontes sobre os diagramas e a representação

- [Mermaid — documentação oficial](https://mermaid.js.org/)
- [Mermaid Live Editor](https://mermaid.live/)
- [Graphviz — documentação oficial](https://graphviz.org/documentation/)
- [Graphviz DOT Language](https://graphviz.org/doc/info/lang.html)

Essas são fontes **de ferramentas de modelagem**, não referências regulatórias.
