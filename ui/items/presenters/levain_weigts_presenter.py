import tkinter as tk
from tkinter import ttk

from domain.models.levain_models import LevainWeight
from ui.styles.recipe_styles import header_style, ingredient_style, levain_buffert_header_style


class LevainWeightsPresenterItem(ttk.Frame):
    def __init__(self, parent, levain: LevainWeight, add_buffert=False, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.levain = levain
        self.add_buffert = add_buffert
        self.buffert_levain = None
        self.create_content()

    def create_content(self):
        self.levain_header_label = ttk.Label(self, text=f'Levain, {self.levain.total:.0f} g', style=header_style())
        self.levain_header_label.grid(sticky='ew', pady=5)
        
        self.actual_levain = LevainWeightsFrame(self, self.levain)
        self.actual_levain.grid(row=1, column=0, sticky='nsew')

        if self.add_buffert:
            inital_buffert = 10 # Percent
            buffert_padx = 40
            self.buffert_header_frame = ttk.Frame(self)
            self.buffert_header_frame.grid(row=0, column=1, sticky='ew', padx=buffert_padx)
            self.buffert_header_label = ttk.Label(
                self.buffert_header_frame, 
                text=f'Buffert, {self.get_buffert_levain(inital_buffert).total:.0f} g (', 
                style=levain_buffert_header_style())
            self.buffert_header_label.grid(row=0, column=0, pady=5)

            self.buffert_size_var = tk.StringVar()
            self.buffert_size_var.trace("w", self.on_buffert_size_changed)
            self.buffert_size_var.set(str(inital_buffert))
            self.buffert_size_entry = ttk.Entry(
                self.buffert_header_frame, textvariable=self.buffert_size_var, width=3
            )
            self.buffert_size_entry.grid(row=0, column=1, sticky='e')
            ttk.Label(self.buffert_header_frame, text='%)', style=levain_buffert_header_style()).grid(
                row=0, column=2, sticky='w'
            )

            self.buffert_levain = LevainWeightsFrame(self, self.get_buffert_levain())
            self.buffert_levain.grid(row=1, column=1, sticky='new', padx=buffert_padx)

    def on_buffert_size_changed(self, *args):
        if self.add_buffert and self.buffert_levain is not None:
            print('on_buffert_size_changed')
            buffert_levain = self.get_buffert_levain()
            self.buffert_header_label.configure(text=f'Buffert, {buffert_levain.total:.0f} g (')
            self.buffert_levain.update_values(buffert_levain)

    def get_buffert_levain(self, buffert_size=None):
        print('get_buffert_levain')
        if buffert_size is None:
            print(f'- {self.buffert_size_var.get()}')
            buffert_size = 1 + float(self.buffert_size_var.get()) / 100
        else:
            buffert_size = 1 + buffert_size / 100
        buffert_flour = self.levain.flour * buffert_size
        buffert_liquid = self.levain.liquid * buffert_size
        buffert_starter = self.levain.starter * buffert_size
        buffert_total = buffert_flour + buffert_liquid + buffert_starter
        return LevainWeight(
            buffert_total,
            buffert_flour,
            buffert_liquid,
            buffert_starter
        )

class LevainWeightsFrame(ttk.Frame):
    def __init__(self, parent, levain: LevainWeight, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.create_content(levain)

    def create_content(self, levain):
        ttk.Label(self, text='Starter', style=ingredient_style()).grid(
            row=1, column=0, sticky='ew', padx=10, pady=2
        )
        self.levain_starter_label = ttk.Label(self, text=f'{levain.starter:.0f} g', style=ingredient_style())
        self.levain_starter_label.grid(
            row=1, column=1, sticky='ew', padx=10, pady=2
        )

        ttk.Label(self, text='Flour', style=ingredient_style()).grid(
            row=2, column=0, sticky='ew', padx=10, pady=2
        )
        self.levain_flour_label = ttk.Label(self, text=f'{levain.flour:.0f} g', style=ingredient_style())
        self.levain_flour_label.grid(
            row=2, column=1, sticky='ew', padx=10, pady=2
        )

        ttk.Label(self, text='Water', style=ingredient_style()).grid(
            row=3, column=0, sticky='ew', padx=10, pady=2
        )
        self.levain_liquid_label = ttk.Label(self, text=f'{levain.liquid:.0f} g', style=ingredient_style())
        self.levain_liquid_label.grid(
            row=3, column=1, sticky='ew', padx=10, pady=2
        )

    def update_values(self, levain: LevainWeight):
        self.levain_starter_label.configure(text=f'{levain.starter:.0f} g')
        self.levain_flour_label.configure(text=f'{levain.flour:.0f} g')
        self.levain_liquid_label.configure(text=f'{levain.liquid:.0f} g')
    