import pyautogui, time
time.sleep(3)

arq = open("spam.txt", "r")

for palavra in arq:
    pyautogui.typewrite(palavra)
    pyautogui.press("enter")
