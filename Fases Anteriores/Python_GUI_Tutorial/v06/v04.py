#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.3
# In conjunction with Tcl version 8.6
#    Jul 09, 2014 10:53:02 AM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import v04_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('EDO_Solver')
    root.geometry('800x600+133+81')
    v04_support.set_Tk_var()
    w = EDO_Solver (root)
    v04_support.init(root, w)
    root.mainloop()

w = None
def create_EDO_Solver (root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('EDO_Solver')
    w.geometry('800x600+133+81')
    v04_support.set_Tk_var()
    w_win = EDO_Solver (w)
    v04_support.init(w, w_win, param)
    return w_win

def destroy_EDO_Solver ():
    global w
    w.destroy()
    w = None


class EDO_Solver:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        master.configure(background=_bgcolor)
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")


        self.EDO_viewer = Label (master)
        self.EDO_viewer.place(relx=0.0,rely=0.0,height=100,width=800)
        self.EDO_viewer.configure(activebackground="#f9f9f9")
        self.EDO_viewer.configure(activeforeground="black")
        self.EDO_viewer.configure(background=_bgcolor)
        self.EDO_viewer.configure(borderwidth="5")
        self.EDO_viewer.configure(foreground="#000000")
        self.EDO_viewer.configure(highlightbackground="#d9d9d9")
        self.EDO_viewer.configure(highlightcolor="black")
        self.EDO_viewer.configure(relief=RIDGE)
        self.EDO_viewer.configure(text='''Diff Equation Here''')
        self.EDO_viewer.configure(width=800)

        self.Label2 = Label (master)
        self.Label2.place(relx=0.0,rely=0.17,height=52,width=310)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#f7f7f7")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(relief=RIDGE)
        self.Label2.configure(text='''Init.Conditions''')

        self.Label3 = Label (master)
        self.Label3.place(relx=0.39,rely=0.17,height=82,width=490)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(relief=RIDGE)
        self.Label3.configure(text='''Input x(t)''')
        self.Label3.configure(width=490)

        self.Output = Canvas (master)
        self.Output.place(relx=0.0,rely=0.3,relheight=0.7,relwidth=1.0)
        self.Output.configure(background="white")
        self.Output.configure(borderwidth="2")
        self.Output.configure(insertbackground="black")
        self.Output.configure(relief=RIDGE)
        self.Output.configure(selectbackground="#c4c4c4")
        self.Output.configure(selectforeground="black")
        self.Output.configure(width=803)

        self.Relat = Radiobutton (master)
        self.Relat.place(relx=0.05,rely=0.27,relheight=0.04,relwidth=0.12)
        self.Relat.configure(activebackground="#d9d9d9")
        self.Relat.configure(activeforeground="#000000")
        self.Relat.configure(background=_bgcolor)
        self.Relat.configure(borderwidth="3")
        self.Relat.configure(foreground="#000000")
        self.Relat.configure(highlightbackground="#d9d9d9")
        self.Relat.configure(highlightcolor="black")
        self.Relat.configure(offrelief="ridge")
        self.Relat.configure(overrelief="ridge")
        self.Relat.configure(padx="2")
        self.Relat.configure(pady="2")
        self.Relat.configure(relief=RIDGE)
        self.Relat.configure(state=ACTIVE)
        self.Relat.configure(text='''Relatório''')
        self.Relat.configure(variable=v04_support.output_selection)
        self.Relat.configure(width=95)

        self.Radiobutton2 = Radiobutton (master)
        self.Radiobutton2.place(relx=0.16,rely=0.27,relheight=0.04
                ,relwidth=0.12)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background=_bgcolor)
        self.Radiobutton2.configure(borderwidth="3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(offrelief="ridge")
        self.Radiobutton2.configure(padx="2")
        self.Radiobutton2.configure(pady="2")
        self.Radiobutton2.configure(relief=RIDGE)
        self.Radiobutton2.configure(state=ACTIVE)
        self.Radiobutton2.configure(text='''Gráfico''')
        self.Radiobutton2.configure(variable=v04_support.output_selection)
        self.Radiobutton2.configure(width=94)

        self.menubar = Menu(master,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)

        self.idioma = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.idioma,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                foreground="#000000",
                label="Idioma")
        self.idioma.add_radiobutton(
                value="NewRadio",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v04_support.TODO,
                foreground="#000000",
                label="Espanhol")
        self.idioma.add_radiobutton(
                value="NewRadio",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v04_support.TODO,
                foreground="#000000",
                label="Inglês")
        self.idioma.add_radiobutton(
                value="NewRadio",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v04_support.TODO,
                foreground="#000000",
                label="Português")
        self.notacao = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.notacao,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                foreground="#000000",
                label="Notacao")
        self.notacao.add_radiobutton(
                value="NewRadio",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v04_support.TODO,
                foreground="#000000",
                label="Linha")
        self.notacao.add_radiobutton(
                value="NewRadio",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v04_support.TODO,
                foreground="#000000",
                label="Leibniz")
        self.notacao.add_radiobutton(
                value="NewRadio",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v04_support.TODO,
                foreground="#000000",
                label="Newton")
        self.notacao.add_radiobutton(
                value="NewRadio",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v04_support.TODO,
                foreground="#000000",
                label="Heavside")
        self.digitosfracionarios = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.digitosfracionarios,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                foreground="#000000",
                label="DigitosFracionarios")
        self.digitosfracionarios.add_radiobutton(
                value="NewRadio",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v04_support.TODO,
                foreground="#000000",
                label="2 digitos")
        self.digitosfracionarios.add_radiobutton(
                value="NewRadio",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v04_support.TODO,
                foreground="#000000",
                label="3 digitos")
        self.digitosfracionarios.add_radiobutton(
                value="NewRadio",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v04_support.TODO,
                foreground="#000000",
                label="4 digitos")






if __name__ == '__main__':
    vp_start_gui()


