# OmniSelect-OCR

**A lightweight, open-source desktop utility that uses local OCR to copy text from any video, image, or application instantly via a global hotkey.**

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🚀 Features

- **Global Hotkey**: Press `Alt+Q` to activate OCR anywhere on your screen
- **Visual Selection**: Snipping tool-style interface to select text regions
- **Instant OCR**: Powered by Tesseract OCR engine for accurate text recognition
- **Auto-Copy**: Extracted text automatically copied to clipboard
- **Desktop Notifications**: Get notified when text is successfully captured
- **Lightweight**: Runs in the background with minimal resource usage
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📋 Prerequisites

Before installing OmniSelect-OCR, you need to install **Tesseract OCR** as a system dependency.

### Installing Tesseract OCR

#### Windows
1. Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run the installer (recommended path: `C:\Program Files\Tesseract-OCR`)
3. Note the installation path for configuration

#### macOS
```bash
brew install tesseract
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install tesseract-ocr
```

#### Linux (Fedora)
```bash
sudo dnf install tesseract
```

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aanishnithin07/OmniSelect-OCR.git
   cd OmniSelect-OCR
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Tesseract Path** (Windows only)
   
   Open `ocr_engine.py` and update the Tesseract path if needed:
   ```python
   # Update this line with your actual Tesseract installation path
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```
   
   For macOS and Linux, Tesseract is usually auto-detected, so you can comment out or remove this line.

## 🎮 Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Capture text**
   - Press `Alt+Q` anywhere on your screen
   - A semi-transparent overlay will appear
   - Click and drag to select the region containing text
   - Release the mouse button to capture
   - Text is automatically copied to your clipboard!

3. **Exit the application**
   - Press `Ctrl+C` in the terminal where the app is running

## 🛠️ Tech Stack

- **Python 3.8+** - Core language
- **Tkinter** - GUI framework for the overlay
- **Tesseract OCR** - Text recognition engine
- **pytesseract** - Python wrapper for Tesseract
- **Pillow (PIL)** - Image processing
- **pyperclip** - Clipboard integration
- **keyboard** - Global hotkey detection
- **plyer** - Cross-platform notifications
- **pystray** - System tray integration (planned)

## 📁 Project Structure

```
OmniSelect-OCR/
├── main.py           # Entry point and hotkey handler
├── overlay.py        # Visual snipping overlay GUI
├── ocr_engine.py     # OCR processing and text extraction
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## 🔍 How It Works

1. **Hotkey Detection**: The `keyboard` library listens for `Alt+Q` globally
2. **Visual Selection**: A fullscreen transparent overlay lets you draw a selection rectangle
3. **Screen Capture**: The selected region is captured using `PIL.ImageGrab`
4. **OCR Processing**: Tesseract extracts text from the captured image
5. **Clipboard Copy**: Text is automatically copied using `pyperclip`
6. **Notification**: Desktop notification confirms the action

## ⚙️ Configuration

### Change Hotkey
Edit `main.py` to customize the hotkey:
```python
# Change 'alt+q' to your preferred combination
keyboard.add_hotkey('alt+q', on_trigger)
```

### Tesseract Path (Windows)
Edit `ocr_engine.py`:
```python
pytesseract.pytesseract.tesseract_cmd = r'YOUR\PATH\TO\tesseract.exe'
```

## 🐛 Troubleshooting

### "Tesseract not found" Error
- **Windows**: Verify the path in `ocr_engine.py` matches your installation
- **macOS/Linux**: Ensure Tesseract is installed and in your PATH

### Hotkey Not Working
- **Linux**: You may need to run with `sudo` for global hotkey access
- **macOS**: Grant accessibility permissions in System Preferences → Security & Privacy

### No Text Detected
- Ensure the selected region contains clear, readable text
- Try selecting a larger area with more context
- Check that the text has good contrast with the background

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open-source and available under the MIT License.

## 🙏 Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - The OCR engine
- All the amazing Python libraries that make this possible

## 📧 Contact

**Aanish Nithin**
- GitHub: [@Aanishnithin07](https://github.com/Aanishnithin07)

---

⭐ If you find this useful, please consider giving it a star on GitHub!
