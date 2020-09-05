import tkinter as tk
from tkinter import ttk

from ui.styles.recipe_styles import header_style, ingredient_style


class IngredientsWeightsPresenterItem(ttk.Frame):
    def __init__(self, parent, ingredients_weights, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ingredients_weights = ingredients_weights
        self.create_content()

    def create_content(self):
        self.ingredients_header_label = ttk.Label(
            self,
            text='Ingredients',
            style=header_style()
        )
        self.ingredients_header_label.grid(row=0, column=0, sticky="ew", pady=5)

        for i, ingredient in enumerate(self.ingredients_weights):
            ttk.Label(self, text=ingredient.name, style=ingredient_style()).grid(
                row=i+1,
                column=0,
                sticky="new",
                padx=10,
                pady=2
            )
            # ttk.Label(self, text=ingredient.type, style=self.ingredient_style).grid(
            #     row=i+1,
            #     column=1,
            #     sticky="ew",
            #     padx=10,
            #     pady=2
            # )
            ttk.Label(self, text=f'{ingredient.amount} g', style=ingredient_style()).grid(
                row=i+1,
                column=2,
                sticky="ew",
                padx=10,
                pady=2
            )
            