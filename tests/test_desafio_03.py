import pytest
from helpers import e_recursiva, parametrizar

MODULOS, IDS = parametrizar("03-pesquisa-binaria-recursiva")
pytestmark = pytest.mark.skipif(not MODULOS, reason="ainda sem soluções")

LISTA = [1, 3, 5, 7, 9, 11]


@pytest.mark.parametrize("m", MODULOS, ids=IDS)
class TestDesafio03:
    @pytest.mark.parametrize("i,valor", list(enumerate(LISTA)))
    def test_encontra_todos(self, m, i, valor):
        assert m.pesquisa_binaria(LISTA, valor) == i

    @pytest.mark.parametrize("alvo", [0, 2, 4, 12, -5])
    def test_nao_existe(self, m, alvo):
        assert m.pesquisa_binaria(LISTA, alvo) == -1

    def test_lista_vazia(self, m):
        assert m.pesquisa_binaria([], 1) == -1

    def test_um_elemento(self, m):
        assert m.pesquisa_binaria([4], 4) == 0
        assert m.pesquisa_binaria([4], 5) == -1

    def test_lista_grande(self, m):
        grande = list(range(0, 20000, 2))
        assert m.pesquisa_binaria(grande, 19998) == 9999
        assert m.pesquisa_binaria(grande, 19999) == -1

    def test_repetidos(self, m):
        lista = [1, 2, 2, 2, 3]
        assert lista[m.pesquisa_binaria(lista, 2)] == 2

    def test_nao_altera_lista(self, m):
        copia = LISTA.copy()
        m.pesquisa_binaria(LISTA, 7)
        assert LISTA == copia

    def test_e_recursiva(self, m):
        assert e_recursiva(m.pesquisa_binaria), "pesquisa_binaria tem de ser recursiva"
