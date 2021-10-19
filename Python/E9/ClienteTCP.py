#!/usr/bin/env python
"""
Created on Sat Sep 25 17:23:52 2021

@author: ShadowFax
"""

import socket
from cryptography.fernet import Fernet
import argparse

description =""" Modo de uso:) :
    ClienteTCP.py -msj "Mensaje a enviar" """
parser = argparse.ArgumentParser(description='Port scanning',
                                 epilog=description, 
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-msj", metavar='MSJ', dest="msj",
                    help="mensaje a enviar", required=True)
params = parser.parse_args()

clave = Fernet.generate_key()
cipher_suite = Fernet(clave)
 
#Almacenamos la clave
file = open('clave.key', 'wb') 
file.write(clave)
file.close()

#Tomar el arguento, y convertirlo a bytes
mensaje = params.msj
mensajeb = mensaje.encode()

#Cifrar el mensaje
msj_cifrado = cipher_suite.encrypt(mensajeb)
print("Mensaje enviado:\n", mensaje)

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048 

obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
obj.connect((TCP_IP, TCP_PORT))
obj.send(msj_cifrado)
respuesta = obj.recv(BUFFER_SIZE).decode()
obj.close()

print("Respuesta recibida:", respuesta)





