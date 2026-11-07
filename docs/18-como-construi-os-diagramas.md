# 18 — Como os diagramas foram construídos e como reproduzi-los

A explicação abaixo documenta **os arquivos e ferramentas usados na preparação da versão atual**. Não atribui ao estudante uma atividade manual que ele ainda não executou. Reproduzir o processo no próprio computador é uma etapa recomendada antes da entrega.

## Por que dois tipos de diagrama?

1. **Diagrama de domínio (obrigatório):** expressa quais entidades existem, quem é agregado raiz, quais são os objetos de valor e os relacionamentos. A primeira decisão foi usar `CargaQuimica` como raiz, porque documentação e estado não deveriam ser alterados isoladamente.
2. **Fluxo de status (obrigatório):** expressa **o que pode mudar**. Começamos com os estados `REGISTRADA`, `EM_ANALISE`, `EM_INSPECAO`, `LIBERADA`, `EM_MOVIMENTACAO`, `BLOQUEADA`, `CANCELADA` e `FINALIZADA`. Depois verificamos contradições como `BLOQUEADA → EM_MOVIMENTACAO` e removemos esse atalho.
3. **Diagrama de arquitetura (opcional):** mostra onde ficam os casos de uso e as regras; evita confundir controller com validação de negócio.

## Ferramentas e arquivos reais do repositório

| Formato | Uso | Arquivo |
|---|---|---|
| `.mmd` | Descrição textual em Mermaid; o GitHub consegue mostrar o código renderizado | [`dominio.mmd`](../diagramas/dominio.mmd), [`status.mmd`](../diagramas/status.mmd) |
| `.dot` | Descrição visual em Graphviz DOT; base das imagens SVG ilustrativas | [`dominio.dot`](../diagramas/dominio.dot), [`status.dot`](../diagramas/status.dot) |
| `.svg` | Imagem vetorial ampliável, gerada a partir do Graphviz DOT | [`dominio.svg`](../diagramas/dominio.svg), [`status.svg`](../diagramas/status.svg) |

**Nota de transparência:** Mermaid e Graphviz são **duas representações de um mesmo modelo conceitual**; suas posições gráficas diferem. As imagens `.svg` atuais foram geradas com **Graphviz 2.42.4**. O Mermaid não foi a ferramenta de exportação desses SVGs.

## Reproduza você mesmo — caminho 1, sem instalar nada

1. Abra [Mermaid Live Editor](https://mermaid.live/).
2. No GitHub, abra `diagramas/dominio.mmd`, clique em **Raw** e copie o conteúdo.
3. Cole no painel de código do Mermaid Live Editor.
4. Identifique `class ProdutoQuimico`, `class CargaQuimica` e os conectores de composição `*--`.
5. Altere **temporariamente** uma cardinalidade para observar o efeito; depois restaure a versão original.
6. Repita com `diagramas/status.mmd`. Tente adicionar `BLOQUEADA --> EM_MOVIMENTACAO` e explique por que isso viola RN08. **Não salve** essa ligação inválida.
7. Confira as duas imagens ampliáveis no README e anote as diferenças de organização visual.

## Reproduza você mesmo — caminho 2, exportando SVG

Instale o [Graphviz](https://graphviz.org/download/) em seu computador. No terminal da pasta raiz do projeto, execute:

```powershell
# Execute no PowerShell, após instalar o Graphviz e disponibilizar `dot` no PATH.
dot -V
dot -Tsvg diagramas/dominio.dot -o diagramas/dominio.svg
dot -Tsvg diagramas/status.dot -o diagramas/status.svg
```

As imagens podem mudar ligeiramente de posição conforme a versão do Graphviz. O conteúdo modelado deve continuar consistente. Para verificar que o desenho realmente é reproduzível, foi feito novo render local nesta revisão.

## Do texto ao desenho — sequência de decisões

| Etapa | Decisão de modelagem | Motivo |
|---|---|---|
| 1 | `ProdutoQuimico` com classificação de risco | Sem classe de risco, não é possível propor validações coerentes |
| 2 | `CargaQuimica` referencia produto e responsável | Permite rastrear qual produto e quem assumiu a responsabilidade |
| 3 | `DocumentoCarga`, `Inspecao` e `EventoHistorico` vinculados à carga | Decisões de liberação dependem desses registros |
| 4 | `QuantidadePositiva` como objeto de valor | Impede zero/negativo no domínio |
| 5 | `EM_INSPECAO` retorna para `EM_ANALISE` após parecer favorável | Parecer positivo não equivale a autorização final |
| 6 | `BLOQUEADA` só retorna para reanálise mediante justificativa | Remoção de pendência não causa liberação automática |

## Como explicar ao professor

> “Eu modelei primeiro as entidades, depois escolhi o agregado que deveria proteger a regra mais crítica: a liberação. Escrevi as relações em Mermaid e usei Graphviz para criar as imagens vetoriais. Para testar a coerência, tentei imaginar operações inválidas, como movimentar uma carga bloqueada, e confrontei o diagrama com as regras RN08 e RN11.”

**Esse é um roteiro de explicação a estudar e adaptar, não uma declaração de experiência já realizada pelo estudante.** Antes da gravação, refaça os passos e confirme que consegue justificar cada seta e relação.

## Cuidado com consistência

Quando alterar um estado ou relação, revise **ambas** as fontes `.mmd` e `.dot`, os SVGs, `docs/03-casos-de-uso.md`, `docs/04-regras-de-negocio.md` e os cenários do plano de qualidade. O GitHub Actions atual valida links e presença de arquivos, mas **não prova equivalência semântica entre as duas sintaxes**.
