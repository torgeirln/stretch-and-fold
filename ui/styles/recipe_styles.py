from tkinter import ttk


def column_title_style(): 
    name = 'Recipe_ColumnTitle.TLabel'
    ttk.Style().configure(name, font="Helvetica 12 bold")
    return name    

def description_style():
    name = 'Recipe_Description.TLabel'
    ttk.Style().configure(name, font="Helvetica 12 italic")
    return name    

def header_style():
    name = 'Recipe_Header.TLabel'
    ttk.Style().configure(name, font="Helvetica 16 bold")
    return name

def ingredient_style(): 
    name = 'Recipe_Ingredient.TLabel'
    ttk.Style().configure(name, font="Helvetica 12")
    return name

def levain_buffert_header_style():
    name = 'Recipe_Levain_Buffert_Header.TLabel'
    ttk.Style().configure(name, font="Helvetica 12 bold italic")
    return name
