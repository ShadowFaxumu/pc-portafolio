# Copyright (c) 28/10/2021
# Created by Paulina y Sáyago

import subprocess

if __name__ == '__main__':
    url = input("Ingrese la url del sitio web: ")
    command = f"powershell -ExecutionPolicy ByPass -File script_nmap.ps1 {url}"
    powershellresult = subprocess.run(command, stdout=subprocess.PIPE)
    if powershellresult.stderr == None:
        print("Resultados listos, en la ruta actual")