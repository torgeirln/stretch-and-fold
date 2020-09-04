import tkinter as tk
from tkinter import ttk

from domain.types.ingredient_types import IngredientTypes
# from domain.models.ingredient_models import IngredientPctModel, SimpleIngredient
from domain.models.ingredient_models import IngredientModel
from ui.styles.recipe_styles import header_style, column_title_style


class IngredientsPctsInputItem(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ingredients_entires = []
        self.init_constants()
        self.create_content()
    
    def init_constants(self):
        self.include_levain = False
        self.main_padx = 0
        self.n_init_rows = 2
        self.n_max_ingredients = 30
    
    def create_content(self):
        self.columnconfigure(0, minsize=300)
        self.columnconfigure(1, minsize=200)
        self.columnconfigure(2, minsize=50)
        self.ingredients_entry_title = ttk.Label(self, text='Ingredients in baker\'s percentages', style=header_style())
        self.ingredients_entry_title.grid(row=0, column=0, sticky='ew', pady=2)
        # Add column titles
        column0_title = ttk.Label(self, text='Name', style=column_title_style())
        column0_title.grid(row=1, column=0, pady=5)
        column1_title = ttk.Label(self, text='Type', style=column_title_style())
        column1_title.grid(row=1, column=1, pady=5)
        column2_title = ttk.Label(self, text='Percentage', style=column_title_style())
        column2_title.grid(row=1, column=2, pady=5)
        # Add must have ingredients
        # self.add_ingredient('Levain', IngredientTypes.levain, pct=22)
        self.__add_levain()
        self.add_ingredient('Vetemjöl special', IngredientTypes.flour, pct=80)
        self.add_ingredient('Grahamsmjöl', IngredientTypes.flour, pct=20)
        self.add_ingredient('Vatten', IngredientTypes.liquid, pct=100)
        self.add_ingredient('Finkornigt salt', IngredientTypes.salt, pct=100)
        # self.add_ingredient('Ost', IngredientTypes.other, pct=10)
        # self.add_ingredient('Jaller', IngredientTypes.other, pct=10)
        # Button
        self.add_ingredient_button = ttk.Button(self, text='Add ingredient', command=self.on_add_ingredient_clicked)
        self.add_ingredient_button.grid(row=self.n_max_ingredients, column=0, sticky='w', padx=10, pady=5)

    def add_ingredient(self, name=None, type_=None, pct=None):
        current_row = len(self.ingredients_entires) + self.n_init_rows
        name_entry = ttk.Entry(self)
        if name is not None:
            name_entry.insert(0, name)
        name_entry.grid(row=current_row, column=0, sticky='ew', padx=10, pady=5)
        
        type_combobox = ttk.Combobox(self, values=IngredientTypes.combobox_types)
        if type_ is not None:
            type_combobox.current(self._get_ingredient_index(type_))
        type_combobox.grid(row=current_row, column=1)

        pct_entry = ttk.Entry(self)
        if pct is not None:
            pct_entry.insert(0, pct)
        pct_entry.grid(row=current_row, column=2, padx=10)

        self.ingredients_entires.append((name_entry, type_combobox, pct_entry))

    def on_add_ingredient_clicked(self, *args):
        print('Add ingredient clicked!')
        self.add_ingredient()

    def _get_ingredient_index(self, type_):
        for index, ingr in enumerate(IngredientTypes.combobox_types):
            if ingr == type_:
                return index

    def get_ingredients(self):
        ingredients = []
        for i, entries in enumerate(self.ingredients_entires):
            name = entries[0].get()
            if i == 0:
                type_ = entries[1].cget('text')
                pct = entries[2].cget('text')
            else:
                type_ = entries[1].get()
                pct = entries[2].get()
            try:
                ingredients.append(IngredientModel(name, type_, float(pct)))
            except:
                pass
        if not self.include_levain:
            ingredients.remove(ingredients[0])
        return ingredients

    def __add_levain(self):
        self.levain_name_entry = ttk.Entry(self)
        self.levain_name_entry.insert(0, 'Levain')
        self.levain_type_label = ttk.Label(self, text=IngredientTypes.levain)
        self.levain_pct_label = ttk.Label(self, text='22')
        self.show_levain()
        self.ingredients_entires.append(
            (self.levain_name_entry, self.levain_type_label, self.levain_pct_label)
        )

    def hide_levain(self):
        self.include_levain = False
        self.levain_name_entry.grid_forget()
        self.levain_type_label.grid_forget()
        self.levain_pct_label.grid_forget()

    def show_levain(self):
        self.include_levain = True
        self.levain_name_entry.grid(row=self.n_init_rows, column=0, sticky='ew', padx=10, pady=5)
        self.levain_type_label.grid(row=self.n_init_rows, column=1)
        self.levain_pct_label.grid(row=self.n_init_rows, column=2, padx=10)

    def update_levain_pct(self, new_pct):
        self.levain_pct_label.configure(text=f'{new_pct}')
        