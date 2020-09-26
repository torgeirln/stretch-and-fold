import tkinter as tk
from tkinter import ttk
from typing import List

from domain.models.ingredient_models import Ingredient
from ui.styles.recipe_styles import header_style, ingredient_style


class IngredientsPctPresenterItem(ttk.Frame):
    def __init__(self, parent, ingredients: List[Ingredient], *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ingredients = ingredients
        self.create_content()

    def create_content(self):
        self.ingredients_header_label = ttk.Label(
            self,
            text=f'Ingredients',
            style=header_style()
        )
        self.ingredients_header_label.grid(row=0, column=0, sticky="ew", pady=5)

        for i, ingredient in enumerate(self.ingredients):
            ttk.Label(self, text=ingredient.name, style=ingredient_style()).grid(
                row=i+1,
                column=0,
                sticky="new",
                padx=10,
                pady=2
            )
            ttk.Label(self, text=f'{ingredient.amount:.1f} %', style=ingredient_style()).grid(
                row=i+1,
                column=2,
                sticky="ew",
                padx=10,
                pady=2
            )
            