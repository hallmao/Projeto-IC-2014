﻿from Tkinter import *
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
from lagrange_image_embedded import lagrange
from newton_image_embedded import newton
from euler_image_embedded import euler
# or copy paste the background variable found in embeddedImage.py
#icon = Image.open(cStringIO.StringIO(base64.b64decode(icone)))
leibniz_im = Image.open(cStringIO.StringIO(base64.b64decode(leibniz)))
lagrange_im = Image.open(cStringIO.StringIO(base64.b64decode(lagrange)))
newton_im = Image.open(cStringIO.StringIO(base64.b64decode(newton)))
euler_im = Image.open(cStringIO.StringIO(base64.b64decode(euler)))


ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
    b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
    b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:icon_file.write(ICON)


#------------------------------------------------------------------

def destroy_EDO_Solver():
    global root, config, prec, notation, idi, checkButton_state

    try:
        config = open("config.txt","w")
        config.write(str(idi.get())+str(notation.get())+str(prec.get())+str(checkButton_state.get()))
        config.close()
    except:
        print "no file"


    root.quit()
    root.destroy()
    raise SystemExit


#_______________________________________________________________________

def vp_start_gui():

    '''Starting point when module is the main routine.'''



    global val, w, root
    root = Tk()
    root.title('EDOLCC')
    root.geometry('1024x768+401+170')
    root.resizable(width = False, height = False)
    #root.wm_iconbitmap(bitmap = icon)

#    root.iconbitmap(default= ICON_PATH )
    #root.iconbitmap(instance = icon)
    #print "Icon",type(icon)
    w = EDO_Solver (root)
    w.set_bind_options()
    root.protocol("WM_DELETE_WINDOW",destroy_EDO_Solver)
    #w.set_bind_entries()
    v5_support.init(root, w)
   # w.slider()

    # root.bind("<Motion>",w.a5_handler)
    # root.bind("<Motion>",w.a4_handler)
    # root.bind("<Motion>",w.a3_handler)
    # root.bind("<Motion>",w.a2_handler)
    # root.bind("<Motion>",w.a1_handler)
    # root.bind("<Motion>",w.a0_handler)
    # root.bind("<Motion>",w.inxT_handler)
    # root.bind("<Motion>",w.y0_handler)
    root.bind("<Motion>",w.can_update)

    # root.bind("<Return>",w.a5_handler)
    # root.bind("<Return>",w.a4_handler)
    # root.bind("<Return>",w.a3_handler)
    # root.bind("<Return>",w.a2_handler)
    # root.bind("<Return>",w.a1_handler)
    # root.bind("<Return>",w.a0_handler)
    # root.bind("<Return>",w.inxT_handler)
    # root.bind("<Return>",w.y0_handler)
    root.bind("<Return>",w.can_update)


    root.mainloop()





