
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import last_page_support

def vp_start_gui_last():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Windows_11_Setup (root)
    last_page_support.init(root, top)
    root.mainloop()

w = None
def create_Windows_11_Setup(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Windows_11_Setup(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Windows_11_Setup (w)
    last_page_support.init(w, top, *args, **kwargs)
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

        top.geometry("623x482+765+208")
        top.minsize(120, 1)
        top.maxsize(2948, 1261)
        top.resizable(1,  1)
        top.title("Windows 11 Setup")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(False, False)

        self.Topic_ONE = tk.Label(top)
        self.Topic_ONE.place(relx=0.032, rely=0.021, height=50, width=554)
        self.Topic_ONE.configure(activebackground="#f9f9f9")
        self.Topic_ONE.configure(activeforeground="black")
        self.Topic_ONE.configure(anchor='w')
        self.Topic_ONE.configure(background="#ffffff")
        self.Topic_ONE.configure(disabledforeground="#a3a3a3")
        self.Topic_ONE.configure(font="-family {Source Sans Pro} -size 24")
        self.Topic_ONE.configure(foreground="#31aed2")
        self.Topic_ONE.configure(highlightbackground="#d9d9d9")
        self.Topic_ONE.configure(highlightcolor="black")
        self.Topic_ONE.configure(text='''Ready to install''')

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

        def exit_program():
            exit()

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
        self.next_btn.configure(text='''Finish''')
        self.next_btn.configure(command=exit_program)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.032, rely=0.124, height=21, width=544)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Source Sans Pro} -size 10")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''You won't be able to use your PC while Windows installs. Save and close your files before you begin''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.032, rely=0.187, height=21, width=164)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#ffffff")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Source Sans Pro} -size 10")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Progress:''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.048, rely=0.373, height=31, width=254)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Source Sans Pro} -size 12 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''✔ Windows 11 Disk Image Ready''')

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.048, rely=0.311, height=31, width=314)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(background="#ffffff")
        self.Label2_1.configure(cursor="fleur")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Source Sans Pro} -size 12 -weight bold")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''✔ Windows 11 Disk Image Hash Checked''')

        self.Label2_2 = tk.Label(top)
        self.Label2_2.place(relx=0.048, rely=0.249, height=21, width=294)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(anchor='w')
        self.Label2_2.configure(background="#ffffff")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font="-family {Source Sans Pro} -size 12 -weight bold")
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''✔ Windows 11 Disk Image Downloaded''')

        self.Label1_2 = tk.Label(top)
        self.Label1_2.place(relx=0.048, rely=0.685, height=21, width=294)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(anchor='w')
        self.Label1_2.configure(background="#ffffff")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font="-family {Source Sans Pro} -size 10")
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''Your computer may restart during the installation.''')

        self.Label1_2_1 = tk.Label(top)
        self.Label1_2_1.place(relx=0.048, rely=0.747, height=31, width=374)
        self.Label1_2_1.configure(activebackground="#f9f9f9")
        self.Label1_2_1.configure(activeforeground="black")
        self.Label1_2_1.configure(anchor='w')
        self.Label1_2_1.configure(background="#ffffff")
        self.Label1_2_1.configure(disabledforeground="#a3a3a3")
        self.Label1_2_1.configure(font="-family {Source Sans Pro} -size 10")
        self.Label1_2_1.configure(foreground="#000000")
        self.Label1_2_1.configure(highlightbackground="#d9d9d9")
        self.Label1_2_1.configure(highlightcolor="black")
        self.Label1_2_1.configure(text='''if something happens and the update won't continue, make sure to''')

        self.Label1_2_1_1 = tk.Label(top)
        self.Label1_2_1_1.place(relx=0.642, rely=0.747, height=31, width=154)
        self.Label1_2_1_1.configure(activebackground="#f9f9f9")
        self.Label1_2_1_1.configure(activeforeground="black")
        self.Label1_2_1_1.configure(anchor='w')
        self.Label1_2_1_1.configure(background="#ffffff")
        self.Label1_2_1_1.configure(cursor="fleur")
        self.Label1_2_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_2_1_1.configure(font="-family {Source Sans Pro} -size 10 -weight bold")
        self.Label1_2_1_1.configure(foreground="#000000")
        self.Label1_2_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_2_1_1.configure(highlightcolor="black")
        self.Label1_2_1_1.configure(text='''START THE UPDATE AGAIN''')

# if __name__ == '__main__':
#     vp_start_gui_last()





