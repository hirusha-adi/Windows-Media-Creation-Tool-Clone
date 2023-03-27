
import sys

import tkinter as tk
import tkinter.ttk as ttk
py3 = True

import first_page_support

import second_page

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    first_page_support.set_Tk_var()
    top = Windows_11_Setup (root)
    first_page_support.init(root, top)
    root.mainloop()

w = None
def create_Windows_11_Setup(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Windows_11_Setup(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    first_page_support.set_Tk_var()
    top = Windows_11_Setup (w)
    first_page_support.init(w, top, *args, **kwargs)
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

        top.geometry("623x500+786+222")
        top.minsize(120, 1)
        top.maxsize(2948, 1261)
        top.resizable(1,  1)
        top.title("Windows 11 Setup")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(False, False)

        self.Topic_ONE = tk.Label(top)
        self.Topic_ONE.place(relx=0.032, rely=0.02, height=51, width=484)
        self.Topic_ONE.configure(activebackground="#f9f9f9")
        self.Topic_ONE.configure(activeforeground="black")
        self.Topic_ONE.configure(anchor='w')
        self.Topic_ONE.configure(background="#ffffff")
        self.Topic_ONE.configure(disabledforeground="#a3a3a3")
        self.Topic_ONE.configure(font="-family {Source Sans Pro} -size 24")
        self.Topic_ONE.configure(foreground="#31aed2")
        self.Topic_ONE.configure(highlightbackground="#d9d9d9")
        self.Topic_ONE.configure(highlightcolor="black")
        self.Topic_ONE.configure(text='''What do you want to do?''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        first_page_support.selectedButton.set("2")

        self.UpgradePCnow = tk.Radiobutton(top)
        self.UpgradePCnow.place(relx=0.048, rely=0.14, relheight=0.05
                , relwidth=0.43)
        self.UpgradePCnow.configure(activebackground="#ececec")
        self.UpgradePCnow.configure(activeforeground="#000000")
        self.UpgradePCnow.configure(anchor='w')
        self.UpgradePCnow.configure(background="#ffffff")
        self.UpgradePCnow.configure(disabledforeground="#a3a3a3")
        self.UpgradePCnow.configure(font="-family {Source Sans Pro} -size 16")
        self.UpgradePCnow.configure(foreground="#000000")
        self.UpgradePCnow.configure(highlightbackground="#d9d9d9")
        self.UpgradePCnow.configure(highlightcolor="#c1c1c1")
        self.UpgradePCnow.configure(justify='left')
        self.UpgradePCnow.configure(text='''Upgrade this PC now''')
        self.UpgradePCnow.configure(variable=first_page_support.selectedButton)
        self.UpgradePCnow.configure(value=1)

        self.createISO = tk.Radiobutton(top)
        self.createISO.place(relx=0.048, rely=0.2, relheight=0.05
                , relwidth=0.928)
        self.createISO.configure(activebackground="#ececec")
        self.createISO.configure(activeforeground="#000000")
        self.createISO.configure(anchor='w')
        self.createISO.configure(background="#ffffff")
        self.createISO.configure(disabledforeground="#a3a3a3")
        self.createISO.configure(font="-family {Source Sans Pro} -size 16")
        self.createISO.configure(foreground="#000000")
        self.createISO.configure(highlightbackground="#d9d9d9")
        self.createISO.configure(highlightcolor="#c1c1c1")
        self.createISO.configure(justify='left')
        self.createISO.configure(text='''Create installation media for another PC''')
        self.createISO.configure(variable=first_page_support.selectedButton)
        self.createISO.configure(value=2)

        self.ms_label = tk.Label(top)
        self.ms_label.place(relx=0.048, rely=0.92, height=31, width=74)
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
        self.support_label.place(relx=0.177, rely=0.92, height=31, width=64)
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
        self.legal_label.place(relx=0.289, rely=0.92, height=31, width=44)
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

        def exit_program():
            exit()

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
        self.exit_btn.configure(text='''Exit''')
        self.exit_btn.configure(command=exit_program)

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
        self.next_btn.configure(command=go_to_second_page)

if __name__ == '__main__':
    vp_start_gui()





