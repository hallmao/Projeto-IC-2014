from Tkinter import *
import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from ODE_methods  import*
import tempfile

import v5_support

def vp_start_gui():

    ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
    b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
    b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

    _, ICON_PATH = tempfile.mkstemp()
    with open(ICON_PATH, 'wb') as icon_file:
     icon_file.write(ICON)
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('EDO_Solver')
    root.geometry('1024x768+401+170')
    root.resizable(width = False, height = False)
    root.wm_iconbitmap(default = ICON_PATH)
    w = EDO_Solver (root)
    w.set_bind_options()
    root.after(250,w.set_bind_entries())
    v5_support.init(root, w)
    w.set_bind_entries()
    root.mainloop()



def destroy_EDO_Solver ():
    global w
    w.destroy()
    w = None

class EDO_Solver:


    def update_saida(self):

        
        global canvas_latex,canvas_plots,latex_fig,plot_fig
        ##Log de texto setando
        self.saida_log_txt.delete(1.0, END)
        self.saida_log_txt.insert(END,log_print())


        canvas_plots.get_tk_widget().destroy()
        canvas_latex.get_tk_widget().destroy()

        latex_fig.clear()
        plot_fig.clear()

        latex_fig = print_latex()
        plot_fig  = show_plots()


        canvas_plots = FigureCanvasTkAgg(plot_fig,self.frame_plot)
        canvas_latex = FigureCanvasTkAgg(latex_fig,self.frame_latex)
        canvas_latex.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)
        canvas_plots.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)











