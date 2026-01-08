# OmniSelect-OCR ⚡
### The "God Mode" Copy-Paste Tool for Windows

**OmniSelect** is a lightweight, open-source desktop utility that lets you copy text from **anywhere** on your screen—images, protected PDFs, Zoom calls, or YouTube videos—instantly.

Unlike Chrome extensions, OmniSelect works **system-wide**. If you can see it, you can copy it.

![Status](https://img.shields.io/badge/Status-Alpha-green) ![Python](https://img.shields.io/badge/Made%20with-Python-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Features
* **Global Hotkey:** Press `Alt + Q` (configurable) to activate the overlay.
* **Visual Selection:** Drag a box over any text on your screen.
* **Instant OCR:** Uses Tesseract-OCR to recognize text locally (Offline & Private).
* **Zero Friction:** Text is automatically copied to your clipboard with a system notification.
* **Lightweight:** Runs quietly in the background; no heavy resources used.
�️ Prerequisites

OmniSelect relies on **Tesseract OCR** for its vision engine. You must install this separately.

1.  **Download Tesseract:** [UB-Mannheim Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
2.  **Install it:** Run the installer and note the installation path (Default: `C:\Program Files\Tesseract-OCR`).o dnf install tesseract
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
   � Installation (For Developers)

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Aanishnithin07/OmniSelect-OCR.git
    cd OmniSelect-OCR
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    python main.py
    ```
- **Python 3.8+** - Core language
- **Tkinter** - GUI framework for the overlay
- **Tesseract OCR** - Text recognition engine
- **�️ Roadmap
- [ ] System Tray Icon for easy exit.
- [ ] "Smart Format" (Detect tables and copy as CSV).
- [ ] Multi-monitor support optimization.
- [ ] Web Version (Upload image -> Get Text).
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - The OCR engine
- All the amazing Python libraries that make this possible

## 📧 Contact

**Aanish Nithin**
- GitHub: [@Aanishnithin07](https://github.com/Aanishnithin07)

---

⭐ If you find this useful, please consider giving it a star on GitHub!
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---
*Built with ❤️ by Aanish Nithin*