# Imports
import psutil
import pynvml
import ttkbootstrap as ttk
from tkinter import *
from ttkbootstrap import Style

# screen
root = Tk()
root.title("Stream Deck - Python Edition")
root.geometry("500x475")
style = Style(theme="darkly")
# variables
size = 75

#definitions for top row
def button_def(button,row):
    if button == 1:
        print("1")
    if button == 2:
        print("2")
    if button == 3:
        print("3")
    if button == 4:
        print("4")
    if button == 5:
        print("5")

# frame for top row
top_row = ttk.Frame(root)
top_row.pack(pady=10)
# frame for top row buttonas
Btn_1_Top_F = ttk.Frame(top_row, width=size, height=size)
Btn_1_Top_F.pack(side="left", padx=10)
Btn_1_Top_F.pack_propagate(False)

Btn_2_Top_F = ttk.Frame(top_row, width=size, height=size)
Btn_2_Top_F.pack(side="left", padx=10)
Btn_2_Top_F.pack_propagate(False)

Btn_3_Top_F = ttk.Frame(top_row, width=size, height=size)
Btn_3_Top_F.pack(side="left", padx=10)
Btn_3_Top_F.pack_propagate(False)

Btn_4_Top_F = ttk.Frame(top_row, width=size, height=size)
Btn_4_Top_F.pack(side="left", padx=10)
Btn_4_Top_F.pack_propagate(False)

Btn_5_Top_F = ttk.Frame(top_row, width=size, height=size)
Btn_5_Top_F.pack(side="left", padx=10)
Btn_5_Top_F.pack_propagate(False)

# Top button 1
Btn_1_Top = ttk.Button(
    Btn_1_Top_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(1,1)
)

# Top button 2
Btn_2_Top = ttk.Button(
    Btn_2_Top_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(2,1)
)

# Top button = 3
Btn_3_Top = ttk.Button(
    Btn_3_Top_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(3,1)
)

# Top button = 4
Btn_4_Top = ttk.Button(
    Btn_4_Top_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(4,1)
)

# Top button = 5
Btn_5_Top = ttk.Button(
    Btn_5_Top_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(5,1)
)


Btn_1_Top.pack(fill="both", expand=True, side="left")
Btn_2_Top.pack(fill="both", expand=True, side="left")
Btn_3_Top.pack(fill="both", expand=True, side="left")
Btn_4_Top.pack(fill="both", expand=True, side="left")
Btn_5_Top.pack(fill="both", expand=True, side="left")


# frame for middle row
mid_row = ttk.Frame(root)
mid_row.pack(pady=10)
# frame for top row buttonas
Btn_1_Mid_F = ttk.Frame(mid_row, width=size, height=size)
Btn_1_Mid_F.pack(side="left", padx=10)
Btn_1_Mid_F.pack_propagate(False)

Btn_2_Mid_F = ttk.Frame(mid_row, width=size, height=size)
Btn_2_Mid_F.pack(side="left", padx=10)
Btn_2_Mid_F.pack_propagate(False)

Btn_3_Mid_F = ttk.Frame(mid_row, width=size, height=size)
Btn_3_Mid_F.pack(side="left", padx=10)
Btn_3_Mid_F.pack_propagate(False)

Btn_4_Mid_F = ttk.Frame(mid_row, width=size, height=size)
Btn_4_Mid_F.pack(side="left", padx=10)
Btn_4_Mid_F.pack_propagate(False)

Btn_5_Mid_F = ttk.Frame(mid_row, width=size, height=size)
Btn_5_Mid_F.pack(side="left", padx=10)
Btn_5_Mid_F.pack_propagate(False)

# Top button 1
Btn_1_Mid = ttk.Button(
    Btn_1_Mid_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(1,2)
)

# Top button 2
Btn_2_Mid = ttk.Button(
    Btn_2_Mid_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(2,2)
)

