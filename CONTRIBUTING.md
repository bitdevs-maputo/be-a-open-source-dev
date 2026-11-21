# Regras de Contribuição

Lê isto com atenção antes do teu primeiro Pull Request.

## 1. Branches

| Branch | Quem mexe | Para quê |
|---|---|---|
| `main` | **Só o professor** | Código estável. Cada merge aqui gera uma tag/release. |
| `dev` | Alunos (via PR aprovado) | Integração das soluções. |
| `feature/*` | Aluno (no seu fork) | Uma branch por desafio. |
| `release/x.y.z` | Professor | Preparação de uma versão. |
| `hotfix/*` | Professor | Correcções urgentes em `main`. |

Nome da tua branch: `feature/desafio-<número>-<teu-usuario-github>`
Exemplo: `feature/desafio-01-anamatsinhe`

## 2. Onde colocar a tua solução

Cada aluno cria **o seu próprio ficheiro**, para nunca haver conflitos:

```
desafios/<pasta-do-desafio>/solucoes/<teu-usuario-github>.py
```

Copia o `modelo.py` da pasta do desafio e preenche. **Não alteres** ficheiros de outros alunos, nem os testes.

## 3. Conventional Commits

Formato: `tipo(escopo): descrição curta no imperativo`

Tipos permitidos: `feat`, `fix`, `docs`, `test`, `refactor`, `style`, `chore`, `ci`, `build`, `perf`, `revert`.

Exemplos válidos:
- `feat(desafio-01): adiciona fatorial recursivo`
- `fix(desafio-02): corrige validação de limites negativos`
- `docs(desafio-03): comenta caso base da pesquisa binária`

Detalhes: [docs/04-conventional-commits.md](docs/04-conventional-commits.md)

## 4. Pull Request

- **Base:** `dev` do repositório original. **Compare:** a tua branch `feature/...`.
- **Título** segue Conventional Commits (o CI valida).
- Preenche o template, liga a issue com `Closes #N`.
- 1 desafio = 1 PR. Não misturar desafios.
- Responde aos comentários de revisão fazendo novos commits na mesma branch.

## 5. Merge

- Alunos **não** fazem merge. O professor faz merge dos PRs em `dev` (*squash* ou *merge commit*).
- `dev → main` é exclusivo do professor, através de `release/x.y.z` + tag anotada `vX.Y.Z`.

## 6. Tags (obrigação do aluno)

Quando o teu PR for aceite, no **teu fork** crias uma tag anotada:
`desafio-01/teu-usuario-v1.0.0` e publicas uma release. Passo a passo em [docs/06](docs/06-tags-e-releases.md).

## 7. Código

- Funções com os **nomes exactos** pedidos no README do desafio.
- Docstrings e nomes de variáveis claros.
- Sem `print` solto nem código de teste dentro do ficheiro da solução (usa `if __name__ == "__main__":` se quiseres exemplos).
- Respeita o [Código de Conduta](CODE_OF_CONDUCT.md).

## 8. Checklist antes de abrir o PR

- [ ] Fiz fork e sincronizei a `dev`
- [ ] Branch `feature/desafio-XX-usuario` criada a partir de `dev`
- [ ] Apenas o meu ficheiro em `solucoes/` foi adicionado
- [ ] `pytest` passa localmente
- [ ] Commits em Conventional Commits
- [ ] PR aponta para `dev` e liga a issue
