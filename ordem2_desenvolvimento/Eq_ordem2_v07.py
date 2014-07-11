import matplotlib.pyplot as plt

from   numpy import array
from   numpy import arange
from sympy import *
#from sympy import simplify
##from sympy.integrals import laplace_transform,inverse_laplace_transform
from sympy.abc import t,s

from math import exp



def entrada_dados():

    #Definindo parametros como variaveis globais:
    global a2,a1,a0,b0,y0,y1,xT,xTcheck,flag_FdeX

    print ("Entre com os coefs para uma EDO do tipo"+
           " a2*(d^2*y(t)/dt^^2) +  a1*(dy(t)/dt) + a0*y(t)  = b0*x(t)")

    #Entrada porca no console (só pra testes,claro !)
    a2 = S(input("a2 = "))
    a1 = S(input("a1 = "))
    a0 = S(input("a0 = "))
    b0 = S(input("b0 = "))
    y0 = S(input("Condicao Inicial de y(0) =  "))
    y1 = S(input("Condicao Inicial de y'(0) =  "))
    print "Entrada x(t),favor inserir no formato e**(q*t),sin(q*t),cos(q*t),q*t,t**q onde q e uma cte:"


      ##Flag para verificar se xT é uma f(x) ou uma cte (degrau, impulso)
    flag_FdeX = True
    #xTcheck = 0.0
    ##Checando xT, verificando se é uma função em x ou impulso

    ##Tente converter x(t) pra float, só funciona se
    #o mesmo for uma constante, do contrario, ignore



    if b0 != 0 :
        xT =raw_input("x(t) = ")

    else:
        xT = 0


    try:
        #xTcheck = float(xT)
        #print  type(xTcheck)
        #print  xT,xTcheck
        flag_FdeX = False
    except:
        pass


entrada_dados()

##s = Symbol ('s')
##t = Symbol ('t')


####--------Calculo da eq diferencial por Laplace


###Primeiramente resposta Natural1

#yn(t) é obtido considerando-se a entrada nula x(t) = 0

## PAsso numero 1, transformar x(t) do dominio do tempo para o dominio da frequência
#com a transformada de laplace
print xT
#saida_laplace,r,v = laplace_transform(eval(xT),t,s)

xS,tr1,tr2 = laplace_transform(xT,t,s,)

print type (xS)

print"Saida Laplace X(s): " +  str(xS)


                

yForcadaXs = sympify(xS/(a2*(s**2) +a1*s+a0))  


#print"YF fraction:", YFF


print "YforcadaXs: ",yForcadaXs

##yForcadaXs =decompose(yForcadaXs)
##
##print "YforcadaXs: ",type(yForcadaXs)
##yForcadaXs = yForcadaXs.pop()
##
##print "List Index:",type(yForcadaXs)

yForcadaXt = inverse_laplace_transform(yForcadaXs,s,t)

print "Resposta Forcada:" ,sympify(yForcadaXt, rational = False, evaluate = True).evalf(2)

yNaturalXs = nsimplify(((a2*s*y0 + a2*y1 + a1*y0)/(a2*(s**2) + a1*s + a0)), tolerance = 0.1)


yNaturalXt = inverse_laplace_transform(yNaturalXs,s,t)


#yNaturalxT = nsimplify((yNaturalXt),tolerance = 0.1)

print "Resposta Natural: ",sympify(yNaturalXt, rational = False, evaluate = True).evalf(2)

yCompletaXt = yNaturalXt + yForcadaXt

#yCompletaXs = simplify (yForcadaXs + yNaturalXs)

#yCompletaXt = inverse_laplace_transform(yCompletaXs,s,t)

#yCompletaXt  = nsimplify((yNaturalXt + yForcadaXt), tolerance = 0.001)

print "  Resposta Completa: ",yCompletaXt.evalf(2)











