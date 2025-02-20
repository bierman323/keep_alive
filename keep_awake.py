import pyautogui
import time
import os

def send_keypress():
    # Use xdotool if on Linux, or other platform-specific methods
    if os.name == 'posix':
        os.system('xdotool key space')
    elif os.name == 'nt':
        # Windows equivalent if needed
        os.system('nircmd sendkey space press')
    else:
        print("Unsupported OS")

while True:
    send_keypress()
    time.sleep(240)  # 4 minutes