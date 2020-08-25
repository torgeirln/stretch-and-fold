import tkinter as tk
from tkinter import ttk


class IngredientItem(ttk.Frame):
    def __init__(self, parent, ingredient):
        super().__init__(parent)
        self.ingredient = ingredient
        self.init_constants()
        self.init_styles()
        self.create_content()

    def init_constants(self):
        self.pady = 1

    def init_styles(self):
        # Ingredient name
        ttk.Style().configure('IngredientItem_Name.TLabel', foreground='green', font="Helvetica 10")
        # Ingredient type
        ttk.Style().configure('IngredientItem_Type.TLabel', foreground='red')

    def create_content(self):
        self.name_label = ttk.Label(self, text=f'{self.ingredient.name}', style='IngredientItem_Name.TLabel')
        self.name_label.grid(column=0, row=0, sticky=tk.W, padx=2, pady=self.pady)

        self.type_label = ttk.Label(self, text=f'{self.ingredient.type}')
        self.type_label.grid(column=1, row=0, sticky=tk.W, padx=2, pady=self.pady)

        self.amount_label = ttk.Label(self, text=f'{self.ingredient.amount}')
        self.amount_label.grid(column=2, row=0, sticky=tk.W, padx=2, pady=self.pady)
