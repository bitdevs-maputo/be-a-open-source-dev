import pytest
from helpers import parametrizar

MODULOS, IDS = parametrizar("02-gerador-numeros-primos")
pytestmark = pytest.mark.skipif(not MODULOS, reason="ainda sem soluções")


@pytest.mark.parametrize("m", MODULOS, ids=IDS)
class TestDesafio02:
    @pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 97, 7919])
    def test_primos(self, m, n):
        assert m.e_primo(n) is True

    @pytest.mark.parametrize("n", [-7, 0, 1, 4, 9, 100, 7917])
    def test_nao_primos(self, m, n):
        assert m.e_primo(n) is False

    def test_intervalo_basico(self, m):
        assert m.primos_no_intervalo(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_limites_inclusivos(self, m):
        assert m.primos_no_intervalo(7, 13) == [7, 11, 13]

    def test_intervalo_sem_primos(self, m):
        assert m.primos_no_intervalo(0, 1) == []
        assert m.primos_no_intervalo(24, 28) == []

    def test_um_unico_numero(self, m):
        assert m.primos_no_intervalo(13, 13) == [13]

    def test_resultado_ordenado(self, m):
        r = m.primos_no_intervalo(1, 100)
        assert r == sorted(r) and len(r) == 25

    def test_inicio_maior_que_fim(self, m):
        with pytest.raises(ValueError):
            m.primos_no_intervalo(20, 1)

    def test_negativos(self, m):
        with pytest.raises(ValueError):
            m.primos_no_intervalo(-5, 10)

    @pytest.mark.parametrize("a,b", [(1.5, 10), ("1", 10), (1, None)])
    def test_tipos_invalidos(self, m, a, b):
        with pytest.raises(TypeError):
            m.primos_no_intervalo(a, b)
