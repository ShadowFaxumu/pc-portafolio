# copyright (c) 03/10/2021
# Created by Shadow and Salo

import pyautogui,time
import argparse

msj1 = "Autollenado de forms para 1920x1080"
description =""" Modo de uso 😃:
    pyautogui_forms.py -a "respuesta" "repuesta 2" -b "respuesta" "repuesta 2" -c "respuesta" "repuesta 2" -d "respuesta" "repuesta 2"

    Pregunta1= ¿Qué prefieres? --> Marvel, DC, Ambos o Ninguno
    Pregunta2= Escriba un refrán, catchphrase, dicho popular o cita de libro o película
    Pregunta3= ¿Cuál es la mejor hora del día para comer pastel?
    Pregunta4= Ingresa una dirección de correo electrónico falsa, antes del @
    """
parser = argparse.ArgumentParser(description=msj1,
                                epilog=description, 
                                formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-a", dest="question1", 
                    type=str, 
                    choices=['Marvel', 'DC', 'Ambos', 'Ninguno'],
                    default='Marvel',
                    help="Respuesta a la pregunta 1",
                    nargs=2)
parser.add_argument("-b", dest="question2", type=str, help="Respuesta a la pregunta 2",nargs=2)

parser.add_argument("-c", dest="question3", 
                    type=str, 
                    choices=['8AM', '9AM', '10AM', '11AM', '12PM', 
                    '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM+'],
                    help="Respuesta a la pregunta 3",
                    nargs=2)

parser.add_argument("-d", dest="question4", type=str, help="Respuesta a la pregunta 4", nargs=2)

params = parser.parse_args()

def tab_enter():
    pyautogui.press('tab')
    pyautogui.press('enter')

def tab():
    pyautogui.press('tab')
    pyautogui.press('tab')

def down(x):
    for x in range(x):
        pyautogui.press('down')


class ShadowxSalo:
    def __init__(self, q1, q2, q3, q4):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        
    def firstq(self):
        if self.q1 == 'Marvel':
            pyautogui.click(x=529, y = 593, clicks = 1)

        elif self.q1 == 'DC':
            pyautogui.click(x=529, y = 646, clicks = 1)

        elif self.q1 == 'Ambos':
            pyautogui.click(x=529, y = 695, clicks = 1)

        elif self.q1 == 'Ninguno':
            pyautogui.click(x=529, y = 745, clicks = 1)

    def secondq(self):
        answer2 = self.q2
        pyautogui.typewrite(answer2) 

    def thirdq(self):
        if self.q3 == '8AM':
            down(1)
        elif self.q3 == '9AM':
            down(2)
        elif self.q3 == '10AM':
            down(3)
        elif self.q3 == '11AM':
            down(4)
        elif self.q3 == '12PM':
            down(5)
        elif self.q3 == '1PM':
            down(6)
        elif self.q3 == '2PM':
            down(7)
        elif self.q3 == '3PM':
            down(8)
        elif self.q3 == '4PM':
            down(9)
        elif self.q3 == '5PM':
            down(10)
        elif self.q3 == '6PM':
            down(11)
        elif self.q3 == '7PM+':
            down(12)

    def fourthq(self):
        answer4 = self.q4
        pyautogui.typewrite(answer4)
        pyautogui.hotkey('altright','q')
        pyautogui.typewrite("falso.com") 

if __name__ == "__main__":

    shadow = ShadowxSalo(params.question1[0],params.question2[0],params.question3[0],params.question4[0])
    shadow.firstq()
    tab()
    shadow.secondq()
    tab()
    shadow.thirdq()
    tab()
    shadow.fourthq()

    tab_enter()
    time.sleep(3)
    tab_enter()

    salo = ShadowxSalo(params.question1[1],params.question2[1],params.question3[1],params.question4[1])
    salo.firstq()
    tab()
    salo.secondq()
    tab()
    salo.thirdq()
    tab()
    salo.fourthq()
    
    tab_enter()