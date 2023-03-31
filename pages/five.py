import sys
import time
import tkinter as tk
import tkinter.ttk as ttk

import pages.six as sixth_page
import pages.four as fourth_page


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def vp_start_gui_fifth():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Windows_11_Setup(root)
    init(root, top)
    root.mainloop()


w = None


def create_Windows_11_Setup(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Windows_11_Setup(root, *args, **kwargs)' .'''
    global w, w_win, root
    root = rt
    w = tk.Toplevel(root)
    top = Windows_11_Setup(w)
    init(w, top, *args, **kwargs)
    return (w, top)


class Windows_11_Setup:
    def __init__(self, top: tk.Tk = None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        top.geometry("623x482+758+244")
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
        self.Topic_ONE.configure(text='''Downloading''')

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

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

        def go_to_fourth_page():
            top.destroy()
            fourth_page.vp_start_gui_fourth()

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
        self.exit_btn.configure(command=go_to_fourth_page)

        def go_to_last_page():
            top.destroy()
            sixth_page.vp_start_gui_last()

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
        self.next_btn.configure(command=go_to_last_page)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.032, rely=0.124, height=21, width=334)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='nw')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Source Sans Pro} -size 10")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Please click the start button to start downloading ths ISO file''')

        def stop():
            self.TProgressbar1.stop()

        self.STOP = tk.Button(top)
        self.STOP.place(relx=0.53, rely=0.353, height=34, width=77)
        self.STOP.configure(activebackground="#ececec")
        self.STOP.configure(activeforeground="#000000")
        self.STOP.configure(background="#e0e0e0")
        self.STOP.configure(borderwidth="0")
        self.STOP.configure(disabledforeground="#a3a3a3")
        self.STOP.configure(foreground="#000000")
        self.STOP.configure(highlightbackground="#d9d9d9")
        self.STOP.configure(highlightcolor="black")
        self.STOP.configure(pady="0")
        self.STOP.configure(text='''Stop''')
        self.STOP.configure(command=stop)

        def step():
            for x in range(5):
                self.TProgressbar1['value'] += 20
                root.update_idletasks()
                time.sleep(1)

        self.STOP_1 = tk.Button(top)
        self.STOP_1.place(relx=0.369, rely=0.353, height=34, width=77)
        self.STOP_1.configure(activebackground="#ececec")
        self.STOP_1.configure(activeforeground="#000000")
        self.STOP_1.configure(background="#e0e0e0")
        self.STOP_1.configure(borderwidth="0")
        self.STOP_1.configure(disabledforeground="#a3a3a3")
        self.STOP_1.configure(foreground="#000000")
        self.STOP_1.configure(highlightbackground="#d9d9d9")
        self.STOP_1.configure(highlightcolor="black")
        self.STOP_1.configure(pady="0")
        self.STOP_1.configure(text='''Start''')
        self.STOP_1.configure(command=step)

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.096, rely=0.249, relwidth=0.819, relheight=0.0, height=22)
        self.TProgressbar1.configure(length="510")
        self.TProgressbar1.configure(mode='determinate')
