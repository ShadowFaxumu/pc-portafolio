# Copyright (c) 29/10/2021
# Created by Shadow & Salo

import email, smtplib, ssl
import pwinput

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    sender_email = input("\tIngrese el correo remitente (@gmail):\t")
    password = pwinput.pwinput("\tIngrese la contraseña:\t")
    try:
        smtp.login(sender_email, password)
        print("\n\tConexión exitosa c:")
        return sender_email, password
    except:
        print("\n\tUsuario o contraseña no validos :c")
        exit()


def form(sender_email):
    subject = input("\tIngrese el asunto:\t")
    body = input("\tIngrese el mensaje:\t")
    file = input("\tIngrese la ruta del archivo a adjuntar:\t")
    receiver_email = input("\tIngrese el correo destinatario:\t")

    # Se crea el objeto, y se declaran los headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Se añade el contenido del mensaje
    message.attach(MIMEText(body, "plain"))

    filename = file  
    headerarchivo = "memingo_uwu.jpg"

    # Se abre el archivo en bytes owo
    with open(filename, "rb") as attachment:

        # Se añade el archivo como application/octet-stream
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Se codifica en ascii lo que se enviará   
    encoders.encode_base64(part)

    # Se le añade un header al archivo
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {headerarchivo}",
    )

    # Se añade el archivo al mensaje y se hace cadena
    message.attach(part)
    text = message.as_string()
    return receiver_email, text


def send_message(sender_email, password, receiver_email, text):
    # Nos logeamos y mandamos el mensaje
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
        print("\n\tCorreo enviado exitosamente, bye! uwu")


if __name__ == '__main__':
    print("\t<-- Envio de correos con archivos adjuntos -->\n")
    print("\t===== Validacion de credenciales =====\n")
    email, password = main()
    print("\n\t===== Estructura del correo =====\n")
    receiver, text = form(email)
    send_message(email, password, receiver, text)