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

    def get_mc_versions(self, stable=True) -> list:
        req = requests.get("https://meta.fabricmc.net/v2/versions/game")
        res = []

        # Adds only stable releases if true, else adds everything
        for i in req.json():
            if stable and i["stable"]:
                res.append(i)
            elif not stable:
                res.append(i)

        return res
