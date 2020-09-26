import tkinter as tk
from tkinter import ttk

from domain.models.levain_models import LevainPct
from ui.styles.recipe_styles import header_style, ingredient_style


class LevainPctPresenterItem(ttk.Frame):
    def __init__(self, parent, levain: LevainPct, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.levain = levain
        self.create_content()

    def create_content(self):
        self.levain_header_label = ttk.Label(self, text=f'Levain', style=header_style())
        self.levain_header_label.grid(sticky='ew', pady=5)
        
        ttk.Label(self, text='Hydration', style=ingredient_style()).grid(
            row=1, column=0, sticky='ew', padx=10, pady=2
        )
        ttk.Label(self, text=f'{self.levain.hydration:.0f} %', style=ingredient_style()).grid(
            row=1, column=1, sticky='ew', padx=10, pady=2
        )

        ttk.Label(self, text='Ratio', style=ingredient_style()).grid(
            row=2, column=0, sticky='ew', padx=10, pady=2
        )
        ttk.Label(self, text=f'{self.levain.ratio:.0f} %', style=ingredient_style()).grid(
            row=2, column=1, sticky='ew', padx=10, pady=2
        )

        ttk.Label(self, text='Starter hydration', style=ingredient_style()).grid(
            row=3, column=0, sticky='ew', padx=10, pady=2
        )
        ttk.Label(self, text=f'{self.levain.starter_hydration:.0f} %', style=ingredient_style()).grid(
            row=3, column=1, sticky='ew', padx=10, pady=2
        )
