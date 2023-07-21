import cv2
import numpy as np
import pyautogui
from time import sleep

sleep(3)


# Convert the screenshot to a numpy array
screenshot = np.array(pyautogui.screenshot())

# Calculate the absolute differences between neighboring pixels in each channel, including horizontal
diff_channels1 = np.abs(np.diff(screenshot, axis=1))
diff_channels2 = np.abs(np.diff(screenshot, axis=0))

# Resize diff_channels2 to match the shape of diff_channels1
diff_channels2 = cv2.resize(diff_channels2, (diff_channels1.shape[1], diff_channels1.shape[0]))

# Add the two diff_channels arrays together
diff_channels = diff_channels1 + diff_channels2

# Check if any channel has a non-zero difference at each pixel position
any_diff = np.any(diff_channels, axis=2)

# Create an edge map with white pixels where any_diff is True
edge_map = np.where(any_diff, 255, 0).astype(np.uint8)

# Show the edge map
cv2.imshow('Edge Map', edge_map)
cv2.waitKey(0)
cv2.destroyAllWindows()
