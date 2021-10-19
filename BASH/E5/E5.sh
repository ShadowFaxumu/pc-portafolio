#!/bin/bash

#cfccfca8a55b497f9f3c5b22a9cd132a
#Función para hacer invisible lo que 
#se ponga en la consola

redColour="\e[0;31m\033[1m"
endColour="\033[0m\e[0m"

function invapikey(){
 
  echo
  echo -n "Introduzca su APIKEY: "
  read -s apikey
  echo
  
}

function correos(){
  for line in $(cat correos.txt)
  do
    correo=$line
    lapi=`curl -s https://haveibeenpwned.com/api/v3/breachedaccount/$correo?truncateResponse=false -H 'hibp-api-key':$apikey | jq -j '.[] | "Organización: ", .Title, " --- Fecha de vulneración: ", .BreachDate, "\n" '`

    if [[ "$lapi" == "" ]]; then
      echo -e "\n El correo $correo no ha sido vulnerado, felicidades uwu."
    else
      echo -----------------------------------------------------------
      echo -e "\n${redColour}El correo $correo ha sido vulnerado por:${endColour} \n $lapi "
    fi
  done
}

invapikey
correos