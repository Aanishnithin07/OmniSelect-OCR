"""
OmniSelect-OCR Main Application
Entry point for the desktop OCR utility
"""

from pynput import keyboard
from plyer import notification
from PIL import ImageGrab
from overlay import SnippingOverlay
from ocr_engine import extract_text
import platform
import pytesseract


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
    Launches the snipping overlay, captures the selected region,
    performs OCR, and shows a notification.
    """
    
    def capture_and_process(x1, y1, x2, y2):
        """
        Callback function to handle the captured coordinates.
        
        Args:
            x1, y1, x2, y2: Coordinates of the selected region
        """
        try:
            # Capture the screen area
            screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            
            # Perform OCR on the captured image
            text = extract_text(screenshot)
            
            # Show notification based on result
            if text:
                notification.notify(
                    title="OmniSelect-OCR",
                    message=f"Text copied to clipboard!\n{text[:50]}...",
                    app_name="OmniSelect-OCR",
                    timeout=3
                )
            else:
                notification.notify(
                    title="OmniSelect-OCR",
                    message="No text found in selection.",
                    app_name="OmniSelect-OCR",
                    timeout=3
                )
        except Exception as e:
            notification.notify(
                title="OmniSelect-OCR",
                message=f"Error: {str(e)}",
                app_name="OmniSelect-OCR",
                timeout=3
            )
    
    # Launch the snipping overlay
    overlay = SnippingOverlay()
    overlay.start_capture(capture_and_process)


def main():
    """
    Main entry point for the application.
    Sets up Tesseract, the hotkey listener, and runs in the background.
    """
    # Setup Tesseract for the current OS
    setup_tesseract()
    
    print("OmniSelect-OCR is running...")
    print("Press Cmd+Shift+2 (macOS) or Ctrl+Shift+2 (Windows/Linux) to capture text from screen")
    print("Press Ctrl+C to exit")
    
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
    
    # Set up the keyboard listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nExiting OmniSelect-OCR...")


if __name__ == "__main__":
    main()
