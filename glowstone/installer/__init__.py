import tkinter as tk
from tkinter import ttk

from .fabric import Fabric
from .forge import Forge


class Installer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.notebook = ttk.Notebook(self)

        self.fabric = Fabric(self.notebook)
        self.forge = Forge(self.notebook)

        self.notebook.add(self.fabric, text="Fabric")
        self.notebook.add(self.forge, text="Forge")

        self.notebook.pack()
