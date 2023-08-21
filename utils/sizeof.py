import pyautogui

# Get screen size
screen_width, screen_height = pyautogui.size()

# this position follows pyautogui.size()
x, y = pyautogui.position()

# Capture a screenshot
screenshot = pyautogui.screenshot()

# Get the size of the screenshot
screenshot_size = screenshot.size

# Print screen size
print("PyAutoGUI width/ Cuser Range: ", screen_width)
print("PyAutoGUI height/ Cuser Range: ", screen_height)
print("Screenshot size: "+str(screenshot_size))

