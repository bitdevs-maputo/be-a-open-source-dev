import pytest
from helpers import e_recursiva, parametrizar

MODULOS, IDS = parametrizar("01-calculadora-recursiva")
pytestmark = pytest.mark.skipif(not MODULOS, reason="ainda sem soluções")


@pytest.mark.parametrize("m", MODULOS, ids=IDS)
class TestDesafio01:
    @pytest.mark.parametrize("n,esperado", [(0, 1), (1, 1), (2, 2), (5, 120), (10, 3628800)])
    def test_fatorial(self, m, n, esperado):
        assert m.fatorial(n) == esperado

    @pytest.mark.parametrize("n,esperado", [(0, 0), (1, 1), (2, 1), (7, 13), (10, 55), (15, 610)])
    def test_fibonacci(self, m, n, esperado):
        assert m.fibonacci(n) == esperado

    def test_negativos(self, m):
        with pytest.raises(ValueError):
            m.fatorial(-1)
        with pytest.raises(ValueError):
            m.fibonacci(-1)

    def test_sao_recursivas(self, m):
        assert e_recursiva(m.fatorial), "fatorial tem de ser recursivo"
        assert e_recursiva(m.fibonacci), "fibonacci tem de ser recursivo"
