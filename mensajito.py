import pyautogui
import time

time.sleep(5)

while True:
    a = 1
    while a <= 10:
        mensaje = f" prueba de codigo py num{a}"
        pyautogui.typewrite(mensaje)
        pyautogui.press('enter')
        a += 1
    
    respuesta = input("Presione Q para salir o cualquier otra tecla para reiniciar el programa:")
    if respuesta.lower() == "q":
        break