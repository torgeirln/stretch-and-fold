import tkinter as tk
from tkinter import ttk

from domain.types.ingredient_types import IngredientTypes
from domain.models.ingredient_models import Ingredient, LeaveningAgents
from ui.items.inputs.ingredient_type_combobox import LeaveningAgentFlags
from ui.items.inputs.ingredient_pct_entry import IngredientPctEntry, IngredientEntryFlags
from ui.styles.recipe_styles import header_style, column_title_style


class IngredientsPctsInputItem(ttk.Frame):
    def __init__(self, parent, leavening_agent_changed_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.leavening_agent_changed_callback = leavening_agent_changed_callback
        self.ingredients_entires = []
        self.init_constants()
        self.create_content()
    
    def init_constants(self):
        self.main_padx = 0
        self.n_init_rows = 2
        self.n_max_ingredients = 30
        self.pct_entry_width = 5
    
    def create_content(self):
        # self.columnconfigure(0, minsize=300)
        # self.columnconfigure(1, minsize=200)
        # self.columnconfigure(2, minsize=50)
        self.ingredients_entry_title = ttk.Label(self, text='Ingredients in baker\'s percentages', style=header_style())
        self.ingredients_entry_title.grid(row=0, column=0, sticky='ew', pady=2)
        # Add column titles
        # column0_title = ttk.Label(self, text='Name', style=column_title_style())
        # column0_title.grid(row=1, column=0, pady=5)
        # column1_title = ttk.Label(self, text='Type', style=column_title_style())
        # column1_title.grid(row=1, column=1, pady=5)
        # column2_title = ttk.Label(self, text='Percentage', style=column_title_style())
        # column2_title.grid(row=1, column=2, pady=5)
        # Add must have ingredients
        self.add_ingredient('Levain (finmalt grovmjöl)', IngredientTypes.levain, pct=20)
        self.add_ingredient('Vetemjöl special', IngredientTypes.flour, pct=70)
        self.add_ingredient('Grahamsmjöl', IngredientTypes.flour, pct=30)
        self.add_ingredient('Finkornigt salt', IngredientTypes.salt, pct=100)
        self.add_ingredient('Vatten', IngredientTypes.liquid, pct=100)
        # Button
        self.add_ingredient_button = ttk.Button(self, text='Add ingredient', command=self.on_add_ingredient_clicked)
        self.add_ingredient_button.grid(row=self.n_max_ingredients, column=0, sticky='w', padx=10, pady=5)

    def add_ingredient(self, name=None, type_=None, pct=None):
        current_row = len(self.ingredients_entires) + self.n_init_rows
        
        ingredient_entry = IngredientPctEntry(self, 
            name, type_, pct,
            self.on_ingredient_entry_changed)
        ingredient_entry.grid(row=current_row, sticky='nsew', padx=10, pady=5)

        self.ingredients_entires.append(ingredient_entry)

    def on_add_ingredient_clicked(self, *args):
        print('Add ingredient clicked!')
        self.add_ingredient()
            
    def on_ingredient_entry_changed(self, flag, *data):
        if flag == IngredientEntryFlags.name_changed:
            pass
        elif flag == IngredientEntryFlags.type_changed:
            self.leavening_agent_changed_callback(*data)
        elif flag == IngredientEntryFlags.pct_changed:
            if data[0] == IngredientTypes.levain:
                self.leavening_agent_changed_callback(LeaveningAgentFlags.levain_updated, data[1])
            elif data[0] == IngredientTypes.yeast:
                self.leavening_agent_changed_callback(LeaveningAgentFlags.yeast_updated, data[1])

    def get_ingredients(self):
        ingredients = []
        for i, ingr_entry in enumerate(self.ingredients_entires):
            ingr = self.get_ingredient_from_entry(ingr_entry)
            if ingr is not None:
                ingredients.append(ingr)
        return ingredients
    
    def get_ingredient_from_entry(self, ingr_entry):
        name, type_, pct = ingr_entry.get_raw_ingredient_values()
        if len(name) > 0 and len(type_) > 0 and len(pct) > 0:
            return Ingredient(name, type_, float(pct))
        else:
            # The ingredient is not entered
            return None

    def get_leavening_agents(self):
        levain = self.get_ingredients_with_type(IngredientTypes.levain)
        levain_pct = levain[0].amount if len(levain) > 0 else 0
        yeast = self.get_ingredients_with_type(IngredientTypes.yeast)
        yeast_pct = yeast[0].amount if len(yeast) > 0 else 0
        return LeaveningAgents(levain_pct, yeast_pct)

    def get_ingredients_with_type(self, ingr_type):
        ingredients = []
        for ingr_entry in self.ingredients_entires:
            type_ = ingr_entry.get_type()
            if type_ == ingr_type:
                ingr = self.get_ingredient_from_entry(ingr_entry)
                if ingr is not None: 
                    ingredients.append(ingr)
        return ingredients

    def contains_ingredient_with_type(self, ingr_type):
        return len(self.get_ingredients_with_type(ingr_type)) > 0
    