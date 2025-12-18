import tkinter as tk
import webbrowser
from ttkbootstrap import Style, Window, Button, Entry
from ttkbootstrap.constants import *

def open_custom_link():
    url = url_entry.get()
    if url:
        if not url.startswith(('http://', 'https://')) and not url.endswith('.com'):
            url = 'https://' + url + '.com'
        webbrowser.open(url)

# Create window
root = Window(themename="vapor")
root.title("Custom URL Opener")
root.geometry("400x150")

# URL Entry
tk.Label(root, text="Enter URL:").pack(pady=5)
url_entry = Entry(root, width=40)
url_entry.insert(0, "")
url_entry.pack(pady=5)

# Open button
open_btn = Button(
    root,
    text="Open URL",
    command=open_custom_link,
    bootstyle="warning",
    width=20
)
open_btn.pack(pady=15)

root.mainloop()