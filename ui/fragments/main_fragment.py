import tkinter as tk
from tkinter import ttk

from ui.fragments.recipe_fragment import RecipeFragment
from ui.fragments.summary_fragment import SummaryFragment


class MainFragment(ttk.Frame):
    def __init__(self, parent, view_model, *args, **kwargs):
        super().__init__(parent, *args, padding="10 10 10 10", **kwargs)
        self.view_model = view_model
        self.init_constants()
        self.init_styles()
        self.create_content()
    
    def init_constants(self):
        # Paddings
        self.padx = 20
        self.pady = 2

    def init_styles(self):
        # Description
        ttk.Style().configure('RecipeItem_Description.TLabel', font="Helvetica 14 bold")

    def create_content(self):
        self.summary_fragment = SummaryFragment(self, self.view_model, self.on_show_recipe)
        self.set_currernt_fragment(self.summary_fragment)
        
    def on_show_recipe(self, recipe):
        self.summary_fragment.forget()
        recipe_fragment = RecipeFragment(self, recipe)
        self.set_currernt_fragment(recipe_fragment)

    def on_show_summary(self):
        self.set_currernt_fragment(self.summary_fragment)
        
    def set_currernt_fragment(self, fragment):
        self.current_fragment = fragment
        self.current_fragment.pack(fill="both", expand=True)
    