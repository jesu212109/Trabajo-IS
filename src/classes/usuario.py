from sql.sql_queries import buscar_usuario_por_credenciales
from sql.sql_functions import *

class Usuario:
    def __init__(self, id_usuario, nombre, correo_electronico, contraseña, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contraseña = contraseña
        self.rol = rol

    @staticmethod
    def login(cursor, correo_electronico, contraseña):
        print(type(cursor))
        resultado = buscar_usuario_por_credenciales(cursor, correo_electronico, contraseña)

        if resultado:
            id_usuario, nombre, correo_electronico, contraseña, rol = resultado
            return Usuario(id_usuario, nombre, correo_electronico, contraseña, rol)
        else:
            return None