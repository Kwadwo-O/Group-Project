# Imports
import ttkbootstrap as ttk
from tkinter import *
from ttkbootstrap import Style

# variables
size = 75

# screen
root = Tk()
root.title("Stream Deck - Python Edition")
root.geometry("620x320")
style = Style(theme="darkly")

#definitions for top row
def top(button):
    print("hi")
    if button == 1:
        print("1")

# frame for top buttons
top_row = ttk.Frame(root)
top_row.pack(pady=10)

# Top button 1
Btn_1_Top_F = ttk.Frame(top_row, width=size, height=size)
Btn_1_Top_F.pack(side="left", padx=10)
Btn_1_Top_F.pack_propagate(False)

Btn_1_Top = ttk.Button(
    Btn_1_Top_F,
    text="Info",
    bootstyle="info",
    command=top(1)
)
Btn_1_Top.pack(fill="both", expand=True, side="left")

# Top button 2
Btn_2_Top_F = ttk.Frame(top_row, width=size, height=size)
Btn_2_Top_F.pack(side="left", padx=10)
Btn_2_Top_F.pack_propagate(False)

Btn_2_Top = ttk.Button(
    Btn_2_Top_F,
    text="Info",
    bootstyle="info"
)
Btn_2_Top.pack(fill="both", expand=True, side="left")

# Top button = 3
Btn_3_Top_F = ttk.Frame(top_row, width=size, height=size)
Btn_3_Top_F.pack(side="left", padx=10)
Btn_3_Top_F.pack_propagate(False)

Btn_3_Top = ttk.Button(
    Btn_3_Top_F,
    text="Info",
    bootstyle="info"
)
Btn_3_Top.pack(fill="both", expand=True, side="left")

# Top button = 4
Btn_4_Top_F = ttk.Frame(top_row, width=size, height=size)
Btn_4_Top_F.pack(side="left", padx=10)
Btn_4_Top_F.pack_propagate(False)

Btn_4_Top = ttk.Button(
    Btn_4_Top_F,
    text="Info",
    bootstyle="info"
)
Btn_4_Top.pack(fill="both", expand=True, side="left")

# Top button = 5
Btn_5_Top_F = ttk.Frame(top_row, width=size, height=size)
Btn_5_Top_F.pack(side="left", padx=10)
Btn_5_Top_F.pack_propagate(False)

Btn_5_Top = ttk.Button(
    Btn_5_Top_F,
    text="Info",
    bootstyle="info"
)
Btn_5_Top.pack(fill="both", expand=True, side="left")


root.mainloop()


# m = ttk.Meter(
#     master=root,
#     metersize=150,
#     amountused=45,
#     subtext="meter widget",
#     bootstyle="info",
#     interactive=False,
# )
# m.pack(pady=10)