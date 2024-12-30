from pynput import mouse, keyboard
import pyautogui
import time
import logging
import threading

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Global variables for hotkeys and control
pause = False
stop = False
search_region = None

# Image paths
reference_image_path = "whisper.png"
invalid_image_path = "invalid.png"

def get_click_position(prompt):
    """
    Waits for a mouse click and returns the position.
    """
    print(prompt)
    position = []

    def on_click(x, y, button, pressed):
        if pressed and not position:
            position.append((x, y))
            return False  # Stop listener

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    return position[0]


def get_search_region():
    """
    Lets the user define the search region by two mouse clicks.
    Returns a tuple (x, y, width, height) for the defined region.
    """
    top_left = get_click_position("Click on the top left corner of the search area.")
    print(f"Top-left corner: {top_left}")
    bottom_right = get_click_position("Click on the bottom right corner of the search area.")
    print(f"Bottom-right corner: {bottom_right}")

    # Calculate the width and height
    x1, y1 = top_left
    x2, y2 = bottom_right
    width = x2 - x1
    height = y2 - y1

    return (x1, y1, width, height)


def find_and_click_image(image_path, region, confidence=0.8):
    """
    Searches for an image within a defined region and clicks it if found.
    Returns True if the image is found, otherwise False.
    """
    try:
        location = pyautogui.locateOnScreen(image_path, region=region, confidence=confidence)
        if location:
            center_x, center_y = pyautogui.center(location)
            logger.info(f"New trade offer found at ({center_x}, {center_y}). Clicking the offer...")
            pyautogui.click(center_x, center_y)
            return True
        else:
            logger.info(f"Waiting for new trade offers... (Image not found yet, confidence={confidence})")
    except pyautogui.ImageNotFoundException:
        logger.info(f"Image search failed with confidence {confidence}. Waiting for trade offer.")
    return False


def search_for_invalid_image():
    """
    Checks if the image "invalid.png" appears anywhere on the screen.
    Returns True if found, otherwise False.
    """
    try:
        location = pyautogui.locateOnScreen(invalid_image_path, confidence=0.8)
        if location:
            logger.warning(f"Invalid offer detected! Pausing search for 'whisper.png' for 1 minute.")
            return True
    except pyautogui.ImageNotFoundException:
        pass
    return False


def listen_for_hotkeys():
    """
    Listens for hotkeys to pause, reset region, or stop the program.
    """
    global pause, stop, search_region

    def on_press(key):
        global pause, stop
        try:
            if key.char == "p":
                pause = not pause
                logger.info("Pause toggled: %s", "enabled" if pause else "disabled")
            elif key.char == "r":
                search_region = get_search_region()
                logger.info("Search region reset.")
            elif key.char == "q":
                stop = True
                logger.info("Program stopped.")
                return False
        except AttributeError:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    global pause, stop, search_region

    logger.info("Defining the search area by clicking twice. Please define the area where trade offers will appear.")
    search_region = get_search_region()
    logger.info(f"Search area defined: {search_region}")

    # Hotkey listener in a separate thread
    hotkey_thread = threading.Thread(target=listen_for_hotkeys, daemon=True)
    hotkey_thread.start()

    while not stop:
        if pause:
            time.sleep(0.5)  # Reduce CPU usage in paused mode
            continue

        # If "invalid.png" is found, pause the search for "whisper.png" for 1 minute
        if search_for_invalid_image():
            logger.info("Pausing search for 'whisper.png' for 1 minute due to invalid offer detection.")
            time.sleep(60)  # Pause for 1 minute

        if find_and_click_image(reference_image_path, search_region, confidence=0.8):
            logger.info("Waiting for the next trade offer to appear...")
            time.sleep(2)
        else:
            logger.info("No trade offer found yet. Still waiting...")
            time.sleep(1)

    logger.info("Program ended.")


if __name__ == "__main__":
    main()
