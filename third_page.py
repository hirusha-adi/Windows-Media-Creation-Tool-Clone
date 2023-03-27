
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

import second_page
import fourth_page

def vp_start_gui_third():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    set_Tk_var()
    top = Windows_11_Setup (root)
    init(root, top)
    root.mainloop()

w = None
def create_Windows_11_Setup(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Windows_11_Setup(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    set_Tk_var()
    top = Windows_11_Setup (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Windows_11_Setup():
    global w
    w.destroy()
    w = None

class Windows_11_Setup:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("623x482+778+220")
        top.minsize(120, 1)
        top.maxsize(2948, 1261)
        top.resizable(1,  1)
        top.title("Windows 11 Setup")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(False, False)

        self.Topic_ONE = tk.Label(top)
        self.Topic_ONE.place(relx=0.032, rely=0.021, height=50, width=504)
        self.Topic_ONE.configure(activebackground="#f9f9f9")
        self.Topic_ONE.configure(activeforeground="black")
        self.Topic_ONE.configure(anchor='w')
        self.Topic_ONE.configure(background="#ffffff")
        self.Topic_ONE.configure(disabledforeground="#a3a3a3")
        self.Topic_ONE.configure(font="-family {Source Sans Pro} -size 24")
        self.Topic_ONE.configure(foreground="#31aed2")
        self.Topic_ONE.configure(highlightbackground="#d9d9d9")
        self.Topic_ONE.configure(highlightcolor="black")
        self.Topic_ONE.configure(text='''Choose what to keep''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.ms_label = tk.Label(top)
        self.ms_label.place(relx=0.048, rely=0.919, height=30, width=74)
        self.ms_label.configure(activebackground="#f9f9f9")
        self.ms_label.configure(activeforeground="black")
        self.ms_label.configure(background="#ffffff")
        self.ms_label.configure(disabledforeground="#a3a3a3")
        self.ms_label.configure(font="-family {Source Sans Pro} -size 11 -weight bold")
        self.ms_label.configure(foreground="#6e6e6e")
        self.ms_label.configure(highlightbackground="#d9d9d9")
        self.ms_label.configure(highlightcolor="black")
        self.ms_label.configure(text='''Microsoft''')

        self.support_label = tk.Label(top)
        self.support_label.place(relx=0.177, rely=0.919, height=30, width=64)
        self.support_label.configure(activebackground="#f9f9f9")
        self.support_label.configure(activeforeground="black")
        self.support_label.configure(background="#ffffff")
        self.support_label.configure(disabledforeground="#a3a3a3")
        self.support_label.configure(font="-family {Source Sans Pro} -size 11")
        self.support_label.configure(foreground="#6e6e6e")
        self.support_label.configure(highlightbackground="#d9d9d9")
        self.support_label.configure(highlightcolor="black")
        self.support_label.configure(text='''Support''')

        self.legal_label = tk.Label(top)
        self.legal_label.place(relx=0.289, rely=0.919, height=30, width=44)
        self.legal_label.configure(activebackground="#f9f9f9")
        self.legal_label.configure(activeforeground="black")
        self.legal_label.configure(background="#ffffff")
        self.legal_label.configure(disabledforeground="#a3a3a3")
        self.legal_label.configure(font="-family {Source Sans Pro} -size 11")
        self.legal_label.configure(foreground="#6e6e6e")
        self.legal_label.configure(highlightbackground="#d9d9d9")
        self.legal_label.configure(highlightcolor="black")
        self.legal_label.configure(text='''Legal''')

        def go_to_second_page():
            top.destroy()
            second_page.vp_start_gui_second() 

        self.exit_btn = tk.Button(top)
        self.exit_btn.place(relx=0.69, rely=0.9, height=34, width=77)
        self.exit_btn.configure(activebackground="#ececec")
        self.exit_btn.configure(activeforeground="#000000")
        self.exit_btn.configure(background="#e0e0e0")
        self.exit_btn.configure(borderwidth="0")
        self.exit_btn.configure(disabledforeground="#a3a3a3")
        self.exit_btn.configure(foreground="#000000")
        self.exit_btn.configure(highlightbackground="#d9d9d9")
        self.exit_btn.configure(highlightcolor="black")
        self.exit_btn.configure(pady="0")
        self.exit_btn.configure(text='''Back''')
        self.exit_btn.configure(command=go_to_second_page)

        def go_to_fourth_page():
            top.destroy()
            fourth_page.vp_start_gui_fourth()

        self.next_btn = tk.Button(top)
        self.next_btn.place(relx=0.835, rely=0.9, height=34, width=77)
        self.next_btn.configure(activebackground="#ececec")
        self.next_btn.configure(activeforeground="#000000")
        self.next_btn.configure(background="#e0e0e0")
        self.next_btn.configure(borderwidth="0")
        self.next_btn.configure(disabledforeground="#a3a3a3")
        self.next_btn.configure(foreground="#000000")
        self.next_btn.configure(highlightbackground="#d9d9d9")
        self.next_btn.configure(highlightcolor="black")
        self.next_btn.configure(pady="0")
        self.next_btn.configure(text='''Next''')
        self.next_btn.configure(command=go_to_fourth_page)

        selectedButton.set("3")

        self.Radiobutton1 = tk.Radiobutton(top)
        self.Radiobutton1.place(relx=0.064, rely=0.145, relheight=0.052
                , relwidth=0.43)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(anchor='w')
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#b0b0b0")
        self.Radiobutton1.configure(font="-family {Source Sans Pro} -size 12 -weight bold")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#ffffff")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''Keep personal files and apps''')
        self.Radiobutton1.configure(variable=selectedButton)
        self.Radiobutton1.configure(value=1)

        self.Radiobutton1_1 = tk.Radiobutton(top)
        self.Radiobutton1_1.place(relx=0.064, rely=0.29, relheight=0.052
                , relwidth=0.43)
        self.Radiobutton1_1.configure(activebackground="#ececec")
        self.Radiobutton1_1.configure(activeforeground="#000000")
        self.Radiobutton1_1.configure(anchor='w')
        self.Radiobutton1_1.configure(background="#ffffff")
        self.Radiobutton1_1.configure(disabledforeground="#b0b0b0")
        self.Radiobutton1_1.configure(font="-family {Source Sans Pro} -size 12 -weight bold")
        self.Radiobutton1_1.configure(foreground="#000000")
        self.Radiobutton1_1.configure(highlightbackground="#ffffff")
        self.Radiobutton1_1.configure(highlightcolor="black")
        self.Radiobutton1_1.configure(justify='left')
        self.Radiobutton1_1.configure(text='''Keep personal files only''')
        self.Radiobutton1_1.configure(variable=selectedButton)
        self.Radiobutton1_1.configure(value=2)

        self.Radiobutton1_1_1 = tk.Radiobutton(top)
        self.Radiobutton1_1_1.place(relx=0.064, rely=0.436, relheight=0.052
                , relwidth=0.43)
        self.Radiobutton1_1_1.configure(activebackground="#ececec")
        self.Radiobutton1_1_1.configure(activeforeground="#000000")
        self.Radiobutton1_1_1.configure(anchor='w')
        self.Radiobutton1_1_1.configure(background="#ffffff")
        self.Radiobutton1_1_1.configure(disabledforeground="#b0b0b0")
        self.Radiobutton1_1_1.configure(font="-family {Source Sans Pro} -size 12 -weight bold")
        self.Radiobutton1_1_1.configure(foreground="#000000")
        self.Radiobutton1_1_1.configure(highlightbackground="#ffffff")
        self.Radiobutton1_1_1.configure(highlightcolor="black")
        self.Radiobutton1_1_1.configure(justify='left')
        self.Radiobutton1_1_1.configure(text='''Nothing''')
        self.Radiobutton1_1_1.configure(variable=selectedButton)
        self.Radiobutton1_1_1.configure(value=3)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.08, rely=0.207, height=31, width=304)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='nw')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 10")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(justify='right')
        self.Label1.configure(text='''You will be able to manage your Windows settings.''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.08, rely=0.353, height=31, width=404)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(anchor='nw')
        self.Label1_1.configure(background="#ffffff")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Segoe UI} -size 10")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(justify='right')
        self.Label1_1.configure(text='''Your settings and apps will be deleted, but your files will be kept''')

        self.Label1_1_1 = tk.Label(top)
        self.Label1_1_1.place(relx=0.096, rely=0.498, height=31, width=404)
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(activeforeground="black")
        self.Label1_1_1.configure(anchor='nw')
        self.Label1_1_1.configure(background="#ffffff")
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(font="-family {Segoe UI} -size 10")
        self.Label1_1_1.configure(foreground="#000000")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(justify='right')
        self.Label1_1_1.configure(text='''Everything will be deleted, including files, apps and settings.''')

# if __name__ == '__main__':
#     vp_start_gui_third()





