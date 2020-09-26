import tkinter as tk
from tkinter import ttk

from domain.types.ingredient_types import LevainTypes
from domain.models.levain_models import LevainPct
from ui.styles.recipe_styles import header_style, ingredient_style


class LevainPctsInputItem(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.init_constants()
        self.create_content()
    
    def init_constants(self):
        self.main_padx = 5
        self.row_spacing = 2
        
    def create_content(self):
        self.levain_title = ttk.Label(self, text='Levain', style=header_style())
        self.levain_title.grid(row=0, column=0, sticky='ew', pady=5)

        self.hydration_label = ttk.Label(self, text='Hydration:', style=ingredient_style())
        self.hydration_label.grid(row=1, column=0, sticky='ew', padx=self.main_padx, pady=self.row_spacing)
        self.hydration_entry = ttk.Entry(self)
        self.hydration_entry.insert(0, 175)
        self.hydration_entry.grid(row=1, column=1, sticky='ew', pady=2)

        self.starter_ratio_label = ttk.Label(self, text='Ratio of starter:', style=ingredient_style())
        self.starter_ratio_label.grid(row=2, column=0, sticky='ew', padx=self.main_padx, pady=self.row_spacing)
        self.starter_ratio_enty = ttk.Entry(self)
        self.starter_ratio_enty.insert(0, 25)
        self.starter_ratio_enty.grid(row=2, column=1, sticky='ew', pady=2)

        self.starter_hydration_label = ttk.Label(self, text='Hydration of starter:', style=ingredient_style())
        self.starter_hydration_label.grid(row=3, column=0, sticky='ew', padx=self.main_padx, pady=self.row_spacing)
        self.starter_hydration_entry = ttk.Entry(self)
        self.starter_hydration_entry.insert(0, 175)
        self.starter_hydration_entry.grid(row=3, column=1, sticky='ew', pady=2)

    def get_pcts(self):
        return LevainPct(
            float(self.hydration_entry.get()),
            float(self.starter_ratio_enty.get()),
            float(self.starter_hydration_entry.get())
        )
