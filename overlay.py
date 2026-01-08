"""
Visual Overlay for OmniSelect-OCR
Provides a snipping tool interface for screen capture
"""

import tkinter as tk


class SnippingOverlay:
    """
    A fullscreen transparent overlay that allows users to select a region
    by drawing a rectangle with their mouse.
    """
    
    def __init__(self):
        self.root = None
        self.canvas = None
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.callback = None
        
    def start_capture(self, callback):
        """
        Open the overlay window and capture a screen region.
        
        Args:
            callback: Function to call with coordinates (x1, y1, x2, y2) when done
        """
        self.callback = callback
        
        # Create fullscreen transparent window
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)
        self.root.configure(bg='black')
        
        # Create canvas for drawing
        self.canvas = tk.Canvas(
            self.root,
            bg='black',
            highlightthickness=0,
            cursor='crosshair'
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind mouse events
        self.canvas.bind('<ButtonPress-1>', self._on_press)
        self.canvas.bind('<B1-Motion>', self._on_drag)
        self.canvas.bind('<ButtonRelease-1>', self._on_release)
        
        # Start the GUI loop
        self.root.mainloop()
    
    def _on_press(self, event):
        """Handle mouse button press - start drawing rectangle."""
        self.start_x = event.x
        self.start_y = event.y
        
        # Create rectangle
        self.rect = self.canvas.create_rectangle(
            self.start_x,
            self.start_y,
            self.start_x,
            self.start_y,
            outline='red',
            width=2
        )
    
    def _on_drag(self, event):
        """Handle mouse drag - update rectangle size."""
        if self.rect:
            # Update rectangle coordinates
            self.canvas.coords(
                self.rect,
                self.start_x,
                self.start_y,
                event.x,
                event.y
            )
    
    def _on_release(self, event):
        """Handle mouse release - capture coordinates and close window."""
        if self.rect:
            # Get final coordinates
            x1 = min(self.start_x, event.x)
            y1 = min(self.start_y, event.y)
            x2 = max(self.start_x, event.x)
            y2 = max(self.start_y, event.y)
            
            # Destroy the window
            self.root.destroy()
            
            # Call the callback with coordinates
            if self.callback:
                self.callback(x1, y1, x2, y2)
