# Desafio 01 — Calculadora Recursiva
🟢 **Nível:** Fácil

## Enunciado
1. Cria uma função recursiva para calcular o **fatorial** de um número.
2. Implementa a **sequência de Fibonacci** usando recursividade.

**Conceitos:** funções, recursividade e condições.

## Funções a implementar (nomes exactos)

```python
def fatorial(n: int) -> int: ...
def fibonacci(n: int) -> int: ...
```

## Requisitos
- Ambas **têm de ser recursivas** (o teste verifica que a função se chama a si própria).
- `fatorial(0) == 1`, `fatorial(5) == 120`.
- `fibonacci(0) == 0`, `fibonacci(1) == 1`, `fibonacci(10) == 55`.
- Para `n` negativo, levanta `ValueError`.

## Como entregar
1. Copia `modelo.py` para `solucoes/<teu-usuario-github>.py`
2. Implementa as funções.
3. Corre `pytest tests/test_desafio_01.py -v`
4. Segue o fluxo em [CONTRIBUTING.md](../../CONTRIBUTING.md) → branch `feature/desafio-01-<usuario>` → PR para `dev`.

## 💡 Dica
Pensa sempre em: **caso base** (quando parar?) e **caso recursivo** (como reduzir o problema?).
