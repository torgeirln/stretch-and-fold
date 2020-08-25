import tkinter as tk
from tkinter import ttk


class SidePanelFragment(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding="10 10 10 10", relief='raised')
        self.ipadx = 2
        self.pady = 2
        self.pack(expand=True, fill=tk.BOTH)
        self.create_content()
        # self.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.W)

    def create_content(self):
        self.button1 = ttk.Button(self, text="Recipes", command=self.on_button_clicked)
        self.button1.grid(sticky=tk.W+tk.E, pady=self.pady, ipadx=self.ipadx)

        self.button2 = ttk.Button(self, text="Create new Recipe", command=self.on_button_clicked)
        self.button2.grid(row=1, sticky=tk.W+tk.E, pady=self.pady, ipadx=self.ipadx)

    def on_button_clicked(self, *args):
        print('Button clicked!')
