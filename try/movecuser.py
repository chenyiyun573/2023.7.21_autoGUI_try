import pyautogui
import time

pyautogui.FAILSAFE = False

for _ in range(10):  # Will run for 10 iterations
    for i in range(100, 1500, 10): 
        pyautogui.moveTo(i, 100, duration=0.1)
    for i in range(100, 800, 10): 
        pyautogui.moveTo(1500, i, duration=0.1)
    for i in range(1500, 100, -10): 
        pyautogui.moveTo(i, 800, duration=0.1)
    for i in range(800, 100, -10): 
        pyautogui.moveTo(100, i, duration=0.1)
    time.sleep(1)
