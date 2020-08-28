import tkinter as tk 
from tkinter import ttk

from ui.fragments.side_panel_fragment import SidePanelFragment
from ui.fragments.main_fragment import MainFragment
from ui.view_model import ViewModel


class Application():
    def __init__(self, root):
        self.root = root
        self.root.rowconfigure(0, minsize=800, weight=1)
        self.root.columnconfigure(1, minsize=800, weight=1)
        self.root.title('Bread app')
        self.root.geometry("+400+100")
        self.create_content()

    def mainloop(self):
        self.root.mainloop()
        
    def create_content(self):
        view_model = ViewModel()
        self.side_panel = SidePanelFragment(self.root)
        self.side_panel.grid(row=0, column=0, sticky="ns")

        self.main_fragment = MainFragment(self.root, view_model)
        self.main_fragment.grid(row=0, column=1, sticky="nsew")
