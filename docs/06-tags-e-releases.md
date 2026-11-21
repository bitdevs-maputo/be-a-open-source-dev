# 6. Tags e Releases

Uma **tag** marca um ponto concreto da história do Git (normalmente uma versão). Uma **release** é a tag publicada no GitHub com notas.

Usamos [Semantic Versioning](https://semver.org/lang/pt-BR/): `MAJOR.MINOR.PATCH`.

## Obrigação do aluno (no teu fork)

Depois do teu PR ser **aceite** na `dev` do original:

```bash
# 1. sincroniza
git checkout dev
git fetch upstream
git merge upstream/dev
git push origin dev

# 2. cria uma tag ANOTADA
git tag -a desafio-01/teu-usuario-v1.0.0 -m "Desafio 01 concluído: calculadora recursiva"

# 3. envia a tag para o teu fork
git push origin desafio-01/teu-usuario-v1.0.0
```

> ⚠️ Se o teu nome de usuário tiver pontos ou espaços, usa só letras, números e `-`.

4. No teu fork (GitHub) → **Releases → Draft a new release** → escolhe a tag → escreve notas:
   - O que implementaste
   - Complexidade/abordagem
   - O que aprendeste

Comandos úteis:
```bash
git tag                       # listar
git show desafio-01/teu-usuario-v1.0.0   # detalhes
git tag -d NOME               # apagar local
git push origin --delete NOME # apagar remota
```

## Obrigação do professor (repositório original)

Só o professor cria tags em `main`:

```bash
git tag -a v1.0.0 -m "Release 1.0.0 — desafios 01, 02, 03"
git push origin v1.0.0
```
e publica a Release com o changelog.

## Convenção de versões

| Alteração | Sobe |
|---|---|
| Novo desafio | MINOR (`0.1.0 → 0.2.0`) |
| Correcção em testes/docs | PATCH (`0.1.0 → 0.1.1`) |
| Mudança que quebra soluções existentes | MAJOR |
