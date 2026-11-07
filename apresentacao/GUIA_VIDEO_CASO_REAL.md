# Vídeo — defesa técnica do QuimiPort em aproximadamente 8 minutos

**Observação:** este é um roteiro de ensaio. A apresentação deve ser falada pelo estudante com compreensão própria. Não alegue pesquisa de campo, implantação ou medição de indicadores.

| Faixa de tempo | Abrir na tela | Explicar com suas palavras |
|---|---|---|
| 0:00–0:45 | README, título | O que é o QuimiPort e qual é a pergunta de negócio |
| 0:45–1:35 | `docs/16-estudo-de-caso.md` | A carga fictícia C-001 chega com pendência; quem trabalha nela? |
| 1:35–2:15 | `docs/17-fontes-e-evidencias.md` | Diferença entre fonte oficial e hipótese de produto; PSP não é substituído |
| 2:15–3:15 | `diagramas/dominio.svg` + `.mmd` | Entidades, valor, agregado raiz e relação produto–carga–documentos |
| 3:15–4:05 | `docs/03-casos-de-uso.md` | UC03, UC04 e UC06 conectados ao problema |
| 4:05–4:55 | `diagramas/status.svg` | Por que a carga não sai de `EM_ANALISE` se a política está pendente |
| 4:55–5:45 | `docs/05-arquitetura.md` | Por que domínio não fica na interface e por que monólito modular |
| 5:45–6:35 | `docs/07-plano-de-qualidade.md` | Caso de teste de documento ausente e cenário válido; erros e mocks |
| 6:35–7:15 | `docs/08-javascript-typescript.md` | Tipo, interface, função de validação, JS moderno |
| 7:15–8:00 | `docs/09-decisoes-e-roadmap.md` | Próximas fases, entrevistas pendentes, integração futura (sem confundir com entrega) |

## Três perguntas que a banca pode fazer

**1. O problema é comprovado no Porto de Santos?**  
Não como falha quantitativamente medida. O processo regulatório é real e documentado; a necessidade de pré-conferência interna é uma **hipótese de produto a validar**. A Fase 01 pede proposta técnica, não piloto real.

**2. Por que não basta um checkbox “documento válido”?**  
Porque o requisito depende da natureza da carga e da operação; a validação real exige política versionada, referência documental, autoridade e histórico. A flag isolada não comprova conformidade.

**3. Por que usar um agregado CargaQuimica?**  
Porque a decisão de liberação depende da consistência entre documentos, inspeção, bloqueios, status e histórico, que não deveriam ser atualizados de forma independente.

## Antes de gravar

Reproduza os diagramas no Mermaid Live Editor, percorra as fontes oficiais e tente explicar o caso C-001 sem consultar esta página. Revise o áudio, a duração e eventuais dados pessoais exibidos na tela.