class EDO_Solver:
    ##Onde user input eh a entrada anterior dos campos de entrada, em ordem,
    # ao,a1,a2,a3,a4,a5,y0,dy0,d2y0,d3y0,d4y0,xT
    global user_input, idi, flag_graf, flag_rep
    #flag_rep = False    #flags para nao ficar reconstruindo os objetos td vez q o foco volta para
    #flag_graf = False   #o widget(como qndo o usuario minimiza e depois retorna para o programa)
    user_input = [0]*12



    # def last_entry_equal(self,last_entry,who):
    #     global user_input
    #     print "hiii"
    #     print type(who),who
    #     print "le",last_entry
    #     print "c",user_input[5]
    #     if who == 'a0':
    #         user_input[0] = last_entry
    #     elif who == 'a1':
    #         user_input[1] = last_entry
    #         pass
    #     elif who == 'a2':
    #         user_input[2] = last_entry
    #     elif who == 'a3':
    #         user_input[3] = last_entry
    #     elif who == 'a4':
    #         user_input[4] = last_entry
    #     elif who == 'a5':
    #         user_input[5] = last_entry
    #     elif who == 'y0':
    #         user_input[6] = last_entry
    #     elif who == 'dy0':
    #         user_input[7] = last_entry
    #     elif who == 'xT':
    #         user_input[8] = last_entry
        #user_input = last_entry
        #print "Em : " + who, "Entrada anterior ",last_entry




    def update_saida(self):

        a2 = self.in_a2.get()
        a3 = self.in_a3.get()
        a4 = self.in_a4.get()
        a5 = self.in_a5.get()
        
        global canvas_latex,canvas_plots,latex_fig,plot_fig
        try:

            if(a5=="0"):#0 esta como string pois os widgets retornam variaveis do tipo string
                self.in_d4y0.configure(state="disabled")
            if(a5=="0" and a4=="0"):
                self.in_d4y0.configure(state="disabled")
                self.in_d3y0.configure(state="disabled")
            if(a5=="0" and a4=="0" and a3=="0"):
                self.in_d4y0.configure(state="disabled")
                self.in_d3y0.configure(state="disabled")
                self.in_d2y0.configure(state="disabled")
            if(a5=="0" and a4=="0" and a3=="0" and a2=="0"):
                self.in_d4y0.configure(state="disabled")
                self.in_d3y0.configure(state="disabled")
                self.in_d2y0.configure(state="disabled")
                self.in_dy0.configure(state="disabled")

            if(a5!="0"):
                self.in_d4y0.configure(state="normal")
                self.in_d3y0.configure(state="normal")
                self.in_d2y0.configure(state="normal")
                self.in_dy0.configure(state="normal")
            if(a4!="0"):
                self.in_d3y0.configure(state="normal")
                self.in_d2y0.configure(state="normal")
                self.in_dy0.configure(state="normal")
            if(a3!="0"):
                self.in_d2y0.configure(state="normal")
                self.in_dy0.configure(state="normal")
            if(a2!="0"):
                self.in_dy0.configure(state="normal")

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



    def can_update(self, event):
        global user_input
        n_changes = 0
        tal = get_tal()

        a0 = self.in_a0.get()
        a1 = self.in_a1.get()
        a2 = self.in_a2.get()
        a3 = self.in_a3.get()
        a4 = self.in_a4.get()
        a5 = self.in_a5.get()
        y0 = self.in_y0.get()
        dy0 = self.in_dy0.get()
        d2y0 = self.in_d2y0.get()
        d3y0 = self.in_d3y0.get()
        d4y0 = self.in_d4y0.get()
        xT = self.in_xT.get()

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

        if user_input[3] != a3:
            set_a3(a3)
            user_input[3] = a3
            n_changes = n_changes +1

        if user_input[4] != a4:
            set_a4(a4)
            user_input[4] = a4
            n_changes = n_changes +1

        if user_input[5] != a5:
            set_a5(a5)
            user_input[5] = a5
            n_changes = n_changes +1

        if user_input[6] != y0:
            set_y0(y0)
            user_input[6] = y0
            n_changes = n_changes +1

        if user_input[7] != dy0:
            set_dy0(dy0)
            user_input[7] = dy0
            n_changes = n_changes +1

        if user_input[8] != d2y0:
            set_d2y0(d2y0)
            user_input[8] = d2y0
            n_changes = n_changes +1

        if user_input[9] != d3y0:
            set_d3y0(d3y0)
            user_input[9] = d3y0
            n_changes = n_changes +1

        if user_input[10] != d4y0:
            set_d4y0(d4y0)
            user_input[10] = d4y0
            n_changes = n_changes +1

        if user_input[11] != xT:
            set_xT(xT)
            user_input[11] = xT
            n_changes = n_changes +1

        if(n_changes != 0):
            #tal=get_tal()
            edo_main()
            self.ScaleMin.configure(from_=0.0, to= self.ScaleMax.get()-1)
            self.ScaleMin.set(0)
            self.ScaleMax.configure(from_= self.ScaleMin.get()+1 , to= 10.0)
            self.ScaleMax.set(5.0)
            self.update_saida()



