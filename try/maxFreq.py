import pyautogui
import time
import numpy as np
import os

# Duration of the test
duration = 600
frame_count = 0
start_time = time.time()
end_time = start_time + duration

os.makedirs("screenshots", exist_ok=True)

while time.time() < end_time:
    screenshot = pyautogui.screenshot()
    np.save(f"screenshots/frame_{frame_count}.npy", np.array(screenshot))
    frame_count += 1

elapsed_time = time.time() - start_time
fps = frame_count / elapsed_time

print(f"Captured {frame_count} frames in {elapsed_time:.2f} seconds for an average of {fps:.2f} FPS.")
