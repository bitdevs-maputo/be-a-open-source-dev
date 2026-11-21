"""Desafio 02 — Gerador de Números Primos."""


def e_primo(n: int) -> bool:
    """Devolve True se n for primo."""
    raise NotImplementedError


def primos_no_intervalo(inicio: int, fim: int) -> list[int]:
    """Devolve a lista ordenada de primos em [inicio, fim].

    TypeError se os limites não forem inteiros.
    ValueError se algum for negativo ou se inicio > fim.
    """
    raise NotImplementedError


if __name__ == "__main__":
    print(primos_no_intervalo(1, 50))
