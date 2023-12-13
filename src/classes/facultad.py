class Facultad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregarMiembro(self, miembro):
        if isinstance(miembro, str):
            self.miembros.append(miembro)
            return True
        else:
            print("Error: El miembro debe ser una cadena de texto.")
            return False