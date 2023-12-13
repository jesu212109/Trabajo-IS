class ActividadAcademica:
    def __init__(self, nombre, tematica, fecha, duracion, aforo):
        self.nombre = nombre
        self.tematica = tematica
        self.fecha = fecha
        self.duracion = duracion
        self.aforo = aforo
        self.participantes = []

    def agregarParticipante(self, participante):
        if len(self.participantes) < self.aforo:
            self.participantes.append(participante)
            return True
        else:
            print(f"No se puede agregar a {participante}, la actividad ha alcanzado su aforo máximo.")
            return False