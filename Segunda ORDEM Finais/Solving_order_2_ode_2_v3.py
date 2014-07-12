import matplotlib.pyplot as plt
from sympy import Function, dsolve, pprint, exp, cos
from sympy.abc import t
from sympy import *
from numpy import arange

prec = 2


##Loop para testes
while True:

    #Entrada pelo console
    def input_coefs():
        global a2,a1,a0,xT,y0,dy0
        print "Insira os coefs e entrada para uma EDO do tipo: "
        print "     a2*y''(t) +a1*y'(t) +a0*y(t) = x(t)"
        a2 = input("a2:")
        a1 = input("a1:")
        a0 = input("a0:")   
        xT = input("x(t):")
        y0 = input("Condicao inicial de y(0) = ")
        if(a2 != 0): #se for EDO de ordem 1 nao tem y'(0)
            dy0 = input("Condicao inicial de y'(0) = ")


    def raizes():
        
        delta = ((a1*a1)-(4*a2*a0))

        if(delta>0):    # raizes reais e distintas
            r1 = ((-a1)+(delta**(0.5)))/(2*a2)
            r2 = ((-a1)-(delta**(0.5)))/(2*a2)

        if(delta==0):   # raizes repetidas
            r=(-a1)/(2*a2)
            #se precisar de duas raizes para o grafico
            ##r1=(-a1)/(2*a2)
            ##r2=(-a1)/(2*a2)

        if(delta<0): # raizes complexas conjugadas
            r = (-a1)/(2*a2) #parte real das raizes
            r_u = (delta*(-1))**(0.5) #sqrt(-x) = sqrt(x)*sqrt(-1) = sqrt(x)*i //parte imaginaria
            #u eh a parte imaginaria das raizes
            u = r_u/(2*a2)

            #se precisar de duas raizes para o grafico
            #r1 = r + u*I
            #r2 = r - u*I

        #return

    def Resp_Nat(yfn):
        
        if(ordem_1): # Edo de ordem 1

            #Yfn = C1*e**(r*t); Yn = y0*e**(r*t)
            RespNat = yfn.subs(C1, y0)
            
        else: #Edo de ordem 2
            dyfn = yfn.diff(t)  # Yfn'(t)

            yfn0 = yfn.subs(t, 0) # Yfn(0)
            dyfn0 = dyfn.subs(t, 0) #Yfn'(0)

            #c1 e c2 são os valores de C1 e C2
            #solve(eq, var); eq=equacao a ser resolvida; var=variavel que se quer achar
            #solve iguala a equacao a 0, portanto, yt0 - y0 = 0 => yt0 = y0
            res = solve((yfn0 - y0, dyfn0 - dy0), C1, C2) #solve retorna um dictionary(hash)
            c1 = res.get(C1)                           #com keys C1 e C2
            c2 = res.get(C2)

            #Para substituir mais de uma variavel ao mesmo tempo tem que passar
            #uma lista [(old,new),...,(old,new)] para a função subs.
            RespNat = yfn.subs([(C1, c1), (C2, c2)])

        return RespNat
    
            