####Handlers-------------------------------------------
  #user input -># ao,a1,a2,y0,dy0,xT

 #    def a0_handler(self,event):
 #
 #        global  user_input
 #        #print "apertei",self.in_a2.get()
 #        okay_entry_a0 = self.in_a0.register(self.last_entry_equal)
 #        self.in_a0.configure(validate = 'all',validatecommand = (okay_entry_a0,'%s','a0'))
 #        a0 = self.in_a0.get()
 #        #print "User input",user_input
 #        #print "In a0 now",a0
 #        self.can_update()
 #        # if user_input[0] != a0:
 #        #     print  "Recalculando"
 #        #     set_a0(a0)
 #        #     edo_main()
 #        #     self.update_saida()
 #    #user input -># ao,a1,a2,y0,dy0,xT
 #
 #    def a1_handler(self,event):
 #        global  user_input
 #        #print "apertei",self.in_a2.get()
 #        okay_entry_a1 = self.in_a1.register(self.last_entry_equal)
 #        self.in_a1.configure(validate = 'all',validatecommand = (okay_entry_a1,'%s','a1'))
 #        a1 = self.in_a1.get()
 #        #print "User input",user_input
 #        #print "In a1 now",a1
 #        self.can_update()
 #        # if user_input[1] != a1:
 #        #     print  "Recalculando"
 #        #     set_a1(a1)
 #        #     edo_main()
 #        #     self.update_saida()
 #
 #    def a2_handler(self,event):
 #        global  user_input
 #        #print "apertei",self.in_a2.get()
 #        okay_entry_a2 = self.in_a2.register(self.last_entry_equal)
 #        self.in_a2.configure(validate = 'all',validatecommand = (okay_entry_a2,'%s','a2'))
 #        a2 = self.in_a2.get()
 #        #print "User input",user_input
 #        #print "In a2 now",a2
 #        self.can_update()
 #        # if user_input[2] != a2:
 #        #     print  "Recalculando"
 #        #     set_a2(a2)
 #        #     edo_main()
 #        #     self.update_saida()
 #
 #    def a3_handler(self,event):
 #        global  user_input
 #
 #        okay_entry_a3 = self.in_a3.register(self.last_entry_equal)
 #        self.in_a3.configure(validate = 'all',validatecommand = (okay_entry_a3,'%s','a3'))
 #        a3 = self.in_a3.get()
 #
 #        self.can_update()
 #
 #    def a4_handler(self,event):
 #        global  user_input
 #
 #        okay_entry_a4 = self.in_a4.register(self.last_entry_equal)
 #        self.in_a4.configure(validate = 'all',validatecommand = (okay_entry_a4,'%s','a4'))
 #        a4 = self.in_a4.get()
 #
 #        self.can_update()
 #
 #
 #    def a5_handler(self,event):
 #        global  user_input
 #
 #        okay_entry_a5 = self.in_a5.register(self.last_entry_equal)
 #        self.in_a5.configure(validate = 'all',validatecommand = (okay_entry_a5,'%s','a5'))
 #        a5 = self.in_a5.get()
 #
 #        self.can_update()
 #
 #
 #
 #
 #    def inxT_handler(self,event):
 #        #print "apertei",self.in_a2.get()
 #        okay_entry_xT = self.in_xT.register(self.last_entry_equal)
 #        self.in_xT.configure(validate = 'all',validatecommand = (okay_entry_xT,'%s','xT'))
 #        xT = self.in_xT.get()
 #        #print "User input",user_input
 #        #print "In xT now",xT
 #        self.can_update()
 #        # if user_input[5] != xT:
 #        #     print  "Recalculando"
 #        #     set_xT(xT)
 #        #     edo_main()
 #        #     self.update_saida()
 # #user input -># ao,a1,a2,y0,dy0,xT
 #    def y0_handler(self,event):
 #        #print "apertei",self.in_a2.get()
 #        okay_entry_y0 = self.in_y0.register(self.last_entry_equal)
 #        self.in_y0.configure(validate = 'all',validatecommand = (okay_entry_y0,'%s','y0'))
 #        y0 = self.in_y0.get()
 #        #print "User input",user_input
 #        #print "In y0 now",y0
 #        self.can_update()
 #        # if user_input[3] != y0:
 #        #     print  "Recalculando"
 #        #     set_y0(y0)
 #        #     edo_main()
 #        #     self.update_saida()
 #
 #    def dy0_handler(self,event):
 #      #print "apertei",self.in_a2.get()
 #        okay_entry_dy0 = self.in_dy0.register(self.last_entry_equal)
 #        self.in_dy0.configure(validate = 'all',validatecommand = (okay_entry_dy0,'%s','dy0'))
 #        dy0 = self.in_dy0.get()
 #        #print "User input",user_input
 #        #print "In dy0 now",dy0
 #        self.can_update()
 #        # if user_input[4] != dy0:
 #        #     print  "Recalculando"
 #        #     set_dy0(dy0)
 #        #     edo_main()
 #        #     self.update_saida()

    def abaLatex_handler(self,event):
        global canvas_latex,canvas_plots,toolbar

##        if(flag_rep==False):
        toolbar.pack_forget()
        toolbar = NavigationToolbar2TkAgg(canvas_latex,self.label_menu_plot)
        toolbar.pack(side = TOP, fill = Y)
        self.label_menu_plot.configure(text="")

