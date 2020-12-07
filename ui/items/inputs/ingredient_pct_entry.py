import tkinter as tk
from tkinter import ttk

from domain.types.ingredient_types import IngredientTypes
from ui.items.inputs.ingredient_type_combobox import IngreidentTypeCombobox, LeaveningAgentFlags


class IngredientEntryFlags:
    name_changed = 'FLAG_name_changed'
    type_changed = 'FLAG_type_changed'
    pct_changed = 'FLAG_pct_changed'


class IngredientPctEntry(ttk.Frame):
    def __init__(self, parent, ingr_name, ingr_type, ingr_pct, 
            ingredient_entry_changed_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ingr_name = ingr_name
        self.ingr_type = ingr_type
        self.ingr_pct = ingr_pct
        self.ingredient_entry_changed_callback = ingredient_entry_changed_callback
        self.init_constants()
        self.create_content()

    def init_constants(self):
        self.levain_selected = False
        self.yeast_selected = False
        self.pct_entry_width = 5

    def create_content(self):
        self.name_entry_var = tk.StringVar()
        self.name_entry_var.trace('w', 
            lambda *data: self.on_ingredient_entry_changed(IngredientEntryFlags.name_changed, *data))
        self.name_entry = ttk.Entry(self, textvariable=self.name_entry_var)
        self.name_entry.grid(row=0, column=0, sticky='nsew', padx=10, pady=5)

        self.type_combobox = IngreidentTypeCombobox(
            self, 
            self.ingr_type, 
            self.on_leavening_agent_type_changed
        )
        self.type_combobox.grid(row=0, column=1)

        self.pct_entry_var = tk.StringVar()
        self.pct_entry_var.trace('w', 
            lambda *data: self.on_ingredient_entry_changed(IngredientEntryFlags.pct_changed, *data))
        self.pct_entry = ttk.Entry(self, textvariable=self.pct_entry_var, width=self.pct_entry_width)
        self.pct_entry.grid(row=0, column=2, padx=10)

        if self.ingr_name is not None:
            self.name_entry_var.set(self.ingr_name)
        if self.ingr_pct is not None:
            self.pct_entry_var.set(str(self.ingr_pct))

    def on_ingredient_entry_changed(self, flag, *data):
        ingr_name, ingr_type, ingr_pct = self.get_ingredient_values()
        if flag == IngredientEntryFlags.name_changed:
            self.ingredient_entry_changed_callback(flag, ingr_name)
        elif flag == IngredientEntryFlags.type_changed:
            print(f'type_changed data= {data}')
            self.ingredient_entry_changed_callback(flag, *data)
        elif flag == IngredientEntryFlags.pct_changed:
            self.ingredient_entry_changed_callback(flag, ingr_type, ingr_pct)

    def on_leavening_agent_type_changed(self, flag):
        if flag == LeaveningAgentFlags.levain_added or flag == LeaveningAgentFlags.yeast_added:
            _, _, ingr_pct = self.get_ingredient_values()
            self.on_ingredient_entry_changed(
                IngredientEntryFlags.type_changed, 
                flag, 
                ingr_pct
            )
        elif flag == LeaveningAgentFlags.levain_removed or flag == LeaveningAgentFlags.yeast_removed:
            self.on_ingredient_entry_changed(
                IngredientEntryFlags.type_changed, 
                flag
            )

    def get_ingredient_values(self):
        return self.get_name(), self.get_type(), self.get_pct()

    def get_raw_ingredient_values(self):
        return self.name_entry_var.get(), self.type_combobox.get_type(), self.pct_entry_var.get()

    def get_name(self):
        return self.name_entry_var.get()

    def get_type(self):
        return self.type_combobox.get_type()

    def get_pct(self):
        pct_entry_value = self.pct_entry_var.get()
        pct_value = float(pct_entry_value) if len(pct_entry_value) > 0 else 0
        return pct_value
