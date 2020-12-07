import tkinter as tk
from tkinter import ttk

from domain.models.overview_models import Overview
from domain.types.ingredient_types import IngredientTypes
from ui.styles.recipe_styles import header_style, ingredient_style


class OverviewInputItem(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.levain_entry_callback = levain_entry_callback
        self.init_constants()
        self.create_content()

    def init_constants(self):
        self.main_padx = 5
        self.row_spacing = 2
        self.entry_width = 5
        
    def create_content(self):
        # - Title
        ttk.Label(self, text='Overview', style=header_style()).grid(
            row=0, column=0, sticky='nsew', pady=self.row_spacing
        )
        # - Hydration
        ttk.Label(self, text='Hydration: ', style=ingredient_style()).grid(
            row=2, column=0, sticky="nsew", padx=self.main_padx, pady=self.row_spacing
        )
        self.item_hydartion_entry = ttk.Entry(self, width=self.entry_width)
        self.item_hydartion_entry.insert(0, 75)
        self.item_hydartion_entry.grid(row=2, column=1, sticky="w", pady=self.row_spacing)
        # - Salt
        ttk.Label(self, text='Salt: ', style=ingredient_style()).grid(
            row=3, column=0, sticky="nsew", padx=self.main_padx, pady=self.row_spacing
        )
        self.item_salt_entry = ttk.Entry(self, width=self.entry_width)
        self.item_salt_entry.insert(0, 2.3)
        self.item_salt_entry.grid(row=3, column=1, sticky="w", pady=self.row_spacing)
        # - Levain
        # if False: # An extensive upgrade to the UI is needed for the displaing of leavening agents to work properly.
        ttk.Label(self, text='Levain: ', style=ingredient_style()).grid(
            row=4, column=0, sticky='w', padx=self.main_padx, pady=self.row_spacing
        )
        self.item_levain_value_label = ttk.Label(self, text='0', style=ingredient_style())
        self.item_levain_value_label.grid(row=4, column=1, sticky='w')
        # - Yeast
        self.item_yeast_label = ttk.Label(self, text='Yeast: ', style=ingredient_style()).grid(
            row=5, column=0, sticky='w', padx=self.main_padx, pady=self.row_spacing
        )
        self.item_yeast_value_label = ttk.Label(self, text='0', style=ingredient_style())
        self.item_yeast_value_label.grid(row=5, column=1, sticky='w')

    def update_leavening_agent(self, agent_type, new_value):
        if agent_type == IngredientTypes.levain:
            self.item_levain_value_label.configure(text=f'{new_value}')
        elif agent_type == IngredientTypes.yeast:
            self.item_yeast_value_label.configure(text=f'{new_value}')

    def get_overview(self):
        return Overview(
            float(self.item_hydartion_entry.get()),
            float(self.item_salt_entry.get()),
            float(self.item_levain_value_label.cget('text')),
            float(self.item_yeast_value_label.cget('text'))
        )
