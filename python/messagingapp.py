import random
import json
from tkinter import *
from tkinter import ttk

# Start and setup tkinter
root = Tk()
root.configure(bg="#2b2b2b") 
frm = ttk.Frame(root, padding=10, style="Custom.TFrame")
frm.grid()
frm.configure(style="Custom.TFrame")
frm.pack(fill="both", expand=True)
style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.TFrame", background="#2b2b2b")

# Button Style
style.configure(
    "Custom.TButton",
    background="#454545",
    foreground="white",
    font=("Segoe UI", 11, "bold"),
    padding=10,
    borderwidth=0,
    focusthickness=0,
    focuscolor="none",
    relief="flat"
)

class user():
    def __init__(self, username, password):
        self.username = username
        self.passwords = password
        
    