import cv2
import pyautogui
import numpy as np
import time
import keyboard

# Load the uploaded images
capture_path = 'capture.PNG'  # Update this path if needed
ekran_path = 'coin.png'  # Update this path if needed

capture_icon = cv2.imread(capture_path, cv2.IMREAD_GRAYSCALE)
ekran_icon = cv2.imread(ekran_path, cv2.IMREAD_GRAYSCALE)

# Ensure the images are loaded successfully
if capture_icon is None:
    raise FileNotFoundError(f"Capture icon image not found at path: {capture_path}")
if ekran_icon is None:
    raise FileNotFoundError(f"Ekran icon image not found at path: {ekran_path}")

capture_h, capture_w = capture_icon.shape
ekran_h, ekran_w = ekran_icon.shape

# Set the pyautogui pause to a very small value for rapid clicking
pyautogui.PAUSE = 0.00001

# Function to find an icon on the screen and return its coordinates
def find_icon_on_screen(icon, threshold=0.8):
    # Capture the screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Template matching to find the pattern on the entire screen
    result = cv2.matchTemplate(gray_screenshot, icon, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        top_left = max_loc
        return top_left, max_val
    else:
        return None, max_val

paused = False

# Main loop to continuously check for icons
while True:
    # Check if 'esc' is pressed to exit
    if keyboard.is_pressed('esc'):
        print("Exiting.")
        break

    # Check if 'p' is pressed to pause
    if keyboard.is_pressed('p'):
        paused = True
        print("Paused. Press 'c' to continue.")

    # Check if 'c' is pressed to continue
    if keyboard.is_pressed('c'):
        paused = False
        print("Continuing.")

    # If paused, skip the rest of the loop
    if paused:
        time.sleep(0.1)
        continue

    # Check for the presence of capture icon
    capture_location, capture_score = find_icon_on_screen(capture_icon)

    if capture_location:
        print("Capture icon found! No action taken.")
        time.sleep(1)  # Adjust the sleep time as needed
    else:
        print("Capture icon not found. Checking for ekran icon.")
        ekran_location, ekran_score = find_icon_on_screen(ekran_icon)
        
        if ekran_location:
            print("Ekran icon found!")
            
            # Calculate the center of the matched area
            center_x = ekran_location[0] + ekran_w // 2
            center_y = ekran_location[1] + ekran_h // 2

            # Move the mouse to the detected coordinates and click
            while not find_icon_on_screen(capture_icon)[0]:
                if keyboard.is_pressed('esc'):
                    print("Exiting.")
                    exit()
                if keyboard.is_pressed('p'):
                    paused = True
                    print("Paused. Press 'c' to continue.")
                if paused:
                    break
                pyautogui.click(center_x, center_y)
        else:
            print("Ekran icon not found.")
    
    time.sleep(0.05)  # Adjust the sleep time as needed
