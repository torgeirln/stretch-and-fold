import tkinter as tk
from tkinter import ttk


class SidePanelFragment(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding="10 10 10 10", relief='raised')
        self.btn_ipadx = 0
        self.btn_pady = 2
        self.create_content()

    def create_content(self):
        self.button1 = ttk.Button(self, text="Recipes", command=self.on_button_clicked)
        self.button1.grid(sticky=tk.W+tk.E, pady=self.btn_pady, ipadx=self.btn_ipadx)

        self.button2 = ttk.Button(self, text="Create new recipe", command=self.on_button_clicked)
        self.button2.grid(row=1, sticky=tk.W+tk.E, pady=self.btn_pady, ipadx=self.btn_ipadx)

    def on_button_clicked(self, *args):
        print('Button clicked!')
