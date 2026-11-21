# Desafio 03 — Pesquisa Binária Recursiva
🟡 **Nível:** Intermédio

## Enunciado
Implementa um algoritmo de pesquisa binária utilizando recursividade.

## Função a implementar (nome exacto)

```python
def pesquisa_binaria(lista: list[int], alvo: int, inicio: int = 0, fim: int | None = None) -> int: ...
```

## Requisitos
- Receber uma **lista ordenada** (crescente).
- Receber o **elemento a procurar**.
- Retornar a **posição** do elemento ou **-1** se não existir.
- Tem de ser **recursiva** (o teste verifica).
- Lista vazia → `-1`.
- Se houver elementos repetidos, qualquer posição válida é aceite.

## Exemplo
```python
pesquisa_binaria([1, 3, 5, 7, 9, 11], 7)   # 3
pesquisa_binaria([1, 3, 5, 7, 9, 11], 4)   # -1
```

## Como entregar
1. Copia `modelo.py` para `solucoes/<teu-usuario-github>.py`
2. Implementa e corre `pytest tests/test_desafio_03.py -v`
3. Branch `feature/desafio-03-<usuario>` → PR para `dev`.

## 💡 Dica
A cada chamada, olha para o **meio**: se o alvo é menor, procura à esquerda; se é maior, à direita. Não uses `list.index`, `in` nem `bisect`.
