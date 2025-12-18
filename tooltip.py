import tkinter as tk

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip = None
        widget.bind("<Enter>", self.show)
        widget.bind("<Leave>", self.hide)
        widget.bind("<Motion>", self.move)

    def show(self, event=None):
        if self.tip is not None:
            return
        self.tip = tk.Toplevel(self.widget)
        self.tip.wm_overrideredirect(True)
        label = tk.Label(
            self.tip, text=self.text,
            background="#333", foreground="white",
            borderwidth=1, relief="solid",
            padx=4, pady=2
        )
        label.pack()
        self.move(event)

    def move(self, event):
        if self.tip:
            x = event.x_root + 10
            y = event.y_root + 10
            self.tip.wm_geometry(f"+{x}+{y}")

    def hide(self, event=None):
        if self.tip:
            self.tip.destroy()
            self.tip = None
