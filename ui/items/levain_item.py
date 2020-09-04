import tkinter as tk
from tkinter import ttk


class LevainItem(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.init_constants()
        self.init_styles()
        self.create_content()
    
    def init_constants(self):
        self.main_padx = 0
        
    def init_styles(self):
        self.header_style = 'LevainItem_Header.TLabel'
        ttk.Style().configure(self.header_style, font="Helvetica 16 bold")
        self.column_title_style = 'LevainItem_ColumnTitle.TLabel'
        ttk.Style().configure(self.column_title_style, font="Helvetica 12 bold")
    
    def create_content(self):
        self.levain_title = ttk.Label(self, text='Levain:', style=self.header_style)
        self.levain_title.grid(row=0, column=0, sticky='ew', pady=5)

        self.hydration_label = ttk.Label(self, text='Hydration:')
        self.hydration_label.grid(row=1, column=0, sticky='ew', padx=5, pady=2)

        self.hydration_entry = ttk.Entry(self)
        self.hydration_entry.insert(0, 175)
        self.hydration_entry.grid(row=1, column=1, sticky='ew', pady=2)

        self.starter_pct_label = ttk.Label(self, text='Ratio of starter:')
        self.starter_pct_label.grid(row=2, column=0, sticky='ew', padx=5, pady=2)

        self.starter_pct_enty = ttk.Entry(self)
        self.starter_pct_enty.insert(0, 25)
        self.starter_pct_enty.grid(row=2, column=1, sticky='ew', pady=2)

        self.starter_hydration_label = ttk.Label(self, text='Hydration of starter:')
        self.starter_hydration_label.grid(row=3, column=0, sticky='ew', padx=5, pady=2)

        self.starter_hydration_entry = ttk.Entry(self)
        self.starter_hydration_entry.insert(0, 175)
        self.starter_hydration_entry.grid(row=3, column=1, sticky='ew', pady=2)
