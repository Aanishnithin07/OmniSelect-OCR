"""
OmniSelect-OCR Main Application
Entry point for the desktop OCR utility
"""

import keyboard
from plyer import notification
from PIL import ImageGrab
from overlay import SnippingOverlay
from ocr_engine import extract_text
import time


def on_trigger():
    """
    Triggered when the user presses the hotkey (Alt+Q).
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
    Sets up the hotkey listener and runs in the background.
    """
    print("OmniSelect-OCR is running...")
    print("Press Alt+Q to capture text from screen")
    print("Press Ctrl+C to exit")
    
    # Register the hotkey (Alt+Q)
    keyboard.add_hotkey('alt+q', on_trigger)
    
    try:
        # Keep the application running
        keyboard.wait()
    except KeyboardInterrupt:
        print("\nExiting OmniSelect-OCR...")


if __name__ == "__main__":
    main()
