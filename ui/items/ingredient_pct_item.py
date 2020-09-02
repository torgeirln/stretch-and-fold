import tkinter as tk
from tkinter import ttk

from domain.types.ingredient_types import IngredientTypes


class IngredientPct(ttk.Frame):
    def __init__(self, parent, name=None, type_=None, pct=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.name = name
        self.type = type_
        self.pct = pct
        self.columnconfigure(0, weight=1)
        self.init_constants()
        self.init_styles()
        self.create_content()
    
    def init_constants(self):
        # Paddings
        self.main_padx = 0

    def init_styles(self):
        self.leif = 0
    
    def create_content(self):
        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(row=0, column=0, sticky='ew', pady=5)
        if self.name is not None:
            self.name_entry.insert(0, self.name)

        if self.type == IngredientTypes.main_flour or self.type == IngredientTypes.main_liquid:
            self.type_combobox = ttk.Label(self, text=self.type)
        else:
            self.type_combobox = ttk.Combobox(self, values=IngredientTypes.all_types)
        self.type_combobox.grid(row=0, column=1, sticky='ew', padx=10)

        if self.pct == -1:
            self.pct_entry = ttk.Label(self, text='')
        else:
            self.pct_entry = ttk.Entry(self)
            if self.pct is not None:
                self.pct_entry.insert(0, self.pct)
        self.pct_entry.grid(row=0, column=2, sticky='ew')
