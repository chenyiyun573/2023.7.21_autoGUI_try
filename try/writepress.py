import pyautogui

# Type with quarter-second pause in between each key
pyautogui.write('Hello, world!', interval=0.25)

# Press the Esc key
pyautogui.press('esc')

# Press the Up arrow key 3 times
pyautogui.press('up', presses=3)
