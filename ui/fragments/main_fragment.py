import tkinter as tk
from tkinter import ttk

from ui.fragments.summary_fragment import SummaryFragment


class MainFragment(ttk.Frame):
    def __init__(self, parent, view_model):
        super().__init__(parent, padding="10 10 10 10")
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
        self.current_frame = SummaryFragment(self, self.view_model)
        self.current_frame.pack(fill="both", expand=True)
        
        