####Handlers

   
      


    def a1_handler(self,event): 
            set_a1(self.in_a1.get())
            edo_main()
            self.update_saida()

    def a2_handler(self,event):
        #print "apertei",self.in_a2.get()
        set_a2(self.in_a2.get())
        edo_main()
        self.update_saida()

    def a0_handler(self,event):

        #print "apertei",self.in_a0.get()
        set_a0(self.in_a0.get())
        edo_main()
        self.update_saida()

    def inxT_handler(self,event):

        #print "apertei",self.in_xT.get()
        set_xT(self.in_xT.get())
        edo_main()
        self.update_saida()

    def y0_handler(self,event):
        set_y0(self.in_y0.get())
        edo_main()
        self.update_saida()

    def dy0_handler(self,event):
         set_dy0(self.in_dy0.get())
         edo_main()
         self.update_saida()

    def abaLatex_handler(self,event):
        global canvas_latex,canvas_plots,toolbar
        toolbar.pack_forget()
        toolbar = NavigationToolbar2TkAgg(canvas_latex,self.label_menu_plot)
        toolbar.pack(side = TOP, fill = Y)

    def abaPlots_handler(self,event):
        global canvas_latex,canvas_plots,toolbar
        toolbar.pack_forget()
        toolbar = NavigationToolbar2TkAgg(canvas_plots,self.label_menu_plot)
        toolbar.pack(side = TOP, fill = Y)
        

    def set_bind_options(self):
        self.TNotebook1_pg0.bind("<FocusIn>",self.abaLatex_handler)
        self.TNotebook1_pg1.bind("<FocusIn>",self.abaPlots_handler)

    def set_bind_entries(self):

        #KeyRelease
        #FocusOut
        #<Leave>
        self.in_a2.bind("<Leave>",self.a2_handler)
        self.in_a1.bind("<Leave>",self.a1_handler)
        self.in_a0.bind("<Leave>",self.a0_handler)
        self.in_xT.bind("<Leave>",self.inxT_handler)
        self.in_y0.bind("<Leave>",self.y0_handler)
        self.in_dy0.bind("<Leave>",self.dy0_handler)
        


        
            



    def __init__(self, master=None):
        global canvas_latex,canvas_plots,latex_fig,plot_fig,toolbar
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font14 = "-family Arial -size 14 -weight normal -slant roman  " + \
            "-underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 12 -weight normal -slant  " + \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        master.configure(background=_bgcolor)
        master.configure(highlightbackground="#adced8")
        master.configure(highlightcolor="black")


        self.cond_ini_label = Label (master)
        self.cond_ini_label.place(relx=0.0,rely=0.095,height=63,width=582)
        self.cond_ini_label.configure(activebackground="#f9f9f9")
        self.cond_ini_label.configure(activeforeground="black")
        self.cond_ini_label.configure(anchor=W)
        self.cond_ini_label.configure(background="white")
        self.cond_ini_label.configure(borderwidth="4")
        self.cond_ini_label.configure(disabledforeground="#a3a3a3")
        self.cond_ini_label.configure(font=font14)
        self.cond_ini_label.configure(foreground="#000000")
        self.cond_ini_label.configure(highlightbackground="#d9d9d9")
        self.cond_ini_label.configure(highlightcolor="#000000")
        self.cond_ini_label.configure(relief=RIDGE)
        self.cond_ini_label.configure(text='''Conds  Iniciais     y(t) =                         y'(t) =''')

        self.xT_label = Label (master)
        self.xT_label.place(relx=0.57,rely=0.095,height=63,width=442)
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

        self.style.configure('TNotebook.Tab',background=_bgcolor)
        self.style.configure('TNotebook.Tab',foreground=_fgcolor)
        self.style.map('TNotebook.Tab',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(master)
        self.TNotebook1.place(relx=0.0,rely=0.18,relheight=0.76,relwidth=1.0)
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

        self.frame_latex = Frame (self.TNotebook1_pg0)
        self.frame_latex.place(relx=-0.06,rely=-0.11,relheight=1.18
                ,relwidth=1.08)
        self.frame_latex.configure(relief=GROOVE)
        self.frame_latex.configure(borderwidth="2")
        self.frame_latex.configure(relief=GROOVE)
        self.frame_latex.configure(background="white")
        self.frame_latex.configure(highlightbackground="#d9d9d9")
        self.frame_latex.configure(highlightcolor="black")
        self.frame_latex.configure(width=1105)

        self.frame_plot = Frame (self.TNotebook1_pg1)
        self.frame_plot.place(relx=0.0,rely=0.0,relheight=1.0,relwidth=1.0)
        self.frame_plot.configure(relief=GROOVE)
        self.frame_plot.configure(borderwidth="2")
        self.frame_plot.configure(relief=GROOVE)
        self.frame_plot.configure(background="white")
        self.frame_plot.configure(highlightbackground="#d9d9d9")
        self.frame_plot.configure(highlightcolor="black")
        self.frame_plot.configure(width=1025)
        


        self.saida_log_txt = Text (self.TNotebook1_pg2)
        self.saida_log_txt.place(relx=0.0,rely=0.0,relheight=0.95,relwidth=1.0)
        self.saida_log_txt.configure(background="white")
        self.saida_log_txt.configure(font="TkTextFont")
        self.saida_log_txt.configure(foreground="black")
        self.saida_log_txt.configure(highlightbackground="#d9d9d9")
        self.saida_log_txt.configure(highlightcolor="black")
        self.saida_log_txt.configure(insertbackground="black")
        self.saida_log_txt.configure(selectbackground="#c4c4c4")
        self.saida_log_txt.configure(selectforeground="black")
        self.saida_log_txt.configure(width=1024)

        self.eq_label = Label (master)
        self.eq_label.place(relx=0.0,rely=0.0,height=70,width=1024)
        self.eq_label.configure(activebackground="#f9f9f9")
        self.eq_label.configure(activeforeground="black")
        self.eq_label.configure(background="white")
        self.eq_label.configure(disabledforeground="#a3a3a3")
        self.eq_label.configure(foreground="#000000")
        self.eq_label.configure(highlightbackground="#d9d9d9")
        self.eq_label.configure(highlightcolor="black")
        self._img1 = PhotoImage(file="C:\PyInstaller-2.1\Leibniz_im.gif")
        self.eq_label.configure(image=self._img1)
        self.eq_label.configure(text='''Label''')
        self.eq_label.configure(width=1002)

        self.in_a5 = Entry (master)
        self.in_a5.place(relx=0.19,rely=0.03,relheight=0.04,relwidth=0.03)
        self.in_a5.configure(background="white")
        self.in_a5.configure(disabledforeground="#a3a3a3")
        self.in_a5.configure(font="TkFixedFont")
        self.in_a5.configure(foreground="#000000")
        self.in_a5.configure(highlightbackground="#d9d9d9")
        self.in_a5.configure(highlightcolor="black")
        self.in_a5.configure(insertbackground="black")
        self.in_a5.configure(selectbackground="#c4c4c4")
        self.in_a5.configure(selectforeground="black")
        self.in_a5.configure(width=34)
        self.in_a5.configure(state='disabled')

        self.in_a4 = Entry (master)
        self.in_a4.place(relx=0.35,rely=0.03,relheight=0.04,relwidth=0.03)
        self.in_a4.configure(background="white")
        self.in_a4.configure(disabledforeground="#a3a3a3")
        self.in_a4.configure(font="TkFixedFont")
        self.in_a4.configure(foreground="#000000")
        self.in_a4.configure(highlightbackground="#d9d9d9")
        self.in_a4.configure(highlightcolor="black")
        self.in_a4.configure(insertbackground="black")
        self.in_a4.configure(selectbackground="#c4c4c4")
        self.in_a4.configure(selectforeground="black")
        self.in_a4.configure(width=34)
        self.in_a4.configure(state='disabled')

        self.in_a3 = Entry (master)
        self.in_a3.place(relx=0.02,rely=0.03,relheight=0.04,relwidth=0.03)
        self.in_a3.configure(background="white")
        self.in_a3.configure(disabledforeground="#a3a3a3")
        self.in_a3.configure(font="TkFixedFont")
        self.in_a3.configure(foreground="#000000")
        self.in_a3.configure(highlightbackground="#d9d9d9")
        self.in_a3.configure(highlightcolor="black")
        self.in_a3.configure(insertbackground="black")
        self.in_a3.configure(selectbackground="#c4c4c4")
        self.in_a3.configure(selectforeground="black")
        self.in_a3.configure(width=34)
        self.in_a3.configure(state='disabled')

        self.in_a2 = Entry (master)
        self.in_a2.place(relx=0.52,rely=0.03,relheight=0.04,relwidth=0.03)
        self.in_a2.configure(background="white")
        self.in_a2.configure(disabledforeground="#a3a3a3")
        self.in_a2.configure(font="TkFixedFont")
        self.in_a2.configure(foreground="#000000")
        self.in_a2.configure(highlightbackground="#d9d9d9")
        self.in_a2.configure(highlightcolor="black")
        self.in_a2.configure(insertbackground="black")
        self.in_a2.configure(selectbackground="#c4c4c4")
        self.in_a2.configure(selectforeground="black")
        self.in_a2.configure(width=34)

        self.in_a1 = Entry (master)
        self.in_a1.place(relx=0.67,rely=0.03,relheight=0.04,relwidth=0.03)
        self.in_a1.configure(background="white")
        self.in_a1.configure(disabledforeground="#a3a3a3")
        self.in_a1.configure(font="TkFixedFont")
        self.in_a1.configure(foreground="#000000")
        self.in_a1.configure(highlightbackground="#d9d9d9")
        self.in_a1.configure(highlightcolor="black")
        self.in_a1.configure(insertbackground="black")
        self.in_a1.configure(selectbackground="#c4c4c4")
        self.in_a1.configure(selectforeground="black")
        self.in_a1.configure(width=34)

        self.in_a0 = Entry (master)
        self.in_a0.place(relx=0.83,rely=0.03,relheight=0.04,relwidth=0.03)
        self.in_a0.configure(background="white")
        self.in_a0.configure(disabledforeground="#a3a3a3")
        self.in_a0.configure(font="TkFixedFont")
        self.in_a0.configure(foreground="#000000")
        self.in_a0.configure(highlightbackground="#d9d9d9")
        self.in_a0.configure(highlightcolor="black")
        self.in_a0.configure(insertbackground="black")
        self.in_a0.configure(selectbackground="#c4c4c4")
        self.in_a0.configure(selectforeground="black")

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
                command=v5_support.TODO,
                foreground="#000000",
                label="Portugues")
        self.idioma.add_radiobutton(
                value="English",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v5_support.TODO,
                foreground="#000000",
                label="English")
        self.idioma.add_radiobutton(
                value="Espanol",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v5_support.TODO,
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
                command=v5_support.TODO,
                foreground="#000000",
                label="Leibniz")
        self.notacao.add_radiobutton(
                value="Lagrange",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v5_support.TODO,
                foreground="#000000",
                label="Lagrange")
        self.notacao.add_radiobutton(
                value="Heaviside",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v5_support.TODO,
                foreground="#000000",
                label="Heaviside")
        self.notacao.add_radiobutton(
                value="Euler",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v5_support.TODO,
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
                command=v5_support.TODO,
                foreground="#000000",
                label="2 Digitos")
        self.digitosfracionarios.add_radiobutton(
                value="3 Digitos",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v5_support.TODO,
                foreground="#000000",
                label="3 Digitos")
        self.digitosfracionarios.add_radiobutton(
                value="4 Digitos",
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=v5_support.TODO,
                foreground="#000000",
                label="4 Digitos")


        self.label_menu_plot = Label (master)
        self.label_menu_plot.place(relx=-0.01,rely=0.94,height=46,width=1052)
        self.label_menu_plot.configure(activebackground="#f9f9f9")
        self.label_menu_plot.configure(activeforeground="black")
        self.label_menu_plot.configure(background="white")
        self.label_menu_plot.configure(borderwidth="4")
        self.label_menu_plot.configure(disabledforeground="#a3a3a3")
        self.label_menu_plot.configure(foreground="#000000")
        self.label_menu_plot.configure(highlightbackground="#d9d9d9")
        self.label_menu_plot.configure(highlightcolor="black")
        self.label_menu_plot.configure(relief=RIDGE)

       

        self.in_y0 = Entry (master)
        self.in_y0.place(relx=0.21,rely=0.12,relheight=0.04,relwidth=0.04)
        self.in_y0.configure(background="white")
        self.in_y0.configure(disabledforeground="#a3a3a3")
        self.in_y0.configure(font="TkFixedFont")
        self.in_y0.configure(foreground="#000000")
        self.in_y0.configure(highlightbackground="#d9d9d9")
        self.in_y0.configure(highlightcolor="black")
        self.in_y0.configure(insertbackground="black")
        self.in_y0.configure(selectbackground="#c4c4c4")
        self.in_y0.configure(selectforeground="black")
        self.in_y0.configure(width=44)

        self.in_dy0 = Entry (master)
        self.in_dy0.place(relx=0.37,rely=0.12,relheight=0.04,relwidth=0.04)
        self.in_dy0.configure(background="white")
        self.in_dy0.configure(disabledforeground="#a3a3a3")
        self.in_dy0.configure(font="TkFixedFont")
        self.in_dy0.configure(foreground="#000000")
        self.in_dy0.configure(highlightbackground="#d9d9d9")
        self.in_dy0.configure(highlightcolor="black")
        self.in_dy0.configure(insertbackground="black")
        self.in_dy0.configure(selectbackground="#c4c4c4")
        self.in_dy0.configure(selectforeground="black")
        self.in_dy0.configure(width=44)

        self.in_xT = ttk.Entry (master)
        self.in_xT.place(relx=0.65,rely=0.11,relheight=0.06,relwidth=0.22)
        self.in_xT.configure(font=font15)
        self.in_xT.configure(width=226)
        self.in_xT.configure(takefocus="")
        self.in_xT.configure(cursor="ibeam")

        #-----------------------------INIT configs-------------------------------------
        self.in_xT.insert(END, '1')
        self.in_y0.insert(END, '1')
        self.in_dy0.insert(END, '1')
        self.in_a0.insert(END, '1')
        self.in_a1.insert(END, '1')
        self.in_a2.insert(END, '1')

        latex_fig = print_latex()
        plot_fig  = show_plots()
        canvas_plots = FigureCanvasTkAgg(plot_fig,self.frame_plot)
        canvas_latex = FigureCanvasTkAgg(latex_fig,self.frame_latex)
        canvas_latex.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)
        canvas_latex.get_renderer(cleared=True)
        canvas_plots.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)

        toolbar = NavigationToolbar2TkAgg(canvas_latex,self.label_menu_plot)
        toolbar.pack(side = TOP, fill = Y)

        self.saida_log_txt.delete(1.0, END)
        self.saida_log_txt.insert(END,log_print())


        #canvas_latex.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)





        #latex_fig.canvas.draw()
        #canvas_latex.draw()
        #canvas_latex.show()




if __name__ == '__main__':
    init(1,1,1,1,1,1)
    vp_start_gui()



