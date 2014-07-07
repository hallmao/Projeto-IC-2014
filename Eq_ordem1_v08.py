import matplotlib.pyplot as plt
from   math  import e 
from   numpy import array,sin,cos,exp
from   numpy import arange
###Funções renomeadas para facilitar digitação


while True :

    #EDO ordem1
    # a1*y´(t) + a0*(t)  = b0*x(t)

    #1--eq homogenea
    # a1*y´(t) + a0*y(t) = 0

    #Equacao Caracteristica:
    # a1*r + a0 = 0
    #Raiz:
    # r = -a0/a1

    #1--Forma natural de resposta:
    ########Yfn(t) = C*e^(rt)*u(t) , onde r = -a0/a1

    #Coeficientes da equação diferencial
    #----------------------------------
    a1 = 0
    a0 = 0
    b0 = 0
    #------------------
    t  = 0 # Variável no tempo
    x0 = 0
    #----------------------------------

    #2--Resposta natural:

    #Condição inicial

    y0 = 0

    # Condiçãp inicial y(0) = d

    # d = C*e^(-a0/a1)*0
    # c = d
    ######## ynat(t) = d* e^(-a0/a1)*u(t)


    #3--Resposta forçada :
    # Entrada : x(t) = f*u(t)

    #ypar(t) = k*u(t)

    #ypar´(t) = 0

    # a1*0 + a0*k = b0*f

    # k = (b0*f)/a0

    ####### ypar(t) = [(bo*f)/a0] *u(t)

    # yfor(t) = ytran(t) + ypar(t)

    # yfor(t) = C*e^[(-a0/a1)*t] + (b0*f)/a0

    ##### yfor(t) =[-(b0*f)/a0]*e^[(-a0/a1)*t]*u(t) + [(b0*f)/a0]*u(t)


    #4--Resposta Completa

    # yc(t) = ynat(t) + yfor(t) =
    # = d*e^[(-a0/a1)*t]  + (-b0/a0)*e^[(-a0/a1)*t] + (b0*f)/a0

    ### yc(t) = ( d- (b0*f)/a0)*e^[(-a0/a1)*t]

    print "Entre com os coefs para uma EDO do tipo a1*(dy(t)/dt) + a0*y(t)  = b0*x(t)"

    #Entrada porca no console (só pra testes,claro !)
    a1 = float(input("a1 = "))
    a0 = float(input("a0 = "))
    b0 = float(input("b0 = "))
    y0 = float(input("Condicao Inicial de y(0) =  "))
    print "Entrada x(t),favor inserir no formato e**(q*t),sin(q*t),cos(q*t),q*t,t**q onde q e uma cte:"

    if b0 != 0 :
        xT = raw_input("x(t) = ")

    else:
        xT = 0

    ##Flag para verificar se xT é uma f(x) ou uma cte (degrau, impulso)
    flag_FdeX = True
    #xTcheck = 0.0
    ##Checando xT, verificando se é uma função em x ou impulso

    ##Tente converter x(t) pra float, só funciona se
    #o mesmo for uma constante, do contrario, ignore
    try:
        xTcheck = float(xT)
        #print  type(xTcheck)
        #print  xT,xTcheck
        flag_FdeX = False
    except:
        pass


    ##Precisão no log de saída :
    precLog = 2
        
    #print xTcheck    



    ###1--Homogenea

    #1--eq homogenea
    # a1*y´(t) + a0*y(t) = 0

    #Equacao Caracteristica:
    # a1*r + a0 = 0
    #Raiz:
    # r = -a0/a1

    #1--Forma natural de resposta:
    ########Yfn(t) = C*e^(rt)*u(t) , onde r = -a0/a1

    ##Conds Iniciais
    # d = C*e^(-a0/a1)*0
    # c = d
    ######## ynat(t) = d* e^(-a0/a1)*u(t)


    #-------------------Resolucao---------------------


    ###Resposta natural
    r = -(a0/a1) ## Raiz da eq
        #Forma Natural





    def log_print():
        print "\nRelatorio"
        print "Equacao diferencial-->\n"
        print str(a1)+"*(dy(t)/dt) "+str(a0)+"*y(t) " + "= "+str(b0)+"*("+xT+")\n"
        print "Raiz(es) da equacao = " + str(round(r,precLog))
        print "Forma natural da resposta:\n"+"yfn(t)= " + "C*e^("+str(round(r,precLog))+"t)*u(t)"
    ##Resposta forma natural com conds iniciais
        print "\nResposta natural:\n"+"ynat(t)= " +str(round(y0,precLog))+"*e^("+str(round(r,precLog))+"t)*u(t)"
        ##Resposta completa
        if b0 == 0:
            print "\nResposta completa : yc(t) = ynat(t) + yfor(t)"
            print "yc(t) = ("+str(round(r,precLog))+"*"+"e^("+str(round(r,precLog))+"t)*u(t)"

        
        if b0 != 0:
            print "\nResposta forcada"
            print "ypart(t) ="+str(round(b0/a0,precLog))+"*("+xT+")*u(t)"
            ##ytran(t)
            print "ytran(t) = "+str(round(-b0/a0,precLog))+"*("+xT+")*e^("+str(round(r,precLog))+"t)*u(t)"
            ## Yforçada(t)
            print "yfor(t) = ytran(t) + ypart(t)"
            print "yfor(t) = "+str(round(-b0/a0,precLog))+"*("+xT+")*e^("+str(round(r,precLog))+"t)*u(t) + "+str(round(b0/a0,2))+"*"+xT+"*u(t)"
            ###Resposta completa
            print "\nResposta completa : yc(t) = ynat(t) + yfor(t)"
            print "yc(t) = ("+str(round(y0,precLog))+str(round(-b0/a0,precLog))+"*("+xT+")*e^("+str(round(r,precLog))+"t)*u(t) + "+str(round(b0/a0,precLog))+"*"+xT+"*u(t)"
        


    #Print

    log_print()


    def plot_and_show():

        #Plot resposta natural:

        # t variable adjusting
        ###Ideia futura, t ajustável pelo Usuário !!
        t       = arange(0.0,20.0,0.01)

        
        plotNat = y0*e**(r*t)
        ##Nome da Janela dos graficos
        plt.figure("EDOs a coeficientes constantes")
        plt.subplot(333)
        #plt.figure("Resposta Natural ynat(t)")
        plt.title("ynat(t)")
        plt.xlabel("Tempo t")
        plt.ylabel("Amplitude")
        RespNatplot= plt.plot(t,plotNat,lw = 2)
        plt.ylim(-abs(y0+1),abs(y0+1))



        if b0!= 0 and flag_FdeX : ## Para x(t) funcao de t


                ###Plot x(t)
            plotXt = eval(xT)
            plt.subplot(3,3,1)
            plt.title("x(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            funcXplot = plt.plot(t,plotXt, lw = 2)
            

           
            #Plot Resposta Particular
            plotPart = (b0/a0)* eval(xT)
            #plt.figure("Resposta Particular ypart(t)")
            plt.subplot(332)
            plt.title("ypart(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespPartPlot= plt.plot(t,plotPart,lw = 2)
            #plt.ylim(-abs((b0/a0)+1),abs((b0/a0)+1))


            #Plot Resposta Transitoria
            #print "ytran(t) = "+str((-b0/a0))+"*("+xT+")*e^("+str(r)+"t)*u(t)"
     
            plotTran = (-b0/a0)*eval(xT)*(e**r)
            plt.subplot(335)
            #plt.figure("Resposta Transitoria ytran(t)")
            plt.title("ytran(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespTranPlot= plt.plot(t,plotTran,lw = 2)
            #plt.ylim(-abs((b0/a0)+5),abs((b0/a0)+5))

            ##Plot Resposta Forçada
            ##print "yfor(t) = ytran(t) + ypart(t)"
            plotFor = (-b0/a0)*eval(xT)*(e**r) + (b0/a0)*eval(xT)
            plt.subplot(3,3,8)
            #plt.figure("Resposta Forcada yfor(t)")
            plt.title("yfor(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespForPlot= plt.plot(t,plotFor,lw = 2)
            ##Plotting on 2 distinct places
            plt.subplot(3,3,6)
            plt.title("yfor(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespForPlot= plt.plot(t,plotFor,lw = 2)
            #plt.ylim(-abs((b0/a0)+5),abs((b0/a0)+5))
            
            ##Plot Resposta Completa
            ##print "\nResposta completa : yc(t) = ynat(t) + yfor(t)"
            plotCom = y0*e**(r*t) + ((-b0/a0)*eval(xT)*(e**r)) + (b0/a0)*eval(xT)
            plt.subplot(339)
            #plt.figure("Resposta Completa yc(t)")
            plt.title("yc(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespComPlot= plt.plot(t,plotCom,lw = 2)
            #plt.ylim(-abs((b0/a0)+5),abs((b0/a0)+5))
            
        else: # Para x(t) constante ou funcao degrau/impulso

            ## Nosso t precisa ser multiplicado por essa constant,
            # t deixa de ser um escalar e vira um vetor
                # print xTcheck
            t=t*xTcheck
            #print type(t),t

                ###Plot x(t)
            plotXt = t
            plt.subplot(3,3,1)
            plt.title("x(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            funcXplot = plt.plot(t,plotXt, lw = 2)


            
        
            #Plot Resposta Particular
            plotPart = (b0/a0)*t
            plt.subplot(332)
            #plt.figure("Resposta Particular ypart(t)")
            plt.title("ypart(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespPartPlot= plt.plot(t,plotPart,lw = 2)
            #plt.ylim(-abs((b0/a0)+1),abs((b0/a0)+1))


            #Plot Resposta Transitoria
            #print "ytran(t) = "+str((-b0/a0))+"*("+xT+")*e^("+str(r)+"t)*u(t)"

            plotTran = (-b0/a0)*t*(e**r)
            plt.subplot(335)
            #plt.figure("Resposta Transitoria ytran(t)")
            plt.title("ytran(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespTranPlot= plt.plot(t,plotTran,lw = 2)
            #plt.ylim(-abs((b0/a0)+5),abs((b0/a0)+5))

            ##Plot Resposta Forçada
            ##print "yfor(t) = ytran(t) + ypart(t)"
            plotFor = (-b0/a0)*t*(e**r) + (b0/a0)*t
            plt.subplot(338)
            #plt.figure("Resposta Forcada yfor(t)")
            plt.title("yfor(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespForPlot= plt.plot(t,plotFor,lw = 2)
            plt.subplot(336)
            #plt.figure("Resposta Forcada yfor(t)")
            plt.title("yfor(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespForPlot= plt.plot(t,plotFor,lw = 2)
            #plt.ylim(-abs((b0/a0)+5),abs((b0/a0)+5))
            
            ##Plot Resposta Completa
            ##print "\nResposta completa : yc(t) = ynat(t) + yfor(t)"
            plotCom = y0*e**(r*t) + ((-b0/a0)*t*(e**r)) + (b0/a0)*t
            plt.subplot(339)
            #plt.figure("Resposta Completa yc(t)")
            plt.title("yc(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespComPlot= plt.plot(t,plotCom,lw = 2)
            #plt.ylim(-abs((b0/a0)+5),abs((b0/a0)+5))

        ##Manual Plot spacing
        plt.subplots_adjust(left=0.05, bottom=0.10, right=0.97, top=0.95,
                    wspace=0.29, hspace=0.65)
 
        plt.show()





    #Plot Answers
    plot_and_show()

    ##raw_input()
    



    


    
    
    
    
    











