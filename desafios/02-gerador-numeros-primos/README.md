# Desafio 02 — Gerador de Números Primos
🟡 **Nível:** Intermédio

## Enunciado
Cria uma função que receba um intervalo e apresente todos os números primos existentes nesse intervalo.

## Funções a implementar (nomes exactos)

```python
def e_primo(n: int) -> bool: ...
def primos_no_intervalo(inicio: int, fim: int) -> list[int]: ...
```

## Requisitos
- **Validar os limites:**
  - `inicio` e `fim` têm de ser inteiros → senão `TypeError`
  - não podem ser negativos → senão `ValueError`
  - `inicio` não pode ser maior que `fim` → senão `ValueError`
- **Função de verificação de primalidade** `e_primo` (0, 1 e negativos não são primos).
- **Resultados ordenados** (ordem crescente), intervalo **inclusivo** nos dois extremos.

## Exemplo
```python
primos_no_intervalo(1, 20)  # [2, 3, 5, 7, 11, 13, 17, 19]
```

## Como entregar
1. Copia `modelo.py` para `solucoes/<teu-usuario-github>.py`
2. Implementa e corre `pytest tests/test_desafio_02.py -v`
3. Branch `feature/desafio-02-<usuario>` → PR para `dev`.

## 💡 Dica
Para testar se `n` é primo, basta verificar divisores até `√n`.
