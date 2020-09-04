import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from domain.types.ingredient_types import IngredientTypes
from ui.items.inputs.ingredients_pcts_input import IngredientsPctsInputItem
from ui.items.inputs.levain_pcts_input import LevainPctsInputItem
from ui.items.inputs.desired_result_input import DesiredResultInputItem
from ui.items.presenters.ingredients_weights_presenter import IngredientsWeightsPresenterItem
from ui.items.presenters.levain_weigts_presenter import LevainWeightsPresenterItem
from ui.base.scrollable_frame import ScrollableFrame
from ui.styles.recipe_styles import header_style, ingredient_style


class CreateBakersPctRecipeFragment(ScrollableFrame):
    def __init__(self, parent, view_model, *args, **kwargs):
        super().__init__(parent, *args, padding="20 20 20 20", **kwargs)
        self.view_model = view_model
        self.rowconfigure(0, minsize=20)
        self.columnconfigure(1, weight=1)
        self.n_ingredients = 0
        self.ingredients = []
        self.n_init_rows = 1
        self.init_constants()
        self.create_content()

    def init_constants(self):
        self.row_spacing = 5
        
    def create_content(self):
        self.title_label = ttk.Label(self.scrollable_frame, text='Recipe title: ', style=ingredient_style())
        self.title_label.grid(row=0, column=0, sticky="nsew", pady=self.row_spacing)
        self.title_entry = ttk.Entry(self.scrollable_frame)
        self.title_entry.grid(row=0, column=1, sticky="nsew", pady=self.row_spacing)

        self.description_label = ttk.Label(self.scrollable_frame, text='Description: ', style=ingredient_style())
        self.description_label.grid(row=1, column=0, sticky='new')
        self.description_entry = ScrolledText(self.scrollable_frame, width=70, height=7)
        self.description_entry.grid(row=1, column=1, sticky='nsew', pady=self.row_spacing)

        self.sourdough_recipe_label = ttk.Label(self.scrollable_frame, text='Sourdough recipe', style=ingredient_style())
        self.sourdough_recipe_label.grid(row=2, column=0, sticky='nsew', pady=self.row_spacing)
        self.sourdough_recipe_checkbox_var = tk.IntVar()
        self.sourdough_recipe_checkbox_var.set(1)
        self.sourdough_recipe_checkbox = ttk.Checkbutton(
            self.scrollable_frame, 
            variable=self.sourdough_recipe_checkbox_var, 
            command=self.on_sourdough_recipe_clicked
        )
        self.sourdough_recipe_checkbox.grid(row=2, column=1, sticky='w')

        self.add_image_button = ttk.Button(
            self.scrollable_frame, 
            text='Add image', 
            command=self.on_add_image_button_clicked
        )
        self.add_image_button.grid(row=3, column=0, sticky='w', pady=self.row_spacing)
        self.add_image_label = ttk.Label(self.scrollable_frame, text='Default')
        self.add_image_label.grid(row=3, column=1, sticky='w')

        self.desired_result_frame = DesiredResultInputItem(
            self.scrollable_frame,
            levain_entry_callback=self.on_levain_entry_changed
        )
        self.desired_result_frame.grid(row=5, column=0, columnspan=2, sticky='nsew', pady=10)

        self.levain_frame = LevainPctsInputItem(self.scrollable_frame)
        self._show_levain_frame()
        
        self.ingredients_frame = IngredientsPctsInputItem(self.scrollable_frame)
        self.ingredients_frame.grid(row=11, column=0, columnspan=2, sticky='nsew', pady=10)

        self.button_frame = ttk.Frame(self.scrollable_frame)
        self.show_weights_button = ttk.Button(
            self.button_frame, 
            text='Show weights',
            command=self.on_show_weights_clicked
        )
        self.show_weights_button.grid(row=0, column=0, sticky='new')
        self.save_button = ttk.Button(
            self.button_frame, 
            text='Save recipe',
            command=self.on_save_recipe_clicked
        )
        self.save_button.grid(row=0, column=1, sticky='e', padx=5)
        self.button_frame.grid(row=12, column=0, sticky='new', pady=10)

        self.on_show_weights_clicked()

    def show_weights(self, ingreidents_weights, levain):
        total_dough_weight = 0
        for ingredient in ingreidents_weights:
            total_dough_weight += ingredient.amount
            print(f'{ingredient.name} {ingredient.type} {ingredient.amount}')
        print(f'total_dough_weight = {total_dough_weight}')
        self.levain_weights_frame = LevainWeightsPresenterItem(self.scrollable_frame, levain)
        self.levain_weights_frame.grid(row=15, column=0, columnspan=2, sticky='nsew', pady=10)
        self.ingredients_weights_frame = IngredientsWeightsPresenterItem(
            self.scrollable_frame,
            ingreidents_weights
        )
        self.ingredients_weights_frame.grid(row=16, column=0, columnspan=2, sticky='nsew', pady=10)

    def on_sourdough_recipe_clicked(self, *args):
        print('Sourdough recipe checkbox clicked!')
        if self.sourdough_recipe_checkbox_var.get() == 0:
            print('- Removing sourdough items')
            self.desired_result_frame.hide_levain_input()
            self._hide_levain_frame()
            self.ingredients_frame.hide_levain()
        else:
            print('- Adding sourdough items')
            self.desired_result_frame.show_levain_input()
            self._show_levain_frame()
            self.ingredients_frame.show_levain()
        
    def on_show_weights_clicked(self, *args):
        print('Show weights button clicked!')
        ingredients_pct = self.ingredients_frame.get_ingredients()
        # print(ingredients_pct[0].name)
        # print(ingredients_pct[0].type)
        # print(ingredients_pct[0].amount)
        levain = self.levain_frame.get_pcts()
        total_dough_weight = float(self.desired_result_frame.get_dough_weight())
        self.view_model.compute_recipe_weights(
            self.show_weights,
            total_dough_weight,
            self.desired_result_frame.get_desired_result(),
            ingredients_pct, 
            levain
        )

    def on_save_recipe_clicked(self, *args):
        print('Save recipe button clicked!')

    def on_add_image_button_clicked(self, *args):
        print('Add image button clicked!')
        # path_to_image = ...
        # self.add_image_label.configure(text=path_to_image)

    def on_levain_entry_changed(self, new_value):
        try:
            self.ingredients_frame.update_levain_pct(new_value)
        except:
            pass

    def _show_levain_frame(self):
        self.levain_frame.grid(row=10, column=0, columnspan=2, sticky='nsew', pady=10)

    def _hide_levain_frame(self):
        self.levain_frame.grid_forget()
