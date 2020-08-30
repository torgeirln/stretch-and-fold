import tkinter as tk 
from tkinter import ttk

# from ui.fragments.main_fragment import MainFragment
from ui.fragments.recipe_fragment import RecipeFragment
from ui.fragments.side_panel_fragment import SidePanelFragment
from ui.fragments.summary_fragment import SummaryFragment
from ui.view_model import ViewModel


class Application(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack(fill='both', expand=True)
        self.root = root
        self.rowconfigure(0, minsize=1000, weight=1)
        self.columnconfigure(1, minsize=800, weight=1)
        self.root.title('Stretch and fold')
        self.root.geometry("+400+5")
        self.create_content()

    def create_content(self):
        view_model = ViewModel()
        self.side_panel = SidePanelFragment(self)
        self.side_panel.grid(row=0, column=0, sticky="ns")

        self.summary_fragment = SummaryFragment(self, view_model)
        self.set_currernt_fragment(self.summary_fragment)

    def show_recipe(self, recipe):
        recipe_fragment = RecipeFragment(self, recipe)
        self.replace_currernt_fragment(recipe_fragment)

    def show_recipes_overview(self):
        print('- show_recipes_overview')
        self.replace_currernt_fragment(self.summary_fragment)

    def set_currernt_fragment(self, fragment):
        self.current_fragment = fragment
        self.current_fragment.grid(row=0, column=1, sticky="nsew")

    def replace_currernt_fragment(self, fragment):
        self.current_fragment.grid_forget()
        self.set_currernt_fragment(fragment)

    