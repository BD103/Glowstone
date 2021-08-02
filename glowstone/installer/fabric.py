import json
import tkinter as tk
from tkinter import ttk

import requests


class Fabric(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.install_button = ttk.Button(self, text="Install")

        self.format()

    def format(self):
        self.install_button.grid(column=2, row=3)
