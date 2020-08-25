import tkinter as tk 
from tkinter import ttk

from ui.activities.main_activity import MainActivity
from ui.view_model import ViewModel


class Application(ttk.Frame):
	def __init__(self, root):
		super().__init__(root, padding="12 12 12 12")
		self.pack(expand=True, fill=tk.BOTH)
		self.root = root
		self.root.title('Bread app')
		self.root.geometry("+400+100")
		self.create_content()
		# self.bind('<Configure>', self.on_configured)
		
	def create_content(self):
		view_model = ViewModel()
		self.activity = MainActivity(self, view_model)

	def on_configured(self, event=None):
		print(f'Configured application {event}')
	