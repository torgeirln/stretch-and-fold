import tkinter as tk
from tkinter import ttk

from domain.models.dough_size_models import DoughSize
from ui.styles.recipe_styles import header_style, ingredient_style


class DoughSizeInput(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.init_constants()
        self.create_content()

    def init_constants(self):
        self.main_padx = 5
        self.row_spacing = 2
        self.entry_width = 5
    
    def create_content(self):
        ttk.Label(self, text='Total dough weight', style=header_style()).grid(
            row=0, column=0, columnspan=3, sticky='nsew', pady=self.row_spacing)

        # Weight per item
        ttk.Label(self, text='Weight per item: ', style=ingredient_style()).grid(
            row=1, column=0, sticky="w", padx=self.main_padx, pady=self.row_spacing)
        self.item_weight_entry = ttk.Entry(self, width=self.entry_width)
        self.item_weight_entry.insert(0, 700)
        self.item_weight_entry.grid(row=1, column=1, sticky="w", pady=self.row_spacing)
        ttk.Label(self, text='g', style=ingredient_style()).grid(
            row=1, column=2, sticky="w", padx=2, pady=self.row_spacing)
        
        # Number of items
        ttk.Label(self, text='Number of items: ', style=ingredient_style()).grid(
            row=2, column=0, sticky="w", padx=self.main_padx, pady=self.row_spacing)
        self.number_of_items_entry = ttk.Entry(self, width=self.entry_width)
        self.number_of_items_entry.insert(0, 2)
        self.number_of_items_entry.grid(row=2, column=1, sticky="w", pady=self.row_spacing)
        
    def get_total_dough_weight(self):
        item_weight = float(self.item_weight_entry.get())
        n_items = int(self.number_of_items_entry.get())
        return item_weight * n_items
    
    def get_dough_size(self):
        return DoughSize(
            item_weight=float(self.item_weight_entry.get()),
            n_items=int(self.number_of_items_entry.get())
        )
