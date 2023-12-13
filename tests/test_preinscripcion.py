from datetime import date
import pytest
from src.classes.preinscripcion import Preinscripcion 

def test_realizar_preinscripcion_exitosa():
    preinscripcion = Preinscripcion()
    assert preinscripcion.realizar_preinscripcion("Pago1", "Pago2")
    assert preinscripcion.estado is True
    assert preinscripcion.fecha_inscripcion == date.today()
    assert preinscripcion.detalles_pago == "Pago1 - Pago2"

def test_realizar_preinscripcion_fallida():
    preinscripcion = Preinscripcion()
    preinscripcion.realizar_preinscripcion("Pago1", "Pago2")
    assert not preinscripcion.realizar_preinscripcion("NuevoPago1", "NuevoPago2")

def test_estado_inicial_preinscripcion():
    preinscripcion = Preinscripcion()
    assert preinscripcion.estado is False
    assert preinscripcion.fecha_inscripcion is None
    assert preinscripcion.detalles_pago == ""
