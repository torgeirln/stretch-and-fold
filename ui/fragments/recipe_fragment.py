import tkinter as tk
from tkinter import ttk

from ui.base.scrollable_frame import ScrollableFrame
from ui.base.image_frame import ImageFrame
from ui.items.presenters.ingredients_weights_presenter import IngredientsWeightsPresenterItem
from ui.items.presenters.levain_weigts_presenter import LevainWeightsPresenterItem
from ui.styles.recipe_styles import description_style, header_style, ingredient_style


class RecipeFragment(ScrollableFrame):
    def __init__(self, parent, recipe, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.recipe = recipe
        self.init_constants()
        self.create_content()
    
    def init_constants(self):
        # Paddings
        self.main_padx = 20
        
    def create_content(self):
        self.description_label = ttk.Label(
            self.scrollable_frame, 
            text=self.recipe.description, 
            style=description_style(), 
            justify='left',
            wraplength=450
        )
        self.description_label.grid(row=1, column=0, sticky="new", padx=self.main_padx, pady=10)
        
        self.image_frame = ImageFrame(self.scrollable_frame, self.recipe.image_path, size=(128*2, 128*2))
        self.image_frame.grid(row=2, column=1, rowspan=2, sticky='ns', padx=5)

        self.ingredients_frame = IngredientsWeightsPresenterItem(
            self.scrollable_frame,
            self.recipe.ingredients
        )
        self.ingredients_frame.grid(row=3, column=0, sticky='new', padx=self.main_padx, pady=10)

        self.levain_frame = LevainWeightsPresenterItem(
            self.scrollable_frame,
            self.recipe.levain
        )
        self.levain_frame.grid(row=4, column=0, sticky='new', padx=self.main_padx, pady=10)

        self.bakers_per_header_label = ttk.Label(
            self.scrollable_frame,
            text='Baker\'s percentages',
            style=header_style()
        )
        self.bakers_per_header_label.grid(row=5, column=0, sticky="ew", padx=self.main_padx, pady=10)
