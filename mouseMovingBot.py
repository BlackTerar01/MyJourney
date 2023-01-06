import pyautogui as pag
import time as t
import random as r

while True:
    x = r.randint(500, 550)
    y = r.randint(500, 550)
    pag.moveTo(x, y)
    t.sleep(5)