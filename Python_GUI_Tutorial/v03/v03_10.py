#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.3
# In conjunction with Tcl version 8.6
#    Jul 07, 2014 07:23:15 PM
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

import v03_10_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('EDO_Solver')
    root.geometry('800x600+1778+296')
    v03_10_support.set_Tk_var()
    w = EDO_Solver (root)
    v03_10_support.init(root, w)
    root.mainloop()

w = None
def create_EDO_Solver (root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('EDO_Solver')
    w.geometry('800x600+1778+296')
    v03_10_support.set_Tk_var()
    w_win = EDO_Solver (w)
    v03_10_support.init(w, w_win, param)
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
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        master.configure(background=_bgcolor)
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")


        self.menubar = Menu(master,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)

        self.idiomas = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.idiomas,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                foreground="#000000",
                label="Idiomas")
        self.idiomas.add_radiobutton(
                value="EN",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v03_10_support.TODO,
                foreground="#000000",
                label="English")
        self.idiomas.add_radiobutton(
                value="ES",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v03_10_support.TODO,
                foreground="#000000",
                label="Espanol")
        self.idiomas.add_radiobutton(
                value="PT",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v03_10_support.TODO,
                foreground="#000000",
                label="Portugues")
        self.notacao = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.notacao,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                foreground="#000000",
                label="Notacao")
        self.notacao.add_radiobutton(
                value="Newton",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v03_10_support.TODO,
                foreground="#000000",
                label="Newton")
        self.notacao.add_radiobutton(
                value="Leibniz",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v03_10_support.TODO,
                foreground="#000000",
                label="Leibniz")
        self.notacao.add_radiobutton(
                value="Heavside",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v03_10_support.TODO,
                foreground="#000000",
                label="Heavside")
        self.notacao.add_radiobutton(
                value="Linha",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v03_10_support.TODO,
                foreground="#000000",
                label="Linha")
        self.digitosfracionarios = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.digitosfracionarios,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                foreground="#000000",
                label="DigitosFracionarios")
        self.digitosfracionarios.add_radiobutton(
                value="2 Digitos",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v03_10_support.TODO,
                foreground="#000000",
                label="2 Digitos")
        self.digitosfracionarios.add_radiobutton(
                value="3 Digitos",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v03_10_support.TODO,
                foreground="#000000",
                label="3 Digitos")
        self.digitosfracionarios.add_radiobutton(
                value="4 Digitos",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v03_10_support.TODO,
                foreground="#000000",
                label="4 Digitos")


        self.TLabel1 = ttk.Label (master)
        self.TLabel1.place(relx=0.0,rely=0.0,height=90,width=800)
        self.TLabel1.configure(background=_bgcolor)
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(borderwidth="2")
        self.TLabel1.configure(relief=SUNKEN)
        self.TLabel1.configure(takefocus="0")
        self.TLabel1.configure(text='''Image''')
        self.TLabel1.configure(width=800)
        self._img1 = PhotoImage(file="images/Leibniz_order2_notation.gif")
        self.TLabel1.configure(image=self._img1)
        self.TLabel1.configure(compound="top")

        self.TEntry4 = ttk.Entry (master)
        self.TEntry4.place(relx=0.33,rely=-0.05,relheight=0.04,relwidth=0.24)
        self.TEntry4.configure(takefocus="")
        self.TEntry4.configure(cursor="ibeam")

        self.conds_inics_frame = ttk.Labelframe (master)
        self.conds_inics_frame.place(relx=0.0,rely=0.15,relheight=0.06
                ,relwidth=0.43)
        self.conds_inics_frame.configure(relief=SUNKEN)
        self.conds_inics_frame.configure(text='''Condições Iniciais : y'(0) =               y(0) =''')
        self.conds_inics_frame.configure(relief=SUNKEN)
        self.conds_inics_frame.configure(width=340)
        self.conds_inics_frame.configure(takefocus="0")

        self.ylinhainit_entrada = ttk.Entry (self.conds_inics_frame)
        self.ylinhainit_entrada.place(relx=0.56,rely=0.0,relheight=0.74
                ,relwidth=0.12)
        self.ylinhainit_entrada.configure(takefocus="")
        self.ylinhainit_entrada.configure(cursor="ibeam")

        self.yinit_entrada = ttk.Entry (self.conds_inics_frame)
        self.yinit_entrada.place(relx=0.85,rely=0.0,relheight=0.74
                ,relwidth=0.12)
        self.yinit_entrada.configure(takefocus="")
        self.yinit_entrada.configure(cursor="ibeam")

        self.entradaxT_frame = ttk.Labelframe (master)
        self.entradaxT_frame.place(relx=0.43,rely=0.15,relheight=0.06
                ,relwidth=0.57)
        self.entradaxT_frame.configure(text='''Entrada x(t) =''')
        self.entradaxT_frame.configure(width=460)
        self.entradaxT_frame.configure(takefocus="0")

        self.entrada_xT = ttk.Entry (self.entradaxT_frame)
        self.entrada_xT.place(relx=0.22,rely=0.0,relheight=1.03,relwidth=0.78)
        self.entrada_xT.configure(textvariable=v03_10_support.0)
        self.entrada_xT.configure(takefocus="")
        self.entrada_xT.configure(cursor="ibeam")

        self.style.configure('TNotebook.Tab',background=_bgcolor)
        self.style.configure('TNotebook.Tab',foreground=_fgcolor)
        self.style.map('TNotebook.Tab',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.Abas = ttk.Notebook(master)
        self.Abas.place(relx=0.0,rely=0.22,relheight=0.78,relwidth=1.0)
        self.Abas.configure(width=804)
        self.Abas.configure(takefocus="")
        self.Abas_pg0 = ttk.Frame(self.Abas)
        self.Abas.add(self.Abas_pg0, padding=3)
        self.Abas.tab(0, text="Relatorio",underline="-1",)
        self.Abas_pg1 = ttk.Frame(self.Abas)
        self.Abas.add(self.Abas_pg1, padding=3)
        self.Abas.tab(1, text="Graficos",underline="-1",)





if __name__ == '__main__':
    vp_start_gui()


