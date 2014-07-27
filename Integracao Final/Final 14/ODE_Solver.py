from Tkinter import *
import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from ODE_methods  import*
import tempfile
import v5_support





##---------------------File Image Encoder

##import base64
##
##im_filename = 'C:\PyInstaller-2.1\leibniz_im.gif'
##im_variable_name = 'background'
##py_filename = 'embeddedImage.py'
##
##with open(im_filename,'rb') as f:
##    str64 = base64.b64encode(f.read())
##
##with open(py_filename,'w') as f:
##    f.write('%s="%s"'%(im_variable_name,str64))

from PIL import Image,ImageTk
import cStringIO
import base64

from icon_embedded import icone
from leibniz_image_embedded import leibniz
# or copy paste the background variable found in embeddedImage.py
#icon = Image.open(cStringIO.StringIO(base64.b64decode(icone)))
leibniz_im = Image.open(cStringIO.StringIO(base64.b64decode(leibniz)))

ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
    b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
    b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:icon_file.write(ICON)


#------------------------------------------------------------------

def destroy_EDO_Solver():
    global root
    root.quit()
    root.destroy()
    raise SystemExit


#_______________________________________________________________________

def vp_start_gui():

    '''Starting point when module is the main routine.'''



    global val, w, root
    root = Tk()
    root.title('EDLCC')
    root.geometry('1024x768+401+170')
    root.resizable(width = False, height = False)
    #root.wm_iconbitmap(bitmap = icon)
    #root.iconbitmap(default= ICON_PATH )
    #root.iconbitmap(instance = icon)
    #print "Icon",type(icon)
    w = EDO_Solver (root)
    w.set_bind_options()
    root.protocol("WM_DELETE_WINDOW",destroy_EDO_Solver)
    w.set_bind_entries()
    v5_support.init(root, w)

    root.bind("<Motion>",w.a2_handler)
    root.bind("<Motion>",w.a1_handler)
    root.bind("<Motion>",w.a0_handler)
    root.bind("<Motion>",w.inxT_handler)
    root.bind("<Motion>",w.y0_handler)
    root.bind("<Motion>",w.dy0_handler)


    root.bind("<Return>",w.a2_handler)
    root.bind("<Return>",w.a1_handler)
    root.bind("<Return>",w.a0_handler)
    root.bind("<Return>",w.inxT_handler)
    root.bind("<Return>",w.y0_handler)
    root.bind("<Return>",w.dy0_handler)


    root.mainloop()





class EDO_Solver:
    ##Onde user input eh a entrada anterior dos campos de entrada, em ordem,
    # ao,a1,a2,y0,dy0,xT
    global user_input, idi, flag_graf, flag_rep
    flag_rep = False    #flags para nao ficar reconstruindo os objetos td vez q o foco volta para
    flag_graf = False   #o widget(como qndo o usuario minimiza e depois retorna para o programa)
    user_input = [0]*6



    def last_entry_equal(self,last_entry,who):
        global user_input
        print type(who),who
        if who == 'a0':
            user_input[0] = last_entry
        elif who == 'a1':
            user_input[1] = last_entry
            pass
        elif who == 'a2':
            user_input[2] = last_entry
        elif who == 'y0':
            user_input[3] = last_entry
        elif who == 'dy0':
            user_input[4] = last_entry
        elif who == 'xT':
            user_input[5] = last_entry
        #user_input = last_entry
        #print "Em : " + who, "Entrada anterior ",last_entry




    def update_saida(self):

        
        global canvas_latex,canvas_plots,latex_fig,plot_fig
        try:
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

        except:
            pass



    def can_update(self):
        global user_input
        n_changes = 0
        tal = get_tal()

        a0 = self.in_a0.get()
        a1 = self.in_a1.get()
        a2 = self.in_a2.get()
        y0 = self.in_y0.get()
        dy0 = self.in_dy0.get()
        xT= self.in_xT.get()

        if user_input[0] != a0:
            set_a0(a0)
            user_input[0] = a0
            n_changes = n_changes +1

        if user_input[1] != a1:
            set_a1(a1)
            user_input[1] = a1
            n_changes = n_changes +1

        if user_input[2] != a2:
            set_a2(a2)
            user_input[2] = a2
            n_changes = n_changes +1

        if user_input[3] != y0:
            set_y0(y0)
            user_input[3] = y0
            n_changes = n_changes +1

        if user_input[4] != dy0:
            set_dy0(dy0)
            user_input[4] = dy0
            n_changes = n_changes +1

        if user_input[5] != xT:
            set_xT(xT)
            user_input[5] = xT
            n_changes = n_changes +1

        if(n_changes != 0):
            tal=get_tal()
            edo_main()
            self.ScaleMin.configure(from_=0, to=(get_maiorTal()-tal[-1]))
            self.ScaleMin.set(0)
            self.ScaleMax.configure(from_=tal[-1], to=(2*get_maiorTal()))
            self.ScaleMax.set(get_maiorTal())
            self.update_saida()



