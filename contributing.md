# Contributing

> Page is a work in progress, take info with a grain of salt!

## Getting Started

These commands should help you get setup with the standard workflow:

```shell
$ git clone https://github.com/BD103/Glowstone.git
$ python -m venv venv

# Unix (CHOOSE ONE)
$ source venv/bin/activate

# Windows (CHOOSE ONE)
C:\> env/Scripts/activate.bat

$ python -m pip install -r requirements.txt
$ python -m glowstone
```

This project uses Python's default virtual environment to help slim down installation.
Feel free to use another virtual environment program, though!

## Project Setup

Glowstone is set up in a standard package format.
It has a standard API even though the releases will use PyInstaller.
The following is a list explaining the project structure:

```
glowstone/ (main package and program)
  - __main__.py (script used to run program, uses default settings)
  - app.py (root tkinter program)

  installer/ (root page for installer)
    - __init__.py (contains window for installer)
    - fabric.py (frame tab for fabric installer)
    - forge.py (frame tab for forge installer)

assets/ (all developer assets and helpers go here)

- notes.md (development tracker + more)
- requirements.txt (all dependencies)
- contributing.md (help for new developers + reference for experienced)
```

## Building

This program uses PyInstaller to build.
We are working on getting the application working first before we package the thing.
