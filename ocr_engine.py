"""
OCR Engine for OmniSelect-OCR
Handles image-to-text conversion using Tesseract OCR
"""

import pytesseract
import pyperclip
from PIL import Image
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
