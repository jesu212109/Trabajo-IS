class EmailSegmentation:
    def __init__(self):
        self.emails = {
            'usuario1@example.com': {'nombre': 'Usuario1', 'edad': 25, 'ubicacion': 'Ciudad A'},
            'usuario2@example.com': {'nombre': 'Usuario2', 'edad': 35, 'ubicacion': 'Ciudad B'},
            # Agrega más usuarios según sea necesario
        }

    def segmentar_por_edad(self, edad_limite):
        segmento = {email: info for email, info in self.emails.items() if info['edad'] < edad_limite}
        return segmento

    def segmentar_por_ubicacion(self, ciudad):
        segmento = {email: info for email, info in self.emails.items() if info['ubicacion'] == ciudad}
        return segmento
