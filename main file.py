# Imports
from tkinter import messagebox
from tkinter import *
from ttkbootstrap import Style
import webbrowser, os, time, pyvolume, psutil, ttkbootstrap as ttk
from tooltip import Tooltip
from pynput.keyboard import Key, Controller

# screen
root = Tk()
root.title("Stream Deck - Python Edition")
root.geometry("500x500")
style = Style(theme="darkly")
root.iconbitmap("icon.ico")
# variables
size = 75
theme_number = 1

# definitions for the Meters

def cpu():
    CPU_load_wheel.configure(amountused=psutil.cpu_percent())
    RAM_Usage_wheel.configure(amountused=psutil.virtual_memory().percent)
    root.after(1000, cpu)  # update every second


def volume():
    pos = volume_meter['amountused']  # using dictionary-style access
    pyvolume.custom(percent=pos)
    root.after(1000, volume)

# Definition For the settings page

def settings():
    settingsdisp = Toplevel()
    settingsdisp.iconbitmap("cog.ico")
    settingsdisp.title("Settings")
    settingsdisp.geometry("425x220")
    # frame for side-by-side buttons
    top_row = ttk.Frame(settingsdisp)
    top_row.pack(pady=10)
    # frame for side-by-side buttons
    mid_row = ttk.Frame(settingsdisp)
    mid_row.pack(pady=10)
    # frame for side-by-side buttons
    bottom_row = ttk.Frame(settingsdisp)
    bottom_row.pack(pady=10)
    def change_theme():
        global theme_number
        themes = ["cyborg", "journal", "minty", "darkly"]
        Style(theme=themes[theme_number])
        change.config(text=themes[theme_number] if theme_number != 3 else "darkly - default")
        theme_number += 1
        if theme_number == 4:
            theme_number = 0
    # -------- theme change menu button ---------
    change = ttk.Button(
        top_row,
        text="change theme",
        bootstyle="dark",
        command=change_theme,
        width=15
    )
    change.pack(side="left", padx=5)

    # -------- info button ---------
    Info_button = ttk.Button(
        top_row,
        text="Info",
        bootstyle="info",
        # command=info,
        width=15
    )
    Info_button.pack(side="left", padx=5)
    # -------- exit button at bottom ---------
    def exit_page():
        settingsdisp.destroy()
    exit_button = ttk.Button(
        settingsdisp,
        text="Exit",
        bootstyle="danger",
        command=exit_page,
        width=20
    )
    exit_button.pack(side="bottom", pady=10)
    Tooltip(change, "Click to change theme")
    Tooltip(Info_button, "If you dont know how to use the stream deck")
    Tooltip(exit_button, "Click to exit this menu")


#definitions for top row
def button_def(button,row):
    keyboard = Controller()

    if button == 1 and row == 1:
        os.startfile('chrome')
    if button == 2 and row == 1:
        webbrowser.open('https://teams.microsoft.com')
    if button == 3 and row == 1:
        os.startfile("C:\\Program Files\\JetBrains\\PyCharm 2025.1.3\\bin\\pycharm64.exe")
    if button == 4 and row == 1:
        os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
    if button == 5 and row == 1:
        result = messagebox.askyesno(
            title="warning",
            message="Do you want to logoff?",
            icon="warning")
        if result:
            messagebox.showinfo("Success", "Logging off")
            os.startfile("logoff")  # Run your command
    if button == 1 and row == 2:
        webbrowser.open('https://github.com')
    if button == 2 and row == 2:
        webbrowser.open('https://cedar.notredamecoll.ac.uk/ilp')
    if button == 3 and row == 2:
        webbrowser.open('https://chatgpt.com/')
    if button == 4 and row == 2:
        webbrowser.open('https://outlook.office365.com/mail/?realm=ndonline.ac.uk')
    if button == 5 and row == 2:
        webbrowser.open('https://www.google.com/webhp?hl=en&ictx=2&sa=X&ved=0ahUKEwi42I74zb-RAxWvU6QEHbIAJbwQPQgJ')

    if button == 1 and row == 3:
        time.sleep(1)
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release('c')
        keyboard.release(Key.ctrl)

    if button == 2 and row == 3:
        time.sleep(1)
        keyboard.press(Key.ctrl)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl)

    if button == 3 and row == 3:
        time.sleep(1)
        keyboard.press(Key.ctrl)
        keyboard.press('z')
        keyboard.release('z')
        keyboard.release(Key.ctrl)

    if button ==3 and row == 3:
        time.sleep(1)
        keyboard.press(Key.ctrl)
        keyboard.press('y')
        keyboard.release('y')
        keyboard.release(Key.ctrl)

    if button == 5 and row == 3:
        settings()

# frame for top row
top_row = ttk.Frame(root)
top_row.pack(pady=10)
# frame for top row buttons
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
    text="Chrome",
    bootstyle="success",
    command=lambda: button_def(1,1)
)


# Top button 2
Btn_2_Top = ttk.Button(
    Btn_2_Top_F,
    text="Teams",
    bootstyle="success",
    command=lambda: button_def(2,1)
)

