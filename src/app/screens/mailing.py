import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mailing:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_mail(self, to_email, subject, body):
        # Crear el objeto del mensaje
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = to_email
        message["Subject"] = subject

        # Añadir el cuerpo del mensaje
        message.attach(MIMEText(body, "plain"))

        # Configurar la conexión segura
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
            # Iniciar sesión en el servidor SMTP
            server.login(self.sender_email, self.sender_password)

            # Enviar el mensaje
            server.sendmail(self.sender_email, to_email, message.as_string())
        
