import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import Tk, Label
import pyvolume
import math

# ─── GUI Setup ─────────────────────────────
root = Tk()
root.title("Interactive Volume Meter")
root.geometry("300x350")
style = Style(theme="darkly")

# Label showing current volume
volume_label = Label(root, text="Volume: 50%")
volume_label.pack(pady=10)

# Create meter
volume_meter = ttk.Meter(
    master=root,
    metersize=250,
    amountused=50,        # initial value
    subtext="Volume",
    bootstyle="info",
    interactive=True,
    stripethickness=15,
    textfont=("Helvetica", 16),
    textright="%",
)
volume_meter.pack(pady=20)
x = True
def volume():
    global x
    pos = volume_meter['amountused']  # using dictionary-style access
    pyvolume.custom(percent=pos)
    if x:
        root.after(1000,volume)
        x = False
volume()
root.mainloop()
