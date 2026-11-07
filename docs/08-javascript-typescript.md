# 08 — JavaScript Avançado e TypeScript

## Decisões técnicas para evolução

- **Tipagem forte:** contratos de entidades, argumentos e respostas; evitar `any`.
- **Interfaces:** `CargaRepository`, `ProdutoRepository`, `PoliticaDocumental` e serviços de auditoria.
- **Classes:** somente quando houver identidade, estado e invariantes que justifiquem encapsulamento (por exemplo, `CargaQuimica`).
- **Enums/unions:** estados e classificações fechados, impedindo strings arbitrárias; catálogos reais poderão ser versionados.
- **Funções puras:** validações de quantidade, motivo e transições sem efeitos colaterais.
- **Módulos ES6+:** separar domínio, aplicação e infraestrutura.
- **async/await:** integração futura com banco, provedores documentais e serviços externos.
- **Generics:** contratos reutilizáveis para resultado, página de consulta e identificadores.
- **Tratamento de erro:** erros de domínio tipados e conversão na borda HTTP.
- **Tipos compartilhados:** apenas contratos que não introduzam dependências cruzadas indevidas.

## Exemplo conceitual de contrato

```typescript
type StatusCarga =
  | "REGISTRADA"
  | "EM_ANALISE"
  | "EM_INSPECAO"
  | "LIBERADA"
  | "BLOQUEADA"
  | "EM_MOVIMENTACAO"
  | "FINALIZADA"
  | "CANCELADA";

interface Quantidade {
  valor: number;
  unidade: "kg" | "t" | "L";
}

interface RegistroCarga {
  produtoId: string;
  quantidade: Quantidade;
  responsavelTecnicoId: string;
}

interface Repository<T, ID> {
  buscar(id: ID): Promise<T | null>;
  salvar(entidade: T): Promise<void>;
}
```

## Função pura — validação de quantidade

```typescript
function quantidadeValida(valor: number): boolean {
  return Number.isFinite(valor) && valor > 0;
}
```

**Benefício:** permite testes de 0, negativos, `NaN` e valores positivos sem banco, servidor ou interface.

## Encapsulamento do domínio

A classe/entidade `CargaQuimica` deverá expor comandos como `liberar()`, `bloquear(motivo)` e `iniciarMovimentacao()`; escrever `carga.status = "LIBERADA"` diretamente fora do agregado seria uma violação da regra de negócio.

**Limite:** os exemplos são ilustrativos e não constituem implementação portuária homologada.
