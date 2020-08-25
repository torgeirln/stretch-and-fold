import tkinter as tk
from tkinter import ttk

from ui.fragments.recipe_item import RecipeItem

class RecipesFragment(ttk.Frame):
    def __init__(self, parent, view_model):
        super().__init__(parent, relief='raised')
        self.view_model = view_model
        self.init_constants()
        self.init_styles()
        self.create_content()
        # self.pack(side=tk.LEFT, fill=tk.BOTH, anchor=tk.W, expand=True, pady=self.pady, padx=self.padx)

    def init_constants(self):
        # Paddings
        self.padx = 10
        self.pady = 1

    def init_styles(self):
        # Description
        ttk.Style().configure('RecipeItem_Description.TLabel', font="Helvetica 14 bold")

    def create_content(self):
        self.view_model.get_recipes(callback=self.show_recipes)

    def show_recipes(self, recipes):
        self.recipes = recipes
        self.recipe_items = []
        for i, recipe in enumerate(self.recipes):
            recipe_item = RecipeItem(self, recipe)
            # recipe_item.grid(row=i, pady=self.pady, sticky=tk.W+tk.E)
            recipe_item.pack(anchor=tk.W, fill=tk.Y, ipady=self.pady)
            self.recipe_items.append(recipe_item)
