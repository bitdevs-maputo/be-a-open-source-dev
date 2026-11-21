# 1. Fork e Clone

**Fork** = a tua cópia pessoal do repositório no GitHub. Em open source não tens permissão de escrita no projecto original, por isso trabalhas no teu fork e propões alterações via Pull Request.

## Passos

1. No GitHub, abre o repositório original e clica em **Fork** (⚠️ desmarca "Copy the main branch only" para trazeres também a `dev`).
2. Clona **o teu fork**:
   ```bash
   git clone https://github.com/TEU_USUARIO/desafios-open-source.git
   cd desafios-open-source
   ```
3. Liga o repositório original como `upstream`:
   ```bash
   git remote add upstream https://github.com/PROFESSOR/desafios-open-source.git
   git remote -v
   # origin    -> o teu fork
   # upstream  -> o original
   ```
4. Muda para a `dev`:
   ```bash
   git fetch upstream
   git checkout dev
   ```

## Manter o fork sincronizado (antes de cada desafio!)

```bash
git checkout dev
git fetch upstream
git merge upstream/dev      # ou: git rebase upstream/dev
git push origin dev
```

## Configurar a tua identidade

```bash
git config user.name  "O Teu Nome"
git config user.email "o-teu-email@exemplo.com"
```
