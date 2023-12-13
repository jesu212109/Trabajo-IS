from src.classes.facultad import Facultad
import pytest

@pytest.fixture
def facultad():
    return Facultad("Facultad de Ciencias")

def test_agregar_miembro_exitoso(facultad):
    miembro = "Profesor1"
    resultado = facultad.agregarMiembro(miembro)
    assert resultado is True
    assert miembro in facultad.miembros

def test_agregar_miembro_invalido(facultad):
    miembro = 123
    resultado = facultad.agregarMiembro(miembro)
    assert resultado is False
    assert miembro not in facultad.miembros
