import tkinter as tk
from tkinter import ttk

from domain.models.overview_models import Overview
from ui.styles.recipe_styles import header_style, ingredient_style


class DesiredResultInputItem(ttk.Frame):
    def __init__(self, parent, levain_entry_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.levain_entry_callback = levain_entry_callback
        self.init_constants()
        self.create_content()

    def init_constants(self):
        self.main_padx = 5
        self.row_spacing = 2
        
    def create_content(self):
        self.desired_result_label = ttk.Label(self, text='Desired result', style=header_style())
        self.desired_result_label.grid(row=0, column=0, sticky='nsew', pady=self.row_spacing)
        # - Weight per item
        self.item_weight_label = ttk.Label(self, text='Weight per item: ', style=ingredient_style())
        self.item_weight_label.grid(row=1, column=0, sticky="nsew", padx=self.main_padx, pady=self.row_spacing)
        self.item_weight_entry = ttk.Entry(self)
        self.item_weight_entry.insert(0, 800)
        self.item_weight_entry.grid(row=1, column=1, sticky="w", pady=self.row_spacing)
        self.item_weight_unit_label = ttk.Label(self, text='g', style=ingredient_style())
        self.item_weight_unit_label.grid(row=1, column=2, sticky="w", padx=2, pady=self.row_spacing)
        # - Hydration
        self.item_hydartion_label = ttk.Label(self, text='Hydration: ', style=ingredient_style())
        self.item_hydartion_label.grid(row=2, column=0, sticky="nsew", padx=self.main_padx, pady=self.row_spacing)
        self.item_hydartion_entry = ttk.Entry(self)
        self.item_hydartion_entry.insert(0, 80)
        self.item_hydartion_entry.grid(row=2, column=1, sticky="w", pady=self.row_spacing)
        # - Salt
        self.item_salt_label = ttk.Label(self, text='Salt: ', style=ingredient_style())
        self.item_salt_label.grid(row=3, column=0, sticky="nsew", padx=self.main_padx, pady=self.row_spacing)
        self.item_salt_entry = ttk.Entry(self)
        self.item_salt_entry.insert(0, 2.2)
        self.item_salt_entry.grid(row=3, column=1, sticky="w", pady=self.row_spacing)
        # - Levain
        self.item_levain_label = ttk.Label(self, text='Levain: ', style=ingredient_style())
        self.levain_entry_var = tk.StringVar()
        self.levain_entry_var.trace("w", self.on_levain_entry_changed)
        self.item_levain_entry = ttk.Entry(self, textvariable=self.levain_entry_var)
        # self.item_levain_entry.insert(0, 22)
        self.levain_entry_var.set('22')
        self.show_levain_input()

    def hide_levain_input(self):
        self.item_levain_label.grid_forget()
        self.item_levain_entry.grid_forget()

    def show_levain_input(self):
        self.item_levain_label.grid(row=4, column=0, sticky="nsew", padx=self.main_padx, pady=self.row_spacing)
        self.item_levain_entry.grid(row=4, column=1, sticky="w", pady=self.row_spacing)

    def on_levain_entry_changed(self, *args):
        self.levain_entry_callback(self.levain_entry_var.get())

    def get_dough_weight(self):
        return self.item_weight_entry.get()
    
    def get_desired_result(self):
        return Overview(
            float(self.item_weight_entry.get()),
            float(self.item_hydartion_entry.get()),
            float(self.item_salt_entry.get()),
            float(self.item_levain_entry.get())
        )
