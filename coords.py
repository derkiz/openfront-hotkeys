# Find coordinates for app.py

import pyautogui
import time

print("Move your mouse to the desired position. Press Ctrl+C to stop.\n")

try:
    while True:
        x, y = pyautogui.position()
        position_str = f"X: {x:4}  Y: {y:4}"
        print(position_str, end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nDone.")