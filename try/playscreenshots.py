import cv2
import numpy as np
import glob

# Sort the file names so the frames are in the correct order
filenames = sorted(glob.glob("screenshots/*.npy"))

for filename in filenames:
    frame = np.load(filename)
    
    # Convert from RGBA to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)
    
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press Q on the keyboard to stop the playback
        break

cv2.destroyAllWindows()
