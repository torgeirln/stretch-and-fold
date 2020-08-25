import tkinter as tk
from tkinter import ttk

from ui.fragments.side_panel_fragment import SidePanelFragment
from ui.fragments.recipes_fragment import RecipesFragment

class MainActivity(ttk.Frame):
    def __init__(self, parent, view_model):
        super().__init__(parent)
        self.pack(expand=True, fill=tk.BOTH)
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
        self.side_panel = SidePanelFragment(self)
        # self.side_panel.grid(sticky=tk.W+tk.E+tk.N+tk.S)
        self.side_panel.pack(side=tk.LEFT, fill=tk.Y, expand=True)
        # self.side_panel.grid_columnconfigure(0, weight=1)

        self.recipes_fragment = RecipesFragment(self, self.view_model)
        self.set_main_fragment(self.recipes_fragment)
        # self.recipes_fragment.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.RIGHT)

    def on_button_clicked(*args):
        print('Button clicked!')

    def set_main_fragment(self, new_main_fragment):
        self.main_fragment = new_main_fragment
        self.main_fragment.pack(fill=tk.BOTH, expand=True, pady=self.pady, padx=self.padx)
        # self.main_fragment.grid(row=0, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

    def get_main_fragment(self):
        return self.main_fragment
