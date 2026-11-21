# 4. Conventional Commits

Convenção para mensagens de commit legíveis e que permitem gerar changelogs automaticamente.

```
<tipo>(<escopo opcional>): <descrição>

[corpo opcional]

[rodapé opcional]
```

## Tipos

| Tipo | Quando usar |
|---|---|
| `feat` | Nova funcionalidade (ex.: nova solução) |
| `fix` | Correcção de bug |
| `docs` | Só documentação |
| `test` | Testes |
| `refactor` | Reorganizar código sem mudar comportamento |
| `style` | Formatação (espaços, vírgulas) |
| `perf` | Melhoria de desempenho |
| `chore` | Tarefas de manutenção |
| `ci` / `build` | Pipelines / dependências |
| `revert` | Reverter commit anterior |

## Regras
- Descrição em minúsculas, no **imperativo**, sem ponto final, até ~72 caracteres.
- Escopo: usa `desafio-XX`.
- Breaking change: `feat(api)!: ...` ou rodapé `BREAKING CHANGE: ...`.

## Exemplos

✅ Bons
```
feat(desafio-01): adiciona fibonacci recursivo
fix(desafio-02): trata limites negativos
docs(desafio-03): explica caso base
test(desafio-03): cobre lista vazia
```

❌ Maus
```
update
Resolvi o desafio
feat: Adicionei coisas.
FIX bug
```

## Commits pequenos
Faz commits por passo lógico (ex.: um para o fatorial, outro para o fibonacci), não um gigante no fim.
