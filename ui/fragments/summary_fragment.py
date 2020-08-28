import tkinter as tk
from tkinter import ttk

from ui.items.recipe_item import RecipeItem
from ui.base.scrollable_frame import ScrollableFrame


class SummaryFragment(ScrollableFrame):
    def __init__(self, parent, view_model):
        super().__init__(parent)
        self.view_model = view_model
        self.init_constants()
        self.init_styles()
        self.create_content()

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
            recipe_item = RecipeItem(self.scrollable_frame, recipe)
            recipe_item.pack(ipady=self.pady, anchor="w")
            self.recipe_items.append(recipe_item)
