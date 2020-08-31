import tkinter as tk
from tkinter import ttk

from ui.base.scrollable_frame import ScrollableFrame
from ui.base.image_frame import ImageFrame
from ui.items.ingredient_item import IngredientItem


class RecipeFragment(ScrollableFrame):
    def __init__(self, parent, recipe, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.recipe = recipe
        self.init_constants()
        self.init_styles()
        self.create_content()
    
    def init_constants(self):
        # Paddings
        self.main_padx = 20

    def init_styles(self):
        # Description
        self.description_style = 'Recipe_Description.TLabel'
        ttk.Style().configure(self.description_style, font="Helvetica 12 italic")
        self.header_style = 'Recipe_Ingredients_Header.TLabel'
        ttk.Style().configure(self.header_style, font="Helvetica 16 bold")
        self.ingredient_style = 'Recipe_Ingredient.TLabel'
        ttk.Style().configure(self.ingredient_style, font="Helvetica 12")
        

    def create_content(self):
        self.description_label = ttk.Label(
            self.scrollable_frame, 
            text=self.recipe.description, 
            style=self.description_style, 
            justify='left',
            wraplength=450
        )
        self.description_label.grid(row=1, column=0, sticky="new", padx=self.main_padx, pady=10)
        
        self.image_frame = ImageFrame(self.scrollable_frame, self.recipe.rel_image_path, size=(128*2, 128*2))
        self.image_frame.grid(row=2, column=1, rowspan=2, sticky='ns', padx=5)

        # Ingredients table
        self.ingredients_frame = ttk.Frame(self.scrollable_frame)
        self.ingredients_header_label = ttk.Label(
            self.ingredients_frame,
            text='Ingredients',
            style=self.header_style
        )
        self.ingredients_header_label.grid(row=0, column=0, sticky="ew", pady=5)
        for i, ingredient in enumerate(self.recipe.ingredients):
            ttk.Label(self.ingredients_frame, text=ingredient.name, style=self.ingredient_style).grid(
                row=i+1,
                column=0,
                sticky="new",
                padx=10,
                pady=2
            )
            # ttk.Label(self.ingredients_frame, text=ingredient.type, style=self.ingredient_style).grid(
            #     row=i+1,
            #     column=1,
            #     sticky="ew",
            #     padx=10,
            #     pady=2
            # )
            ttk.Label(self.ingredients_frame, text=f'{ingredient.amount} g', style=self.ingredient_style).grid(
                row=i+1,
                column=2,
                sticky="ew",
                padx=10,
                pady=2
            )
        self.ingredients_frame.grid(row=3, column=0, sticky='new', padx=self.main_padx, pady=10)

        self.levain_frame = ttk.Frame(self.scrollable_frame)
        self.levain_header_label = ttk.Label(self.levain_frame, text='Levain', style=self.header_style)
        self.levain_header_label.grid(sticky='ew', pady=5)
        i = 0
        for key, value in self.recipe.levain.items():
            i += 1
            ttk.Label(self.levain_frame, text=key, style=self.ingredient_style).grid(
                row=i+1,
                column=0,
                sticky='ew',
                padx=10,
                pady=2
            )
            ttk.Label(self.levain_frame, text=f'{value} g', style=self.ingredient_style).grid(
                row=i+1,
                column=1,
                sticky='ew',
                padx=10,
                pady=2
            )

        self.levain_frame.grid(row=4, column=0, sticky='new', padx=self.main_padx, pady=10)


        self.bakers_per_header_label = ttk.Label(
            self.scrollable_frame,
            text='Baker\'s percentages',
            style=self.header_style
        )
        self.bakers_per_header_label.grid(row=5, column=0, sticky="ew", padx=self.main_padx, pady=10)
