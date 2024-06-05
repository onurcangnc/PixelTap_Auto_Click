import cv2
import pyautogui
import numpy as np
import time
import keyboard

# Load the capture images
brightyellow_path = 'brightyellow.PNG'
cycle1_path = 'cycle1.PNG'
cycle2_path = 'cycle2.PNG'
three_dot_path = 'refresh1.PNG'  # Three dots icon
reload_page_path = 'refresh2.PNG'  # Reload Page button

brightyellow_icon = cv2.imread(brightyellow_path, cv2.IMREAD_GRAYSCALE)
cycle1_icon = cv2.imread(cycle1_path, cv2.IMREAD_GRAYSCALE)
cycle2_icon = cv2.imread(cycle2_path, cv2.IMREAD_GRAYSCALE)
three_dot_icon = cv2.imread(three_dot_path, cv2.IMREAD_GRAYSCALE)
reload_page_icon = cv2.imread(reload_page_path, cv2.IMREAD_GRAYSCALE)

# Ensure the images are loaded successfully
if brightyellow_icon is None:
    raise FileNotFoundError(f"Brightyellow icon image not found at path: {brightyellow_path}")
if cycle1_icon is None:
    raise FileNotFoundError(f"Cycle1 icon image not found at path: {cycle1_path}")
if cycle2_icon is None:
    raise FileNotFoundError(f"Cycle2 icon image not found at path: {cycle2_path}")
if three_dot_icon is None:
    raise FileNotFoundError(f"Three dots icon image not found at path: {three_dot_path}")
if reload_page_icon is None:
    raise FileNotFoundError(f"Reload Page icon image not found at path: {reload_page_path}")

brightyellow_h, brightyellow_w = brightyellow_icon.shape
cycle1_h, cycle1_w = cycle1_icon.shape
cycle2_h, cycle2_w = cycle2_icon.shape
three_dot_h, three_dot_w = three_dot_icon.shape
reload_page_h, reload_page_w = reload_page_icon.shape

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
click_count = 0
next_click_time = 0
cycle_detected_count = 0  # Counter for cycle detection

# Function to handle keyboard input for pausing and exiting
def handle_keyboard_input():
    global paused
    if keyboard.is_pressed('esc'):
        print("Exiting.")
        exit()
    elif keyboard.is_pressed('p'):
        paused = True
        print("Paused. Press 'c' to continue.")
    elif keyboard.is_pressed('c'):
        paused = False
        print("Continuing.")

# Register the global hotkeys
keyboard.add_hotkey('esc', lambda: handle_keyboard_input())
keyboard.add_hotkey('p', lambda: handle_keyboard_input())
keyboard.add_hotkey('c', lambda: handle_keyboard_input())

# Function to handle refresh process if cycle icons are found
def handle_refresh():
    print("Connection issues, the app will be refreshed.")

    # Click on the three-dot icon
    three_dot_location, three_dot_score = find_icon_on_screen(three_dot_icon)
    if three_dot_location:
        center_x = three_dot_location[0] + three_dot_w // 2
        center_y = three_dot_location[1] + three_dot_h // 2
        pyautogui.click(center_x, center_y)
        time.sleep(1)  # Wait for the menu to appear

    # Click on the "Reload Page" button
    reload_page_location, reload_page_score = find_icon_on_screen(reload_page_icon)
    if reload_page_location:
        center_x = reload_page_location[0] + reload_page_w // 2
        center_y = reload_page_location[1] + reload_page_h // 2
        pyautogui.click(center_x, center_y)
        time.sleep(1)  # Wait for the page to reload

    global cycle_detected_count
    cycle_detected_count = 0  # Reset the cycle detected counter after refresh

# Main loop to continuously check for the capture icon
while True:
    handle_keyboard_input()

    # If paused, skip the rest of the loop
    if paused:
        time.sleep(0.1)
        continue

    # Display remaining time for next click
    if next_click_time > time.time():
        remaining_time = next_click_time - time.time()
        print(f"Next click in {remaining_time:.2f} seconds. Total clicks: {click_count}", end='\r')
        time.sleep(0.1)
        continue

    # Check for the presence of cycle1 and cycle2 icons
    cycle1_location, cycle1_score = find_icon_on_screen(cycle1_icon)
    cycle2_location, cycle2_score = find_icon_on_screen(cycle2_icon)

    if cycle1_location or cycle2_location:
        cycle_detected_count += 1
        if cycle_detected_count > 1:  # Start refresh if cycle detected more than once
            handle_refresh()
            continue  # Restart the loop after handling refresh

    # Check for the presence of brightyellow icon
    brightyellow_location, brightyellow_score = find_icon_on_screen(brightyellow_icon)

    if brightyellow_location:
        if time.time() >= next_click_time:  # Check if it's time for the next click
            print(f"Brightyellow icon found! Clicking on it. Total clicks: {click_count + 1}")
            
            # Calculate the center of the matched area
            center_x = brightyellow_location[0] + brightyellow_w // 2
            center_y = brightyellow_location[1] + brightyellow_h // 2

            # Move the mouse to the detected coordinates and click
            pyautogui.click(center_x, center_y)

            # Increment the click count
            click_count += 1

            # Set the next click time
            next_click_time = time.time() + 5
    else:
        print("Brightyellow icon not found. Waiting for the total coin.", end='\r')

    time.sleep(0.05)  # Adjust the sleep time as needed
