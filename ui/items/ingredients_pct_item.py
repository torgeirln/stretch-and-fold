import tkinter as tk
from tkinter import ttk

from domain.types.ingredient_types import IngredientTypes
from domain.models.ingredient_models import IngredientPctModel


class IngredientsPctItem(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ingredients = []
        # self.init_ids = []
        # self.init_widgets = []
        self.init_constants()
        self.init_styles()
        self.create_content()
    
    def init_constants(self):
        self.main_padx = 0
        self.n_init_rows = 2
        self.n_max_ingredients = 30
        
    def init_styles(self):
        self.header_style = 'IngredientsPctItem_Header.TLabel'
        ttk.Style().configure(self.header_style, font="Helvetica 16 bold")
        self.column_title_style = 'IngredientsPctItem_ColumnTitle.TLabel'
        ttk.Style().configure(self.column_title_style, font="Helvetica 12 bold")
    
    def create_content(self):
        self.columnconfigure(0, minsize=300)
        self.columnconfigure(1, minsize=200)
        self.columnconfigure(2, minsize=50)
        self.ingredients_entry_title = ttk.Label(self, text='Ingredients:', style=self.header_style)
        self.ingredients_entry_title.grid(row=0, column=0, sticky='ew', pady=2)
        # Add column titles
        column0_title = ttk.Label(self, text='Name', style=self.column_title_style)
        column0_title.grid(row=1, column=0, pady=5)
        column1_title = ttk.Label(self, text='Type', style=self.column_title_style)
        column1_title.grid(row=1, column=1, pady=5)
        column2_title = ttk.Label(self, text='Percentage', style=self.column_title_style)
        column2_title.grid(row=1, column=2, pady=5)
        # Add must have ingredients
        self.add_ingredient('Vetemjöl special', IngredientTypes.main_flour, pct=-1)
        self.add_ingredient('Vatten', IngredientTypes.main_liquid, pct=80)
        # Button
        self.add_ingredient_button = ttk.Button(self, text='Add ingredient', command=self.on_add_ingredient_clicked)
        self.add_ingredient_button.grid(row=self.n_max_ingredients, column=0, sticky='w', pady=5)

    def add_ingredient(self, name=None, type_=None, pct=None):
        current_row = len(self.ingredients) + self.n_init_rows
        name_entry = ttk.Entry(self)
        if name is not None:
            name_entry.insert(0, name)
        name_entry.grid(row=current_row, column=0, sticky='ew', padx=10, pady=5)
        
        if type_ == IngredientTypes.main_flour or type_ == IngredientTypes.main_liquid:
            type_combobox = ttk.Label(self, text=type_)
        else:
            type_combobox = ttk.Combobox(self, values=IngredientTypes.all_types)
        type_combobox.grid(row=current_row, column=1)

        if pct == -1:
            pct_entry = ttk.Label(self, text='')
        else:
            pct_entry = ttk.Entry(self)
            if pct is not None:
                pct_entry.insert(0, pct)
        pct_entry.grid(row=current_row, column=2, padx=10)

        # index = len(self.ingredients)
        # self.init_ids.append((index, current_row)) # Used to find index and row of items if deleted
        # if type_ not in [IngredientTypes.main_flour, IngredientTypes.main_liquid]:
        #     delete_button_command = lambda **kwargs : self.on_delete_ingredient_clicked(
        #         index,
        #         current_row,
        #         **kwargs
        #     )
        #     delete_button = ttk.Button(self, text='Delete', command=delete_button_command)
        #     delete_button.grid(row=current_row, column=3, padx=10)
        # else:
        #     delete_button = None
        # self.init_widgets.append((current_row, name_entry, type_combobox, pct_entry, delete_button))

        self.ingredients.append(IngredientPctModel(name, type_, pct))

    def on_add_ingredient_clicked(self, *args):
        print('Add ingredient clicked!')
        self.add_ingredient()

    # def on_delete_ingredient_clicked(self, init_index, init_row, **kwargs):
    #     index = self.get_current_index(init_index)
    #     row = self.init_ids[index][1]
    #     print(f'Deleting ingredient with index {index} at row {row}')
    #     self.ingredients.remove(self.ingredients[index])
    #     self.init_ids.remove(self.init_ids[index])
    #     self.delete_row(init_row)
    #     self.init_widgets.remove(self.init_widgets[init_row])

    # def get_current_index(self, init_index):
    #     current_index = 0
    #     for ids in self.init_ids:
    #         if ids[0] == init_index:
    #             return current_index
    #         else:
    #             current_index += 1

    # def delete_row(self, init_row):
    #     for widgets in self.init_widgets:
    #         if widgets[0] == init_row:
    #             for widget in widgets[1:]:
    #                 widget.grid_forget()
