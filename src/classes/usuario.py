from sql.sql_queries import buscar_usuario_por_credenciales
from sql.sql_functions import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
    
    def actualizar_informacion(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        return None

    def enviar_correo_patrocinio(self):
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_use_tls = True  # Usar True si estás usando el puerto 587
        smtp_use_ssl = False  # Usar True si estás usando el puerto 465

        # Autenticación muy poco segura, habría que encriptar
        username = "astralacademy@gmail.com"
        password = "astralacademy12345678"

        # Crear conexión segura al servidor SMTP
        if smtp_use_tls:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
        elif smtp_use_ssl:
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:
            server = smtplib.SMTP(smtp_server, smtp_port)

        # Iniciar sesión en el servidor SMTP
        server.login(username, password)

        # Crear mensaje de correo electrónico
        from_address = "astralacademy@gmail.com"
        
        resultado = buscar_usuario_por_credenciales(cursor, correo_electronico, contraseña)
        
        if resultado is correo:
            correo_destinatario = correo
            
        to_address = correo_destinatario
        
        subject = "Actividades académicas disponibles"
        body = "Hay nuevas actividades académicas disponibles, echa un vistazo en astralacademy"

        message = MIMEMultipart()
        message["From"] = from_address
        message["To"] = to_address
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Enviar el correo electrónico
        server.sendmail(from_address, to_address, message.as_string())

        # Cerrar la conexión con el servidor SMTP
        server.quit()

