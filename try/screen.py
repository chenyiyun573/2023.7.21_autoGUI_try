import pyautogui
import numpy as np
from PIL import Image

# Take a screenshot using PyAutoGUI
screenshot = pyautogui.screenshot()

# Convert the screenshot to a NumPy array
screenshot_np = np.array(screenshot)

# Print the shape of the array
print(screenshot_np.shape)
