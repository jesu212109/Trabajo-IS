import pytest
from src.app.screens.mailing import EmailSegmentation

@pytest.fixture
def email_segmentation():
    return EmailSegmentation()

def test_segmentar_por_edad(email_segmentation):
    # Prueba la segmentación por edad con una edad límite
    resultado = email_segmentation.segmentar_por_edad(30)
    
    # Verifica que los usuarios esperados estén en el resultado
    assert 'usuario1@example.com' in resultado
    assert 'usuario2@example.com' not in resultado

def test_segmentar_por_ubicacion(email_segmentation):
    # Prueba la segmentación por ubicación con una ciudad específica
    resultado = email_segmentation.segmentar_por_ubicacion('Ciudad A')

    # Verifica que los usuarios esperados estén en el resultado
    assert 'usuario1@example.com' in resultado
    assert 'usuario2@example.com' not in resultado

# Puedes ejecutar estas pruebas con el comando `pytest` en tu terminal.