##            try:
##                self.ScaleMin.destroy()
##                self.ScaleMax.destroy()
##
##            except:
##                pass
##            flag_graf = False
##            flag_rep = True

    def new_range(self, event):
        global plot_fig, canvas_plots
        maiorTal = get_maiorTal()/5
        rangeMin = float(self.ScaleMin.get())
        rangeMax = float(self.ScaleMax.get())
 
        # print "val:", rangeMin
        # print "limx", get_limx_max()

        if(rangeMin != get_limx_min()):
            minTauMaior = maiorTal*rangeMin
            set_limx_min(minTauMaior)
            self.ScaleMax.configure(from_=self.ScaleMin.get()+1)
            canvas_plots.get_tk_widget().destroy()
            plot_fig.clear()

            plot_fig  = show_plots()

            canvas_plots = FigureCanvasTkAgg(plot_fig,self.frame_plot)
            canvas_plots.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)

        if(rangeMax != get_limx_max()):
            maxTauMaior = maiorTal*rangeMax
            set_limx_max(maxTauMaior)
            self.ScaleMin.configure(to=self.ScaleMax.get()-1)
            canvas_plots.get_tk_widget().destroy()
            plot_fig.clear()

            plot_fig  = show_plots()

            canvas_plots = FigureCanvasTkAgg(plot_fig,self.frame_plot)
            canvas_plots.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)

    def autoScale_handler(self):
        global checkButton_state, canvas_plots, plot_fig

        #print "CheckButton value", checkButton_state.get()
        set_autoScale(checkButton_state.get())

        canvas_plots.get_tk_widget().destroy()
        plot_fig.clear()

        plot_fig  = show_plots()


        canvas_plots = FigureCanvasTkAgg(plot_fig,self.frame_plot)

        canvas_plots.get_tk_widget().pack(side = TOP,fill = BOTH, expand = 1)


    def tau_SliderText_handler(self,event):
        self.tau_label.configure(text=
                                                  str(self.ScaleMin.get() ) +  u"\u03C4"  + "\t " + ""+
                                                  str(self.ScaleMax.get() ) +  u"\u03C4")



    def slider(self):

        self.ScaleMin = Scale(self.TNotebook1_pg1)
        self.ScaleMin.place(relx=0.30,rely=0.7,relwidth=0.0,relheight=0.17
                ,height=20,width=20)
        self.ScaleMin.configure(activebackground="gray")
        self.ScaleMin.configure(background="white")
        #self.ScaleMin.configure(label = " *Tau")
        self.ScaleMin.configure(bd=0)
        #self.Scale1.configure(command=self.new_range)
        self.ScaleMin.configure(highlightthickness="0")
        self.ScaleMin.configure(showvalue=0)
        self.ScaleMin.configure(font="TkTextFont")
        self.ScaleMin.configure(foreground="#000000")
        self.ScaleMin.configure(highlightbackground="white")
        self.ScaleMin.configure(highlightcolor="black")
        self.ScaleMin.configure(orient="vertical")
        #self.ScaleMin.configure(variable = "*tau")
        self.ScaleMin.configure(troughcolor="gray")
        self.ScaleMin.configure(resolution = 0.1)
        self.ScaleMin.set(0)
        

        self.ScaleMax = Scale(self.TNotebook1_pg1)
        self.ScaleMax.place(relx=0.34,rely=0.70,relwidth=0.0,relheight=0.17
                ,height=20,width=20)
        self.ScaleMax.configure(activebackground="gray")
        self.ScaleMax.configure(background="white")
        self.ScaleMax.configure(bd=0)
        #self.Scale1.configure(command=self.new_range)
        self.ScaleMax.configure(highlightthickness="0")
        self.ScaleMax.configure(font="TkTextFont")
        self.ScaleMax.configure(showvalue=0)
        #self.ScaleMax.configure(label = " *Tau")
        #self.ScaleMax.configure(variable = "*tau")
        self.ScaleMax.configure(foreground="#000000")
        self.ScaleMax.configure(highlightbackground="#d9d9d9")
        self.ScaleMax.configure(resolution = 0.1)
        self.ScaleMax.configure(highlightcolor="black")
        self.ScaleMax.configure(orient="vertical")
        self.ScaleMax.configure(troughcolor="gray")
        self.ScaleMax.set(5)

        # Init Parameters
        
        self.ScaleMin.configure(from_=0.0,  to=  ( 9 - self.ScaleMax.get()  ) )
        self.ScaleMin.bind("<B1-Motion>",self.tau_SliderText_handler)
        self.ScaleMin.bind("<ButtonRelease-1>", self.new_range)
        
        #self.ScaleMin.bind("<ButtonRelease-1>",self.tau_SliderText_handler)
       

        
        self.ScaleMax.configure(from_= self.ScaleMin.get()+1,   to= 10.0  )
        self.ScaleMax.bind("<B1-Motion>",self.tau_SliderText_handler)
        self.ScaleMax.bind("<ButtonRelease-1>", self.new_range)
        


    def abaPlots_handler(self,event):
        global canvas_latex,canvas_plots,toolbar, flag_graf, flag_rep