####Handlers-------------------------------------------
  #user input -># ao,a1,a2,y0,dy0,xT

    def a0_handler(self,event):

        global  user_input
        #print "apertei",self.in_a2.get()
        okay_entry_a0 = self.in_a0.register(self.last_entry_equal)
        self.in_a0.configure(validate = 'all',validatecommand = (okay_entry_a0,'%s','a0'))
        a0 = self.in_a0.get()
        #print "User input",user_input
        #print "In a0 now",a0
        self.can_update()
        # if user_input[0] != a0:
        #     print  "Recalculando"
        #     set_a0(a0)
        #     edo_main()
        #     self.update_saida()
    #user input -># ao,a1,a2,y0,dy0,xT

    def a1_handler(self,event):
        global  user_input
        #print "apertei",self.in_a2.get()
        okay_entry_a1 = self.in_a1.register(self.last_entry_equal)
        self.in_a1.configure(validate = 'all',validatecommand = (okay_entry_a1,'%s','a1'))
        a1 = self.in_a1.get()
        #print "User input",user_input
        #print "In a1 now",a1
        self.can_update()
        # if user_input[1] != a1:
        #     print  "Recalculando"
        #     set_a1(a1)
        #     edo_main()
        #     self.update_saida()

    def a2_handler(self,event):
        global  user_input
        #print "apertei",self.in_a2.get()
        okay_entry_a2 = self.in_a2.register(self.last_entry_equal)
        self.in_a2.configure(validate = 'all',validatecommand = (okay_entry_a2,'%s','a2'))
        a2 = self.in_a2.get()
        #print "User input",user_input
        #print "In a2 now",a2
        self.can_update()
        # if user_input[2] != a2:
        #     print  "Recalculando"
        #     set_a2(a2)
        #     edo_main()
        #     self.update_saida()



    def inxT_handler(self,event):
        #print "apertei",self.in_a2.get()
        okay_entry_xT = self.in_xT.register(self.last_entry_equal)
        self.in_xT.configure(validate = 'all',validatecommand = (okay_entry_xT,'%s','xT'))
        xT = self.in_xT.get()
        #print "User input",user_input
        #print "In xT now",xT
        self.can_update()
        # if user_input[5] != xT:
        #     print  "Recalculando"
        #     set_xT(xT)
        #     edo_main()
        #     self.update_saida()
 #user input -># ao,a1,a2,y0,dy0,xT
    def y0_handler(self,event):
        #print "apertei",self.in_a2.get()
        okay_entry_y0 = self.in_y0.register(self.last_entry_equal)
        self.in_y0.configure(validate = 'all',validatecommand = (okay_entry_y0,'%s','y0'))
        y0 = self.in_y0.get()
        #print "User input",user_input
        #print "In y0 now",y0
        self.can_update()
        # if user_input[3] != y0:
        #     print  "Recalculando"
        #     set_y0(y0)
        #     edo_main()
        #     self.update_saida()

    def dy0_handler(self,event):
      #print "apertei",self.in_a2.get()
        okay_entry_dy0 = self.in_dy0.register(self.last_entry_equal)
        self.in_dy0.configure(validate = 'all',validatecommand = (okay_entry_dy0,'%s','dy0'))
        dy0 = self.in_dy0.get()
        #print "User input",user_input
        #print "In dy0 now",dy0
        self.can_update()
        # if user_input[4] != dy0:
        #     print  "Recalculando"
        #     set_dy0(dy0)
        #     edo_main()
        #     self.update_saida()

    def abaLatex_handler(self,event):
        global canvas_latex,canvas_plots,toolbar,flag_graf, flag_rep

        if(flag_rep==False):
            toolbar.pack_forget()
            toolbar = NavigationToolbar2TkAgg(canvas_latex,self.label_menu_plot)
            toolbar.pack(side = TOP, fill = Y)
            self.label_menu_plot.configure(text="")

            try:
                self.ScaleMin.destroy()
                self.ScaleMax.destroy()

            except:
                pass
            flag_graf = False
            flag_rep = True

    def new_range(self, event):
        global plot_fig, canvas_plots
        tal= get_tal()
        rangeMin = int(self.ScaleMin.get())
        rangeMax = int(self.ScaleMax.get())
        # print "val:", rangeMin
        # print "limx", get_limx_max()

        if(rangeMin != get_limx_min()):
            set_limx_min(rangeMin)
            self.ScaleMax.configure(from_=self.ScaleMin.get()+tal[-1])
            canvas_plots.get_tk_widget().destroy()
            plot_fig.clear()

            plot_fig  = show_plots()

            canvas_plots = FigureCanvasTkAgg(plot_fig,self.frame_plot)
            canvas_plots.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)

        if(rangeMax != get_limx_max()):
            set_limx_max(rangeMax)
            self.ScaleMin.configure(to=self.ScaleMax.get()-tal[-1])
            canvas_plots.get_tk_widget().destroy()
            plot_fig.clear()

            plot_fig  = show_plots()

            canvas_plots = FigureCanvasTkAgg(plot_fig,self.frame_plot)
            canvas_plots.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)

    def slider(self):

        tal = get_tal()

        self.ScaleMin = Scale(self.TNotebook1_pg1)
        self.ScaleMin.place(relx=0.08,rely=0.65,relwidth=0.24,relheight=0.0
                ,height=63,width=45)
        self.ScaleMin.configure(activebackground="#d9d9d9")
        self.ScaleMin.configure(background="white")
        self.ScaleMin.configure(label = " t = [0....5tau] - >lim.Min")
        self.ScaleMin.configure(bd=0)
        #self.Scale1.configure(command=self.new_range)
        self.ScaleMin.configure(highlightthickness="0")
        self.ScaleMin.configure(font="TkTextFont")
        self.ScaleMin.configure(foreground="#000000")
        self.ScaleMin.configure(highlightbackground="#d9d9d9")
        self.ScaleMin.configure(highlightcolor="black")
        self.ScaleMin.configure(orient="horizontal")
        self.ScaleMin.configure(troughcolor="#d9d9d9")
        self.ScaleMin.set(0)
        self.ScaleMin.configure(from_=0, to=(get_maiorTal()-tal[-1]))
        self.ScaleMin.bind("<ButtonRelease-1>", self.new_range)

        self.ScaleMax = Scale(self.TNotebook1_pg1)
        self.ScaleMax.place(relx=0.08,rely=0.80,relwidth=0.24,relheight=0.0
                ,height=63,width=45)
        self.ScaleMax.configure(activebackground="#d9d9d9")
        self.ScaleMax.configure(background="white")
        self.ScaleMax.configure(bd=0)
        #self.Scale1.configure(command=self.new_range)
        self.ScaleMax.configure(highlightthickness="0")
        self.ScaleMax.configure(font="TkTextFont")
        self.ScaleMax.configure(label = " t = [5tau....t]- >lim.Max")
        self.ScaleMax.configure(foreground="#000000")
        self.ScaleMax.configure(highlightbackground="#d9d9d9")
        self.ScaleMax.configure(highlightcolor="black")
        self.ScaleMax.configure(orient="horizontal")
        self.ScaleMax.configure(troughcolor="#d9d9d9")
        self.ScaleMax.set(get_maiorTal())
        self.ScaleMax.configure(from_=tal[-1], to=(2*self.ScaleMax.get()))
        self.ScaleMax.bind("<ButtonRelease-1>", self.new_range)


    def abaPlots_handler(self,event):
        global canvas_latex,canvas_plots,toolbar, flag_graf, flag_rep

        if(flag_graf==False):
            toolbar.pack_forget()
            toolbar = NavigationToolbar2TkAgg(canvas_plots,self.label_menu_plot)
            toolbar.pack(side = TOP, fill = Y)
            #self.label_menu_plot.configure(anchor=NW")
            self.slider()
            flag_rep = False
            flag_graf = True


    def set_bind_options(self):
        self.TNotebook1_pg0.bind("<FocusIn>",self.abaLatex_handler)
        self.TNotebook1_pg1.bind("<FocusIn>",self.abaPlots_handler)


    def set_idiomas(self):
        global idi
        #print "Idioma:",idi.get()
        if (idi.get() == 1): #Port
            self.menubar.entryconfig(2,label="Notacao")
            self.menubar.entryconfig(3,label="DigitosFracionarios")
            self.digitosfracionarios.entryconfig(0,label="2 Digitos")
            self.digitosfracionarios.entryconfig(1,label="3 Digitos")
            self.digitosfracionarios.entryconfig(2,label="4 Digitos")
            self.TNotebook1.tab(0,text="Representacao Algebrica")
            self.TNotebook1.tab(1,text="Graficos")
            self.TNotebook1.tab(2,text="Log Texto")
            self.cond_ini_label.configure(text='''Condicoes  Iniciais     y(0) =                         y'(0) =''')
            self.xT_label.configure(text='''Entrada x(t) =''')
            set_lingua(1)
            self.update_saida()
            #print "port"
        elif(idi.get() == 2): #English
            self.menubar.entryconfig(2,label="Notation")
            self.menubar.entryconfig(3,label="FractionalDigits")
            self.digitosfracionarios.entryconfig(0,label="2 Digits")
            self.digitosfracionarios.entryconfig(1,label="3 Digits")
            self.digitosfracionarios.entryconfig(2,label="4 Digits")
            self.TNotebook1.tab(0,text="Algebraic Representation")
            self.TNotebook1.tab(1,text="Graphics")
            self.TNotebook1.tab(2,text="Text Log")
            self.cond_ini_label.configure(text='''Initial Conditions      y(0) =                         y'(0) =''')
            self.xT_label.configure(text='''Entry x(t) =''')
            set_lingua(2)
            self.update_saida()
            #print "english"
        else: #Espanol
            self.menubar.entryconfig(2,label="Notacion")
            self.menubar.entryconfig(3,label="DigitosFraccionarios")
            self.digitosfracionarios.entryconfig(0,label="2 Digitos")
            self.digitosfracionarios.entryconfig(1,label="3 Digitos")
            self.digitosfracionarios.entryconfig(2,label="4 Digitos")
            self.TNotebook1.tab(0,text="Representacion Algebraica")
            self.TNotebook1.tab(1,text="Graficos")
            self.TNotebook1.tab(2,text="Log Texto")
            self.cond_ini_label.configure(text='''Condiciones Iniciales   y(0) =                         y'(0) =''')
            self.xT_label.configure(text='''Entrada x(t) =''')
            set_lingua(3)
            self.update_saida()
            #print "espanol"

    def set_bind_entries(self):
        pass

        #KeyRelease
        #FocusOut
        #<Leave>
        #Key



        #self.in_a2.bind("<Leave>",self.a2_handler)
        #self.in_a1.bind("<Leave>",self.a1_handler)
        #self.in_a0.bind("<Leave>",self.a0_handler)
        #self.in_xT.bind("<Leave>",self.inxT_handler)
        #self.in_y0.bind("<Leave>",self.y0_handler)
        #self.in_dy0.bind("<Leave>",self.dy0_handler)



    def __init__(self, master):
        global canvas_latex,canvas_plots,latex_fig,plot_fig,toolbar
        global  user_input, idi
        self.mast = master
        idi = IntVar()
        idi.set(1)
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
            self.style.theme_use('clam')#winnative
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
        self.cond_ini_label.configure(text='''Condicoes  Iniciais     y(0) =                         y'(0) =''')

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
        self.xT_label.configure(text='''Entrada x(t) =\t\t\t\t\t     u(t)''')

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
        self._img1 =ImageTk.PhotoImage(leibniz_im)
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
                label="Idioma/Language/Idioma")

        self.idioma.add_radiobutton(
                variable = idi,
                value=1, # 1- Portugues
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.set_idiomas,
                foreground="#000000",
                label="Portugues")
        self.idioma.add_radiobutton(
                variable = idi,
                value=2, # English
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.set_idiomas,
                foreground="#000000",
                label="English")
        self.idioma.add_radiobutton(
                variable = idi,
                value=3, # Espanol
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.set_idiomas,
                foreground="#000000",
                label="Espanol")

        self.notacao = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.notacao,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                foreground="#000000",
                state="disabled",                 
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
                state="disabled",
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
        self.label_menu_plot.place(relx=-0.01,rely=0.94,height=90,width=1052)
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
        self.in_y0.place(relx=0.25,rely=0.12,relheight=0.04,relwidth=0.04)
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
        self.in_dy0.place(relx=0.42,rely=0.12,relheight=0.04,relwidth=0.04)
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
        self.in_xT.insert(END, '1/2*sin(t-2)+exp(t/3) -t**2')
        self.in_y0.insert(END, '1')
        self.in_dy0.insert(END, '1')
        self.in_a0.insert(END, '1')
        self.in_a1.insert(END, '1')
        self.in_a2.insert(END, '1')
        #ao,a1,a2,y0,dy0,xT -> Definindo valores iniciais de user_input
        user_input[0] = '1'
        user_input[1] = '1'
        user_input[2] = '1'
        user_input[3] = '1'
        user_input[4] = '1'
        user_input[5] = '1/2*sin(t-2)+exp(t/3) -t**2'
       # # self.in_a2.register(last_entry_equal,'%s')
       #  okay_entry_a2 = self.in_a2.register(self.last_entry_equal)
       #  okay_entry_a1 = self.in_a2.register(self.last_entry_equal)
       #  okay_entry_a0 = self.in_a2.register(self.last_entry_equal)
       #  okay_entry_xT = self.in_a2.register(self.last_entry_equal)
       #  okay_entry_y0 = self.in_a2.register(self.last_entry_equal)
       #  okay_entry_dy0 = self.in_a2.register(self.last_entry_equal)
       #
       #  self.in_a2.configure(validate = 'key',validatecommand = (okay_entry_a2,'%s'))


        latex_fig = print_latex()
        plot_fig  = show_plots()
        canvas_plots = FigureCanvasTkAgg(plot_fig,self.frame_plot)
        canvas_latex = FigureCanvasTkAgg(latex_fig,self.frame_latex)
        canvas_latex.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)
        #canvas_latex.get_renderer(cleared=True)
        canvas_plots.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)

        toolbar = NavigationToolbar2TkAgg(canvas_latex,self.label_menu_plot)
        toolbar.pack(side = TOP, fill = Y)

        self.saida_log_txt.delete(1.0, END)
        self.saida_log_txt.insert(END,log_print())







if __name__ == '__main__':
    init(1.0,1.0,1.0,'1/2*sin(t-2)+exp(t/3) -t**2',1.0,1.0)
    vp_start_gui()



