import tkinter as tk
from tkinter import ttk

from ui.base.image_frame import ImageFrame
from ui.base.scrollable_frame import ScrollableFrame
from ui.items.presenters.ingredients_weights_presenter import IngredientsWeightsPresenterItem
from ui.items.presenters.ingredients_pct_presenter import IngredientsPctPresenterItem
from ui.items.presenters.levain_pct_presenter import LevainPctPresenterItem
from ui.items.presenters.levain_weigts_presenter import LevainWeightsPresenterItem
from ui.items.presenters.overview_presenter import OverviewPresenterFrame
from ui.styles.recipe_styles import description_style, header_style, ingredient_style


class RecipeFragment(ScrollableFrame):
    def __init__(self, parent, recipe, view_model, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.recipe = recipe
        self.view_model = view_model
        self.init_constants()
        self.create_content()
    
    def init_constants(self):
        # Paddings
        self.main_padx = 20
        
    def create_content(self):
        # Header 
        self.category_label = ttk.Label(self.scrollable_frame, text=f'- {self.recipe.category}', style=description_style())
        self.category_label.grid(
            row=0, column=0, sticky='new', padx=self.main_padx, pady=10
        )
        self.image_frame = ImageFrame(self.scrollable_frame, self.recipe.image_path, size=(128*2, 128*2))
        self.image_frame.grid(row=0, column=2, rowspan=3, sticky='new', padx=5)
        self.description_label = ttk.Label(
            self.scrollable_frame, 
            text=self.recipe.description, 
            style=description_style(), 
            justify='left',
            wraplength=450
        )
        self.description_label.grid(row=1, column=0, columnspan=2, sticky="new", padx=self.main_padx, pady=10)
        # Overview
        self.overview_presenter_frame = OverviewPresenterFrame(
            self.scrollable_frame, self.recipe.overview)
        self.overview_presenter_frame.grid(row=2, column=0, sticky='w', padx=self.main_padx, pady=10)
        # Levain
        self.levain_pct_presenter_frame = LevainPctPresenterItem(
            self.scrollable_frame, self.recipe.levain)
        self.levain_pct_presenter_frame.grid(row=2, column=1, sticky='w', pady=10)
        # Ingredients
        self.ingredients_pct_presenter_frame = IngredientsPctPresenterItem(
            self.scrollable_frame, self.recipe.ingredients)
        self.ingredients_pct_presenter_frame.grid(row=5, column=0, columnspan=2, sticky='news', padx=self.main_padx, pady=10)
        # Inputs for weights calculation
        self.weights_input_frame = ttk.Frame(self.scrollable_frame)
        ttk.Label(self.weights_input_frame, text='Total dough weight', style=header_style()).grid(
            columnspan=2, sticky='ew', pady=5
        )
        # - Item weight
        ttk.Label(self.weights_input_frame, text=f'Item weight [g]', style=ingredient_style()).grid(
            row=1, column=0, sticky='ew', padx=10, pady=2
        )
        self.item_weight_var = tk.StringVar()
        self.item_weight_var.set(f'{self.recipe.dough_size.item_weight:.0f}')
        self.item_weight_var.trace("w", self.on_total_dough_weight_changed)
        self.item_weight_enty = ttk.Entry(
            self.weights_input_frame, textvariable=self.item_weight_var, width=5
        )
        self.item_weight_enty.grid(row=1, column=1, sticky='nw')
        # - Number of items
        ttk.Label(self.weights_input_frame, text=f'Number of items', style=ingredient_style()).grid(
            row=2, column=0, sticky='ew', padx=10, pady=2
        )
        self.number_of_items_var = tk.StringVar()
        self.number_of_items_var.trace("w", self.on_total_dough_weight_changed)
        self.number_of_items_var.set(f'{self.recipe.dough_size.n_items:.0f}')
        self.number_of_items_enty = ttk.Entry(
            self.weights_input_frame, textvariable=self.number_of_items_var, width=5
        )
        self.number_of_items_enty.grid(row=2, column=1, sticky='nw')
        self.weights_input_frame.grid(row=6, column=0, columnspan=2, sticky='new', padx=self.main_padx, pady=10)

    def on_total_dough_weight_changed(self, *args):
        print('on_total_dough_weight_changed')
        total_dough_weight = float(self.item_weight_var.get()) * int(self.number_of_items_var.get())
        self.view_model.compute_recipe_weights(
            self.show_weights,
            total_dough_weight,
            self.recipe.overview,
            self.recipe.ingredients, 
            self.recipe.levain
        )
        
    def show_weights(self, ingreidents_weights, levain):
        total_dough_weight = 0
        for ingredient in ingreidents_weights:
            total_dough_weight += ingredient.amount
            print(f'{ingredient.name} {ingredient.type_} {ingredient.amount}')
        print(f'total_dough_weight = {total_dough_weight}')
        self.levain_weights_frame = LevainWeightsPresenterItem(self.scrollable_frame, levain, add_buffert=True)
        self.levain_weights_frame.grid(row=15, column=0, columnspan=2, sticky='nsew', padx=self.main_padx, pady=10)
        self.ingredients_weights_frame = IngredientsWeightsPresenterItem(
            self.scrollable_frame,
            ingreidents_weights
        )
        self.ingredients_weights_frame.grid(row=16, column=0, columnspan=2, sticky='nsew', padx=self.main_padx, pady=10)