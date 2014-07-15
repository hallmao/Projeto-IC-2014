﻿#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.3
# In conjunction with Tcl version 8.6
#    Jul 14, 2014 04:24:30 PM
import sys

from final_ode_8_com_plot_v13 import*
from time import sleep

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg


from Tkinter import *
import ttk


import v4_support


   
    

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('EDO_Solver')
    root.geometry('1024x718+395+123')
    w = EDO_Solver (root)
    w.set_bind_entries()
    
    v4_support.init(root, w)
    root.mainloop()
    
    
w = None
def create_EDO_Solver (root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('EDO_Solver')
    w.geometry('1024x718+395+123')
    w_win = EDO_Solver (w)
    v4_support.init(w, w_win, param)
    return w_win

def destroy_EDO_Solver ():
    global w
    w.destroy()
    w = None


class EDO_Solver:

    global canvas_latex

       ##Atualiza parametros na GUI
    def update_saida(self):
        
        global canvas_latex
        ##Log de texto setando
        self.saida_log_txt.delete(1.0, END)
        self.saida_log_txt.insert(END,log_print())
        
        

        
##        ##Plots Setando
##        self.frame_plot.destroy()
##        plot_fig  = show_plots()
##        
##        self.frame_plot = Frame (self.TNotebook1_pg1)
##        self.frame_plot.place(relx=0.0,rely=0.0,relheight=1.07,relwidth=1.0)
##        self.frame_plot.configure(relief=GROOVE)
##        self.frame_plot.configure(borderwidth="2")
##        self.frame_plot.configure(relief=GROOVE)
##        self.frame_plot.configure(background="white")
##        self.frame_plot.configure(highlightbackground="#d9d9d9")
##        self.frame_plot.configure(highlightcolor="black")
##        self.frame_plot.configure(width=1025)
##        canvas_plots = FigureCanvasTkAgg(plot_fig,self.frame_plot)
##        canvas_plots.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)



        ## Forma Algébrica setando
        
        self.frame_latex.destroy()
        latex_fig = print_latex()
        self.frame_latex = Frame (self.TNotebook1_pg0)
        self.frame_latex.place(relx=-0.06,rely=-0.12,relheight=1.24
                ,relwidth=1.08)
        self.frame_latex.configure(relief=GROOVE)
        self.frame_latex.configure(borderwidth="2")
        self.frame_latex.configure(relief=GROOVE)
        self.frame_latex.configure(background="white")
        self.frame_latex.configure(highlightbackground="#d9d9d9")
        self.frame_latex.configure(highlightcolor="black")
        self.frame_latex.configure(width=1105)
        canvas_latex = FigureCanvasTkAgg(latex_fig,self.frame_latex)
        canvas_latex.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)

   
 


        

    ##HAndlers -- Entradas

    def a2_handler(self,event):
        print "apertei",self.in_a2.get()
        set_a2(self.in_a2.get())
        sleep(100e-3)
        edo_main()
        self.update_saida()
 
      
   

    def a1_handler(self,event):
        print "apertei",self.in_a1.get()
        set_a1(self.in_a1.get())
        sleep(0.1)
        edo_main()
        self.update_saida()

    def a0_handler(self,event):
        print "apertei",self.in_a0.get()
        set_a0(self.in_a0.get())
        sleep(0.1)
        edo_main()
        self.update_saida()
            

    def set_bind_entries(self):

        self.in_a2.bind("<KeyRelease>",self.a2_handler)
        self.in_a1.bind("<KeyRelease>",self.a1_handler)
        self.in_a0.bind("<KeyRelease>",self.a0_handler)


    
       


    
    def __init__(self, master=None):
        global canvas_latex
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


        self.cond_ini_label = Label (master)
        self.cond_ini_label.place(relx=0.0,rely=0.1,height=66,width=582)
        self.cond_ini_label.configure(activebackground="#f9f9f9")
        self.cond_ini_label.configure(activeforeground="black")
        self.cond_ini_label.configure(anchor=W)
        self.cond_ini_label.configure(background="white")
        self.cond_ini_label.configure(borderwidth="4")
        self.cond_ini_label.configure(disabledforeground="#a3a3a3")
        self.cond_ini_label.configure(foreground="#000000")
        self.cond_ini_label.configure(highlightbackground="#d9d9d9")
        self.cond_ini_label.configure(highlightcolor="black")
        self.cond_ini_label.configure(relief=RIDGE)
        self.cond_ini_label.configure(text='''Conds iniciais:''')
        self.cond_ini_label.configure(width=582)

        self.xT_label = Label (master)
        self.xT_label.place(relx=0.57,rely=0.1,height=66,width=442)
        self.xT_label.configure(activebackground="#f9f9f9")
        self.xT_label.configure(activeforeground="black")
        self.xT_label.configure(anchor=W)
        self.xT_label.configure(background="white")
        self.xT_label.configure(borderwidth="4")
        self.xT_label.configure(disabledforeground="#a3a3a3")
        self.xT_label.configure(foreground="#000000")
        self.xT_label.configure(highlightbackground="#d9d9d9")
        self.xT_label.configure(highlightcolor="black")
        self.xT_label.configure(relief=RIDGE)
        self.xT_label.configure(text='''Entrada x(t) =''')
        self.xT_label.configure(width=442)

        self.Label4 = Label (master)
        self.Label4.place(relx=0.0,rely=1.0,height=46,width=1032)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="white")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Label''')

        self.style.configure('TNotebook.Tab',background=_bgcolor)
        self.style.configure('TNotebook.Tab',foreground=_fgcolor)
        self.style.map('TNotebook.Tab',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(master)
        self.TNotebook1.place(relx=0.0,rely=0.19,relheight=0.75,relwidth=1.0)
        self.TNotebook1.configure(width=1024)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_pg0 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg0, padding=3)
        self.TNotebook1.tab(0, text="Representacao Algebrica",underline="-1",)
        self.TNotebook1_pg1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg1, padding=3)
        self.TNotebook1.tab(1, text="Graficos",underline="-1",)
        self.TNotebook1_pg2 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg2, padding=3)
        self.TNotebook1.tab(2, text="Log Texto",underline="-1",)


        ##Saida Frame Latex

        self.frame_latex = Frame (self.TNotebook1_pg0)
        self.frame_latex.place(relx=-0.06,rely=-0.12,relheight=1.24
                ,relwidth=1.08)
        self.frame_latex.configure(relief=GROOVE)
        self.frame_latex.configure(borderwidth="2")
        self.frame_latex.configure(relief=GROOVE)
        self.frame_latex.configure(background="white")
        self.frame_latex.configure(highlightbackground="#d9d9d9")
        self.frame_latex.configure(highlightcolor="black")
        self.frame_latex.configure(width=1105)

        ##Inicio do processo de saida
##        canvas_latex = FigureCanvasTkAgg(print_latex(),self.frame_latex)
##        canvas_latex.show()
##        canvas_latex.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)


        self.frame_plot = Frame (self.TNotebook1_pg1)
        self.frame_plot.place(relx=0.0,rely=0.0,relheight=1.07,relwidth=1.0)
        self.frame_plot.configure(relief=GROOVE)
        self.frame_plot.configure(borderwidth="2")
        self.frame_plot.configure(relief=GROOVE)
        self.frame_plot.configure(background="white")
        self.frame_plot.configure(highlightbackground="#d9d9d9")
        self.frame_plot.configure(highlightcolor="black")
        self.frame_plot.configure(width=1025)

         #Inicio do processo de saida
        #canvas_plots = FigureCanvasTkAgg(show_plots(),self.frame_plot)
        #canvas_plots.show()
        #canvas_plots.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)

        self.saida_log_txt = Text (self.TNotebook1_pg2)
        self.saida_log_txt.place(relx=0.0,rely=0.0,relheight=1.09,relwidth=1.0)
        self.saida_log_txt.configure(background="white")
        self.saida_log_txt.configure(font="TkTextFont")
        self.saida_log_txt.configure(foreground="black")
        self.saida_log_txt.configure(highlightbackground="#d9d9d9")
        self.saida_log_txt.configure(highlightcolor="black")
        self.saida_log_txt.configure(insertbackground="black")
        self.saida_log_txt.configure(selectbackground="#c4c4c4")
        self.saida_log_txt.configure(selectforeground="black")
        self.saida_log_txt.configure(width=1024)

        ##LOG de texto na caixa de texto da GUI
        #FRASE REPETITIVA ? DEAL WITH IT
        self.saida_log_txt.insert(END,log_print())



        self.eq_label = Label (master)
        self.eq_label.place(relx=0.0,rely=0.0,height=70,width=1024)
        self.eq_label.configure(activebackground="#f9f9f9")
        self.eq_label.configure(activeforeground="black")
        self.eq_label.configure(background="white")
        self.eq_label.configure(disabledforeground="#a3a3a3")
        self.eq_label.configure(foreground="#000000")
        self.eq_label.configure(highlightbackground="#d9d9d9")
        self.eq_label.configure(highlightcolor="black")
        self._img1 = PhotoImage(file="")
        self.eq_label.configure(image=self._img1)
        self.eq_label.configure(text='''Label''')
        self.eq_label.configure(width=1002)

##        self.in_a5 = Entry (master)
##        self.in_a5.place(relx=0.01,rely=0.03,relheight=0.05,relwidth=0.04)
##        self.in_a5.configure(background="white")
##        self.in_a5.configure(disabledforeground="#a3a3a3")
##        self.in_a5.configure(font="TkFixedFont")
##        self.in_a5.configure(foreground="#000000")
##        self.in_a5.configure(highlightbackground="#d9d9d9")
##        self.in_a5.configure(highlightcolor="black")
##        self.in_a5.configure(insertbackground="black")
##        self.in_a5.configure(selectbackground="#c4c4c4")
##        self.in_a5.configure(text='''0''')
##        self.in_a5.configure(selectforeground="black")
##
##        self.in_a4 = Entry (master)
##        self.in_a4.place(relx=0.18,rely=0.03,relheight=0.05,relwidth=0.04)
##        self.in_a4.configure(background="white")
##        self.in_a4.configure(disabledforeground="#a3a3a3")
##        self.in_a4.configure(font="TkFixedFont")
##        self.in_a4.configure(foreground="#000000")
##        self.in_a4.configure(highlightbackground="#d9d9d9")
##        self.in_a4.configure(highlightcolor="black")
##        self.in_a4.configure(insertbackground="black")
##        self.in_a4.configure(selectbackground="#c4c4c4")
##        self.in_a4.configure(selectforeground="black")
##
##        self.in_a3 = Entry (master)
##        self.in_a3.place(relx=0.34,rely=0.03,relheight=0.05,relwidth=0.04)
##        self.in_a3.configure(background="white")
##        self.in_a3.configure(disabledforeground="#a3a3a3")
##        self.in_a3.configure(font="TkFixedFont")
##        self.in_a3.configure(foreground="#000000")
##        self.in_a3.configure(highlightbackground="#d9d9d9")
##        self.in_a3.configure(highlightcolor="black")
##        self.in_a3.configure(insertbackground="black")
##        self.in_a3.configure(selectbackground="#c4c4c4")
##        self.in_a3.configure(selectforeground="black")

        self.in_a2 = Entry (master)
        self.in_a2.place(relx=0.51,rely=0.03,relheight=0.05,relwidth=0.04)
        self.in_a2.configure(background="white")
        self.in_a2.configure(disabledforeground="#a3a3a3")
        self.in_a2.configure(font="TkFixedFont")
        self.in_a2.configure(foreground="#000000")
        self.in_a2.configure(highlightbackground="#d9d9d9")
        self.in_a2.configure(highlightcolor="black")
        self.in_a2.configure(insertbackground="black")
        self.in_a2.configure(selectbackground="#c4c4c4")
        self.in_a2.configure(selectforeground="black")
        
        

        self.in_a1 = Entry (master)
        self.in_a1.place(relx=0.67,rely=0.03,relheight=0.05,relwidth=0.03)
        self.in_a1.configure(background="white")
        self.in_a1.configure(disabledforeground="#a3a3a3")
        self.in_a1.configure(font="TkFixedFont")
        self.in_a1.configure(foreground="#000000")
        self.in_a1.configure(highlightbackground="#d9d9d9")
        self.in_a1.configure(highlightcolor="black")
        self.in_a1.configure(insertbackground="black")
        self.in_a1.configure(selectbackground="#c4c4c4")
        self.in_a1.configure(selectforeground="black")
        set_a1(self.in_a1.get())

        self.in_a0 = Entry (master)
        self.in_a0.place(relx=0.83,rely=0.03,relheight=0.05,relwidth=0.03)
        self.in_a0.configure(background="white")
        self.in_a0.configure(disabledforeground="#a3a3a3")
        self.in_a0.configure(font="TkFixedFont")
        self.in_a0.configure(foreground="#000000")
        self.in_a0.configure(highlightbackground="#d9d9d9")
        self.in_a0.configure(highlightcolor="black")
        self.in_a0.configure(insertbackground="black")
        self.in_a0.configure(selectbackground="#c4c4c4")
        self.in_a0.configure(selectforeground="black")
        set_a0(self.in_a0.get())

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
                value="Portugues",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v4_support.TODO,
                foreground="#000000",
                label="Portugues")
        self.idioma.add_radiobutton(
                value="English",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v4_support.TODO,
                foreground="#000000",
                label="English")
        self.idioma.add_radiobutton(
                value="Espanol",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v4_support.TODO,
                foreground="#000000",
                label="Espanol")
        self.notacao = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.notacao,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                foreground="#000000",
                label="Notacao")
        self.notacao.add_radiobutton(
                value="Leibniz",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v4_support.TODO,
                foreground="#000000",
                label="Leibniz")
        self.notacao.add_radiobutton(
                value="Lagrange",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v4_support.TODO,
                foreground="#000000",
                label="Lagrange")
        self.notacao.add_radiobutton(
                value="Heaviside",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v4_support.TODO,
                foreground="#000000",
                label="Heaviside")
        self.notacao.add_radiobutton(
                value="Euler",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v4_support.TODO,
                foreground="#000000",
                label="Euler")
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
                command=v4_support.TODO,
                foreground="#000000",
                label="2 Digitos")
        self.digitosfracionarios.add_radiobutton(
                value="3 Digitos",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v4_support.TODO,
                foreground="#000000",
                label="3 Digitos")
        self.digitosfracionarios.add_radiobutton(
                value="4 Digitos",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v4_support.TODO,
                foreground="#000000",
                label="4 Digitos")


        self.label_menu_plot = Label (master)
        self.label_menu_plot.place(relx=-0.01,rely=0.95,height=46,width=1052)
        self.label_menu_plot.configure(background="white")
        self.label_menu_plot.configure(borderwidth="4")
        self.label_menu_plot.configure(disabledforeground="#a3a3a3")
        self.label_menu_plot.configure(foreground="#000000")
        self.label_menu_plot.configure(relief=RIDGE)
        #self.label_menu_plot.configure(text='''Label''')
        self.label_menu_plot.configure(width=1052)

##        ###Config Label Saida Latex, Menu
##        toolbar = NavigationToolbar2TkAgg(canvas_latex,self.label_menu_plot)
##        toolbar.pack(side = TOP, fill = Y)

        self.in_y0 = Entry (master)
        self.in_y0.place(relx=0.15,rely=0.13,relheight=0.05,relwidth=0.06)
        self.in_y0.configure(background="white")
        self.in_y0.configure(disabledforeground="#a3a3a3")
        self.in_y0.configure(font="TkFixedFont")
        self.in_y0.configure(foreground="#000000")
        self.in_y0.configure(insertbackground="black")
        self.in_y0.configure(width=64)

        self.in_dy0 = Entry (master)
        self.in_dy0.place(relx=0.35,rely=0.13,relheight=0.05,relwidth=0.06)
        self.in_dy0.configure(background="white")
        self.in_dy0.configure(disabledforeground="#a3a3a3")
        self.in_dy0.configure(font="TkFixedFont")
        self.in_dy0.configure(foreground="#000000")
        self.in_dy0.configure(insertbackground="black")
        self.in_dy0.configure(width=64)

        self.in_xT = ttk.Entry (master)
        self.in_xT.place(relx=0.69,rely=0.13,relheight=0.05,relwidth=0.18)
        self.in_xT.configure(width=186)
        self.in_xT.configure(takefocus="")
        self.in_xT.configure(cursor="ibeam")
        set_xT(self.in_xT.get())
        





if __name__ == '__main__':
    init(1,-3,-4,t,2,3)
    set_flagInit(True)
    vp_start_gui()
    



