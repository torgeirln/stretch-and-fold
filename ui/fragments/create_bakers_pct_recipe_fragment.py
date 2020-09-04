import tkinter as tk
from tkinter import ttk

from domain.types.ingredient_types import IngredientTypes
from ui.items.ingredients_pct_item import IngredientsPctItem
from ui.items.levain_item import LevainItem
from ui.base.scrollable_frame import ScrollableFrame


class CreateBakersPctRecipeFragment(ScrollableFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, padding="20 20 20 20", **kwargs)
        self.rowconfigure(0, minsize=20)
        self.columnconfigure(1, weight=1)
        self.n_ingredients = 0
        self.ingredients = []
        self.n_init_rows = 1
        self.init_constants()
        self.init_styles()
        self.create_content()

    def init_constants(self):
        self.row_spacing = 5

    def init_styles(self):
        # Description
        self.basic_label_style = 'CreateRecipe_BasicLabel.TLabel'
        ttk.Style().configure(self.basic_label_style, font="Helvetica 12")
        
    def create_content(self):
        self.title_label = ttk.Label(self.scrollable_frame, text='Recipe title: ', style=self.basic_label_style)
        self.title_label.grid(row=0, column=0, sticky="nsew", pady=self.row_spacing)
        self.title_entry = ttk.Entry(self.scrollable_frame)
        self.title_entry.grid(row=0, column=1, sticky="nsew", pady=self.row_spacing)

        self.n_dough_balls_label = ttk.Label(self.scrollable_frame, text='Number of dough balls: ', style=self.basic_label_style)
        self.n_dough_balls_label.grid(row=1, column=0, sticky="nsew", pady=self.row_spacing)
        self.n_dough_balls_entry = ttk.Entry(self.scrollable_frame)
        self.n_dough_balls_entry.grid(row=1, column=1, sticky="nsew", pady=self.row_spacing)

        self.dough_ball_weight_label = ttk.Label(self.scrollable_frame, text='Weight per dough ball [grams]: ', style=self.basic_label_style)
        self.dough_ball_weight_label.grid(row=2, column=0, sticky="nsew", pady=self.row_spacing)
        self.dough_ball_weight_entry = ttk.Entry(self.scrollable_frame)
        self.dough_ball_weight_entry.grid(row=2, column=1, sticky="nsew", pady=self.row_spacing)

        self.ingredients_frame = IngredientsPctItem(self.scrollable_frame)
        self.ingredients_frame.grid(row=3, column=0, columnspan=2, sticky='nsew', pady=10)

        self.levain_frame = LevainItem(self.scrollable_frame)
        self.levain_frame.grid(row=4, column=0, columnspan=2, sticky='nsew', pady=10)
