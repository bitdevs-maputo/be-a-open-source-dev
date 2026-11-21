# 5. Pull Request

Um **PR** é o pedido formal para integrarem o teu código no projecto.

## Abrir o PR

1. Faz push da tua branch para o teu fork:
   ```bash
   git push -u origin feature/desafio-01-teu-usuario
   ```
2. No GitHub, clica em **Compare & pull request**.
3. Confirma:
   - **base repository:** repositório do professor
   - **base:** `dev`  ⚠️ (nunca `main`)
   - **head repository:** o teu fork
   - **compare:** `feature/desafio-01-teu-usuario`
4. Título em Conventional Commits: `feat(desafio-01): resolve calculadora recursiva`
5. Preenche o template e escreve `Closes #N`.

## Depois de abrir
- Espera o CI (✅ testes, ✅ título).
- Lê os comentários de revisão e responde.
- Para corrigir: faz novos commits na mesma branch e `git push`. O PR actualiza sozinho.
- Se a `dev` avançou e há conflitos:
  ```bash
  git fetch upstream
  git rebase upstream/dev
  git push --force-with-lease
  ```

## O que acontece a seguir
O professor faz o merge em `dev`. Só o professor leva `dev` para `main`.

## Revisão de código
Podes (e deves!) comentar PRs de colegas de forma construtiva. Rever é uma competência fundamental em open source.
