"""Utilitários: carrega todas as soluções dos alunos de um desafio."""
import ast
import importlib.util
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent / "desafios"


def solucoes(pasta_desafio: str):
    """Lista de (nome_do_aluno, módulo) para cada ficheiro em solucoes/."""
    pasta = RAIZ / pasta_desafio / "solucoes"
    resultado = []
    for ficheiro in sorted(pasta.glob("*.py")):
        if ficheiro.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"sol_{ficheiro.stem}", ficheiro)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        resultado.append((ficheiro.stem, modulo))
    return resultado


def e_recursiva(funcao) -> bool:
    """True se o corpo da função contém uma chamada a ela própria."""
    import inspect
    import textwrap

    arvore = ast.parse(textwrap.dedent(inspect.getsource(funcao)))
    nome = funcao.__name__
    for no in ast.walk(arvore.body[0]):
        if isinstance(no, ast.Call) and isinstance(no.func, ast.Name) and no.func.id == nome:
            return True
    return False


def parametrizar(pasta_desafio: str):
    """Devolve (argvalues, ids) para pytest.mark.parametrize."""
    sols = solucoes(pasta_desafio)
    return [m for _, m in sols], [n for n, _ in sols]
