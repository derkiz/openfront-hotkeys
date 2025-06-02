import pyautogui
import keyboard
import time

# Disable the built-in pause
pyautogui.PAUSE = 0  

# === CONFIGURABLE LOCATIONS ===
# === Modify This ===
boat_location = (1280, 640)
city_location = (1368, 827)
nuke_location = (770, 640)
port_location = (1450, 640)
hydrogen_location = (1111, 640)
defensive_location = (1200, 824)
missile_location = (1625, 640)
sam_location = (1790, 640)
# === Modify This END ===

running = True
paused = False
keys_pressed = []

def perform_sequence(target_location, label):
    original_pos = pyautogui.position()
    print(f"[{label}] Captured position: {original_pos}")

    # Right-click at original position
    pyautogui.moveTo(original_pos)
    pyautogui.click(button='right')
    print(f"[{label}] Right-clicked at {original_pos}")
    time.sleep(0.1)

    # Move 80px left and left-click
    left_pos = (original_pos[0] - 80, original_pos[1])
    pyautogui.moveTo(left_pos)
    pyautogui.click()
    print(f"[{label}] Left-clicked 80px left at {left_pos}")
    time.sleep(0.1)

    # Move to final location and left-click
    pyautogui.moveTo(target_location)
    pyautogui.click()
    print(f"[{label}] Final left-click at {target_location}")

    # Return cursor to original position
    pyautogui.moveTo(original_pos)
    print(f"[{label}] Cursor returned to original position: {original_pos}")

def on_press(key):
    global running, keys_pressed, paused

    if key == 'f1':
        paused = not paused
        if paused:
            keys_pressed.clear()
            print("[F1] Paused: all key functions disabled (ESC also disabled)")
        else:
            print("[F1] Unpaused: key functions enabled")
        return

    if paused:
        return

    if key == 'esc':
        print("\n[ESC] Exiting...")
        running = False
        return False

    keys_pressed.append(key.lower())

keyboard.on_press(lambda e: on_press(e.name))

print("Hotkeys active:")
print("  'b' -> Boats")
print("  'v' -> Cities")
print("  'n' -> Nukes")
print("  'p' -> Port")
print("  'h' -> Hydrogen")
print("  'k' -> Defensive Post")
print("  'i' -> Missile")
print("  'o' -> SAM")
print("Press F1 to toggle pause mode (while paused, all keys including ESC are disabled).")
print("Press ESC (when not paused) to quit.")

while running:
    if not paused and keys_pressed:
        key = keys_pressed.pop(0)
        # === Modify This custom hotkeys ===
        if key == 'b':
            perform_sequence(boat_location, 'B - Boats')
        elif key == 'v':
            perform_sequence(city_location, 'V - Cities')
        elif key == 'n':
            perform_sequence(nuke_location, 'N - Nukes')
        elif key == 'p':
            perform_sequence(port_location, 'P - Port')
        elif key == 'h':
            perform_sequence(hydrogen_location, 'H - Hydrogen')
        elif key == 'k':
            perform_sequence(defensive_location, 'K - Defensive Post')
        elif key == 'i':
            perform_sequence(missile_location, 'I - Missile')
        elif key == 'o':
            perform_sequence(sam_location, 'O - SAM')
            # === Modify This custom hotkeys END ===
    time.sleep(0.2)  # using sleep(0.2) as noted for reliable performance
