"""
OCR Engine for OmniSelect-OCR
Handles image-to-text conversion using Tesseract OCR
"""

import pytesseract
import pyperclip
from PIL import Image, ImageGrab
from plyer import notification
import platform

# Configure Tesseract path based on OS
# WINDOWS USERS: Update this path to match your Tesseract installation
# Common locations:
#   - C:\Program Files\Tesseract-OCR\tesseract.exe
#   - C:\Program Files (x86)\Tesseract-OCR\tesseract.exe
# 
# macOS/Linux: Usually auto-detected if installed via package manager
# If Tesseract is not found, uncomment and set the path manually

if platform.system() == 'Windows':
    # Windows: Update this path to your Tesseract installation
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# else:
    # macOS/Linux: Uncomment and set path if auto-detection fails
    # pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'


def extract_text(image):
    """
    Extract text from a PIL Image object using OCR.
    
    Args:
        image: PIL Image object to process
        
    Returns:
        str: Extracted text if found, None otherwise
    """
    try:
        # Convert image to text using Tesseract
        text = pytesseract.image_to_string(image)
        
        # Clean the text
        text = text.strip()
        
        # Check if any text was found
        if text:
            # Copy to clipboard
            pyperclip.copy(text)
            return text
        else:
            return None
            
    except Exception as e:
        print(f"Error during OCR processing: {e}")
        return None


def extract_text_from_region(x1, y1, x2, y2):
    """
    Capture a specific screen region and extract text from it.
    This function handles the entire workflow: capture, OCR, clipboard, and notification.
    
    Args:
        x1, y1, x2, y2: Coordinates of the screen region to capture
    """
    try:
        # Capture the specific screen area
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        
        # Convert image to text using Tesseract
        text = pytesseract.image_to_string(screenshot)
        
        # Clean the text
        text = text.strip()
        
        # Check if any text was found
        if text:
            # Copy to clipboard
            pyperclip.copy(text)
            
            # Send success notification
            notification.notify(
                title="OmniSelect-OCR",
                message=f"Text copied to clipboard!\n{text[:50]}{'...' if len(text) > 50 else ''}",
                app_name="OmniSelect-OCR",
                timeout=3
            )
            
            print(f"Extracted text: {text[:100]}...")
            return text
        else:
            # Send notification that no text was found
            notification.notify(
                title="OmniSelect-OCR",
                message="No text found in selection.",
                app_name="OmniSelect-OCR",
                timeout=3
            )
            
            print("No text found in selected region")
            return None
            
    except Exception as e:
        # Send error notification
        error_msg = f"Error: {str(e)}"
        notification.notify(
            title="OmniSelect-OCR Error",
            message=error_msg,
            app_name="OmniSelect-OCR",
            timeout=3
        )
        
        print(f"Error during OCR processing: {e}")
        return None