# Top button = 3
Btn_3_Top = ttk.Button(
    Btn_3_Top_F,
    text="PyCharm",
    bootstyle="success",
    command=lambda: button_def(3,1)
)

# Top button = 4
Btn_4_Top = ttk.Button(
    Btn_4_Top_F,
    text="Word",
    bootstyle="success",
    command=lambda: button_def(4,1)
)

# Top button = 5
Btn_5_Top = ttk.Button(
    Btn_5_Top_F,
    text="Logoff",
    bootstyle="danger",
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
    text="Github",
    bootstyle="dark",
    command=lambda: button_def(1,2)
)

# Top button 2
Btn_2_Mid = ttk.Button(
    Btn_2_Mid_F,
    text="Cedar",
    bootstyle="dark",
    command=lambda: button_def(2,2)
)

# Top button = 3
Btn_3_Mid = ttk.Button(
    Btn_3_Mid_F,
    text="ChatGPT",
    bootstyle="dark",
    command=lambda: button_def(3,2)
)

# Top button = 4
Btn_4_Mid = ttk.Button(
    Btn_4_Mid_F,
    text="Outlook",
    bootstyle="dark",
    command=lambda: button_def(4,2)
)

# Top button = 5
Btn_5_Mid = ttk.Button(
    Btn_5_Mid_F,
    text="Google",
    bootstyle="dark",
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
    text="Copy",
    bootstyle="info",
    command=lambda: button_def(1,3)
)

# Top button 2
Btn_2_Bot = ttk.Button(
    Btn_2_Bot_F,
    text="Paste",
    bootstyle="info",
    command=lambda: button_def(2,3)
)

# Top button = 3
Btn_3_Bot = ttk.Button(
    Btn_3_Bot_F,
    text="Undo",
    bootstyle="info",
    command=lambda: button_def(3,3)
)

# Top button = 4
Btn_4_Bot = ttk.Button(
    Btn_4_Bot_F,
    text="Redo",
    bootstyle="info",
    command=lambda: button_def(4,3)
)

# Top button = 5
Btn_5_Bot = ttk.Button(
    Btn_5_Bot_F,
    text="Settings",
    bootstyle="warning",
    command=lambda: button_def(5,3)
)


Btn_1_Bot.pack(fill="both", expand=True, side="left")
Btn_2_Bot.pack(fill="both", expand=True, side="left")
Btn_3_Bot.pack(fill="both", expand=True, side="left")
Btn_4_Bot.pack(fill="both", expand=True, side="left")
Btn_5_Bot.pack(fill="both", expand=True, side="left")

# pages_F = ttk.Frame()
# pages_T = ttk.Checkbutton(pages_F, bootstyle="round-toggle")
# Pages_Text = ttk.Label(pages_F,text="1/2")
#
# pages_T.pack()
# pages_F.pack()
# Pages_Text.pack(side="left")

setting = Frame(root)

CPU_load_wheel = ttk.Meter(
    master=setting,
    metersize=150,
    amountused=0,
    subtext="CPU usage",
    bootstyle="info",
    interactive=False,
    textright="% / 100",

)

RAM_Usage_wheel = ttk.Meter(
    master=setting,
    metersize=150,
    amountused=0,
    subtext="CPU usage",
    bootstyle="info",
    interactive=False,
    textright="% / 100",
)

volume_meter = ttk.Meter(
    master=setting,
    metersize=150,
    amountused=50,        # initial value
    subtext="Volume",
    bootstyle="info",
    interactive=True,
    textright="%",
)

setting.pack()
CPU_load_wheel.pack(pady=10,side="left",padx=10)
RAM_Usage_wheel.pack(pady=10,side="left")
volume_meter.pack(padx=10)

Tooltip(volume_meter,"change the volume")
Tooltip(CPU_load_wheel,"Display CPU Load")
Tooltip(RAM_Usage_wheel,"Display RAM load")

Tooltip(Btn_1_Top,"click to open Chrome")
Tooltip(Btn_2_Top,"click to open Teams")
Tooltip(Btn_3_Top,"click to open Pycharm")
Tooltip(Btn_4_Top,"click to open Word")
Tooltip(Btn_5_Top,"click to Logoff")

Tooltip(Btn_1_Mid,"click to open Github")
Tooltip(Btn_2_Mid,"click to open Cedar")
Tooltip(Btn_3_Mid,"click to open Chatgpt")
Tooltip(Btn_4_Mid,"click to open Outlook")
Tooltip(Btn_5_Mid,"click to open Google")

Tooltip(Btn_1_Bot,"Copy Text - click this and select text")
Tooltip(Btn_2_Bot,"Paste Text - click this and select text")
Tooltip(Btn_3_Bot,"Undo - click this and go back to the software")
Tooltip(Btn_4_Bot,"Redo - click this and go back to the software")
Tooltip(Btn_5_Bot,"Settings")


cpu()
volume()

root.mainloop()