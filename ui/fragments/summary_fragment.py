import tkinter as tk
from tkinter import ttk

from ui.items.summary_item import SummaryItem
from ui.base.scrollable_frame import ScrollableFrame


class SummaryFragment(ScrollableFrame):
    def __init__(self, parent, view_model, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.view_model = view_model
        self.init_constants()
        self.init_styles()
        self.create_content()

    def init_constants(self):
        # Paddings
        self.padx = 10
        self.summary_item_pady = 5
        self.summary_item_padx = 10

    def init_styles(self):
        # Description
        ttk.Style().configure('Leif.TFrame', background="red")

    def create_content(self):
        self.view_model.get_recipes(callback=self.show_recipes)

    def show_recipes(self, recipes):
        self.recipes = recipes
        self.summary_items = []
        for i, recipe in enumerate(self.recipes):
            summary_item = SummaryItem(self.scrollable_frame, recipe, self.on_summary_item_clicked)
            summary_item.pack(anchor="w", fill='x', expand=True, pady=self.summary_item_pady, padx=self.summary_item_padx)
            self.summary_items.append(summary_item)

    def on_summary_item_clicked(self, recipe):
        print(f'- Opening recipe {recipe.title}')
        self.parent.show_recipe(recipe)
