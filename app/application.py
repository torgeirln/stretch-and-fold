import tkinter as tk 
from tkinter import ttk

from ui.fragments.create_bakers_pct_recipe_fragment import CreateBakersPctRecipeFragment
from ui.fragments.recipe_fragment import RecipeFragment
from ui.fragments.side_panel_fragment import SidePanelFragment
from ui.fragments.summary_fragment import SummaryFragment
from ui.view_model import ViewModel


class Application(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack(fill='both', expand=True)
        self.root = root
        self.rowconfigure(1, minsize=900, weight=1)
        self.columnconfigure(1, minsize=900, weight=1)
        self.root.title('Stretch and fold')
        self.root.geometry("+400+5")
        self.view_model = ViewModel()
        self.init_styles()
        self.create_content()

    def init_styles(self):
        self.title_bar_style = 'Title_bar.TLabel'
        ttk.Style().configure(self.title_bar_style, font="Helvetica 42 bold")

    def create_content(self):
        self.title_bar = ttk.Label(self, text='All recipes', style=self.title_bar_style)
        self.title_bar.grid(row=0, column=1, sticky='new', padx=20, pady=20)

        self.side_panel = SidePanelFragment(self)
        self.side_panel.grid(row=0, rowspan=2, column=0, sticky="ns")

        self.summary_fragment = SummaryFragment(self, self.view_model)
        self.set_currernt_fragment(self.summary_fragment)
        # self.set_currernt_fragment(CreateBakersPctRecipeFragment(self, self.view_model))

    def show_recipe(self, recipe):
        recipe_fragment = RecipeFragment(self, recipe)
        self.title_bar.configure(text=recipe.title)
        self.replace_currernt_fragment(recipe_fragment)

    def show_recipes_overview(self):
        print('- show_recipes_overview')
        self.title_bar.configure(text='All recipes')
        self.replace_currernt_fragment(self.summary_fragment)

    def show_create_new_recipe(self):
        print('- show_create_new_recipe')
        self.title_bar.configure(text='Create new recipe')
        self.replace_currernt_fragment(CreateBakersPctRecipeFragment(self, self.view_model))

    def set_currernt_fragment(self, fragment):
        self.current_fragment = fragment
        self.current_fragment.grid(row=1, column=1, sticky="nsew", padx=20)

    def replace_currernt_fragment(self, fragment):
        self.current_fragment.grid_forget()
        self.set_currernt_fragment(fragment)

    