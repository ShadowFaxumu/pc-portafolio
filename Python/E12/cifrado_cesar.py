# Copyright (c) 2021
# By ShadowFax, Salo❤️

import argparse, sys
import detectEsp

description =""" Modo de uso 😃:
    cifrado_cesar.py -[e][d][c] "Mensaje" [-k][Default=5] "Clave"
    """

msj1 = "Metodo de Cifrado Cesar"
msj2= "Clave para la codificación o decodificación. Default = 5"
parser = argparse.ArgumentParser(description=msj1,
                                epilog=description, 
                                formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument( "-e", dest="encode", type=str, help="Codificar un mensaje")
parser.add_argument("-d", dest="decode", type=str, help="Decodificar un mensaje")
parser.add_argument("-c", dest="crack", type=str, help="Crackear un mensaje")
parser.add_argument("-k", dest="key", help=msj2, required=False)
params = parser.parse_args()
#print(params)

def encoding(clave_shell):
    message = params.encode
    espacios = 1
    if clave_shell == None: 
        key = 5
    else:
        while espacios > 0:
            espacios = clave_shell.count(' ')
            if clave_shell.isalpha() == False:
                espacios += 1
        key = len(clave_shell)

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''
    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            #print(translatedIndex)
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    print("Mensaje codificado:",translated)

def decoding(clave_shell):
    message = params.decode
    espacios = 1
    if clave_shell == None:
        key = 5
    else:
        while espacios > 0:
            espacios = clave_shell.count(' ')
            if clave_shell.isalpha() == False:
                espacios += 1
        key = len(clave_shell)

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            #print(translatedIndex)
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print("Mensaje decodificado:",translated)

def cracking():
    message = params.crack
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):

        lista = []

        translated = ''
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                translated = translated + symbol
        lista.append(translated)

        #Validacion de cadenas en español
        for clave in lista:
            if detectEsp.isSpanish(clave):
             print("La posible traducción es:", clave)

    
if __name__ == '__main__':

    if params.encode and params.decode or params.crack and params.encode:
        print("¡No puedes usar más de una caracteristica a la vez!")
        exit()
    if params.encode != None:
        encoding(params.key)
    if params.decode != None:
        decoding(params.key)
    if params.crack != None:
        cracking()