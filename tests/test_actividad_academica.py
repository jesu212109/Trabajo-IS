from datetime import datetime, timedelta
import pytest
from src.classes.actividadacademica import ActividadAcademica

def test_agregar_participante_exitoso():
    actividad = ActividadAcademica("Taller Python", "Programación", datetime.now(), timedelta(hours=2), 5)
    assert actividad.agregarParticipante("Juan")
    assert len(actividad.participantes) == 1
    assert actividad.participantes[0] == "Juan"

def test_agregar_participante_aforo_maximo():
    actividad = ActividadAcademica("Taller Python", "Programación", datetime.now(), timedelta(hours=2), 2)
    actividad.agregarParticipante("Juan")
    actividad.agregarParticipante("Maria")
    assert not actividad.agregarParticipante("Carlos")
    assert len(actividad.participantes) == 2

def test_agregar_participante_sin_aforo():
    actividad = ActividadAcademica("Taller Python", "Programación", datetime.now(), timedelta(hours=2), 0)
    assert not actividad.agregarParticipante("Juan")
    assert len(actividad.participantes) == 0
