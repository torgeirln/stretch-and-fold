import tkinter as tk
from tkinter import ttk

from ui.styles.recipe_styles import header_style, ingredient_style


class OverviewPresenterFrame(ttk.Frame):
    def __init__(self, parent, overview, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.overview = overview
        self.create_content()

    def create_content(self):
        self.overview_header_label = ttk.Label(self, text=f'Overview', style=header_style())
        self.overview_header_label.grid(sticky='ew', pady=5)

        self.hydration_name_label = ttk.Label(self, text=f'Hydration', style=ingredient_style())
        self.hydration_name_label.grid(row=1, column=0, sticky='ew', padx=5, pady=2)
        self.hydration_value_label = ttk.Label(self, text=f'{self.overview.hydration:.1f} %', style=ingredient_style())
        self.hydration_value_label.grid(row=1, column=1, sticky='ew')

        self.salt_name_label = ttk.Label(self, text=f'Salt', style=ingredient_style())
        self.salt_name_label.grid(row=2, column=0, sticky='ew', padx=5, pady=2)
        self.salt_value_label = ttk.Label(self, text=f'{self.overview.salt:.1f} %', style=ingredient_style())
        self.salt_value_label.grid(row=2, column=1, sticky='ew')

        if self.overview.levain is not None:
            self.levain_name_label = ttk.Label(self, text=f'Levain', style=ingredient_style())
            self.levain_name_label.grid(row=3, column=0, sticky='ew', padx=5, pady=2)
            self.levain_value_label = ttk.Label(self, text=f'{self.overview.levain:.1f} %', style=ingredient_style())
            self.levain_value_label.grid(row=3, column=1, sticky='ew')
