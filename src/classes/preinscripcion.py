from datetime import date

class Preinscripcion:
    def __init__(self):
        self.estado = False  
        self.fecha_inscripcion = None
        self.detalles_pago = ""

    def realizar_preinscripcion(self, p1, p2):
        
        if not self.estado:  
            self.estado = True
            self.fecha_inscripcion = date.today()
            self.detalles_pago = f"{p1} - {p2}"  
            return True
        else:
            print("La preinscripción ya ha sido realizada.")
            return False