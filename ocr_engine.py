"""
OCR Engine for OmniSelect-OCR
Handles image-to-text conversion using Tesseract OCR
"""

import pytesseract
import pyperclip
from PIL import Image

# Configure Tesseract path (update this based on your OS)
# Windows: r'C:/Program Files/Tesseract-OCR/tesseract.exe'
# macOS: Usually auto-detected if installed via Homebrew
# Linux: Usually auto-detected if installed via package manager
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


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
