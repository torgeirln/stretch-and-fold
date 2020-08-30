import tkinter as tk
from tkinter import ttk


class SidePanelFragment(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, padding="10 10 10 10", relief='raised', **kwargs)
        self.parent = parent
        self.btn_ipadx = 20
        self.btn_pady = 2
        self.btn_padx = 5
        self.create_content()

    def create_content(self):
        self.button1 = ttk.Button(self, text="Recipes", command=self.on_recipes_button_clicked)
        self.button1.grid(sticky=tk.W+tk.E, padx=self.btn_ipadx, pady=self.btn_pady, ipadx=self.btn_ipadx)

        self.button2 = ttk.Button(self, text="Create new recipe", command=self.on_create_new_recipe_button_clicked)
        self.button2.grid(row=1, sticky=tk.W+tk.E, padx=self.btn_ipadx, pady=self.btn_pady, ipadx=self.btn_ipadx)

    def on_recipes_button_clicked(self, *args):
        print('Recipes button clicked!')
        self.parent.show_recipes_overview()

    def on_create_new_recipe_button_clicked(self, *args):
        print('Create new recipe button clicked!')
