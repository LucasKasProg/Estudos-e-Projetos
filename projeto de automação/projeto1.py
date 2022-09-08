# automação da tarefa de fazer backup de um arquivo no drive

import pyautogui
import time

pyautogui.alert('Não mexa em nada, o programa esta rodando!')
pyautogui.PAUSE = 0.8

# abrir o chorme, digitar drive, pressionar enter 

pyautogui.press('win')
pyautogui.write('Edge')
pyautogui.press('enter')
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

# entrar na area de trabalho

pyautogui.hotkey('winleft', 'd')
time.sleep(1.5)

# clicar no arquivo que quero fazer backup e arrastar ele

pyautogui.moveTo(1246, 50)
pyautogui.mouseDown()
pyautogui.moveTo(729, 575)

# "alt + tab" para voltar ao google drive

pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.mouseUp()

# eperar 5seg

time.sleep(5)
pyautogui.alert('Pronto tarefa concluida!')