import tkinter as tk
from tkinter import ttk

from ui.base.image_frame import ImageFrame


class SummaryItem(ttk.Frame):
    def __init__(self, parent, recipe, show_recipe_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.recipe = recipe
        self.show_recipe_callback = show_recipe_callback
        self.init_styles()
        self.create_content()
        self.bind('<Button-1>', self.on_item_clicked)

    def init_styles(self):
        # Description
        self.title_style = 'RecipeItem_Title.TLabel'
        ttk.Style().configure(self.title_style, font="Helvetica 16 bold")
        self.description_style = 'RecipeItem_Description.TLabel'
        ttk.Style().configure(self.description_style, font="Helvetica 11 italic")

    def create_content(self):
        self.title_label = ttk.Label(self, text=f'{self.recipe.title}', style=self.title_style)
        self.title_label.bind('<Button-1>', self.on_item_clicked)
        self.title_label.grid(row=0, column=0, sticky="new", pady=5)

        self.description_label = ttk.Label(
            self, 
            text=self.recipe.description, 
            style=self.description_style, 
            justify='left',
            wraplength=400
        )
        self.description_label.bind('<Button-1>', self.on_item_clicked)
        self.description_label.grid(row=1, column=0, sticky="new", pady=5, padx=5)

        self.image_frame = ImageFrame(self, self.recipe.image_path, size=(128, 128))
        self.image_frame.bind('<Button-1>', self.on_item_clicked)
        self.image_frame.grid(row=1, column=1, sticky='nse', padx=5)

    def on_item_clicked(self, *args):
        print('Item pressed!')
        self.show_recipe_callback(self.recipe)
