import tkinter as tk
from tkinter import ttk


class Forge(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.install_button = ttk.Button(self, text="InstallF")

        self.format()

    def format(self):
        self.install_button.grid(column=2, row=3)
