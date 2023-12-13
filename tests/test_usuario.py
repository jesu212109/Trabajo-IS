import pytest
from src.classes.usuario import Usuario

@pytest.fixture
def usuario_de_prueba():
    # Aquí puedes inicializar un objeto de Usuario para usarlo en las pruebas
    return Usuario(id_usuario=1, nombre="Usuario1", correo_electronico="usuario1@example.com", contraseña="secreto", rol="Registrado")

def test_actualizar_informacion(usuario_de_prueba):
    # Act: Llama al método que quieres probar
    usuario_de_prueba.actualizar_informacion("NuevoNombre")

    # Assert: Verifica que la instancia del Usuario se actualizó correctamente
    assert usuario_de_prueba.nombre == "NuevoNombre"
