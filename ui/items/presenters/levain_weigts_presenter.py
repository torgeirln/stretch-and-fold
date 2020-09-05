import tkinter as tk
from tkinter import ttk

from ui.styles.recipe_styles import header_style, ingredient_style


class LevainWeightsPresenterItem(ttk.Frame):
    def __init__(self, parent, levain, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.levain = levain
        self.create_content()

    def create_content(self):
        self.levain_header_label = ttk.Label(self, text='Levain', style=header_style())
        self.levain_header_label.grid(sticky='ew', pady=5)
        i = 0
        for key, value in self.levain.items():
            i += 1
            ttk.Label(self, text=key, style=ingredient_style()).grid(
                row=i+1,
                column=0,
                sticky='ew',
                padx=10,
                pady=2
            )
            ttk.Label(self, text=f'{value} g', style=ingredient_style()).grid(
                row=i+1,
                column=1,
                sticky='ew',
                padx=10,
                pady=2
            )