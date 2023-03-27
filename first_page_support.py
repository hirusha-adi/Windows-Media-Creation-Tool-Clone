
import sys

import tkinter as tk
import tkinter.ttk as ttk
py3 = True

def set_Tk_var():
    global selectedButton
    selectedButton = tk.IntVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import first_page
    first_page.vp_start_gui()




