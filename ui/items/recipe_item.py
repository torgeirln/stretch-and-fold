import tkinter as tk
from tkinter import ttk

from ui.items.ingredient_item import IngredientItem

class RecipeItem(ttk.Frame):
    def __init__(self, parent, recipe):
        super().__init__(parent)
        self.recipe = recipe
        self.init_constants()
        self.init_styles()
        self.create_content()

    def init_constants(self):
        # Paddings
        self.padx = 20
        self.ipadx = 2
        self.ipady = 2

    def init_styles(self):
        # Description
        ttk.Style().configure('RecipeItem_Description.TLabel', font="Helvetica 14 bold")

    def create_content(self):
        self.description_label = ttk.Label(self, text=f'{self.recipe.description}', style='RecipeItem_Description.TLabel')
        self.description_label.grid(row=0, column=0, sticky=tk.W)
        self.ingredient_items = []
        for i, ingredient in enumerate(self.recipe.ingredients):
            ingredient_item = IngredientItem(self, ingredient)
            ingredient_item.grid(row=i+1, column=0, sticky=tk.W+tk.E, padx=self.padx)
            self.ingredient_items.append(ingredient_item)
        self.modify_btn = ttk.Button(self, text='Modify', command=self.on_modify_btn_pressed)
        self.modify_btn.grid(row=i+2, column=0, sticky=tk.E)

    def on_modify_btn_pressed(self, *args):
        print('Modify button pressed!')
