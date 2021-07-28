import tkinter as tk

from .app import Application

if __name__ == "__main__":
    root = tk.Tk()

    app = Application(root)
    app.mainloop()
