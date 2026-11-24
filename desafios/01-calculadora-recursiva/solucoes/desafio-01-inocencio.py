def calculadora_fatorial(n: int) -> int:
    """Calcula o fatorial de um número de forma recursiva."""
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    if n == 0 or n == 1:
        return 1
    return n * calculadora_fatorial(n - 1)


def calculadora_fibonacci(n: int) -> int:
    """Retorna o n-ésimo número da sequência de Fibonacci de forma recursiva."""
    if n < 0:
        raise ValueError("A sequência de Fibonacci não aceita números negativos.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return calculadora_fibonacci(n - 1) + calculadora_fibonacci(n - 2)


# Testes rápidos (você pode apagar isso antes de enviar, se o professor não pedir)
if __name__ == "__main__":
    print(f"Fatorial de 5: {calculadora_fatorial(5)}") # Deve dar 120
    print(f"Fibonacci de 6: {calculadora_fibonacci(6)}") # Deve dar 8