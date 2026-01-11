"""
OmniSelect-OCR Main Application
Thread-safe entry point for the desktop OCR utility
"""

from pynput import keyboard
from plyer import notification
from PIL import ImageGrab
import tkinter as tk
from overlay import SnippingOverlay
from ocr_engine import extract_text, extract_text_from_region
import platform
import pytesseract
import threading


# Global flag for thread-safe hotkey triggering
TRIGGER_RECEIVED = False


def setup_tesseract():
    """
    Automatically configure Tesseract path based on the operating system.
    macOS: Assumes Tesseract is in PATH (installed via Homebrew)
    Windows: Sets the default installation path
    """
    if platform.system() == 'Darwin':  # macOS
        # On macOS, Tesseract is usually in PATH after Homebrew install
        pytesseract.pytesseract.tesseract_cmd = 'tesseract'
    elif platform.system() == 'Windows':
        # Windows default path
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Linux usually auto-detects, so no need to set


def on_trigger():
    """
    Triggered when the user presses the hotkey (Cmd+Shift+2 on macOS).
    This runs on a background thread, so it only sets a flag.
    """
    global TRIGGER_RECEIVED
    TRIGGER_RECEIVED = True


def process_ocr_in_background(x1, y1, x2, y2):
    """
    Process OCR in a background thread to avoid freezing the UI.
    
    Args:
        x1, y1, x2, y2: Coordinates of the selected region
    """
    thread = threading.Thread(target=extract_text_from_region, args=(x1, y1, x2, y2))
    thread.daemon = True
    thread.start()


def main_loop_watcher(root):
    """
    Runs on the Main Thread. Checks the global flag every 100ms.
    If the flag is True, launches the SnippingOverlay on the main thread.
    
    Args:
        root: The Tkinter root window (invisible, for main thread management)
    """
    global TRIGGER_RECEIVED
    
    if TRIGGER_RECEIVED:
        TRIGGER_RECEIVED = False  # Reset flag
        
        # Launch overlay on main thread
        try:
            overlay = SnippingOverlay()
            overlay.start_capture(process_ocr_in_background)
        except Exception as e:
            print(f"Error launching overlay: {e}")
            notification.notify(
                title="OmniSelect-OCR Error",
                message=f"Failed to launch overlay: {str(e)}",
                app_name="OmniSelect-OCR",
                timeout=3
            )
    
    # Schedule next check in 100ms
    root.after(100, main_loop_watcher, root)


def start_hotkey_listener():
    """
    Start the keyboard listener in a background thread.
    """
    # Define the hotkey combination
    # For macOS: Cmd+Shift+2
    # For Windows/Linux: Ctrl+Shift+2
    if platform.system() == 'Darwin':  # macOS
        hotkey_combo = {keyboard.Key.cmd, keyboard.Key.shift, keyboard.KeyCode.from_char('2')}
    else:  # Windows/Linux
        hotkey_combo = {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode.from_char('2')}
    
    current_keys = set()
    
    def on_press(key):
        """Handle key press events."""
        current_keys.add(key)
        
        # Check if the hotkey combination is pressed
        if hotkey_combo.issubset(current_keys):
            on_trigger()
    
    def on_release(key):
        """Handle key release events."""
        try:
            current_keys.remove(key)
        except KeyError:
            pass
    
    # Create and start the listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.daemon = True
    listener.start()


def main():
    """
    Main entry point for the application.
    Sets up Tesseract, creates an invisible Tkinter root for main thread management,
    starts the hotkey listener, and runs the main loop watcher.
    """
    # Setup Tesseract for the current OS
    setup_tesseract()
    
    print("OmniSelect-OCR is running...")
    print("Press Cmd+Shift+2 (macOS) or Ctrl+Shift+2 (Windows/Linux) to capture text from screen")
    print("Close this window to exit")
    
    # Create an invisible Tkinter root window for main thread management
    root = tk.Tk()
    root.withdraw()  # Hide the window
    
    # Start the hotkey listener in a background thread
    start_hotkey_listener()
    
    # Start the main loop watcher on the main thread
    root.after(100, main_loop_watcher, root)
    
    # Run the Tkinter main loop (keeps main thread alive)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nExiting OmniSelect-OCR...")
        root.destroy()


if __name__ == "__main__":
    main()
