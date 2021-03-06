﻿
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

import GUI_Layout_1_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('Diff_Eq_Solver')
    root.geometry('800x600+305+102')
    GUI_Layout_1_support.set_Tk_var()
    w = Diff_Eq_Solver (root)
    GUI_Layout_1_support.init(root, w)
    root.mainloop()

w = None
def create_Diff_Eq_Solver (root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('Diff_Eq_Solver')
    w.geometry('800x600+305+102')
    GUI_Layout_1_support.set_Tk_var()
    w_win = Diff_Eq_Solver (w)
    GUI_Layout_1_support.init(w, w_win, param)
    return w_win

def destroy_Diff_Eq_Solver ():
    global w
    w.destroy()
    w = None


class Diff_Eq_Solver:
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
        master.configure(relief="ridge")
        master.configure(background=_bgcolor)
        master.configure(highlightcolor="#000000")


        self.menubar = Menu(master,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)



        self.style.configure('TNotebook.Tab',background=_bgcolor)
        self.style.configure('TNotebook.Tab',foreground=_fgcolor)
        self.style.map('TNotebook.Tab',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.Abas = ttk.Notebook(master)
        self.Abas.place(relx=0.0,rely=0.43,relheight=0.43,relwidth=1.0)
        self.Abas.configure(width=804)
        self.Abas.configure(takefocus="")
        self.Abas_pg0 = ttk.Frame(self.Abas)
        self.Abas.add(self.Abas_pg0, padding=3)
        self.Abas.tab(0, text="Solução Log",underline="-1",)
        self.Abas_pg1 = ttk.Frame(self.Abas)
        self.Abas.add(self.Abas_pg1, padding=3)
        self.Abas.tab(1, text="Gráficos",underline="-1",)

        self.Message1 = Message (self.Abas_pg0)
        self.Message1.place(relx=0.13,rely=0.45,relheight=0.01,relwidth=0.0)
        self.Message1.configure(background=_bgcolor)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Message''')
        self.Message1.configure(width=-13)

        self.graficos_plot = Frame (self.Abas_pg1)
        self.graficos_plot.place(relx=0.0,rely=0.0,relheight=1.02,relwidth=1.01)

        self.graficos_plot.configure(relief=GROOVE)
        self.graficos_plot.configure(borderwidth="2")
        self.graficos_plot.configure(relief=GROOVE)
        self.graficos_plot.configure(background="#bad6d8")
        self.graficos_plot.configure(width=755)

        self.EDO_Display = Frame (master)
        self.EDO_Display.place(relx=0.0,rely=0.0,relheight=0.23,relwidth=1.02)
        self.EDO_Display.configure(relief=GROOVE)
        self.EDO_Display.configure(borderwidth="2")
        self.EDO_Display.configure(relief=GROOVE)
        self.EDO_Display.configure(background="#cfeaff")
        self.EDO_Display.configure(highlightbackground="#b2e0ff")
        self.EDO_Display.configure(width=815)

        self.Grau5 = Entry (self.EDO_Display)
        self.Grau5.place(relx=0.02,rely=0.37,relheight=0.2,relwidth=0.04)
        self.Grau5.configure(background="white")
        self.Grau5.configure(font="TkFixedFont")
        self.Grau5.configure(foreground="#000000")
        self.Grau5.configure(insertbackground="black")
        self.Grau5.configure(width=32)

        self.Grau4 = Entry (self.EDO_Display)
        self.Grau4.place(relx=0.16,rely=0.37,relheight=0.2,relwidth=0.04)
        self.Grau4.configure(background="white")
        self.Grau4.configure(font="TkFixedFont")
        self.Grau4.configure(foreground="#000000")
        self.Grau4.configure(insertbackground="black")
        self.Grau4.configure(width=32)

        self.Grau3 = Entry (self.EDO_Display)
        self.Grau3.place(relx=0.27,rely=0.37,relheight=0.2,relwidth=0.04)
        self.Grau3.configure(background="white")
        self.Grau3.configure(font="TkFixedFont")
        self.Grau3.configure(foreground="#000000")
        self.Grau3.configure(insertbackground="black")
        self.Grau3.configure(width=32)

        self.Grau2 = Entry (self.EDO_Display)
        self.Grau2.place(relx=0.37,rely=0.37,relheight=0.2,relwidth=0.04)
        self.Grau2.configure(background="white")
        self.Grau2.configure(font="TkFixedFont")
        self.Grau2.configure(foreground="#000000")
        self.Grau2.configure(insertbackground="black")
        self.Grau2.configure(width=32)

        self.Entry5 = Entry (self.EDO_Display)
        self.Entry5.place(relx=0.47,rely=0.37,relheight=0.2,relwidth=0.04)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(width=32)

        self.Grau0 = Entry (self.EDO_Display)
        self.Grau0.place(relx=0.56,rely=0.37,relheight=0.2,relwidth=0.04)
        self.Grau0.configure(background="white")
        self.Grau0.configure(font="TkFixedFont")
        self.Grau0.configure(foreground="#000000")
        self.Grau0.configure(insertbackground="black")
        self.Grau0.configure(width=32)

        self.Entry7 = Entry (self.EDO_Display)
        self.Entry7.place(relx=0.7,rely=0.37,relheight=0.2,relwidth=0.04)
        self.Entry7.configure(background="white")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(width=32)

        self.xTEntryBox = Entry (self.EDO_Display)
        self.xTEntryBox.place(relx=0.76,rely=0.37,relheight=0.2,relwidth=0.19)
        self.xTEntryBox.configure(background="white")
        self.xTEntryBox.configure(font="TkFixedFont")
        self.xTEntryBox.configure(foreground="#000000")
        self.xTEntryBox.configure(insertbackground="black")

        self.Language_selection = Frame (master)
        self.Language_selection.place(relx=0.0,rely=0.87,relheight=0.14
                ,relwidth=1.01)
        self.Language_selection.configure(relief=GROOVE)
        self.Language_selection.configure(borderwidth="2")
        self.Language_selection.configure(relief=GROOVE)
        self.Language_selection.configure(background="#cfeaff")
        self.Language_selection.configure(width=805)

        self.Button2 = Button (self.Language_selection)
        self.Button2.place(relx=0.04,rely=0.35,height=28,width=35)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background=_bgcolor)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(text='''Es''')
        self.Button2.configure(width=30)

        self.Button3 = Button (self.Language_selection)
        self.Button3.place(relx=0.1,rely=0.35,height=28,width=36)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background=_bgcolor)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(text='''En''')
        self.Button3.configure(width=30)

        self.Button4 = Button (self.Language_selection)
        self.Button4.place(relx=0.16,rely=0.35,height=28,width=35)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background=_bgcolor)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(text='''Pt''')
        self.Button4.configure(width=30)

        self.Button5 = Button (self.Language_selection)
        self.Button5.place(relx=0.93,rely=0.35,height=28,width=30)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background=_bgcolor)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(text='''?''')
        self.Button5.configure(width=30)

        self.PrecisaoDecimal = Spinbox (master,from_=1.0,to=100.0)
        self.PrecisaoDecimal.place(relx=0.03,rely=0.28,relheight=0.06
                ,relwidth=0.07)
        self.PrecisaoDecimal.configure(activebackground="#f9f9f9")
        self.PrecisaoDecimal.configure(background="white")
        self.PrecisaoDecimal.configure(buttonbackground="#d9d9d9")
        self.PrecisaoDecimal.configure(foreground="black")
        self.PrecisaoDecimal.configure(from_="1.0")
        self.PrecisaoDecimal.configure(highlightbackground="black")
        self.PrecisaoDecimal.configure(highlightcolor="black")
        self.PrecisaoDecimal.configure(insertbackground="black")
        self.PrecisaoDecimal.configure(selectbackground="#c4c4c4")
        self.PrecisaoDecimal.configure(selectforeground="black")
        self.PrecisaoDecimal.configure(textvariable=GUI_Layout_1_support.Precisao_Decimal)
        self.PrecisaoDecimal.configure(to="100.0")
        self.PrecisaoDecimal.configure(width=55)

        self.Precis_Dec_Text_box = Text (master)
        self.Precis_Dec_Text_box.place(relx=0.1,rely=0.28,relheight=0.06
                ,relwidth=0.25)
        self.Precis_Dec_Text_box.configure(background="#c2e7ff")
        self.Precis_Dec_Text_box.configure(font="TkTextFont")
        self.Precis_Dec_Text_box.configure(foreground="black")
        self.Precis_Dec_Text_box.configure(highlightbackground="#d9d9d9")
        self.Precis_Dec_Text_box.configure(highlightcolor="black")
        self.Precis_Dec_Text_box.configure(insertbackground="black")
        self.Precis_Dec_Text_box.configure(selectbackground="#c4c4c4")
        self.Precis_Dec_Text_box.configure(selectforeground="black")
        self.Precis_Dec_Text_box.configure(width=198)

        self.Mudar_Not = Button (master)
        self.Mudar_Not.place(relx=0.43,rely=0.28,height=48,width=120)
        self.Mudar_Not.configure(activebackground="#d9d9d9")
        self.Mudar_Not.configure(activeforeground="#000000")
        self.Mudar_Not.configure(background=_bgcolor)
        self.Mudar_Not.configure(foreground="#000000")
        self.Mudar_Not.configure(highlightbackground="#d9d9d9")
        self.Mudar_Not.configure(highlightcolor="black")
        self.Mudar_Not.configure(text='''Mudar Notação''')
        self.Mudar_Not.configure(width=120)

        self.Notacao_Lista = Listbox (master)
        self.Notacao_Lista.place(relx=0.59,rely=0.23,relheight=0.19
                ,relwidth=0.38)
        self.Notacao_Lista.configure(background="#cfeaff")
        self.Notacao_Lista.configure(font="TkFixedFont")
        self.Notacao_Lista.configure(foreground="#000000")
        self.Notacao_Lista.configure(width=302)





if __name__ == '__main__':
    vp_start_gui()



