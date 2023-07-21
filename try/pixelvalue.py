import pyautogui
from time import sleep
# Get the screen size from pyautogui
autogui_size = pyautogui.size()

# Capture a screenshot
screenshot = pyautogui.screenshot()

# Get the size of the screenshot
screenshot_size = screenshot.size

for _ in range(60):
    # Get the current position of the cursor
    x, y = pyautogui.position()

    # Rescale cursor position to match the screenshot size
    x_scaled = int(x * screenshot_size[0] / autogui_size[0])
    y_scaled = int(y * screenshot_size[1] / autogui_size[1])

    # Get the pixel value at the rescaled cursor position
    pixel = screenshot.getpixel((x_scaled, y_scaled))

    sleep(0.5)

    # Display the cursor position, pixel value
    print(f"Cursor Position: ({x}, {y}) - Pixel Value: {pixel}")
