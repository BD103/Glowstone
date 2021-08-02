import tkinter as tk
from tkinter import ttk

from .installer import Installer


# master is root, Application is mainframe
class Application(tk.Frame):
    def __init__(self, root=None):
        root.title("Glowstone")
        super().__init__(root)
        self.root = root
        self.pack()

        self.installer = Installer(self)
        self.installer.pack()