##    def Resp_Part(yp):
##
##        if(xT == 0): #se for eq homogenea
##            yp = 0 #Não ha Resposta particular na eq. homogenea
##        else:
##            yp = yp
##
##        return yp
            
    def Resp_Trans(yfn, yp):
        yt = yfn + yp   #Ytrans(t)

        if(ordem_1): # Edo de ordem 1
            yt0 = yt.subs(t, 0) #Aplicando as condicoes iniciais; Ytrans(0)
            
            #c1 eh o valor de C1
            #solve(eq, var); eq=equacao a ser resolvida; var=variavel que se quer achar
            #solve iguala a equacao a 0, portanto, yt0 - y0 = 0 => yt0 = y0
            res = solve((yt0 - y0), C1) #solve retorna um dictionary(hash)
            c1 = res.get(C1)            #com keys C1
            RespTrans = yt.subs(C1, c1)
        else:
            dyt = yt.diff(t)    #Ytrans'(t)
            
            yt0 = yt.subs(t, 0) #Aplicando condições iniciais; y(0)
            dyt0 = dyt.subs(t, 0)#Aplicando condições iniciais; y'(0)


            #c1 e c2 são os valores de C1 e C2 em Y transitorio
            #solve((yf0 - y0, dyf0 - dy0), C1, C2) monta um sistema de eqs. p/ achar C1 e C2
            res = solve((yt0 - y0, dyt0 - dy0), C1, C2) #solve retorna um dictionary(hash)
            c1 = res.get(C1)                            #com keys C1 e C2
            c2 = res.get(C2)
            
            #Para substituir mais de uma variavel ao mesmo tempo tem que passar
            #uma lista [(old,new),...,(old,new)] para a função subs.
            RespTrans = yt.subs([(C1, c1), (C2, c2)])

        return RespTrans

    def log_print():
        pprint(eq)
        print "\nForma natural de resposta:\n"+"Yfn(t) =", (sympify(RespFNat, rational = False , evaluate = False).evalf(prec))
        print "\nResposta natural:\n"+"Ynat(t) =", (sympify(RespNat, rational = False , evaluate = False).evalf(prec))

        if(xT != 0):
            print "\nResposta particular:\n"+"Yp(t) =", (sympify(RespPart, rational = False , evaluate = False).evalf(prec))
            print "\nResposta transitoria:\n"+"Yt(t) =", (sympify(RespTrans, rational = False , evaluate = False).evalf(prec))
            print "\nResposta forcada:\n"+"Yf(t) =", (sympify(RespForc, rational = False , evaluate = False).evalf(prec))
        
        print "\nReposta completa:\n"+"Yc(t) =", (sympify(RespComp, rational = False , evaluate = False).evalf(prec))

        
    input_coefs()

    y = Function('y')

    if(xT == 0):
        temp_xT = t
        ##Adicionando os coefs a eq diferencial
        eq =sympify(a2*y(t).diff(t,2) + a1*y(t).diff(t) +a0*y(t) -temp_xT)
    else:
        ##Adicionando os coefs a eq diferencial
        eq =sympify(a2*y(t).diff(t,2) + a1*y(t).diff(t) +a0*y(t) -xT)

    #pprint(eq)
    #print ""

    ###Dif equation solver
    solvedEq = dsolve(sympify(eq),y(t),hint='nth_linear_constant_coeff_undetermined_coefficients')

    ##Transformação do tipo sympy_unity para o sympy_mul (mais operações permitidas)
    sepEq = solvedEq._args[1]
    #print "sepEq =", sepEq

    ##PRocesso de separação de resp natural e resposta transitória
    elementosEq = sepEq.atoms(Symbol)
    C1 = elementosEq.pop()
    C2 = elementosEq.pop()


    if C2 != t :
        ordem_1 = False
        #print "Tem c2"
        RespPart =  sepEq.subs([(C2,0),(C1,0)])
        
        
    else:
        #print "Soh c1"
        ordem_1 = True
        RespPart =  sepEq.subs(C1,0)
        
    ##Resposta particular alocada em  RespPart, Forma Natural em RespFNat

    RespFNat  =  sepEq.subs(RespPart,0) #Forma natural de resposta
    RespNat = Resp_Nat(RespFNat)    #Resposta natural
    RespComp = RespNat      #Resposta completa p/ eqs. homogeneas

    if(xT != 0): #Eqs nao homogeneas
        RespPart = RespPart  #Resposta particular
        RespTrans = Resp_Trans(RespFNat, RespPart)  #Resposta transitoria
        RespForc = RespTrans + RespPart     #Resposta forcada
        RespComp = RespNat + RespForc   #Respsota completa p/ eqs. nao-homogeneas

    


    def plot_and_show():
        
        # tempo variable adjusting
        ###Ideia futura, t ajustável pelo Usuário !!
        t = arange(0.0,20.0,0.01)

        #Plot Resposta Natural
        ##Nome da Janela dos graficos
        plotNat = RespNat
        #plotNat = plotNat.replace("exp", "e**")
        
        plt.figure("EDOs a coeficientes constantes")
        plt.subplot(333)
        #plt.figure("Resposta Natural ynat(t)")
        plt.title("ynat(t)")
        plt.xlabel("Tempo t")
        plt.ylabel("Amplitude")
        RespNatplot= plt.plot(t,plotNat,lw = 2)
        plt.ylim(-abs(y0+1),abs(y0+1))


        ##Plot das raizes (nesse caso só uma)
        plotRaizes = r
        plt.subplot(334)
        plt.title("Raizes")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        respRaizesPlot = plt.plot(r,'x')

        if(xT != 0): #eqs. nao homogeneas
            
            ###Plot x(t)
            #plotXt = eval(xT)
            plt.subplot(3,3,1)
            plt.title("x(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            funcXplot = plt.plot(t,xT, lw = 2)

            #Plot Resposta Particular
            #plotPart = (b0/a0)* eval(xT)
            #plt.figure("Resposta Particular ypart(t)")
            plt.subplot(332)
            plt.title("ypart(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespPartPlot= plt.plot(t,RespPart,lw = 2)
            #plt.ylim(-abs((b0/a0)+1),abs((b0/a0)+1))


            #Plot Resposta Transitoria     
            #plotTran = (-b0/a0)*eval(xT)*(e**r)
            plt.subplot(335)
            #plt.figure("Resposta Transitoria ytran(t)")
            plt.title("ytran(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespTranPlot= plt.plot(t,RespTrans,lw = 2)
            #plt.ylim(-abs((b0/a0)+5),abs((b0/a0)+5))

            ##Plot Resposta Forçada
            ##print "yfor(t) = ytran(t) + ypart(t)"
            #plotFor = (-b0/a0)*eval(xT)*(e**r) + (b0/a0)*eval(xT)
            plt.subplot(3,3,8)
            #plt.figure("Resposta Forcada yfor(t)")
            plt.title("yfor(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespForPlot= plt.plot(t,RespForc,lw = 2)
            ##Plotting on 2 distinct places
            plt.subplot(3,3,6)
            plt.title("yfor(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespForPlot= plt.plot(t,RespForc,lw = 2)
            #plt.ylim(-abs((b0/a0)+5),abs((b0/a0)+5))
            
            ##Plot Resposta Completa
            ##print "\nResposta completa : yc(t) = ynat(t) + yfor(t)"
            #plotCom = y0*e**(r*t) + ((-b0/a0)*eval(xT)*(e**r)) + (b0/a0)*eval(xT)
            plt.subplot(339)
            #plt.figure("Resposta Completa yc(t)")
            plt.title("yc(t)")
            plt.xlabel("Tempo t")
            plt.ylabel("Amplitude")
            RespComPlot= plt.plot(t,RespComp,lw = 2)
            #plt.ylim(-abs((b0/a0)+5),abs((b0/a0)+5))



    log_print()
    plot_and_show()
