# QuimiPort | FIAP Pós-Tech — Tech Challenge, Fase 01

**Proposta técnica e arquitetural para o gerenciamento de cargas químicas em contexto portuário**, inspirado nas operações logísticas do Porto de Santos.

**Autor da proposta:** Leandro Dias  
**Curso:** Pós-Tech Full Stack Development — FIAP  
**Disciplinas:** JavaScript Avançado · Arquitetura de Software com TypeScript · Domain-Driven Design · Qualidade de Software  
**Natureza:** projeto acadêmico conceitual — **não é software homologado para operações reais**.

> **Escopo da Fase 01:** o enunciado solicita documentação técnica, modelagem do domínio, casos de uso, regras, arquitetura, diagramas, plano de qualidade, decisões de JavaScript/TypeScript, **link de repositório Git** e **vídeo de 5 a 10 minutos**. Não exige frontend, backend ou banco de dados funcionando nesta etapa.

## O problema

O acompanhamento descentralizado de produtos, classificações de risco, documentação, inspeções e autorizações pode dificultar a rastreabilidade das decisões sobre cargas químicas. O **QuimiPort** propõe centralizar esses dados e definir regras consistentes para que uma carga seja registrada, analisada, liberada, bloqueada ou cancelada conforme condições documentadas.

**Cenário de exemplo:** uma carga apresenta documentação obrigatória pendente. A proposta mantém a carga em análise e impede sua liberação, registrando o motivo e o responsável pela decisão. Os requisitos e controles regulatórios reais devem ser definidos e validados com especialistas antes de qualquer uso operacional.

## Modelagem visual — dois diagramas obrigatórios

**Domínio, entidades e agregados**  
[Ver diagrama](diagramas/dominio.svg) · [SVG ampliável](diagramas/dominio.svg) · [Fonte Mermaid](diagramas/dominio.mmd)

![Diagrama conceitual de domínio do QuimiPort](diagramas/dominio.svg)

**Máquina de estados da carga**  
[Ver diagrama](diagramas/status.svg) · [SVG ampliável](diagramas/status.svg) · [Fonte Mermaid](diagramas/status.mmd)

![Fluxo de estados de uma carga química](diagramas/status.svg)

## Documentação — requisitos da Fase 01

| Ordem | Documento | Conteúdo |
|---|---|---|
| 01 | [Entendimento do domínio](docs/01-contexto-e-domínio.md) | Problema, atores, processos, riscos e linguagem ubíqua |
| 02 | [Modelagem DDD](docs/02-ddd.md) | Entidades, VOs, agregados, atributos, responsabilidades e relações |
| 03 | [Casos de uso](docs/03-casos-de-uso.md) | 11 casos: objetivo, ator, entrada, saída, regras e erros |
| 04 | [Regras de negócio](docs/04-regras-de-negocio.md) | RN01–RN16 e responsabilidades arquiteturais |
| 05 | [Arquitetura e organização](docs/05-arquitetura.md) | Monólito modular, camadas, contratos e pastas |
| 06 | [Diagramas técnicos](docs/06-diagramas.md) | Domínio e status obrigatórios; arquitetura complementar |
| 07 | [Planejamento de qualidade](docs/07-plano-de-qualidade.md) | Testes planejados, cenários, mocks e integração futura |
| 08 | [JavaScript e TypeScript](docs/08-javascript-typescript.md) | Tipos, interfaces, funções puras, módulos, async/await e generics |
| 09 | [Decisões e roadmap](docs/09-decisoes-e-roadmap.md) | Justificativas arquiteturais e evolução planejada |
| 10 | [Roteiro de vídeo](docs/10-roteiro-video.md) | Estrutura para apresentação de 5–10 minutos |
| 11 | [Checklist de entrega](docs/11-checklist-entrega.md) | Verificações antes da submissão |
| 12 | [Extensão industrial futura](docs/12-extensao-industrial-futura.md) | Evolução opcional, **fora do escopo obrigatório** |
| 13 | [Como entregar à FIAP](docs/13-como-entregar-na-fiap.md) | Procedimento e pontos a confirmar no portal |
| 14 | [Texto-base da apresentação](docs/14-fala-apresentacao.md) | Material de ensaio |
| 15 | [Matriz de aderência ao PDF](docs/15-matriz-de-aderencia-pdf.md) | Correspondência entre enunciado e documentação |

## Apresentação

- [Slides em PDF — 11 telas, alvo de ~8 minutos](apresentacao/QuimiPort_Fase01_Slides.pdf)
- [PowerPoint editável](apresentacao/QuimiPort_Fase01_Slides_Editavel.pptx)
- [Roteiro de fala por slide](apresentacao/ROTEIRO_FALA_8_MINUTOS.md)
- [Checklist de gravação do vídeo](apresentacao/PREPARAR_VIDEO.md)

**Vídeo:** ainda não gravado. O link será acrescentado após a gravação, de acordo com o método de entrega autorizado pelo portal FIAP.

## Decisões resumidas

- `CargaQuimica` é raiz de agregado, responsável por invariantes de liberação, bloqueio e transição de status. `ProdutoQuimico` é agregado de catálogo independente.
- **Monólito modular inicial**, com separação entre apresentação, aplicação, domínio e infraestrutura; repositórios são interfaces, não implementações acopladas a banco.
- Sem documentos obrigatórios aprovados, ou com parecer desfavorável quando aplicável, uma carga **não é liberada** no fluxo conceitual.
- A classificação de riscos e a política documental aqui são **modelos acadêmicos**, não validação de exigências oficiais para produtos específicos.
- A integração posterior com o recebimento e o estoque de uma fábrica é uma **proposta de evolução**, não a entrega portuária da Fase 01.

## Verificação da documentação

Execute opcionalmente (requer Python 3):

```bash
python scripts/validar_entrega.py
```

A verificação examina estrutura e links internos da documentação e presença dos diagramas; **não equivale a testes funcionais nem a aprovação acadêmica**. Se o GitHub Actions estiver habilitado, a mesma verificação poderá ser executada nos commits.

## Situação da entrega

Documentos e slides: **preparados para revisão autoral**. Repositório publicado. Permanecem pendentes a confirmação da entrega individual pela FIAP, a verificação do prazo e do procedimento no portal, a gravação do vídeo de 5–10 minutos e a submissão formal.

## Link oficial do projeto

https://github.com/lionzionion/quimiport-fiap-fase01-proposta-tecnica
