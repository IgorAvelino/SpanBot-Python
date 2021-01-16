import pyautogui, time
time.sleep(3)

arq = open("span.txt", "r")

for palavra in arq:
    pyautogui.typewrite(palavra)
    pyautogui.press("enter")
