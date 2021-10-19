#!/bin/bash
if type -t wevtutil &> /dev/null
then
    OS=MSWin
elif type -t scutil &> /dev/null
then
    OS=macOS
else
    OS=Linux
fi
echo "El sistema operativo es:" $OS >> scriptBash.txt

#Ejemplo de scanner de puertos
#Obtenido de pentestlab.wordpress.com
#Parámetros
host=10.0.2.15
firstport=10
lastport=500
#Funcion para escanear puertos
function portscan {
for ((counter=$firstport; counter<=$lastport; counter++))
do
    (echo >/dev/tcp/$host/$counter) > /dev/null 2>&1 && echo "$counter open" >> scriptBash.txt
done
}
#llamada de la funcion
portscan

function is_alive_ping() {
  ping -c 1 $1 > /dev/null 2>&1
  [ $? -eq 0 ] && echo "Node with IP: $i is up." >> scriptBash.txt
}
for i in 10.0.2.{1..255}
do
is_alive_ping $i & disown 
done
