# 🧑‍🏫 Guia do Professor (configuração do repositório)

## 1. Criar e publicar

```bash
cd desafios-open-source
git init -b main
git add .
git commit -m "chore: estrutura inicial do repositório"
git branch dev
git remote add origin https://github.com/SEU_USUARIO/desafios-open-source.git
git push -u origin main dev
git tag -a v0.1.0 -m "Release 0.1.0"
git push origin v0.1.0
```

No GitHub: **Settings → General → Default branch = `dev`** (assim os PRs dos alunos apontam para `dev` por defeito).

## 2. Proteger as branches (Settings → Branches → Add rule)

**`main`**
- ✅ Require a pull request before merging
- ✅ Require status checks (`testes`, `origem-main`)
- ✅ Restrict who can push → só tu
- ✅ Do not allow bypassing

**`dev`**
- ✅ Require a pull request before merging (1 aprovação)
- ✅ Require status checks (`testes`, `titulo-pr`)
- ✅ Restrict who can push/merge → só tu

Colaboradores: não precisas de adicionar alunos; eles usam fork.

## 3. Editar CODEOWNERS
Troca `@SEU_USUARIO` em `.github/CODEOWNERS`.

## 4. Criar as issues
Cria 1 issue por desafio (label `desafio`) com o conteúdo do README do desafio. Ex.: *"feat(desafio-01): Calculadora Recursiva"*.

## 5. Revisão e merge
- Revê o PR, pede alterações, aprova.
- Merge em `dev` (recomendado: **Squash and merge** para manter a história limpa).

## 6. Fazer uma release
Ver [docs/02-gitflow.md](02-gitflow.md) — branch `release/x.y.z` → PR para `main` → tag anotada → merge de volta à `dev`.

## 7. Nota sobre os enunciados
Os desafios estão numerados sequencialmente de 01 a 03. Para adicionar mais desafios, segue o padrão `desafios/NN-nome/` (README, modelo.py, solucoes/) e cria `tests/test_desafio_NN.py`.
