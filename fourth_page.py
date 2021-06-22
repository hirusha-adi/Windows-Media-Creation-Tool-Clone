
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

import fourth_page_support

import third_page
import fifth_page

def vp_start_gui_fourth():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Windows_11_Setup (root)
    fourth_page_support.init(root, top)
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
    fourth_page_support.init(w, top, *args, **kwargs)
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
        self.Topic_ONE.configure(text='''Select language, architecture, edition''')

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

        def go_to_third_page():
            top.destroy()
            third_page.vp_start_gui_third()
        
        def go_to_fifth_page():
            top.destroy()
            fifth_page.vp_start_gui_fifth()
            
            
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
        self.exit_btn.configure(command=go_to_third_page)

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
        self.next_btn.configure(text='''Download''')
        self.next_btn.configure(command=go_to_fifth_page)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.032, rely=0.124, height=21, width=334)
        self.Label1.configure(anchor='nw')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Source Sans Pro} -size 10")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Please select from one of the available options to continue''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.048, rely=0.207, height=21, width=74)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Source Sans Pro} -size 10")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Language''')
        
        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.048, rely=0.311, height=21, width=74)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(background="#ffffff")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Source Sans Pro} -size 10")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Edition''')

        self.Label2_1_1 = tk.Label(top)
        self.Label2_1_1.place(relx=0.048, rely=0.415, height=21, width=84)
        self.Label2_1_1.configure(activebackground="#f9f9f9")
        self.Label2_1_1.configure(activeforeground="black")
        self.Label2_1_1.configure(anchor='w')
        self.Label2_1_1.configure(background="#ffffff")
        self.Label2_1_1.configure(cursor="fleur")
        self.Label2_1_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1_1.configure(font="-family {Source Sans Pro} -size 10")
        self.Label2_1_1.configure(foreground="#000000")
        self.Label2_1_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1_1.configure(highlightcolor="black")
        self.Label2_1_1.configure(text='''Architecture''')
        
        self.clicked_lang = tk.StringVar()
        self.clicked_lang.set("English (United States)")
        
        self.options_language = [
            "English (United States)",
            "Spanish (Mexico)",
            "Norwegian (Bokmål)",
            "Serbian (Latin)",
            "Russian",
            "Spanish (Spain)",
            "French",
            "Simplified Chinese (China)",
            "Afrikaans",
            "Azərbaycan",
            "euskara",
            "Filipino"
            ]
        
        self.One = tk.OptionMenu(top, self.clicked_lang, *self.options_language)
        self.One.place(relx=0.209, rely=0.207, height=21, width=194)
        self.One.configure(background="#d9d9d9")
        self.One.configure(disabledforeground="#a3a3a3")
        self.One.configure(foreground="#000000")
        # self.One.configure(text='''DropdownMenuOne will go here''')
        
        
        self.clicked_edition = tk.StringVar()
        self.clicked_edition.set("Windows 11 Pro")
        
        self.options_edition = [
            "Windows 11 Home",
            "Windows 11 Pro",
            "Windows 11 Mobile",
            "Windows 11 Enterprise",
            "Windows 11 Enterprise LTSB",
            "Windows 11 Mobile Enterprise",
            "Windows 11 Education",
            "Windows 11 IoT Core"
        ]

        self.Two = tk.OptionMenu(top, self.clicked_edition, *self.options_edition)
        self.Two.place(relx=0.209, rely=0.311, height=21, width=194)
        self.Two.configure(activebackground="#f9f9f9")
        self.Two.configure(activeforeground="black")
        self.Two.configure(background="#d9d9d9")
        self.Two.configure(disabledforeground="#a3a3a3")
        self.Two.configure(foreground="#000000")
        self.Two.configure(highlightbackground="#d9d9d9")
        self.Two.configure(highlightcolor="black")
        # self.Two.configure(text='''DropdownMenuOne will go here''')
        
        
        self.clicked_architecture = tk.StringVar()
        self.clicked_architecture.set("64-bit (x64)")
        
        self.options_architecture = [
        "64-bit (x64)",
        "32-bit (x86)",
        "Windows on ARM"
        ]

        self.Three = tk.OptionMenu(top, self.clicked_architecture, *self.options_architecture)
        self.Three.place(relx=0.209, rely=0.415, height=21, width=194)
        self.Three.configure(activebackground="#f9f9f9")
        self.Three.configure(activeforeground="black")
        self.Three.configure(background="#d9d9d9")
        self.Three.configure(disabledforeground="#a3a3a3")
        self.Three.configure(foreground="#000000")
        self.Three.configure(highlightbackground="#d9d9d9")
        self.Three.configure(highlightcolor="black")
        # self.Three.configure(text='''DropdownMenuOne will go here''')

# if __name__ == '__main__':
#     vp_start_gui_fourth()




