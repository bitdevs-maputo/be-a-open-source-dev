# Desafios Open Source

Repositório de treino para aprender a **contribuir em projectos open source** da forma como se faz no mundo real:
fork, branches, Gitflow, issues, Conventional Commits, Pull Requests, tags e releases — resolvendo desafios de programação.

> Linguagem dos desafios: **Python 3.10+** (o fluxo Git é o mesmo para qualquer linguagem).

## O que vais aprender

| Competência | Onde ver |
|---|---|
| Fork e clone | [docs/01-fork-e-clone.md](docs/01-fork-e-clone.md) |
| Gitflow | [docs/02-gitflow.md](docs/02-gitflow.md) |
| Issues | [docs/03-issues.md](docs/03-issues.md) |
| Conventional Commits | [docs/04-conventional-commits.md](docs/04-conventional-commits.md) |
| Pull Requests | [docs/05-pull-request.md](docs/05-pull-request.md) |
| Tags e Releases | [docs/06-tags-e-releases.md](docs/06-tags-e-releases.md) |

## Regras (resumo)

1. **Nunca** fazes push directo para `main` nem `dev`. Trabalhas sempre no teu **fork**.
2. Cada desafio tem uma **issue**. Antes de começar, comenta na issue: *"Quero resolver este desafio"*.
3. Crias a branch a partir de `dev`: `feature/desafio-XX-teu-usuario`.
4. Commits seguem **Conventional Commits** (`feat(desafio-01): adiciona fatorial recursivo`).
5. Abres o Pull Request **para `dev`** do repositório original (nunca para `main`).
6. O CI tem de passar (testes + título do PR).
7. Só o professor faz merge `dev → main` (via branch `release/*`) e publica as releases oficiais.
8. Depois do teu PR ser aceite, crias a **tag** no teu fork (ver [docs/06](docs/06-tags-e-releases.md)).

Regras completas: [CONTRIBUTING.md](CONTRIBUTING.md)

## Desafios

| # | Desafio | Nível | Pasta |
|---|---|---|---|
| 01 | Calculadora Recursiva | Fácil | [desafios/01-calculadora-recursiva](desafios/01-calculadora-recursiva) |
| 02 | Gerador de Números Primos | Intermédio | [desafios/02-gerador-numeros-primos](desafios/02-gerador-numeros-primos) |
| 03 | Pesquisa Binária Recursiva | Intermédio | [desafios/03-pesquisa-binaria-recursiva](desafios/03-pesquisa-binaria-recursiva) |

## Fluxo resumido

```
 repo original (upstream)            o teu fork (origin)            a tua máquina
 ───────────────────────            ───────────────────            ─────────────
 main ◄── release/x.y.z ◄── dev ◄──PR── feature/desafio-01-ana ◄── commits
   │         (professor)      ▲
   └── tags vX.Y.Z (professor)│
                              └── tu sincronizas o teu fork com a dev antes de começar
```

## Correr os testes localmente

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pytest
pytest -v
```

Os testes encontram automaticamente todos os ficheiros em `desafios/*/solucoes/`.
