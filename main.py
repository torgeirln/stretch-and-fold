import tkinter as tk

from app.application import Application


if __name__ == "__main__":
	root = tk.Tk()
	app = Application(root)
	app.mainloop()
