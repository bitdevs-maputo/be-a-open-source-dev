# 2. Gitflow

Gitflow é um modelo de ramificação com papéis bem definidos.

| Branch | Origem | Destino | Quem |
|---|---|---|---|
| `main` | — | — | Professor |
| `dev` | `main` | — | PRs aprovados |
| `feature/*` | `dev` | `dev` | Aluno |
| `release/*` | `dev` | `main` **e** `dev` | Professor |
| `hotfix/*` | `main` | `main` **e** `dev` | Professor |

## Fluxo do aluno

```bash
git checkout dev
git pull upstream dev
git checkout -b feature/desafio-01-teu-usuario

# ... trabalhas e fazes commits ...

git push -u origin feature/desafio-01-teu-usuario
# abres o PR no GitHub: base = dev (upstream)
```

## Fluxo do professor (release)

```bash
git checkout dev && git pull
git checkout -b release/1.0.0
# ajusta CHANGELOG.md, versão, etc.
git push -u origin release/1.0.0
# PR release/1.0.0 -> main (merge)
git checkout main && git pull
git tag -a v1.0.0 -m "Release 1.0.0"
git push origin v1.0.0
# traz as alterações de volta à dev
git checkout dev && git merge main && git push
```

## Regras de ouro
- Uma branch por desafio.
- Branches pequenas e de vida curta.
- Nunca fazer commit directo em `main` ou `dev`.
