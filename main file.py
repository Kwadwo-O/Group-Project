# Imports
import random
import time, pygame, ttkbootstrap as ttk
from tkinter import *
from tkinter import messagebox
from ttkbootstrap import Style

# screen

root = Tk()
root.title("Stream Deck - Python Edition")
root.geometry("550x620")
style = Style(theme="darkly")


# buttons
row_one = ttk.Frame(
    root,
    padding=10
)

row_two = ttk.Frame(
    root,
    padding=10
)

row_three = ttk.Frame(
    root,
    padding=10
)

row_four = ttk.Frame(
    root,
    padding=10
)

row_one.pack(pady=1)
row_two.pack(pady=1)
row_three.pack(pady=1)
row_four.pack(pady=1)

button = ttk.Button(
    row_one,
    text="idk",
    padding="20",
    width="5"
)

button1 = ttk.Button(
    row_two,
    text="idk",
    padding="20",
    width="5"
)

button2 = ttk.Button(
    row_three,
    text="idk",
    padding="20",
    width="5"
)

button3 = ttk.Button(
    row_four,
    text="idk",
    padding="20",
    width="5"
)

button.pack(side="left")
button1.pack(side="left")
button2.pack(side="left")
button3.pack(side="left")

root.mainloop()