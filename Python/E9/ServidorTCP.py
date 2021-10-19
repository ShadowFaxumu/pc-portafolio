
#!/usr/bin/env python
"""
Created on Sat Sep 25 17:23:52 2021

@author: ShadowFax
"""

import socket
from cryptography.fernet import Fernet

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
obj.bind((TCP_IP, TCP_PORT))
obj.listen(1)
(conn, addr) = obj.accept()

print('Dirección de conexión:', addr)

while True:
    msj_cifrado= conn.recv(BUFFER_SIZE)
    conn.send(b"Enterados. Bye! c:")
    break
conn.close()

#Generamos el archivo

file = open('clave.key', 'rb') 
clave = file.read()
file.close()
cifrado = Fernet(clave)

mensajeb = cifrado.decrypt(msj_cifrado, None)
mensaje = mensajeb.decode()
print("Mensaje Recibido:\n", mensaje)
