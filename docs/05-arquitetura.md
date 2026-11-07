# 05 — Arquitetura proposta

## Estilo adotado

**Monólito modular inicial com separação por camadas e fronteiras de domínio.** Essa opção reduz a complexidade de implantação e favorece consistência transacional enquanto o produto é pequeno. Microsserviços ficam para uma evolução justificada por escala e autonomia de equipes.

## Camadas e responsabilidades

| Camada | Responsabilidade | Não deve fazer |
|---|---|---|
| Apresentação | Formulários, controladores HTTP, feedback e validação superficial | Definir critério de liberação |
| Aplicação | Orquestrar casos de uso, permissões e transações | Alterar status sem passar pelo domínio |
| Domínio | Entidades, VOs, políticas, invariantes, transições, erros | Conhecer HTTP, SQL ou interface |
| Infraestrutura | Banco, adaptadores, integrações e persistência | Autorizar uma carga por conta própria |

**Direção das dependências:** apresentação → aplicação → domínio; infraestrutura implementa interfaces de repositório declaradas nas camadas internas.

## Organização de pastas planejada

```text
quimiport/
├── docs/
├── src/
│   ├── domain/
│   │   ├── carga/
│   │   ├── produto/
│   │   └── shared/
│   ├── application/
│   │   ├── use-cases/
│   │   └── ports/
│   ├── infrastructure/
│   │   ├── persistence/
│   │   └── integrations/
│   └── presentation/
│       └── http/
└── tests/
    ├── unit/
    ├── integration/
    └── fixtures/
```

Esta árvore é uma **proposta futura**; a Fase 01 requer documentação e diagramas, não que toda a aplicação esteja implementada.

## Caso de uso `LiberarCarga`

`UI → HTTP → LiberarCargaUseCase → CargaRepository → CargaQuimica + PoliticaDocumental → EventoHistorico → Persistência → Resposta`.

O caso de uso carrega o agregado, identifica o decisor, obtém a política aplicável, verifica o resultado documental e inspeção, solicita a transição e persiste estado/histórico na mesma transação.

## Portas e adaptadores

`CargaRepository` e `ProdutoRepository` são **interfaces**. Uma implementação `SqlCargaRepository` futura não deve interferir nas regras do domínio. Trocar banco ou UI não deve exigir mudar `CargaQuimica`.

## Segurança, auditoria e concorrência

Antes de uso real: autenticação, controle de acesso por papel, registro de decisões atribuídas a usuários, políticas versionadas, armazenamento seguro de anexos, observabilidade, backup, limites de acesso e concorrência otimista por `versao` da carga.

## Decisões e trade-offs

- Monólito modular antes de microsserviços: menos infraestrutura e maior simplicidade.
- Regras de domínio independentes de telas: evita contorno por outras integrações.
- Banco relacional é candidato, mas não escolhido sem estudo de requisitos.
- Validação de documentos e critérios de risco exige levantamento real de normas; não é simulada como autorização oficial.

Veja o [diagrama de arquitetura](../diagramas/arquitetura.mmd) e as [decisões arquiteturais](09-decisoes-e-roadmap.md).