##        if(flag_graf==False):
        toolbar.pack_forget()
        toolbar = NavigationToolbar2TkAgg(canvas_plots,self.label_menu_plot)
        toolbar.pack(side = TOP, fill = Y)
            #self.label_menu_plot.configure(anchor=NW")
##            self.slider()
##            flag_rep = False
##            flag_graf = True


    def set_bind_options(self):
        self.TNotebook1_pg0.bind("<FocusIn>",self.abaLatex_handler)
        self.TNotebook1_pg1.bind("<FocusIn>",self.abaPlots_handler)


    def set_idiomas(self):
        global idi
        #print "Idioma:",idi.get()
        if (idi.get() == 1): #Port
            self.menubar.entryconfig(2,label=u"Notação")
            self.menubar.entryconfig(3,label=u"DigitosFracionários")
            self.digitosfracionarios.entryconfig(0,label=u"2 Dígitos")
            self.digitosfracionarios.entryconfig(1,label=u"3 Dígitos")
            self.digitosfracionarios.entryconfig(2,label=u"4 Dígitos")
            self.TNotebook1.tab(0,text=u"Representação Algébrica")
            self.TNotebook1.tab(1,text=u"Gráficos")
            self.TNotebook1.tab(2,text="Log Texto")
            self.cond_ini_label.configure(text=u"""Condições  Iniciais:
        y\u207D\u2074\u207E(0) =        y\u207D\u00B3\u207E(0) =        y''(0) =        y'(0) =        y(0) =              """, anchor=N, font=("Verdana", 14))
            self.xT_label.configure(text='''Entrada x(t) =\t\t    u(t)''', font=("Verdana", 14))
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
            self.cond_ini_label.configure(text=u"""Initial Conditions:
        y\u207D\u2074\u207E(0) =        y\u207D\u00B3\u207E(0) =        y''(0) =        y'(0) =        y(0) =              """, anchor=N, font=("Verdana", 14))
            self.xT_label.configure(text='''  Input x(t) =\t\t    u(t)''', font=("Verdana", 14))
            set_lingua(2)
            self.update_saida()
            #print "english"
        else: #Espanol
            self.menubar.entryconfig(2,label=u"Notación")
            self.menubar.entryconfig(3,label=u"DígitosFraccionarios")
            self.digitosfracionarios.entryconfig(0,label=u"2 Dígitos")
            self.digitosfracionarios.entryconfig(1,label=u"3 Dígitos")
            self.digitosfracionarios.entryconfig(2,label=u"4 Dígitos")
            self.TNotebook1.tab(0,text=u"Representación Algebraica")
            self.TNotebook1.tab(1,text=u"Gráficos")
            self.TNotebook1.tab(2,text="Log Texto")
            self.cond_ini_label.configure(text=u"""Condiciones Iniciales:
        y\u207D\u2074\u207E(0) =        y\u207D\u00B3\u207E(0) =        y''(0) =        y'(0) =        y(0) =              """, anchor=N, font=("Verdana", 14))
            self.xT_label.configure(text='''Entrada x(t) =\t\t    u(t)''', font=("Verdana", 14))
            set_lingua(3)
            self.update_saida()
            #print "espanol"

    def set_notation(self):
        global notation

        if(notation.get()==1):
            self.eq_label.configure(image=self._img1)
            self.in_a0.place_configure(relx=0.83)
        elif(notation.get()==2):
            self.eq_label.configure(image=self._img2)
            self.in_a0.place_configure(relx=0.815)
        elif(notation.get()==3):
            self.eq_label.configure(image=self._img3)
            self.in_a0.place_configure(relx=0.805)
        elif (notation.get() == 4 ):
            self.eq_label.configure(image=self._img4)
            self.in_a0.place_configure(relx=0.81)

        set_notation(notation.get())
        self.update_saida()

    def set_digitosFracionarios(self):
        global prec

        if(prec.get()==2):
            set_prec(2)
        elif(prec.get()==3):
            set_prec(3)
        else:
            set_prec(4)

        edo_main()
        self.update_saida()

    def load_config(self):
        global idi,notation,prec, checkButton_state

        try:
            config = open("config.txt","r")
            str_config = config.read()
            print "Config = "+str_config
            idi.set(str_config[0])
            notation.set(str_config[1])
            prec.set(str_config[2])
            checkButton_state.set(str_config[3])
            self.set_idiomas()
            self.set_notation()
            self.set_digitosFracionarios()
            self.autoScale_handler()
        except:
            print "Config not found"
            pass

    def __init__(self, master):
        global canvas_latex,canvas_plots,latex_fig,plot_fig,toolbar
        global  user_input, idi, notation, prec, checkButton_state
        global config

        self.mast = master
        idi = IntVar()
        notation = IntVar()
        prec = IntVar()
        checkButton_state = IntVar()
        idi.set(1)
        notation.set(1)
        prec.set(2)
        checkButton_state.set(0)
        _bgcolor = 'white'  # X11 color: 'gray85'
        _fgcolor = 'black'  # X11 color: 'black'
        _compcolor = 'white' # X11 color: 'gray85'
        _ana1color = 'white' # X11 color: 'gray85'
        _ana2color = 'white' # X11 color: 'gray85'
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
        self.cond_ini_label.place(relx=0.0,rely=0.095,height=63,width=655)
        self.cond_ini_label.configure(activebackground="white")
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
        self.cond_ini_label.configure(text=u"""Condições  Iniciais:
        y\u207D\u2074\u207E(0) =        y\u207D\u00B3\u207E(0) =        y''(0) =        y'(0) =        y(0) =              """, anchor=N, font=("Verdana", 14))

        self.xT_label = Label (master)
        self.xT_label.place(relx=0.639,rely=0.095,height=63,width=370)
        self.xT_label.configure(activebackground="white")
        self.xT_label.configure(activeforeground="black")
        self.xT_label.configure(anchor=W)
        self.xT_label.configure(background="white")
        self.xT_label.configure(borderwidth="4")
        self.xT_label.configure(disabledforeground="#a3a3a3")
        self.xT_label.configure(foreground="#000000")
        self.xT_label.configure(highlightbackground="black")
        self.xT_label.configure(highlightcolor="black")
        self.xT_label.configure(relief=RIDGE)
        self.xT_label.configure(text='''Entrada x(t) =\t\t    u(t)''', font=("Verdana", 14))

        self.style.configure('TNotebook.Tab',background="#d9d9d9")
        self.style.configure('TNotebook.Tab',foreground="black")
        self.style.map('TNotebook.Tab',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(master)
        self.TNotebook1.place(relx=0.0,rely=0.18,relheight=0.76,relwidth=1.0)
        self.TNotebook1.configure(width=1024)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_pg0 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg0, padding=3)
        self.TNotebook1.tab(0, text=u"Representação Algébrica",underline="-1",)
        self.TNotebook1_pg1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg1, padding=3)
        self.TNotebook1.tab(1, text=u"Gráficos",underline="-1",)
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
        self.frame_latex.configure(highlightbackground="white")
        self.frame_latex.configure(highlightcolor="black")
        self.frame_latex.configure(width=1105)

        self.frame_plot = Frame (self.TNotebook1_pg1)
        self.frame_plot.place(relx=0.0,rely=0.0,relheight=1.0,relwidth=1.0)
        self.frame_plot.configure(relief=GROOVE)
        self.frame_plot.configure(borderwidth="2")
        self.frame_plot.configure(relief=GROOVE)
        self.frame_plot.configure(background="white")
        self.frame_plot.configure(highlightbackground="white")
        self.frame_plot.configure(highlightcolor="black")
        self.frame_plot.configure(width=1025)
        


        self.saida_log_txt = Text (self.TNotebook1_pg2)
        self.saida_log_txt.place(relx=0.0,rely=0.0,relheight=0.95,relwidth=1.0)
        self.saida_log_txt.configure(background="white")
        self.saida_log_txt.configure(font="TkTextFont")
        self.saida_log_txt.configure(foreground="black")
        self.saida_log_txt.configure(highlightbackground="white")
        self.saida_log_txt.configure(highlightcolor="black")
        self.saida_log_txt.configure(insertbackground="black")
        self.saida_log_txt.configure(selectbackground="gray")
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
        self._img2 =ImageTk.PhotoImage(lagrange_im)
        self._img3 =ImageTk.PhotoImage(newton_im)
        self._img4 =ImageTk.PhotoImage(euler_im)
        self.eq_label.configure(image=self._img1)
        self.eq_label.configure(text='''Label''')
        self.eq_label.configure(width=1002)

        self.in_a4 = Entry (master)
        self.in_a4.place(relx=0.19,rely=0.03,relheight=0.04,relwidth=0.03)
        self.in_a4.configure(background="white")
        self.in_a4.configure(disabledforeground="white")
        self.in_a4.configure(font="TkFixedFont")
        self.in_a4.configure(foreground="#000000")
        self.in_a4.configure(highlightbackground="#d9d9d9")
        self.in_a4.configure(highlightcolor="black")
        self.in_a4.configure(insertbackground="black")
        self.in_a4.configure(selectbackground="#c4c4c4")
        self.in_a4.configure(selectforeground="black")
        self.in_a4.configure(width=34)

        self.in_a3 = Entry (master)
        self.in_a3.place(relx=0.35,rely=0.03,relheight=0.04,relwidth=0.03)
        self.in_a3.configure(background="white")
        self.in_a3.configure(disabledforeground="#a3a3a3")
        self.in_a3.configure(font="TkFixedFont")
        self.in_a3.configure(foreground="#000000")
        self.in_a3.configure(highlightbackground="white")
        self.in_a3.configure(highlightcolor="black")
        self.in_a3.configure(insertbackground="black")
        self.in_a3.configure(selectbackground="#c4c4c4")
        self.in_a3.configure(selectforeground="black")
        self.in_a3.configure(width=34)

        self.in_a5 = Entry (master)
        self.in_a5.place(relx=0.02,rely=0.03,relheight=0.04,relwidth=0.03)
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
                activebackground="white",
                activeforeground="white",
                background="white",
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
                label=u"Português")
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
                label=u"Español")

        self.notacao = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.notacao,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                foreground="#000000",
                state="normal",
                label=u"Notação")
        self.notacao.add_radiobutton(
                variable=notation,
                value=1,#Leibniz
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.set_notation,
                foreground="#000000",
                label="Leibniz")
        self.notacao.add_radiobutton(
                variable=notation,
                value=2, #Lagrange
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.set_notation,
                foreground="#000000",
                label="Lagrange")
        self.notacao.add_radiobutton(
                variable=notation,
                value=3, #Newton
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.set_notation,
                foreground="#000000",
                label="Newton")
        self.notacao.add_radiobutton(
                variable=notation,
                value=4, #Euler
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.set_notation,
                foreground="#000000",
                label="Euler")
        self.digitosfracionarios = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.digitosfracionarios,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                foreground="#000000",
                state="normal",
                label=u"DígitosFracionários")
        self.digitosfracionarios.add_radiobutton(
                variable=prec,
                value=2,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.set_digitosFracionarios,
                foreground="#000000",
                label=u"2 Dígitos")
        self.digitosfracionarios.add_radiobutton(
                variable=prec,
                value=3,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.set_digitosFracionarios,
                foreground="#000000",
                label=u"3 Dígitos")
        self.digitosfracionarios.add_radiobutton(
                variable=prec,
                value=4,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.set_digitosFracionarios,
                foreground="#000000",
                label=u"4 Dígitos")


        self.label_menu_plot = Label (master)
        self.label_menu_plot.place(relx=-0.01,rely=0.94,height=90,width=1052)
        self.label_menu_plot.configure(activebackground="white")
        self.label_menu_plot.configure(activeforeground="black")
        self.label_menu_plot.configure(background="white")
        self.label_menu_plot.configure(borderwidth="4")
        self.label_menu_plot.configure(disabledforeground="#a3a3a3")
        self.label_menu_plot.configure(foreground="#000000")
        self.label_menu_plot.configure(highlightbackground="#d9d9d9")
        self.label_menu_plot.configure(highlightcolor="black")
        self.label_menu_plot.configure(relief=RIDGE)

       

        self.in_d4y0 = Entry (master)
        self.in_d4y0.place(relx=0.092,rely=0.13,relheight=0.035,relwidth=0.035)
        self.in_d4y0.configure(background="white")
        self.in_d4y0.configure(disabledforeground="#a3a3a3")
        self.in_d4y0.configure(font="TkFixedFont")
        self.in_d4y0.configure(foreground="#000000")
        self.in_d4y0.configure(highlightbackground="white")
        self.in_d4y0.configure(highlightcolor="black")
        self.in_d4y0.configure(insertbackground="black")
        self.in_d4y0.configure(selectbackground="#c4c4c4")
        self.in_d4y0.configure(selectforeground="black")
        self.in_d4y0.configure(width=44)

        self.in_d3y0 = Entry (master)
        self.in_d3y0.place(relx=0.228,rely=0.13,relheight=0.035,relwidth=0.035)
        self.in_d3y0.configure(background="white")
        self.in_d3y0.configure(disabledforeground="#a3a3a3")
        self.in_d3y0.configure(font="TkFixedFont")
        self.in_d3y0.configure(foreground="#000000")
        self.in_d3y0.configure(highlightbackground="#d9d9d9")
        self.in_d3y0.configure(highlightcolor="black")
        self.in_d3y0.configure(insertbackground="black")
        self.in_d3y0.configure(selectbackground="#c4c4c4")
        self.in_d3y0.configure(selectforeground="black")
        self.in_d3y0.configure(width=44)

        self.in_d2y0 = Entry (master)
        self.in_d2y0.place(relx=0.353,rely=0.13,relheight=0.035,relwidth=0.035)
        self.in_d2y0.configure(background="white")
        self.in_d2y0.configure(disabledforeground="#a3a3a3")
        self.in_d2y0.configure(font="TkFixedFont")
        self.in_d2y0.configure(foreground="#000000")
        self.in_d2y0.configure(highlightbackground="#d9d9d9")
        self.in_d2y0.configure(highlightcolor="black")
        self.in_d2y0.configure(insertbackground="black")
        self.in_d2y0.configure(selectbackground="#c4c4c4")
        self.in_d2y0.configure(selectforeground="black")
        self.in_d2y0.configure(width=44)


        self.in_dy0 = Entry (master)
        self.in_dy0.place(relx=0.476,rely=0.13,relheight=0.035,relwidth=0.035)
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

        self.in_y0 = Entry (master)
        self.in_y0.place(relx=0.59,rely=0.13,relheight=0.035,relwidth=0.035)
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

        self.in_xT = ttk.Entry (master)
        self.in_xT.place(relx=0.78,rely=0.11,relheight=0.06,relwidth=0.17)
        self.in_xT.configure(font=font15)
        self.in_xT.configure(width=226)
        self.in_xT.configure(takefocus="")
        self.in_xT.configure(cursor="ibeam")

        self.autoScaleButton = Checkbutton (self.TNotebook1_pg1)
        self.autoScaleButton.place(relx=0.28,rely=0.635,relheight=0.04
                ,relwidth=0.17)
        self.autoScaleButton.configure(activebackground="white")
        self.autoScaleButton.configure(activeforeground="#000000")
        self.autoScaleButton.configure(background="white")
        self.autoScaleButton.configure(disabledforeground="#a3a3a3")
        self.autoScaleButton.configure(foreground="#000000")
        self.autoScaleButton.configure(highlightbackground="#d9d9d9")
        self.autoScaleButton.configure(highlightcolor="black")
        self.autoScaleButton.configure(text='''Auto Scale Amplitude''')
        self.autoScaleButton.configure(variable=checkButton_state)
        self.autoScaleButton.configure(command=self.autoScale_handler)


     




        #-----------------------------INIT configs-------------------------------------
        self.in_xT.insert(END, '1')
        self.in_y0.insert(END, '1')
        self.in_dy0.insert(END, '1')
        self.in_d2y0.insert(END, '1')
        self.in_d3y0.insert(END, '1')
        self.in_d4y0.insert(END, '1')
        self.in_a0.insert(END, '1')
        self.in_a1.insert(END, '1')
        self.in_a2.insert(END, '1')
        self.in_a3.insert(END, '0')
        self.in_a4.insert(END, '0')
        self.in_a5.insert(END, '0')
        self.in_d2y0.configure(state="disabled")
        self.in_d3y0.configure(state="disabled")
        self.in_d4y0.configure(state="disabled")
        #ao,a1,a2,y0,dy0,xT -> Definindo valores iniciais de user_input
        user_input[0] = '1'
        user_input[1] = '1'
        user_input[2] = '1'
        user_input[3] = '0'
        user_input[4] = '0'
        user_input[5] = '0'
        user_input[6] = '1'
        user_input[7] = '1'
        user_input[8] = '1'
        user_input[9] = '1'
        user_input[10] = '1'
        user_input[11] = '1'
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

        self.slider()

        self.tau_label = Label (self.TNotebook1_pg1)
        self.tau_label.configure(width=1002)
        self.tau_label.place(relx=0.295,rely=0.92,height=20,width=100)
        self.tau_label.configure( anchor="nw")
        self.tau_label.configure(activebackground="white")
        self.tau_label.configure(activeforeground="black")
        self.tau_label.configure(background="white")
        self.tau_label.configure(disabledforeground="#a3a3a3")
        self.tau_label.configure(foreground="#000000")
        self.tau_label.configure(highlightbackground="#d9d9d9")
        self.tau_label.configure(highlightcolor="black")
        self.tau_label.configure(text=
                                                  str(self.ScaleMin.get() ) +  u"\u03C4"  + "       "+
                                                  str(self.ScaleMax.get() ) +  u"\u03C4")

        self.load_config()
        







if __name__ == '__main__':
    init(0.0,0.0,0.0,1.0,1.0,1.0,'1',1.0,1.0,1.0,1.0,1.0)
    vp_start_gui()