# Top button = 3
Btn_3_Mid = ttk.Button(
    Btn_3_Mid_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(3,2)
)

# Top button = 4
Btn_4_Mid = ttk.Button(
    Btn_4_Mid_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(4,2)
)

# Top button = 5
Btn_5_Mid = ttk.Button(
    Btn_5_Mid_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(5,2)
)


Btn_1_Mid.pack(fill="both", expand=True, side="left")
Btn_2_Mid.pack(fill="both", expand=True, side="left")
Btn_3_Mid.pack(fill="both", expand=True, side="left")
Btn_4_Mid.pack(fill="both", expand=True, side="left")
Btn_5_Mid.pack(fill="both", expand=True, side="left")

# frame for bottom row
bot_row = ttk.Frame(root)
bot_row.pack(pady=10)
# frame for top row buttonas
Btn_1_Bot_F = ttk.Frame(bot_row, width=size, height=size)
Btn_1_Bot_F.pack(side="left", padx=10)
Btn_1_Bot_F.pack_propagate(False)

Btn_2_Bot_F = ttk.Frame(bot_row, width=size, height=size)
Btn_2_Bot_F.pack(side="left", padx=10)
Btn_2_Bot_F.pack_propagate(False)

Btn_3_Bot_F = ttk.Frame(bot_row, width=size, height=size)
Btn_3_Bot_F.pack(side="left", padx=10)
Btn_3_Bot_F.pack_propagate(False)

Btn_4_Bot_F = ttk.Frame(bot_row, width=size, height=size)
Btn_4_Bot_F.pack(side="left", padx=10)
Btn_4_Bot_F.pack_propagate(False)

Btn_5_Bot_F = ttk.Frame(bot_row, width=size, height=size)
Btn_5_Bot_F.pack(side="left", padx=10)
Btn_5_Bot_F.pack_propagate(False)

# Top button 1
Btn_1_Bot = ttk.Button(
    Btn_1_Bot_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(1,3)
)

# Top button 2
Btn_2_Bot = ttk.Button(
    Btn_2_Bot_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(2,3)
)

# Top button = 3
Btn_3_Bot = ttk.Button(
    Btn_3_Bot_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(3,3)
)

# Top button = 4
Btn_4_Bot = ttk.Button(
    Btn_4_Bot_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(4,3)
)

# Top button = 5
Btn_5_Bot = ttk.Button(
    Btn_5_Bot_F,
    text="N/A",
    bootstyle="info",
    command=lambda: button_def(5,3)
)


Btn_1_Bot.pack(fill="both", expand=True, side="left")
Btn_2_Bot.pack(fill="both", expand=True, side="left")
Btn_3_Bot.pack(fill="both", expand=True, side="left")
Btn_4_Bot.pack(fill="both", expand=True, side="left")
Btn_5_Bot.pack(fill="both", expand=True, side="left")

setting = Frame(root)

CPU_load = 0
GPU_load = 0

def cpu():
    global CPU_load,GPU_load
    CPU_load = psutil.cpu_percent(interval=None)  # non-blocking
    CPU_load_wheel.configure(amountused=CPU_load)
    # util = pynvml.nvmlDeviceGetUtilizationRates(handle)
    # GPU_load = util.gpu
    GPU_load_wheel.configure(amountused=GPU_load)
    root.after(1000, cpu)  # update every second

CPU_load_wheel = ttk.Meter(
    master=setting,
    metersize=150,
    amountused=CPU_load,
    subtext="CPU usage",
    bootstyle="info",
    interactive=False,
)
CPU_load_wheel.pack(pady=10,side="left")

GPU_load_wheel = ttk.Meter(
    master=setting,
    metersize=150,
    amountused=GPU_load,
    subtext="GPU usage",
    bootstyle="info",
    interactive=False,
)
GPU_load_wheel.pack(pady=10,side="left")

cpu()

setting.pack()
root.mainloop()


