import tkinter as tk
from tkinter import ttk
# import PIL as pil
from PIL import Image, ImageTk


class ImageFrame(ttk.Frame):
    def __init__(self, parent, image_path, size=None):
        super().__init__(parent)
        self.parent = parent
        self.image_path = image_path
        image = Image.open(image_path)
        if size is not None:
            image.thumbnail(size)
        rendered_image = ImageTk.PhotoImage(image)
        self.image_label = ttk.Label(self, image=rendered_image)
        self.image_label.image = rendered_image
        # image_label.place(x=0, y=0)
        # image_label.pack(fill='both')
        self.image_label.pack()
    
    def bind(self, event, callback):
        self.image_label.bind(event, callback)
