import tkinter as tk
from tkinter import ttk

from domain.types.ingredient_types import IngredientTypes


class LeaveningAgentFlags:
    levain_added = 'FLAG_levain_added'
    levain_updated = 'FLAG_levain_updated'
    levain_removed = 'FLAG_levain_removed'
    yeast_added = 'FLAG_yeast_added'
    yeast_updated = 'FLAG_yeast_updated'
    yeast_removed = 'FLAG_yeast_removed'


class IngreidentTypeCombobox(ttk.Frame):
    def __init__(self, parent, ingr_type, leavening_agent_type_changed_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ingr_type = ingr_type
        self.leavening_agent_type_changed_callback = leavening_agent_type_changed_callback
        self.init_constants()
        self.create_content()

    def init_constants(self):
        self.levain_selected = False
        self.yeast_selected = False
        self.combobox_width = 8

    def create_content(self):
        self.combobox = ttk.Combobox(
            self, 
            values=IngredientTypes.combobox_types, 
            width=self.combobox_width)
        if self.ingr_type is not None:
            self.combobox.current(self._get_ingredient_index(self.ingr_type))
            if self.ingr_type == IngredientTypes.levain:
                self.levain_selected = True
            elif self.ingr_type == IngredientTypes.yeast:
                self.yeast_selected = True
        self.combobox.bind("<MouseWheel>", self.empty_scroll_command)
        self.combobox.bind('<<ComboboxSelected>>', 
            lambda *args: self.on_combobox_changed(self.combobox, *args)
        )
        self.combobox.grid(sticky='news')

    def on_combobox_changed(self, combobox, *args):
        print('Combobox changed!')
        new_type = self.combobox.get()
        print(f'- new_type = {new_type}')
        if new_type == IngredientTypes.levain:
            print('- levain added to combobox')
            self.levain_selected = True
            self.yeast_selected = False
            self.leavening_agent_type_changed_callback(LeaveningAgentFlags.levain_added)
        elif new_type == IngredientTypes.yeast:
            print('- yeast added to combobox')
            self.levain_selected = False
            self.yeast_selected = True
            self.leavening_agent_type_changed_callback(LeaveningAgentFlags.yeast_added)
        elif self.levain_selected: # levain is no longer selected
            print('- levain removed from combobox')
            self.levain_selected = False
            self.leavening_agent_type_changed_callback(LeaveningAgentFlags.levain_removed)
        elif self.yeast_selected: # yeast is no longer selected
            print('- yeast removed from combobox')
            self.yeast_selected = False
            self.leavening_agent_type_changed_callback(LeaveningAgentFlags.yeast_removed)

    def get_type(self):
        return self.combobox.get()

    def _get_ingredient_index(self, ingr_type):
        for index, ingr in enumerate(IngredientTypes.combobox_types):
            if ingr == ingr_type:
                return index
        return 0
        
    def empty_scroll_command(self, event):
        """ Returning 'break' will prevent the default bindings from 
            being processed, thereby disabling the scrolling function. """
        return "break"
    