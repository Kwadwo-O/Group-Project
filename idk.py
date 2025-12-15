import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import Tk, Label
import pyvolume

# ─── GUI Setup ─────────────────────────────
root = Tk()
root.title("Interactive Volume Meter")
root.geometry("300x350")
style = Style(theme="darkly")

# Create meter
volume_meter = ttk.Meter(
    master=root,
    metersize=250,
    amountused=50,        # initial value
    subtext="Volume",
    bootstyle="info",
    interactive=True,
    textfont=("Helvetica", 16),
    textright="%",
)
volume_meter.pack(pady=20)

def volume():
    pos = volume_meter['amountused']  # using dictionary-style access
    pyvolume.custom(percent=pos)
    root.after(1000,volume)

volume()
root.mainloop()
