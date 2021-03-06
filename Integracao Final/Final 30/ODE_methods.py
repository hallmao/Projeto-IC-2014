﻿
from matplotlib.figure import Figure
#from numpy.core.defchararray import decode, replace
import sympy.assumptions.handlers.calculus
import sympy.assumptions.handlers.ntheory
import sympy.assumptions.handlers.order
import sympy.assumptions.handlers.sets
from sympy import Function, exp, cos,  sympify, dsolve, symbols,mpmath, solve, lambdify, sin, im, \
        re, latex,simplify, nsimplify, expand
from sympy.abc import t, tau
import matplotlib.pyplot as plt
from numpy import array
from types import *

from sympy.mpmath import mp


###Parâmetros a serem considerados

###Precisão Decimal
prec = 2 ## Numero de digitos decimais de precisão mostrados no log de dados
#mp.dps = prec
#mp.pretty = True
C1, C2, C3, C4, C5 = symbols("C1 C2 C3 C4 C5")
flag_init = True
lingua = 1 # 1- Portugues; 2- English; 3-Espanol
##Defining our function
y = Function('y')

###Configurações do pprint, registradas somente uma vez
#setattr(pprint,'num_columns',5)
#setattr(pprint,'use_unicode',True)
#setattr(pprint,'order','none')



        #("num_columns = 100,use_unicode = True,order = 'none'")






def drange(start,stop,step):
## Funcão para criar um vetor de valores decimais,
#nativo do python só aceita valores inteirosdef seq(start, stop, step=1):
        n = int(round((stop - start)/float(step)))
        if n > 1:
                return([start + step*i for i in range(n+1)])
        else:
                return([])

# 0- Raizes; 1- Forma Natural da respsota; 2- Resposta Natural;
# 3- Resposta Particular; 4- Resposta Transitoria; 5- Respsota Forcada
# 6- Resposta Completa; 7- xT; 8- eq
Respostas = [0]*9
Respostas[0] = [0] #vetor de raizes
const_orig = [0]*6#usado para quando o usuario muda a precisao
const = [0]*6 #a0, a1, a2, a3, a4, a5   ; nessa ordem
cond_ini_orig = [0]*5 #usado para quando o usuario muda a precisao
cond_ini = [0]*5 #y0, dy0, d2y0, d3y0, d4y0     ; nessa ordem
xT = 0
#----------------------Tal - constante de tempo, para cálculo do coef de amortecimento
tal = []
maiorTal = 0#5*tal
limx_min = 0
limx_max = maiorTal
autoScale = 0
notation = 1
##a2 = None
##a1 = 0
##a0 = 0
##xT = 0
##eq = 0
##fN = 0
##rP = 0
def set_notation(n):
    global notation
    notation = n

def set_prec(p):
    global prec
    prec = p

def get_maiorTal():
    global maiorTal
    return maiorTal
def set_maiorTal(mT):
    global maiorTal
    maiorTal = mT

def set_limx_min(l_min):
    global limx_min
    limx_min = int(l_min)
def get_limx_min():
    global limx_min
    return limx_min

def set_limx_max(l_max):
    global limx_max
    limx_max = int(l_max)
    #set_xlim(right=l_max)
    #print "New limit:", respNatPlot.get_xlim()
def get_limx_max():
    global limx_max
    return limx_max

def set_autoScale(autoS):
    global autoScale
    autoScale = autoS

def get_tal():
        global tal
        return tal
def set_tal(coef):
        global tal
        tal = coef

def set_lingua(l):
    global lingua
    lingua = l

def get_lingua():
    return lingua

def set_flagInit(flagBool):

        flag_init = flagBool

def get_flagInit():
        return flag_init

def set_a5(cte):
        try:
                valid = sympify(cte)
                if(float(valid)):
                    const_orig[5] = float(valid)
        except:
                pass

        try: #para entrada = 0
               const_orig[5] = float(cte)
        except:
                pass


def set_a4(cte):
        try:
                valid = sympify(cte)
                if(float(valid)):
                    const_orig[4] = float(valid)
        except:
                pass

        try: #para entrada = 0
               const_orig[4] = float(cte)
        except:
                pass


def set_a3(cte):
        try:
                valid = sympify(cte)
                if(float(valid)):
                    const_orig[3] = float(valid)
        except:
                pass

        try: #para entrada = 0
               const_orig[3] = float(cte)
        except:
                pass


def set_a2(cte):
        try:
                valid = sympify(cte)
                if(float(valid)):
                    const_orig[2] = float(valid)
        except:
                pass

        try: #para entrada = 0
               const_orig[2] = float(cte)
        except:
                pass


def set_a1(cte):
        try:
                valid = sympify(cte)
                if(float(valid)):
                    const_orig[1] = float(valid)
        except:
                pass

        try: #para entrada = 0
               const_orig[1] = float(cte)
        except:
                pass

def set_a0(cte):
        try:
                valid = sympify(cte)
                if(float(valid)):
                    const_orig[0] = float(valid)
        except:
                pass

        try: #para entrada = 0
               const_orig[0] = float(cte)
        except:
                pass

def set_xT(expr):
        global xT
        try:
        #sympify reconhece letras como a,b,c como symbols, portanto se
        #o usuario digitar algo do tipo, o programa efetuaria o sympify
        # e daria crash. O valid transforma nossa variavel t em uma cte
        # e se conseguir transformar o valid em um float, ou seja, foi
        #digitado apenas a letra t(unica variavel valida), o programa
        # reconhece a entrada como valida
                valid = sympify(expr)
                valid = valid.subs(t,1)

                if(float(valid)):
                        Respostas [7]= xT = sympify(expr)
        except:
                pass

        try: #para entrada = 0
               Respostas[7] = xT = float(expr)
        except:
                pass



def set_y0(cte):
        try:
                valid = sympify(cte)
                if(float(valid)):
                    cond_ini_orig[0] = float(valid)
        except:
                pass

        try: #para entrada = 0
               cond_ini_orig[0] = float(cte)
        except:
                pass

def set_dy0(cte):
        try:
                valid = sympify(cte)
                if(float(valid)):
                    cond_ini_orig[1] = float(valid)
        except:
                pass

        try: #para entrada = 0
               cond_ini_orig[1] = float(cte)
        except:
                pass

def set_d2y0(cte):
        try:
                valid = sympify(cte)
                if(float(valid)):
                    cond_ini_orig[2] = float(valid)
        except:
                pass

        try: #para entrada = 0
               cond_ini_orig[2] = float(cte)
        except:
                pass

def set_d3y0(cte):
        try:
                valid = sympify(cte)
                if(float(valid)):
                    cond_ini_orig[3] = float(valid)
        except:
                pass

        try: #para entrada = 0
               cond_ini_orig[3] = float(cte)
        except:
                pass

def set_d4y0(cte):
        try:
                valid = sympify(cte)
                if(float(valid)):
                    cond_ini_orig[4] = float(valid)
        except:
                pass

        try: #para entrada = 0
               cond_ini_orig[4] = float(cte)
        except:
                pass

def get_xT():
        global xT
        return xT



##Entrada pelo console
##def input_coefs():
##                pass
##                print "Insira os coefs e entrada para uma EDO do tipo: "
##                print "a5*y'''''(t) + a4*y''''(t) + a3*y'''(t)  + a2*y''(t) +a1*y'(t) +a0*y(t) = x(t)"
##                #a5 = input("a5:")
##                #a4 = input("a4:")
##                #a3 = input("a3:")
##                a2 = input("a2:")
##                a1 = input("a1:")
##                a0 = input("a0:")
##                xT = input("x(t):")
##                try:
##                        xT = float(expr)
##                except:
##                        pass
##                ##terceira a quinta ordem desativados
##                a5 = a4 = a3 = 0
##                return a5, a4, a3, a2, a1, a0, xT
def init(a5, a4, a3, a2, a1, a0, xT, y0, dy0, d2y0, d3y0, d4y0):

        set_xT(xT)
        set_a0(a0)
        set_a1(a1)
        set_a2(a2)
        set_a3(a3)
        set_a4(a4)
        set_a5(a5)
        set_y0(y0)
        set_dy0(dy0)
        set_d2y0(d2y0)
        set_d3y0(d3y0)
        set_d4y0(d4y0)
        Respostas[7] = get_xT()
        edo_main()


def  evaluate_roots(roots):

        #print "Metodo Evaluate Roots"

        #print roots,len(roots)

        RaizesC = [0]*len(roots)
        RaizesR = [0]*len(roots)
        output  = [0]*len(roots)

        for i in range(len(roots)):

                #print "for loop",i

                RaizesC[i] = round(im(roots[i]),prec)
                RaizesR[i] = round(re(roots[i]),prec)
                #print RaizesR[i]
               # print RaizesC[i]

                if RaizesC[i] != 0 and RaizesR[i] != 0:

                        ratio  = 0

                        ratio = abs(RaizesC[i]/RaizesR[i])
                        flagRatio = False


                        #print "Ratio: ",ratio


                        if ratio <  (1.0/100):
                                #print "Parte complexa ignorada"

                                output[i] = complex(RaizesR[i],0)


                        elif ratio > 100:
                                #print "Parte real ignorada"

                                output[i] = complex(0,RaizesC[i])
                        else:
                                #print "Only output"
                                if RaizesR[i] == 0:
                                        output[i] = complex(0,RaizesC[i])
                                if RaizesC[i] == 0:
                                        output[i] = RaizesR[i]
                                else:
                                        output[i] = complex(RaizesR[i],RaizesC[i])

                else:
                  #print "Only output"
                        if RaizesR[i] == 0:
                                output[i] = complex(0,RaizesC[i])
                        if RaizesC[i] == 0:
                                output[i] =RaizesR[i]
                        else:
                                output[i] = complex(RaizesR[i],RaizesC[i])
        #print "Raizes ---:",output
        #print "------------------------------------------------"
        return output


def raizes():
                #polyroots retorna uma lista
                if(const[5] != 0):
                                roots = mpmath.polyroots([const[5], const[4], const[3], const[2], const[1], const[0]])
                           # print roots[0], roots[1], roots[2], roots[3], roots[4]
                elif((const[5] == 0) and (const[4] !=0)):
                                roots = mpmath.polyroots([const[4], const[3], const[2], const[1], const[0]])
                           # print roots[0], roots[1], roots[2], roots[3]
                elif((const[4] == 0) and (const[3] !=0)):
                                roots = mpmath.polyroots([const[3], const[2], const[1], const[0]])
                           # print roots[0], roots[1], roots[2]
                elif((const[3] == 0) and (const[2] !=0)):
                                roots = mpmath.polyroots([const[2], const[1], const[0]])
                           # print roots[0], roots[1]
                elif((const[2] == 0) and (const[1] !=0)):
                                roots = mpmath.polyroots([const[1], const[0]])
                           # print roots[0]

                Respostas[0] = evaluate_roots(roots)


def cte_tempo():
                global tal, maiorTal, limx_max, limx_min
                #--------------Implementação----TAL -----------------------------
                plotRaizesT = (Respostas[0])
                plotRaizesR = [0]*len(plotRaizesT)
                for i in range(len(plotRaizesT)):
                    plotRaizesR[i] = re(plotRaizesT[i])

                plotRaizesR.sort()
                # Define o vetor de tal e inverte todas as raizes  reais
                tal = [None]*len(plotRaizesR)

                for i in range(len(plotRaizesR)):
                        if plotRaizesR[i] != 0:
                                temp   = abs(plotRaizesR[i])
                                tal[i] = float(temp**-1)
                                if tal[i] >= 1000:
                                        tal[i] = 100



                        else:
                                tal[i] = 1.0
                #Define qual o maior valor de tal e aloca este valor em talMaior
                tal.sort()
                for i in range(len(tal)):
                    tal[i] = round(tal[i],prec)
                ##----Pega o maior valor de tal e calcula o coef de amortecimento
                maiorTal = int(5*tal[-1])
                if maiorTal > 100e3:
                        maiorTal = int(maiorTal/100e5)
                #print "Raizes, reais inversas  (tal)",tal
                #print "5 Tal = ",int(maiorTal)
                limx_min = 0
                limx_max = maiorTal


def conds_iniciais_aplicadas(fN, rP):

                #print "Favor inserir as conds iniciais y(0) e y'(0)...:"

                ##Verificando a ordem da EDO para se ter o numero correto de conds Iniciais e
                #uma resolução própria

                #Ordem 1
                if ((const[5] == 0) and (const[4] == 0)
                   and (const[3] == 0) and (const[2] == 0)):
                                #Entrada cond inicial:
                                y0 = cond_ini[0]
                                ##Resolução para se obter o valor da constante C1:

                                #Aplicando t = 0 em y(t)
                                fNt0 = fN.subs(t,0)
                                #print "Valor de fN com t = 0:",fNt0
                                ##Resolvendo o sistema para se obter o valor da constante C1
                                valorConstantes = solve(fNt0 - y0)
                                #print "Valor de C1: ",valorConstantes,type(valorConstantes)



                                ##Agora a resposta natural, com o C1 encontrado na substituição aplicado na funcão natural:
                                nC1 = valorConstantes.pop()

                                respNatural = fN.subs(C1,nC1)#.evalf(prec)
                                Respostas[2] = respNatural #Adiciona Resposta Natural na lista de respostas

                                ##Tenta resolver parâmetros não terminados, se possível



                                ##Saida da Resposta Natural no console
                                #print "Resposta Natural:"
                                #pprint(respNatural)

                                if(Respostas[7] != 0):    #Eq. nao homogenea
                                                yt = fN + rP #Yt(t) = Yfn(t) + Yp
                                                #, rational = False,evaluate= False)#.evalf(prec)
                                                yt0 = yt.subs(t, 0) #Aplicando as condicoes iniciais; Ytrans(0)

                                                #c1 eh o valor de C1
                                                #solve(eq, var); eq=equacao a ser resolvida; var=variavel que se quer achar
                                                #solve iguala a equacao a 0, portanto, yt0 - y0 = 0 => yt0 = y0
                                                valorConstantes = solve(yt0 - y0) #solve retorna um dictionary(hash)
                                                tC1 = valorConstantes.pop()           #com keys C1
                                                respTrans = yt.subs(C1, tC1)
                                                Respostas[4] = respTrans #Adiciona Resposta Transitoria a lista de respostas

                                                #print "Resposta Transitoria:"
                                                #pprint(respTrans)
                                else:
                                    Respostas[4] = 0



                #Ordem 2
                elif ((const[5] == 0) and (const[4] == 0)
                   and (const[3] == 0)):
                                y0 = cond_ini[0]
                                dy0 = cond_ini[1]

                                ##Primeiramente a resposta Natural
                                ##Solucao geral é : formaNat
                                #antes de aplicar as conds iniciais é necessário ter y'(t) e y(t) da resp natural

                                #Forma natural é derivada uma vez
                                ylinhaNat = fN.diff(t)
                                formaNatural  = fN
                                #print"yLinhaNat:", ylinhaNat

                                ## Agora é necessário resolver o sistema:
                                #  ynat(t) = y(0)
                                #  ynat'(0)= y'(0)
                                #print "Valor das constantes com t",valorConstantes
                                ### Agora com os valores em t = 0  para y'(t)  e y(t), substituindo:
                                ylinhaNat    = ylinhaNat.subs(t,0)
                                formaNatural = formaNatural.subs(t,0)

                                #print "YlinhaNat em t = 0: ",ylinhaNat
                                #print "Forma Natural em t = 0: ",formaNatural
                                ##Resolvendo o sistema:
                                valorConstantes = solve([formaNatural -y0,ylinhaNat -dy0])
                                #print type(valorConstantes)
                                #print "Constantes C1 e C2: ",valorConstantes
                                ### Agora a resposta natural com as constantes encontradase aplicadas na funcão natural:
                                nC1 = valorConstantes[C1]
                                nC2     = valorConstantes[C2]
                                #print "Valor de C1 e C2:",nC1,nC2

                                respNatural = fN.subs([(C1,nC1),(C2,nC2)])#.evalf(prec)
                                Respostas[2] = respNatural #Adiciona Resposta Natural na lista de respostas

                                ##Tenta resolver parâmetros não terminados, se possível


                                #print "Resposta Natural:"
                                #pprint(respNatural)

                                if(Respostas[7] != 0): #Eq. nao homogenea
                                                yt = fN + rP #Yt(t) = Yfn(t) + Yp

                                                #Resposta Transitoria é derivada uma vez
                                                ylinhaTran = yt.diff(t) #)
                                                #print"yLinhaTran:", ylinhaTran

                                                ## Agora é necessário resolver o sistema:
                                                #  ytran(0) = y(0)
                                                #  ytran'(0)= y'(0)
                                                #print "Valor das constantes com t",valorConstantes
                                                ### Agora com os valores em t = 0  para y'(t)  e y(t), substituindo:
                                                ylinhaTran    = ylinhaTran.subs(t,0)
                                                yt0 = yt.subs(t,0)

                                                #print "YlinhaTran em t = 0: ",ylinhaNTran
                                                #print "Resposta Transitoria em t = 0: ",yt0
                                                ##Resolvendo o sistema:
                                                valorConstantes = solve([yt0 -y0,ylinhaTran -dy0])
                                                #print type(valorConstantes)
                                                #print "Constantes C1 e C2: ",valorConstantes
                                                ### Agora a resposta transitoria com as constantes encontradase aplicadas na funcão natural:
                                                tC1 = valorConstantes[C1]
                                                tC2     = valorConstantes[C2]
                                                #print "Valor de C1 e C2:",tC1,tC2

                                                respTrans = yt.subs([(C1,tC1),(C2,tC2)])#.evalf(prec)
                                                Respostas[4] = respTrans#.evalf(prec) #Adiciona Resposta Transitoria a lista de respostas
                                                #print "Respsota Transitoria:"
                                                #pprint(respTrans)
                                else:
                                    Respostas[4] = 0



                #Ordem 3
                elif ((const[5] == 0) and (const[4] == 0)):
                                y0 = cond_ini[0]
                                dy0 = cond_ini[1]
                                d2y0 = cond_ini[2]


                                ##Primeiramente a resposta Natural
                                ##Solucao geral é : formaNat
                                #antes de aplicar as conds iniciais é necessário ter y''(t) y'(t) e y(t) da resp natural

                                #Forma natural é derivada a primeira e à segunda
                                y2linhaNat = sympify(fN.diff(t,2))
                                ylinhaNat = sympify(fN.diff(t))
                                formaNatural  = fN
                                #print"yLinhaTran:", ylinhaTran

                                ## Agora é necessário resolver o sistema:
                                #  ynat(t) = y(0)
                                #  ynat'(0)= y'(0)
                                # ynat''(0) = y''(0)
                                #print "Valor das constantes com t",valorConstantes
                                ### Agora com os valores em t = 0  para y'(t)  e y(t), substituindo:
                                y2linhaNat   = y2linhaNat.subs(t,0)
                                ylinhaNat    = ylinhaNat.subs(t,0)
                                formaNatural = formaNatural.subs(t,0)

                                #print "YlinhaNat em t = 0: ",ylinhaNat
                                #print "Forma Natural em t = 0: ",formaNatural
                                ##Resolvendo o sistema:
                                valorConstantes = solve([formaNatural -y0,ylinhaNat -dy0,y2linhaNat-d2y0])
                                #print type(valorConstantes)
                                #print "Constantes C1  C2 e C3: ",valorConstantes
                                ### Agora a resposta natural com as constantes encontradase aplicadas na funcão natural:
                           # print valorConstantes
                                nC1 = valorConstantes[C1]
                                nC2     = valorConstantes[C2]
                                nC3 = valorConstantes[C3]
                                #print "Valor de C1 e C2:",nC1,nC2

                                respNatural = fN.subs([(C1,nC1),(C2,nC2),(C3,nC3)])#.evalf(prec)
                                Respostas[2] = respNatural #Adiciona Resposta Natural na lista de respostas

                                ##Tenta resolver parâmetros não terminados, se possível


                                #print "Resposta Natural:"
                                #pprint(respNatural)


                                if(Respostas[7] != 0): #Eq. nao homogenea
                                                yt = fN + rP #Yt(t) = Yfn(t) + Yp

                                                #Resposta Transitoria é derivada a primeira e à segunda
                                                y2linhaTran = sympify(yt.diff(t,2)  ) #, rational = False, evaluate = False).evalf(prec)
                                                ylinhaTran = sympify(yt.diff(t) )##, rational = False, evaluate = False).evalf(prec)
                                                #yt  = sympify(yt, rational = False,evaluate= False).evalf(prec)
                                                #print"yLinhaTran:", ylinhaTran

                                                ## Agora é necessário resolver o sistema:
                                                #  ytran(t) = y(0)
                                                #  ytran'(0)= y'(0)
                                                #  ytran''(0) = y''(0)
                                                #print "Valor das constantes com t",valorConstantes
                                                ### Agora com os valores em t = 0  para y'(t)  e y(t), substituindo:
                                                y2linhaTran   = y2linhaTran.subs(t,0)
                                                ylinhaTran    = ylinhaTran.subs(t,0)
                                                yt0 = yt.subs(t,0)

                                                #print "YlinhaTran em t = 0: ",ylinhaTran
                                                #print "Resposta Transitoria em t = 0: ",yt0
                                                ##Resolvendo o sistema:
                                                valorConstantes = solve([yt0 -y0,ylinhaTran -dy0,y2linhaTran-d2y0])
                                                #print type(valorConstantes)
                                                #print "Constantes C1  C2 e C3: ",valorConstantes
                                                ### Agora a resposta transitoria com as constantes encontradase aplicadas na funcão natural:
                                                #print valorConstantes
                                                tC1 = valorConstantes[C1]
                                                tC2     = valorConstantes[C2]
                                                tC3 = valorConstantes[C3]
                                                #print "Valor de C1 e C2:",nC1,nC2

                                                respTrans = yt.subs([(C1,tC1),(C2,tC2),(C3,tC3)])#.evalf(prec)
                                                Respostas[4] = respTrans #Adiciona Resposta Transitoria a lista de respostas

                                                #print "Respsota Transitoria:"
                                           # pprint(respTrans)
                                else:
                                    Respostas[4] = 0


                #Ordem 4
                elif ((const[5] == 0)):
                                y0 = cond_ini[0]
                                dy0 = cond_ini[1]
                                d2y0 = cond_ini[2]
                                d3y0 = cond_ini[3]


                                ##Primeiramente a resposta Natural
                                ##Solucao geral é : formaNat
                                #antes de aplicar as conds iniciais é necessário ter  y'''(t) y''(t) y'(t) e y(t) da resp natural

                                #Forma natural é derivada a primeira , segunda e terceira
                                y3linhaNat = sympify(fN.diff(t,3)) #, rational = False, evaluate = False).evalf(prec)
                                y2linhaNat = sympify(fN.diff(t,2)) #, rational = False, evaluate = False).evalf(prec)
                                ylinhaNat = sympify(fN.diff(t))# , rational = False, evaluate = False).evalf(prec)
                                formaNatural  = fN#, rational = False,evaluate= False).evalf(prec)
                                #print"yLinhaNat:", ylinhaNat

                                ## Agora é necessário resolver o sistema:
                                #  ynat(t) = y(0)
                                #  ynat'(0)= y'(0)
                                # ynat''(0) = y''(0)
                                #ynat'''(0) = y'''(0)
                                #print "Valor das constantes com t",valorConstantes
                                ### Agora com os valores em t = 0  para conds iniciais, substituindo:
                                y3linhaNat   = y3linhaNat.subs(t,0)
                                y2linhaNat   = y2linhaNat.subs(t,0)
                                ylinhaNat    = ylinhaNat.subs(t,0)
                                formaNatural = formaNatural.subs(t,0)

                                #print "YlinhaNat em t = 0: ",ylinhaNat
                                #print "Forma Natural em t = 0: ",formaNatural
                                ##Resolvendo o sistema:
                                valorConstantes = solve([formaNatural -y0, ylinhaNat -dy0 , y2linhaNat-d2y0 , y3linhaNat-d3y0])
                                #print type(valorConstantes)
                                #print "Constantes C1  C2 e C3: ",valorConstantes
                                ### Agora a resposta natural com as constantes encontradase aplicadas na funcão natural:
                                nC1 = valorConstantes[C1]
                                nC2     = valorConstantes[C2]
                                nC3 = valorConstantes[C3]
                                nC4 = valorConstantes[C4]
                                #print "Valor de C1 e C2:",nC1,nC2

                                respNatural = fN.subs([(C1,nC1),(C2,nC2),(C3,nC3),(C4,nC4)])#.evalf(prec)
                                Respostas[2] = respNatural #Adiciona Resposta Natural na lista de respostas

                           # print "Resposta Natural:"
                                #pprint(respNatural)

                                if(Respostas[7] != 0): #Eq. nao homogenea
                                                yt = fN + rP #Yt(t) = Yfn(t) + Yp

                                                #Resposta Transitoria é derivada a primeira , segunda e terceira
                                                y3linhaTran = sympify(yt.diff(t,3))#, rational = False, evaluate = False).evalf(prec)
                                                y2linhaTran = sympify(yt.diff(t,2))#, rational = False, evaluate = False).evalf(prec)
                                                ylinhaTran = sympify(yt.diff(t))#, rational = False, evaluate = False).evalf(prec)
                                                #yt = sympify(yt, rational = False,evaluate= False).evalf(prec)
                                                #print"yLinhaNTran:", ylinhaTran

                                                ## Agora é necessário resolver o sistema:
                                                #  ytran(t) = y(0)
                                                #  ytran'(0)= y'(0)
                                                # ytran''(0) = y''(0)
                                                #ytran'''(0) = y'''(0)
                                                #print "Valor das constantes com t",valorConstantes
                                                ### Agora com os valores em t = 0  para conds iniciais, substituindo:
                                                y3linhaTran   = y3linhaTran.subs(t,0)
                                                y2linhaTran   = y2linhaTran.subs(t,0)
                                                ylinhaTran    = ylinhaTran.subs(t,0)
                                                yt0 = yt.subs(t,0)

                                                #print "YlinhaTran em t = 0: ",ylinhaTran
                                                #print "Resposta Transitoria em t = 0: ",yt0
                                                ##Resolvendo o sistema:
                                                valorConstantes = solve([yt0 -y0, ylinhaNat -dy0 , y2linhaTran-d2y0 , y3linhaTran-d3y0])
                                                #print type(valorConstantes)
                                                #print "Constantes C1  C2 e C3: ",valorConstantes
                                                ### Agora a resposta transitoria com as constantes encontradase aplicadas na funcão natural:
                                                tC1 = valorConstantes[C1]
                                                tC2     = valorConstantes[C2]
                                                tC3 = valorConstantes[C3]
                                                tC4 = valorConstantes[C4]
                                                #print "Valor de C1 e C2:",tC1,tC2

                                                respTrans = yt.subs([(C1,tC1),(C2,tC2),(C3,tC3),(C4,tC4)])#.evalf(prec)
                                                Respostas[4] = respTrans #Adiciona Resposta Transitoria a lista de respostas

                                                #print "Respsota Transitoria:"
                                           # pprint(respTrans)
                                else:
                                    Respostas[4] = 0


                #Ordem 5
                else:
                                y0 = cond_ini[0]
                                dy0 = cond_ini[1]
                                d2y0 = cond_ini[2]
                                d3y0 = cond_ini[3]
                                d4y0 = cond_ini[4]

                                ##Primeiramente a resposta Natural
                                ##Solucao geral é : formaNat
                                #antes de aplicar as conds iniciais é necessário ter y''''(t)  y'''(t) y''(t) y'(t) e y(t) da resp natural

                                #Forma natural é derivada a primeira , segunda, terceira e quarta
                                y4linhaNat = sympify(fN.diff(t,4))#, rational = False, evaluate = False).evalf(prec)
                                y3linhaNat = sympify(fN.diff(t,3))#, rational = False, evaluate = False).evalf(prec)
                                y2linhaNat = sympify(fN.diff(t,2))#, rational = False, evaluate = False).evalf(prec)
                                ylinhaNat = sympify(fN.diff(t))#, rational = False, evaluate = False).evalf(prec)
                                formaNatural  = fN#, rational = False,evaluate= False).evalf(prec)
                                #print"yLinhaNat:", ylinhaNat

                                ## Agora é necessário resolver o sistema:
                                #  ynat(t) = y(0)
                                #  ynat'(0)= y'(0)
                                # ynat''(0) = y''(0)
                                #ynat'''(0) = y'''(0)
                                #ynat''''(0) = y''''(0)
                                #print "Valor das constantes com t",valorConstantes
                                ### Agora com os valores em t = 0  para conds iniciais, substituindo:
                                y4linhaNat   = y4linhaNat.subs(t,0)
                                y3linhaNat   = y3linhaNat.subs(t,0)
                                y2linhaNat   = y2linhaNat.subs(t,0)
                                ylinhaNat    = ylinhaNat.subs(t,0)
                                formaNatural = formaNatural.subs(t,0)

                                #print "YlinhaNat em t = 0: ",ylinhaNat
                                #print "Forma Natural em t = 0: ",formaNatural
                                ##Resolvendo o sistema:
                                valorConstantes = solve([formaNatural -y0, ylinhaNat -dy0 , y2linhaNat-d2y0 , y3linhaNat-d3y0,  y4linhaNat - d4y0])
                           #print type(valorConstantes)
                                #print "Constantes C1  C2 e C3: ",valorConstantes
                                ### Agora a resposta natural com as constantes encontradase aplicadas na funcão natural:
                                nC1 = valorConstantes[C1]
                                nC2     = valorConstantes[C2]
                                nC3 = valorConstantes[C3]
                                nC4 = valorConstantes[C4]
                                nC5 = valorConstantes[C5]
                                #print "Valor de C1 e C2:",nC1,nC2

                                respNatural = fN.subs([(C1,nC1),(C2,nC2),(C3,nC3),(C4,nC4),(C5,nC5)])#.evalf(prec)
                                Respostas[2] = respNatural #Adiciona Resposta Natural na lista de respostas

                           # print "Resposta Natural:"
                           # pprint(respNatural)

                                if(Respostas[7] != 0): #Eq. nao homogenea
                                                yt = fN + rP #Yt(t) = Yfn(t) + Yp

                                                #Resposta transitoria é derivada a primeira , segunda, terceira e quarta
                                                y4linhaTran = sympify(yt.diff(t,4))#, rational = False, evaluate = False).evalf(prec)
                                                y3linhaTran = sympify(yt.diff(t,3))#, rational = False, evaluate = False).evalf(prec)
                                                y2linhaTran = sympify(yt.diff(t,2))#, rational = False, evaluate = False).evalf(prec)
                                                ylinhaTran = sympify(yt.diff(t))#, rational = False, evaluate = False).evalf(prec)
                                               # yt  = sympify(yt, rational = False,evaluate= False).evalf(prec)
                                                #print"yLinhaTran:", ylinhaTran

                                                ## Agora é necessário resolver o sistema:
                                                #  ytran(t) = y(0)
                                                #  ytran'(0)= y'(0)
                                                # ytran''(0) = y''(0)
                                                #ytran'''(0) = y'''(0)
                                                #ytran''''(0) = y''''(0)
                                                #print "Valor das constantes com t",valorConstantes
                                                ### Agora com os valores em t = 0  para conds iniciais, substituindo:
                                                y4linhaTran   = y4linhaTran.subs(t,0)
                                                y3linhaTran   = y3linhaTran.subs(t,0)
                                                y2linhaTran   = y2linhaTran.subs(t,0)
                                                ylinhaTran    = ylinhaTran.subs(t,0)
                                                yt0 = yt.subs(t,0)

                                                #print "YlinhaTran em t = 0: ",ylinhaTran
                                                #print "Forma Natural em t = 0: ",yt0
                                                ##Resolvendo o sistema:
                                                valorConstantes = solve([yt0 -y0, ylinhaTran -dy0 , y2linhaTran-d2y0 , y3linhaTran-d3y0,  y4linhaTran - d4y0])
                                                #print type(valorConstantes)
                                                #print "Constantes C1  C2 e C3: ",valorConstantes
                                                ### Agora a resposta transitoria com as constantes encontradase aplicadas na funcão natural:
                                                tC1 = valorConstantes[C1]
                                                tC2 = valorConstantes[C2]
                                                tC3 = valorConstantes[C3]
                                                tC4 = valorConstantes[C4]
                                                tC5 = valorConstantes[C5]
                                                #print "Valor de C1 e C2:",tC1,tC2

                                                respTrans = yt.subs([(C1,tC1),(C2,tC2),(C3,tC3),(C4,tC4),(C5,tC5)])#.evalf(prec)
                                                Respostas[4] = respTrans #Adiciona Resposta Transitoria a lista de respostas

                                                #print "Respsota Transitoria:"
                                                #pprint(respTrans)
                                else:
                                    Respostas[4] = 0



                #print "Valor das constantes com t = 0",valorConstantesT0


def idioma_log_print():
    global lingua

    if(lingua==1):
        idi_eq = u"Equação diferencial: "
        idi_hom = u"Equação homogênea: "
        idi_car = u"Equação característica: "
        if(len(Respostas[0])==1):
            idi_raiz = "Raiz: "
        else:
            idi_raiz = u"Raízes: "
        if(len(tal)==1):
            idi_tal = "Constante de tempo: "
        else:
            idi_tal = "Constantes de tempo: "
        idi_yfn = "Forma natural de resposta: Yfn(t) = "
        idi_yn = "Resposta natural: Ynat(t) = "
        idi_yp = "Resposta particular: Ypart(t) = "
        idi_ytrans = u"Resposta transitória: Ytrans(t) = "
        idi_yf = u"Resposta forçada: Yforc(t) = "
        idi_yc = "Resposta completa: Yc(t) = "
        idi_cond_sing = u"Condição inicial:  "
        idi_cond_pl = u"Condições iniciais:  "
        return idi_eq, idi_hom, idi_car, idi_raiz, idi_tal, idi_yfn, idi_yn, idi_yp, idi_ytrans, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl

    elif(lingua==2):
        idi_eq = "Differential equation: "
        idi_hom = "Homogeneous\ Equation: "
        idi_car = "Characteristic Equation: "
        if(len(Respostas[0])==1):
            idi_raiz = "Root: "
        else:
            idi_raiz = "Roots: "
        if(len(tal)==1):
            idi_tal = "Time constant: "
        else:
            idi_tal = "Time constants: "
        idi_yfn = "Complementary solution: Ycomplementary(t) = "
        idi_yn = "Natural response: Ynat(t) = "
        idi_yp = "Particular solution: Ypart(t) = "
        idi_ytrans = "Transient solution: Ytrans(t) = "
        idi_yf = "Forced response: Yforc(t) = "
        idi_yc = "Complete solution: Yc(t) = "
        idi_cond_sing = "Initial condition:  "
        idi_cond_pl = "Initial conditions:  "
        return idi_eq, idi_hom, idi_car, idi_raiz, idi_tal, idi_yfn, idi_yn, idi_yp, idi_ytrans, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl

    else:
        idi_eq = u"Ecuación diferencial: "
        idi_hom = u"Ecuación homogénea: "
        idi_car = u"Ecuación característica: "
        if(len(Respostas[0])==1):
            idi_raiz = u"Raíz: "
        else:
            idi_raiz = u"Raíces: "
        if(len(tal)==1):
            idi_tal = "Constante de tiempo: "
        else:
            idi_tal = "Constantes de tiempo: "
        idi_yfn = u"Solución general: Ygen(t) = "
        idi_yn = "Respuesta natural: Ynat(t) = "
        idi_yp = u"Solución particular: Ypart(t) = "
        idi_ytrans = "Respuesta transitoria: Ytrans(t) = "
        idi_yf = "Respuesta forzada: Yforz(t) = "
        idi_yc = "Respuesta completa: Yc(t) = "
        idi_cond_sing = u"Condición inicial:  "
        idi_cond_pl = "Condiciones iniciales:  "
        return idi_eq, idi_hom, idi_car, idi_raiz, idi_tal, idi_yfn, idi_yn, idi_yp, idi_ytrans, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl

def log_print():

        idi_eq, idi_hom, idi_car, idi_raiz, idi_tal, idi_yfn, idi_yn, idi_yp, idi_ytrans, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl = idioma_log_print()

        str_const=[str(const[0]), str(const[1]), str(const[2]), str(const[3]), str(const[4]), str(const[5])]

        for i in range(len(const)):
            if(const[i]>0):
                str_const[i] = "+"+str_const[i]

        # equacao = Respostas[8] + Respostas[7]
        # equacao = equacao.subs("Derivative(y(t), t)","dy(t)")
        # equacao = equacao.subs("Derivative(dy(t), t)","d2y(t)")
        # equacao = equacao.subs("Derivative(d2y(t), t)","d3y(t)")
        # equacao = equacao.subs("Derivative(d3y(t), t)","d4y(t)")
        # equacao = equacao.subs("Derivative(d4y(t), t)","d5y(t)")


        str_eq = ""
        if(const[0] != 0):
            str_eq = str_const[0]+"*y(t) "
        if(const[1] != 0):
            str_eq = str_const[1]+"*dy(t) "+str_eq
        if(const[2] != 0):
            str_eq = str_const[2]+"*d2y(t) "+str_eq
        if(const[3] != 0):
            str_eq = str_const[3]+"*d3y(t) "+str_eq
        if(const[4] != 0):
            str_eq = str_const[4]+"*d4y(t) "+str_eq
        if(const[5] != 0):
            str_eq = str_const[5]+"*d5y(t) "+str_eq

        if(str_eq[0]=="+"):
            str_eq = str_eq[1:] #exclui o primeiro caractere da string

        eqCar = str_eq

        #equacao = str(equacao)
        eqGer = idi_eq+str_eq+" = "+str(Respostas[7])
        #print equacao
        str_xT = "x(t) = "
        str_xT = str_xT+"( "+str(Respostas[7])+" )*u(t)"

        eqHom = idi_hom+str_eq+" = 0"

        eqCar = eqCar.replace("d5y(t)","r**(5)")
        eqCar = eqCar.replace("d4y(t)","r**(4)")
        eqCar = eqCar.replace("d3y(t)","r**(3)")
        eqCar = eqCar.replace("d2y(t)","r**(2)")
        eqCar = eqCar.replace("dy(t)","r")
        eqCar = eqCar.replace("*y(t)","")
        eqCar = idi_car+eqCar+" = 0"



        str_raiz = idi_raiz
        count = 0
        if(len(Respostas[0])==1):
            str_raiz = idi_raiz
            str_raiz = str_raiz+" r = "+str(Respostas[0][0])
        else:
            while(count < len(Respostas[0])):
                    str_raiz = str_raiz+"    "+"r"+str(count+1)+"= "+str(Respostas[0][count])
                    count = count+ 1
        str_tal = idi_tal
        count=0
        if(len(tal)==1):
            str_tal = idi_tal
            str_tal = str_tal+"tau = "+str(tal[0])
        else:
            while(count < len(tal)):
                    str_tal = str_tal+"    "+"tau"+str(count+1)+"= "+str(tal[count])
                    count = count+ 1

        #print str_raiz

        str_yfn = idi_yfn+"( "+str(Respostas[1])+" )*u(t)"
        #print str_yfn

        str_yn = idi_yn+"( "+str(Respostas[2])+" )*u(t)"
        #print str_yn

        if(Respostas[7] != 0):
            str_yp = idi_yp+"( "+str(Respostas[3])+" )*u(t)\n"
            #print str_yp

            str_ytrans = idi_ytrans+"( "+str(Respostas[4])+" )*u(t)\n"
            #print str_ytrans

            str_yforc = idi_yf+"( "+str(Respostas[5])+" )*u(t)\n"
            #print str_yforc
        else:
            str_yp = ""
            str_ytrans = ""
            str_yforc = ""

        str_yc = idi_yc+"( "+str(Respostas[6])+" )*u(t)"
        #print str_yc

        str_cond_ini = ""
        if((const[5] == 0) and (const[4] == 0) and (const[3] == 0) and (const[2]==0)):#eq ordem 1
            str_cond_ini = idi_cond_sing+"y(0) = "+str(cond_ini[0])
        elif ((const[5] == 0) and (const[4] == 0) and (const[3] == 0)):#eq ordem 2
            str_cond_ini = idi_cond_pl+"y(0) = "+str(cond_ini[0])
            str_cond_ini = str_cond_ini+"    dy(0) = "+str(cond_ini[1])
        elif ((const[5] == 0) and (const[4] == 0)):#eq ordem 3
            str_cond_ini = idi_cond_pl+"y(0) = "+str(cond_ini[0])
            str_cond_ini = str_cond_ini+"    dy(0) = "+str(cond_ini[1])
            str_cond_ini = str_cond_ini+"    d2y(0) = "+str(cond_ini[2])
        elif ((const[5] == 0)):#eq ordem 4
            str_cond_ini = idi_cond_pl+"y(0) = "+str(cond_ini[0])
            str_cond_ini = str_cond_ini+"    dy(0) = "+str(cond_ini[1])
            str_cond_ini = str_cond_ini+"    d2y(0) = "+str(cond_ini[2])
            str_cond_ini = str_cond_ini+"    d3y(0) = "+str(cond_ini[3])
        else:#eq ordem 5
            str_cond_ini = idi_cond_pl+"y(0) = "+str(cond_ini[0])
            str_cond_ini = str_cond_ini+"    dy(0) = "+str(cond_ini[1])
            str_cond_ini = str_cond_ini+"    d2y(0) = "+str(cond_ini[2])
            str_cond_ini = str_cond_ini+"    d3y(0) = "+str(cond_ini[3])
            str_cond_ini = str_cond_ini+"    d4y(0) = "+str(cond_ini[4])


        str_resp = eqGer+"\n"+eqHom+"\n"+eqCar+"\n"+str_raiz+"\n"+str_tal+"\n"+str_yfn+"\n"+str_cond_ini+"\n"+str_yn+"\n"+str_xT+"\n"+str_yp+str_ytrans+str_yforc+str_yc
        #print str_resp

        #return c tds as respostas em uma variavel
        return str_resp

        ##return c cada resposta sendo uma variavel
        #return equacao, str_raiz, str_yfn, str_yn, str_yp, str_ytrans, str_yforc, str_yc


def conversao_numpy(symbol):
        ###Transforma todas as respostas em funcoes Lambda
        #Compativeis de forma nativa no python e sem a necessidade de bibliotecas externas
        ##Array with same length as Respostas variable
        plots_numpy = [0]*len(Respostas)

### SIM SIM EU SEI USA UMA ITERACAO AKA FOR, mas ai...
## quem é que vai entender isso mês que vem ?
        ##Entrada x(t)
        plots_numpy[1] = lambdify(t,sympify(Respostas[7]))
##RespostaNatural
        plots_numpy[2] = lambdify(t,Respostas[2])
##Resposta Particular
        plots_numpy[3] = lambdify(t,Respostas[3])
#Resposta Transitoria
        plots_numpy[4] = lambdify(t,Respostas[4])
#Resposta Forcada
        plots_numpy[5] = lambdify(t,Respostas[5])
##Resposta Completa
        plots_numpy[6] = lambdify(t,Respostas[6])

        #print "plots Numpy",plots_numpy
        return plots_numpy

def idioma_show_plots():
    global lingua, tal

    if(lingua==1):
        idi_amp = "Amplitude"
        idi_yn = "Ynat(t)"
        idi_plot_raiz = u"Mapa de raízes da equação característica"
        if(len(Respostas[0])==1):
            idi_raiz = "Raiz"
        else:
            idi_raiz = u"Raízes"
        if(len(tal)==1):
            idi_tal = "Constante de tempo: "
        else:
            idi_tal = "Constantes de tempo: "
        idi_real = "Real"
        idi_imag = u"Imaginário"
        idi_yp = "Ypart(t)"
        idi_yt = "Ytrans(t)"
        idi_yf = "Yforc(t)"
        idi_yc = "Yc(t)"
        return idi_amp, idi_yn, idi_raiz, idi_tal, idi_real, idi_imag, idi_yp, idi_yt, idi_yf, idi_yc, idi_plot_raiz

    elif(lingua==2):
        idi_amp = "Amplitude"
        idi_yn = "Ynat(t)"
        idi_plot_raiz =  "Characteristic equation roots mapping"
        if(len(Respostas[0])==1):
            idi_raiz = "Root"
        else:
            idi_raiz = "Roots"
        if(len(tal)==1):
            idi_tal = "Time constant: "
        else:
            idi_tal = "Time constants: "
        idi_real = "Real"
        idi_imag = "Imaginary"
        idi_yp = "Ypart(t)"
        idi_yt = "Ytrans(t)"
        idi_yf = "Yforc(t)"
        idi_yc = "Ycomplete(t)"
        return idi_amp, idi_yn, idi_raiz, idi_tal, idi_real, idi_imag, idi_yp, idi_yt, idi_yf, idi_yc, idi_plot_raiz

    else:
        idi_amp = "Amplitud"
        idi_yn = "ynat(t)"
        idi_plot_raiz = u"Mapa de raíces de la ecuación caracterisitica"
        if(len(Respostas[0])==1):
            idi_raiz = u"Raíz"
        else:
            idi_raiz = u"Raíces"
        if(len(tal)==1):
            idi_tal = "Constante de tiempo: "
        else:
            idi_tal = "Constantes de tiempo: "
        idi_real = "Real"
        idi_imag = "Imaginario"
        idi_yp = "ypart(t)"
        idi_yt = "ytrans(t)"
        idi_yf = "yforz(t)"
        idi_yc = "yc(t)"
        return idi_amp, idi_yn, idi_raiz, idi_tal, idi_real, idi_imag, idi_yp, idi_yt, idi_yf, idi_yc, idi_plot_raiz


def show_plots():
        global tal, limx_max, limx_min, autoScale
        idi_amp, idi_yn, idi_raiz, idi_tal, idi_real, idi_imag, idi_yp, idi_yt, idi_yf, idi_yc,idi_plot_raiz = idioma_show_plots()

        #plt.clf()
        plots_numpy = conversao_numpy(t)

        ##Separando parte real e imaginária das raízes
        plotRaizesT = (Respostas[0])
        plotRaizesC = [0]*len(plotRaizesT)
        plotRaizesR = [0]*len(plotRaizesT)

        for i in range(len(plotRaizesT)):

                plotRaizesC[i] = im(plotRaizesT[i])
                plotRaizesR[i] = re(plotRaizesT[i])




        #print  len(plotRaizesC),plotRaizesC,type(plotRaizesC)
        #print  len(plotRaizesR),plotRaizesR,type(plotRaizesR)
        #menor raiz na primeira posicao e maior raiz na ultima posicao
        #necessario para o range do plot
        plotRaizesR.sort()
        plotRaizesC.sort()

        raizesRabs = [None]*len(plotRaizesR)


        for i in range(len(plotRaizesR)):raizesRabs[i] = abs(float(plotRaizesR[i]))
        raizesRabs.sort()

        ## Nossa variável de deslocamento t no eixo x, varia de 0 a 5tal
        #x_t = drange(0,10,0.00001)
        x_t  = drange(limx_min,limx_max,1e-2)

        ###Nossas Variaveis de plot, todas tem o mesmo tamanho do vetor x_t
        ##Now they have equal length
        plotXt    = [None]*len(x_t)
        plotNat   = [None]*len(x_t)
        plotPar   = [None]*len(x_t)
        plotTran  = [None]*len(x_t)
        plotFor   = [None]*len(x_t)
        plotCom   = [None]*len(x_t)


        for i in range(len(x_t)):

            if((plotNat[i-1]>1e12) or (plotPar[i-1]>1e12) or(plotTran[i-1]>1e12)
               or (plotFor[i-1]>1e12) or (plotCom[i-1]>1e12)): #limita o ymax para melhorar a performance
                break
            else:
                try: #resolve problema de alguns indicies nao serem calculados
                    plotXt[i]      = plots_numpy[1](x_t[i])
                    plotNat[i]     = plots_numpy[2](x_t[i])
                    plotPar[i]     = plots_numpy[3](x_t[i])
                    plotTran[i]    = plots_numpy[4](x_t[i])
                    plotFor[i]     = plots_numpy[5](x_t[i])
                    plotCom[i]     = plots_numpy[6](x_t[i])
                    ultimo_valido=i #ultimo indice em que foi possivel fazer o calculo
                except:
                    plotXt[i]      = plots_numpy[1](x_t[ultimo_valido])
                    plotNat[i]     = plots_numpy[2](x_t[ultimo_valido])
                    plotPar[i]     = plots_numpy[3](x_t[ultimo_valido])
                    plotTran[i]    = plots_numpy[4](x_t[ultimo_valido])
                    plotFor[i]     = plots_numpy[5](x_t[ultimo_valido])
                    plotCom[i]     = plots_numpy[6](x_t[ultimo_valido])


        ###-----raiz e tau em latex----####
        raizEmLatex = [0]*(len(Respostas[0]))
        str_raizLatex = [0]*(len(Respostas[0]))
        str_raizLatex[0] =""
        for i in range(len(Respostas[0])):
                raizEmLatex[i] = '$'+str(latex(Respostas[0][i])) +'$'
        if(len(Respostas[0]) == 1):
           rn = "r = "
           rn = '$'+str(latex(rn)) +'$'
           str_raizLatex[i] = rn+raizEmLatex[0]
        else:
                for i in range(len(raizEmLatex)):
                        rn = "r_{"+str(i+1)+"} = "
                        rn = '$'+str(latex(rn)) +'$'
                        str_raizLatex[i] ="\n"+rn+raizEmLatex[i]
        talEmLatex = [0]*(len(tal))
        str_talLatex = [0]*(len(tal))
        str_talLatex[0] = ""
        for i in range(len(tal)):
                talEmLatex[i] = '$'+str(latex(round(tal[i],prec))) +'$'
        if(len(tal) == 1):
           taln = "\\tau = "
           taln = '$'+str(latex(taln)) +'$'
           str_talLatex[i] = taln+talEmLatex[0]

        else:
                for i in range(len(talEmLatex)):
                        taln = "\\tau_{"+str(i+1)+"} = "
                        taln = '$'+str(latex(taln)) +'$'
                        str_talLatex[i] ="\n"+taln+talEmLatex[i]

        ###-----------FIM----------

        ###Setando o tamanho da fonte  para os plots
        font = {#'family' : 'Arial',
        #'weight' : 'normal',
        'size'   : 10}

        #plt.rc('text',usetex = True)
        plt.rc('font',**font)




        outputPlots = plt.figure('Plots',facecolor='white')

        plt_txt = plt.subplot(337, frameon=False)
        plt_txt.get_xaxis().tick_bottom()
        plt_txt.get_xaxis().set_visible(False)
        plt_txt.axes.get_yaxis().set_visible(False)
        plt_txt.text(-0.3, 0.9, idi_raiz+":",fontsize=12)
        plt.text(0.23, 0.9, idi_tal, fontsize=12)
        for i in range(len(str_raizLatex)):
            plt_txt.text(-0.3, 0.7-(0.25*i),str_raizLatex[i], fontsize=12)
            plt_txt.text(0.35, 0.7-(0.25*i),str_talLatex[i], fontsize=12)


        plt_yn = plt.subplot(333)
        plt_yn.grid('on')
        plt_yn.set_title(idi_yn)
        plt_yn.set_ylabel(idi_amp)
        plt_yn.set_xlabel("t")
        plt_yn.axhline(0, color = 'black',lw =2)
        respNatPlot = plt_yn.plot(x_t,plotNat,lw = 2)

        plt_xt = plt.subplot(331)
        plt_xt.grid('on')
        plt_xt.set_title(ur'x(t) = (' +'$'+  latex(Respostas[7])+'$' + ')u(t) ')
        #plt_xt.set_title(r' textbf{x(t)}' )
        plt_xt.set_xlabel("t")
        plt_xt.set_ylabel(idi_amp)
        plt_xt.axhline(0, color = 'black',lw =2)
        plt_xt.axvline(-0.01, color = 'black',lw =2)
        if plotXt[0] == plotXt[-1]:
                plt_xt.set_ylim(ymax = plotXt[0] + 0.2*plotXt[0])
                if plotXt[0] == 0:
                    plt_xt.set_ylim(ymin=-0.2,ymax=0.2)
        respXtPlot = plt_xt.plot(x_t,plotXt,lw = 2)

        plt_r = plt.subplot(334)
        plt_r.grid('on')
        plt_r.set_title(idi_plot_raiz)
        plt_r.set_xlabel(idi_real)
        plt_r.set_ylabel(idi_imag)






        if plotRaizesC[0] != 0:
                plt_r.set_ylim(float(-abs(plotRaizesC[0] + 0.2*plotRaizesC[0])),float(abs(plotRaizesC[-1]+ 0.2*plotRaizesC[-1]) ))
        else:
                plt_r.set_ylim(-1,1)


        if((-(raizesRabs[-1]+ 0.1*raizesRabs[-1])) != (raizesRabs[-1]+ 0.1*raizesRabs[-1]) ):
            plt_r.set_xlim(-(raizesRabs[-1]+ 0.1*raizesRabs[-1]),(raizesRabs[-1]+ 0.1*raizesRabs[-1]))
        else:
            plt_r.set_xlim(-1,1)






        for i in range(  len(Respostas[0]) ):

                #print  str(Respostas[0].count(Respostas[0][i]) )


                if Respostas[0].count(Respostas[0][i]) == 1 :
                        #print " UM"

                        plt_r.plot( re(Respostas[0][i]) , im(Respostas[0][i]) , 'bx',mew=1.5, markersize = 9 )


                elif Respostas[0].count(Respostas[0][i]) == 2 :
                        #print " Dois"

                        plt_r.plot( re(Respostas[0][i]) , im(Respostas[0][i]) , 'bx',mew=1.5, markersize = 9 )

                        plt_r.plot( re(Respostas[0][i]) -  0.05 * re(Respostas[0][i]) , im(Respostas[0][i])  +
                                        0.05* im(Respostas[0][i]), 'bx',mew=1.5, markersize = 9 )

                elif Respostas[0].count(Respostas[0][i]) == 3 :
                        #print "Tres"

                        plt_r.plot( re(Respostas[0][i]) , im(Respostas[0][i]) , 'bx',mew=1.5, markersize = 9 )

                        plt_r.plot( re(Respostas[0][i]) -  0.05 * re(Respostas[0][i]) , im(Respostas[0][i])  +
                                        0.05* im(Respostas[0][i]), 'bx',mew=1.5, markersize = 9 )

                        plt_r.plot( re(Respostas[0][i]) -  0.07 * re(Respostas[0][i]) , im(Respostas[0][i])  +
                                        0.07* im(Respostas[0][i]), 'bx',mew=1.5, markersize = 9 )


        # print "xlim max", -(raizesRabs[-1]+ 0.1*raizesRabs[-1])
        # print "slim min", raizesRabs[-1]+ 0.1*raizesRabs[-1]

##
##        if(len(plotRaizesT)>1):
##            for i in range(len(plotRaizesC)):
##                    if  complex( round ( plotRaizesR[i], 2), round ( plotRaizesC[i], 2) ) !=  complex( round ( plotRaizesR[i-1], 2), round (plotRaizesC[i-1],2 )) :
##                             #print "Raizes Diferentes"
##                             #print "Raiz: ",complex(plotRaizesR[i],plotRaizesC[i])
##                             respRaizesPlot = plt_r.plot(plotRaizesR[i],plotRaizesC[i],'bx',mew=1.5, markersize = 9)
##
##                    elif (plotRaizesR[i] + plotRaizesC[i]) != 0 and (plotRaizesR[i-1] + plotRaizesC[i-1])  != 0 :
##                             respRaizesPlot = plt_r.plot(plotRaizesR[i-1] ,plotRaizesC[i-1] ,'bx',mew=1.5, markersize = 9)
##                             respRaizesPlot = plt_r.plot(plotRaizesR[i] - 0.05*plotRaizesR[i],plotRaizesC[i] + 0.05*plotRaizesC[i],'bx',mew=1.5, markersize = 9)
##                             #print"Raizes repetidas"
##        else:#eqs de ordem 1
##            #print "ordem 1"
##            respRaizesPlot = plt_r.plot(plotRaizesR,plotRaizesC,'bx',mew=1.5, markersize = 9)




        #respRaizesPlot = plt_r.plot(plotRaizesR,plotRaizesC,'bx',mew=1.5, markersize = 9)
        #plt_r.axhline(0, color = 'black',lw =1)
        plt_r.spines['left'].set_position('center')
        plt_r.spines['right'].set_color('none')
        plt_r.spines['bottom'].set_position('center')
        plt_r.spines['top'].set_color('none')
        plt_r.spines['left']#.set_smart_bounds(True)
        plt_r.spines['bottom']#.set_smart_bounds(True)
        plt_r.xaxis.set_ticks_position('bottom')
        plt_r.yaxis.set_ticks_position('left')



        plt_yp = plt.subplot(332)
        plt_yp.grid('on')
        plt_yp.set_title(idi_yp)
        plt_yp.set_xlabel("t")
        plt_yp.set_ylabel(idi_amp)
        plt_yp.axhline(0, color = 'black',lw =2)
        if plotPar[0] == plotPar[2]:
                plt_yp.set_ylim(ymax = plotPar[0] + 0.2*abs(plotPar[0]))
                if plotPar[0] == 0:
                    plt_yp.set_ylim(ymin=-0.2,ymax=0.2)
        respParPlot = plt_yp.plot(x_t,plotPar,lw = 2)

        plt_yt = plt.subplot(335)
        plt_yt.grid('on')
        plt_yt.set_title(idi_yt)
        plt_yt.set_xlabel("t")
        plt_yt.set_ylabel(idi_amp)
        plt_yt.axhline(0, color = 'black',lw =2)
        respTranPlot = plt_yt.plot(x_t,plotTran,lw = 2)

        plt_yf2 = plt.subplot(336)
        plt_yf2.grid('on')
        plt_yf2.set_title(idi_yf)
        plt_yf2.set_xlabel("t")
        plt_yf2.set_ylabel(idi_amp)
        plt_yf2.axhline(0, color = 'black',lw =2)
        respForPlot = plt_yf2.plot(x_t,plotFor,lw = 2)

        plt_yf1 = plt.subplot(338)
        plt_yf1.grid('on')
        plt_yf1.set_title(idi_yf)
        plt_yf1.set_xlabel("t")
        plt_yf1.set_ylabel(idi_amp)
        plt.axhline(0, color = 'black',lw =2)
        respForPlot = plt_yf1.plot(x_t,plotFor,lw = 2)

        plt_yc = plt.subplot(339)
        plt_yc.grid('on')
        plt_yc.set_title(idi_yc)
        plt_yc.set_xlabel("t")
        plt_yc.set_ylabel(idi_amp)
        plt_yc.axhline(0, color = 'black',lw =2)
        respComPlot = plt_yc.plot(x_t,plotCom,lw = 2)


        if(autoScale==0):
           #graficos na mesma coluna com o mesmo limite superior no eixo y
           ymin, ymax = plt_yf1.get_ylim()
           plt_yp.set_ylim( ymax=ymax)
           plt_yt.set_ylim( ymax=ymax)

           ymin, ymax = plt_yc.get_ylim()
           plt_yn.set_ylim( ymax=ymax)
           plt_yf2.set_ylim( ymax=ymax)


        plt.subplots_adjust(left=0.08, bottom=0.10, right=0.97, top=0.95,
                                        wspace=0.46, hspace=0.64)


        return outputPlots

def idioma_print_latex():
    global lingua
    raizRealNeg = 0
    real = None

    for i in range(len(Respostas[0])):

        if(re(Respostas[0][i]) < 0):
            raizRealNeg += 1
        elif(re(Respostas[0][i]) == 0):
            real = 0


    if(lingua==1):

        if(len(Respostas[0])==1):
            idi_raiz = '$'+latex("Raiz:\ ")+'$'
        else:
            idi_raiz = '$'+latex("Ra\\'{\i}zes:\ ")+'$'
        if(len(tal)==1):
            idi_tal = '$'+latex("Constante\ de\ tempo:\ ")+'$'
        else:
            idi_tal = '$'+latex("Constantes\ de\ tempo:\ ")+'$'
        if(raizRealNeg == len(Respostas[0])):
            idi_est_sis = '$'+latex("Sistema\ est\\'{a}vel,\ componente\ real\ das\ ra\\'{\i}zes\ s\~{a}o\ negativas")+'$'
        elif(real==0):
            idi_est_sis = ""
        else:
            idi_est_sis = '$'+latex("Sistema\ n\~{a}o\ est\\'{a}vel,\ componente\ real\ da\ raiz\ \\'{e}\ positiva")+'$'



        idi_eq = '$'+latex("Equac\c\~{a}o\ diferencial:\ ")+'$' #c\c = cedilha
        idi_hom = '$'+latex("Equac\c\~{a}o\ homog\^{e}nea:\ ")+'$'
        idi_car = '$'+latex("Equac\c\~{a}o\ caracter\\'{\i}stica:\ ")+ '$'
        idi_yfn = '$'+latex("Y_{fn}(t) = ")+'$'
        idi_yn = '$'+latex("Y_{nat}(t) = ")+'$'
        idi_yp = '$'+latex("Y_{part}(t) = ")+'$'
        idi_yt = '$'+latex("Y_{trans}(t) = ")+'$'
        idi_yf = '$'+latex("Y_{forc}(t) = ")+'$'
        idi_yc = '$'+latex("Y_c(t) = ")+'$'
        idi_cond_sing = latex("Condic\c\~{a}o\  inicial:\ ")
        idi_cond_pl = latex("Condic\c\~{o}es\ iniciais:\ ")
        str_xt = latex("Entrada\ ")
        return idi_raiz, idi_tal, idi_est_sis, idi_eq, idi_hom, idi_car, idi_yfn, idi_yn, idi_yp, idi_yt, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl, str_xt

    elif(lingua==2):
        if(len(Respostas[0])==1):
            idi_raiz = '$'+latex("Root:\ ")+'$'
        else:
            idi_raiz = '$'+latex("Roots:\ ")+'$'
        if(len(tal)==1):
            idi_tal = '$'+latex("Time\ constant:\ ")+'$'
        else:
            idi_tal = '$'+latex("Time\ constants:\ ") +'$'
        if(raizRealNeg == len(Respostas[0])):
            idi_est_sis = '$'+latex("Stable\ system,\ roots\ real\ components\ are\ negatives")+'$'
        elif(real==0):
            idi_est_sis = ""
        else:
            idi_est_sis = '$'+latex("Unstable\ system,\ root\ real\ component\ is\ positive")+'$'


        idi_eq = '$'+latex("Differential\ Equation:\ ")+'$'
        idi_hom = '$'+latex("Homogenous\ Equation:\ ")+'$'
        idi_car = '$'+latex("Characteristic\ Equation:\ ")+ '$'
        idi_yfn = '$'+latex("Y_{complementary}(t) = ")+'$'
        idi_yn = '$'+latex("Y_{nat}(t) = ")+'$'
        idi_yp = '$'+latex("Y_{part}(t) = ")+'$'
        idi_yt = '$'+latex("Y_{trans}(t) = ")+'$'
        idi_yf = '$'+latex("Y_{forc}(t) = ")+'$'
        idi_yc = '$'+latex("Y_{c}(t) = ")+'$'
        idi_cond_sing = latex("Initial\ condition:\ ")
        idi_cond_pl = latex("Initial\ conditions:\ ")
        str_xt = latex("Input\ ")
        return idi_raiz, idi_tal, idi_est_sis, idi_eq, idi_hom, idi_car, idi_yfn, idi_yn, idi_yp, idi_yt, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl, str_xt

    else:
        if(len(Respostas[0])==1):
            idi_raiz = '$'+latex("Ra\\'{\i}z:\ ")+'$'
        else:
            idi_raiz = '$'+latex("Ra\\'{\i}ces:\ ")+'$'
        if(len(tal)==1):
            idi_tal = '$'+latex("Constante\ de\ tiempo:\ ")+'$'
        else:
            idi_tal = '$'+latex("Constantes\ de\ tiempo:\ ")+'$'
        if(raizRealNeg == len(Respostas[0])):
            idi_est_sis = '$'+latex("Sistema\ estable,\ componente\ reales\ de\ las\ ra\\'{\i}ces\ son\ negativas")+'$'
        elif(real==0):
            idi_est_sis = ""
        else:
            idi_est_sis = '$'+latex("Sistema\ no\ es\ estable,\ componente\ real\ de\ la\ ra\\'{\i}z\ es\ positiva")+'$'


        idi_eq = '$'+latex("Ecuaci\\'{o}n\ diferencial:\ ")+'$'
        idi_hom = '$'+latex("Ecuaci\\'{o}n\ homog\\'{e}nea:\ ")+'$'
        idi_car = '$'+latex("Ecuaci\\'{o}n\ caracter\\'{\i}stica:\ ")+ '$'
        idi_yfn = '$'+latex("Y_{gen}(t) = ")+'$'
        idi_yn = '$'+latex("Y_{nat}(t) = ")+'$'
        idi_yp = '$'+latex("Y_{part}(t) = ")+'$'
        idi_yt = '$'+latex("Y_{trans}(t) = ")+'$'
        idi_yf = '$'+latex("Y_{forz}(t) = ")+'$'
        idi_yc = '$'+latex("Y_{c}(t) = ")+'$'
        idi_cond_sing = latex("Condici\\'{o}n\ inicial:\  ")
        idi_cond_pl = latex("Condiciones\ iniciales:\  ")
        str_xt = latex("Entrada\ ")
        return idi_raiz, idi_tal, idi_est_sis, idi_eq, idi_hom, idi_car, idi_yfn, idi_yn, idi_yp, idi_yt, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl, str_xt

def eq_CondIni_emLatex():
    global notation

    str_const=[str(const[0]), str(const[1]), str(const[2]), str(const[3]), str(const[4]), str(const[5])]

    for i in range(len(const)):
        if(const[i]>0):
            str_const[i] = "+"+str_const[i]

    str_eq = ""
    str_eqC = ""
    if(const[0] != 0):
        str_eqC = str_const[0]
        str_eq = str_const[0]+"y(t)"
        if(notation==4):
            str_eq = str_const[0]+"D_{t}^{0}"
    if(const[1] != 0):
        str_eqC = str_const[1]+"r"+str_eqC
        if(notation==1):
            str_eq = str_const[1]+"\\frac{d}{d t} y(t)"+str_eq
        elif(notation==2):
            str_eq = str_const[1]+"y^{i}(t)"+str_eq#\prime = apostrofo em latex
        elif(notation==3):
            str_eq = str_const[1]+"\dot{y}(t)"+str_eq#\dot{y} = ponto em cima do y(notacao de newton)
        elif(notation==4):
            str_eq = str_const[1]+"D_{t}^{1}"+str_eq
    if(const[2] != 0):
        str_eqC = str_const[2]+"r^{2}"+str_eqC
        if(notation==1):
            str_eq = str_const[2]+"\\frac{d^{2}}{d t^{2}}  y(t)"+str_eq
        elif(notation==2):
            str_eq = str_const[2]+"y^{ii}(t)"+str_eq
        elif(notation==3):
            str_eq = str_const[2]+"\ddot{y}(t)"+str_eq
        elif(notation==4):
            str_eq = str_const[2]+"D_{t}^{2}"+str_eq
    if(const[3] != 0):
        str_eqC = str_const[3]+"r^{3}"+str_eqC
        if(notation==1):
            str_eq = str_const[3]+"\\frac{d^{3}}{d t^{3}}  y(t)"+str_eq
        elif(notation==2):
            str_eq = str_const[3]+"y^{iii}(t)"+str_eq
        elif(notation==3):
            str_eq = str_const[3]+"y^{(iii)}(t)"+str_eq
        elif(notation==4):
            str_eq = str_const[3]+"D_{t}^{3}"+str_eq
    if(const[4] != 0):
        str_eqC = str_const[4]+"r^{4}"+str_eqC
        if(notation==1):
            str_eq = str_const[4]+"\\frac{d^{4}}{d t^{4}}  y(t)"+str_eq
        elif(notation==2):
            str_eq = str_const[4]+"y^{iv}(t)"+str_eq
        elif(notation==3):
            str_eq = str_const[4]+"y^{(iv)}(t)"+str_eq
        elif(notation==4):
            str_eq = str_const[4]+"D_{t}^{4}"+str_eq
    if(const[5] != 0):
        str_eqC = str_const[5]+"r^{5}"+str_eqC
        if(notation==1):
            str_eq = str_const[5]+"\\frac{d^{5}}{d t^{5}}  y(t)"+str_eq
        elif(notation==2):
            str_eq = str_const[5]+"y^{v}(t)"+str_eq
        elif(notation==3):
            str_eq = str_const[5]+"y^{(v)}(t)"+str_eq
        elif(notation==4):
            str_eq = str_const[5]+"D_{t}^{5}"+str_eq

    if(str_eq[0]=="+"):
        str_eq = str_eq[1:] #exclui o primeiro caractere da string
        str_eqC = str_eqC[1:]

    eqDiferencialEntradaLatex = latex(str_eq)
    eqCaracEmLatex = latex(str_eqC)

    condIni_latex = ""

    if((const[5] == 0) and (const[4] == 0) and (const[3] == 0) and (const[2] == 0)):#eq ordem 1
        condIni_latex = "y(0) \ = \ "+str(cond_ini[0])
        if(notation==4):
            condIni_latex = "D_{0}^{0} \ = \ "+str(cond_ini[0])
    elif((const[5] == 0) and (const[4] == 0) and (const[3] == 0) ):#eq ordem 2
        if(notation==1):
            condIni_latex = "y(0) \ = \ "+str(cond_ini[0])+"\quad"+"\\frac{d}{d t} y(0) \ = \ "+ str(cond_ini[1]) #\quad = space
        elif(notation==2):
            condIni_latex = "y(0) \ = \  "+str(cond_ini[0])+"\quad"+"y^{i}(0) \ = \  "+str(cond_ini[1])
        elif(notation==3):
            condIni_latex = "y(0) \ = \ "+str(cond_ini[0])+"\quad"+"\dot{y}(0) \ = \ "+str(cond_ini[1])
        elif(notation==4):
            condIni_latex = "D_{0}^{0} \ = \ "+str(cond_ini[0])+"\quad"+"D_{0}^{1} \ = \ "+str(cond_ini[1])
    elif((const[5] == 0) and (const[4] == 0)):#eq ordem 3
        if(notation==1):
            condIni_latex = "y(0) \ = \ "+str(cond_ini[0])+"\quad"+"\\frac{d}{d t} y(0) \ = \ "+ str(cond_ini[1])+\
                "\quad"+"\\frac{d^{2}}{d t^{2}}  y(0) \ = \ "+str(cond_ini[2])
        elif(notation==2):
            condIni_latex = "y(0) \ = \  "+str(cond_ini[0])+"\quad"+"y^{i}(0) \ = \  "+str(cond_ini[1])+"\quad"+"y^{ii}(0) \ = \  "+str(cond_ini[2])#^ em latex usado para superscript
        elif(notation==3):
            condIni_latex = "y(0) \ = \ "+str(cond_ini[0])+"\quad"+"\dot{y}(0) \ = \ "+str(cond_ini[1])+"\quad"+"\ddot{y}(0) \ = \ "+str(cond_ini[2])
        elif(notation==4):
            condIni_latex = "D_{0}^{0} \ = \ "+str(cond_ini[0])+"\quad"+"D_{0}^{1} \ = \ "+str(cond_ini[1])+"\quad"+"D_{0}^{2} \ = \ "+str(cond_ini[2])
    elif((const[5] == 0)):#eq ordem 4
        if(notation==1):
            condIni_latex = "y(0) \ = \ "+str(cond_ini[0])+"\quad"+"\\frac{d}{d t} y(0) \ = \ "+ str(cond_ini[1])+\
                "\quad"+"\\frac{d^{2}}{d t^{2}}  y(0) \ = \ "+str(cond_ini[2])+"\quad"+"\\frac{d^{3}}{d t^{3}}  y(0) \ = \ "+str(cond_ini[3])
        elif(notation==2):
            condIni_latex = "y(0) \ = \  "+str(cond_ini[0])+"\quad"+"y^{i}(0) \ = \  "+str(cond_ini[1])+"\quad"+"y^{ii}(0) \ = \  "+str(cond_ini[2])+\
                "\quad"+"y^{iii}(0) \ = \  "+str(cond_ini[3])#\left(...\right) = (..) e latex
        elif(notation==3):
            condIni_latex = "y(0) \ = \ "+str(cond_ini[0])+"\quad"+"\dot{y}(0) \ = \ "+str(cond_ini[1])+"\quad"+"\ddot{y}(0) \ = \ "+str(cond_ini[2])+\
                "\quad"+"y^{(iii)}(0) \ = \ "+str(cond_ini[3])
        elif(notation==4):
            condIni_latex = "D_{0}^{0} \ = \ "+str(cond_ini[0])+"\quad"+"D_{0}^{1} \ = \ "+str(cond_ini[1])+"\quad"+"D_{0}^{2} \ = \ "+str(cond_ini[2])+\
                "\quad"+"D_{0}^{3} \ = \ "+str(cond_ini[3])
    else:#eq ordem 5
        if(notation==1):
            condIni_latex = "y(0) \ = \ "+str(cond_ini[0])+"\quad"+"\\frac{d}{d t} y(0) \ = \ "+ str(cond_ini[1])+\
                "\quad"+"\\frac{d^{2}}{d t^{2}}  y(0) \ = \ "+str(cond_ini[2])+"\quad"+"\\frac{d^{3}}{d t^{3}}  y(0) \ = \ "+str(cond_ini[3])+\
                "\quad"+"\\frac{d^{4}}{d t^{4}}  y(0) \ = \ "+str(cond_ini[4])
        elif(notation==2):
            condIni_latex = "y(0) \ = \  "+str(cond_ini[0])+"\quad"+"y^{i}(0) \ = \  "+str(cond_ini[1])+"\quad"+"y^{ii}(0) \ = \  "+str(cond_ini[2])+\
                    "\quad"+"y^{iii}(0) \ = \  "+str(cond_ini[3])+"\quad"+"y^{iv}(0) \ = \  "+str(cond_ini[4])
        elif(notation==3):
            condIni_latex = "y(0) \ = \ "+str(cond_ini[0])+"\quad"+"\dot{y}(0) \ = \ "+str(cond_ini[1])+"\quad"+"\ddot{y}(0) \ = \ "+str(cond_ini[2])+\
                "\quad"+"y^{(iii)}(0) \ = \ "+str(cond_ini[3])+"\quad"+"y^{(iv)}(0) \ = \  "+str(cond_ini[4])
        elif(notation==4):
            condIni_latex = "D_{0}^{0} \ = \ "+str(cond_ini[0])+"\quad"+"D_{0}^{1} \ = \ "+str(cond_ini[1])+"\quad"+"D_{0}^{2} \ = \ "+str(cond_ini[2])+\
                "\quad"+"D_{0}^{3} \ = \ "+str(cond_ini[3])+"\quad"+"D_{0}^{4} \ = \  "+str(cond_ini[4])


    condIni_latex = latex(condIni_latex)

    return eqDiferencialEntradaLatex, eqCaracEmLatex, condIni_latex

def print_latex():
        global t


        idi_raiz, idi_tal, idi_est_sis, idi_eq, idi_hom, idi_car, idi_yfn, idi_yn, idi_yp, idi_yt, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl, str_xt = idioma_print_latex()
        #plt.clf()
        #edo_main()

        # 0- Raizes; 1- Forma Natural da respsota; 2- Resposta Natural;
        # 3- Resposta Particular; 4- Resposta Transitoria; 5- Respsota Forcada
        # 6- Resposta Completa; 7-Sinal de entrada x(t); 8 - eq
        ###

        # eqD = Respostas[8] + Respostas[7] #xT esta negativo dentro da equacao, por isso a soma
        # eqDiferencialEntradaLatex = latex(eqD)

        eqDiferencialEntradaLatex, eqCaracEmLatex, condIni_latex = eq_CondIni_emLatex()

        ##Perfumaria
        dif = 0.9 -0.77
        xdif = -0.15
        font = {#'family' : 'Arial',
                #'weight' : 'normal',
                'size'   : 15}


        plt.rc('font', **font)
        plt.rcParams[ 'mathtext.default' ] = 'regular'
        plt.rcParams['text.latex.unicode'] =  'True'
        #plt.rcParams['mathtext.bf'] = 'serif:bold'


        ##Obtendo as respostas em Latex
        RespostasEmLatex = [0]*(len(Respostas))
        raizEmLatex = [0]*(len(Respostas[0]))
        str_raizLatex =""
        for i in range(len(Respostas[0])):
                raizEmLatex[i] = '$'+str(latex(Respostas[0][i])) +'$'
        if(len(Respostas[0]) == 1):
           rn = "r = "
           rn = '$'+str(latex(rn)) +'$'
           str_raizLatex = str_raizLatex+rn+raizEmLatex[0]
           str_r = idi_raiz
        else:
                for i in range(len(raizEmLatex)):
                        rn = "r_{"+str(i+1)+"} = "
                        rn = '$'+str(latex(rn)) +'$'
                        str_raizLatex = str_raizLatex+"    "+rn+raizEmLatex[i]
                str_r = idi_raiz

        talEmLatex= [0]*(len(tal))
        str_talLatex=""
        for i in range(len(tal)):
                talEmLatex[i] = '$'+str(latex(tal[i])) +'$'
        if(len(tal) == 1):
           taln = "\\tau = "
           taln = '$'+str(latex(taln)) +'$'
           str_talLatex = str_talLatex+taln+talEmLatex[0]
           str_t = idi_tal
        else:
                for i in range(len(talEmLatex)):
                        taln = "\\tau_{"+str(i+1)+"} = "
                        taln = '$'+str(latex(taln)) +'$'
                        str_talLatex = str_talLatex+"    "+taln+talEmLatex[i]
                str_t = idi_tal
        ##print len(RespostasEmLatex)
        for i in range(1,8):
                RespostasEmLatex[i] = '$'+str(latex(Respostas[i])) +'$'
        #print RespostasEmLatex
        #xTLatex = '$' + latex(xT) +'$'
        ###Preparando para imprimir
        log_figure = plt.figure("Representacao",facecolor='white')
        ax1 = plt.axes(frameon = False)
        ax1.get_xaxis().tick_bottom()
        ax1.get_xaxis().set_visible(False)
        ax1.axes.get_yaxis().set_visible(False)
        for i in range(0,11,1):
            plt.axhline(0.86-dif*i,xmin = -10,xmax = 5, color = 'black',lw =0.2, linestyle = ':')
        #plt.axhline(0.86-dif*4, color='black', lw=2)
        #plt.axhline(0.86-dif*5, color='black', lw=2)
        #log_figure.figure("Forma_Representativa:")
        plt.title('')
        plt.text(xdif,0.89,idi_eq+
                 ur'$'+eqDiferencialEntradaLatex+'$'+"  "+
                 ur'$'+latex("=")+'$'+"  "+
                 ur''+RespostasEmLatex[7])

        plt.text(xdif, 0.9-dif,idi_hom+
                 ur'$'+eqDiferencialEntradaLatex+'$'+"  "+
                 ur'$'+latex("=\ 0")+'$')

        plt.text(xdif, 0.9-2*dif,idi_car+ur'$'+eqCaracEmLatex+'$'+"  "+
                 ur'$'+latex("=\ 0")+'$')

        plt.text(xdif,0.9-3*dif,str_r+ur''+
                 str_raizLatex+"    "
                 #+idi_est_sis
        )

        plt.text(xdif,0.9-4*dif,str_t+ur''+str_talLatex)

        plt.text(xdif,0.9-5*dif,ur''+
                 idi_yfn+ur'$'+latex("(")+'$'+
                 ur''+RespostasEmLatex[1]+
                 ur'$'+latex(")u(t)")+'$')

        if((const[5] == 0) and (const[4] == 0) and (const[3] == 0) and (const[2] == 0)):#eq ordem 1
            plt.text(xdif,0.9-6*dif,ur'$'+idi_cond_sing+condIni_latex+'$')
        else:#eq ordem >1
            plt.text(xdif,0.9-6*dif,ur'$'+idi_cond_pl+condIni_latex+'$')

        plt.text(xdif,0.9-7*dif,ur''+idi_yn+
                     ur'$'+latex("(")+'$'+ur''+RespostasEmLatex[2]+
                     ur'$'+latex(")u(t)")+'$')


        plt.text(xdif,0.9-8*dif,ur'$'+str_xt+latex("x(t) = ($")+
                 ur''+RespostasEmLatex[7]+
                 ur'$'+latex(")u(t)")+'$'+"   "
                 ur''+idi_yp+
                 ur'$'+latex("(")+'$'+
                 ur''+RespostasEmLatex[3]+
                 ur'$'+latex(")u(t)")+'$'
                 )

        plt.text(xdif,0.9-9*dif,ur''+idi_yt+
                 ur'$'+latex("(")+'$'+
                 ur''+RespostasEmLatex[4]+
                 ur'$'+latex(")u(t)")+'$')

        plt.text(xdif,0.9-10*dif,ur''+idi_yf+
                 ur'$'+latex("(")+'$'+
                 ur''+RespostasEmLatex[5]+
                 ur'$'+latex(")u(t)")+'$')

        plt.text(xdif,0.9-11*dif,ur''+idi_yc+
                 ur'$'+latex("(")+'$'+
                 ur''+RespostasEmLatex[6]+
                 ur'$'+latex(")u(t)")+'$')
        #plt.text(xdif,0.9-7*dif,'x(t) = '+ur''+RespostasEmLatex[7])


        plt.subplots_adjust(left=0.12, bottom=0.04, right=0.53, top=0.93,
                                                wspace=0.22, hspace=0.21)





        ##log_figure.set_size_inches(19.2,10.8)
        #log_figure.show()
        #plt.show()

        return log_figure


def subs_rootof(eq):

        #print "-----Metodo RootOF"
        eqStr = str(eq)
        #print eqStr
        ct = eqStr.split("C")
        #print ct,len(ct),type(ct)
        ct.pop(0)
        #print ct, len(ct)
        ocur = [None]*len(ct)
        flag_sin_cos = False
        output = ""


        for i in range(  len( ct) ):
                #print "Loop ",i
                #print ct[i]

                if type( Respostas[0][i] ) is ComplexType and not flag_sin_cos :
                        ct[i] = "C" + ct[i]
                        ocur[i] = ct[i].find("e")

                        ct[i] = ct[i] [:ocur[i]]
                        #print "Antes de adicionar raiz",ct[i]

                        ct[i] = "(" + ct[i] + "exp(t*" + str( round(-re(Respostas[0][i]),2) ) + ")" + "*sin(t*" +  str( abs (round( im(Respostas[0][i]),2) ) ) + ")" + ")"

                        #print ct[i]
                        #print ocur
                        flag_sin_cos = True

                elif type( Respostas[0][i] ) is ComplexType and  flag_sin_cos :
                        ct[i] = "C" + ct[i]
                        ocur[i] = ct[i].find("e")

                        ct[i] = ct[i] [:ocur[i]]
                        #print "Antes de adicionar raiz",ct[i]

                        ct[i] = "(" +  ct[i] + "exp(t*" + str( round(-re(Respostas[0][i]),2) ) + ")" + "*cos(t*" +  str( abs ( round(im(Respostas[0][i]),2) ) ) + ")"+ ")"

                        #print ct[i]
                        #print ocur
                        flag_sin_cos = False



                else:
                        ct[i] = "C" + ct[i]
                        ocur[i] = ct[i].find("e")
                        ct[i] = ct[i] [:ocur[i] ]
                        #print "Antes de adicionar raiz",ct[i]
                        ct[i] = "(" + ct[i] + "exp(t*" + str(      round(-re(Respostas[0][i]),2)        ) + ")"+ ")"

                        #print ct[i]
                        #print ocur


        for i in range( len(ct) ):



                if i == 0 :
                        output =  output + ct[i]
                else:
                        output = output + " + " + ct[i]
        #print "Equacao de saida",output
        output = sympify(output)
        #print "Saida",output,type(output)

        return output







##    for i in range(len(rootOf_list)-1):
##        #eq = eq.replace(str(rootOf_list[i]),Respostas[0][-1 + i ])
##        eq = eq.replace(str(rootOf_list[i]),str(Respostas[0][((len(Respostas[0])-2)-i)]))
##
##    eq = eq.replace(str(rootOf_list[-1]),str(Respostas[0][-1]))

   # print "Equacao",eq



def edo_main():
        global t

        #const = [0]*6 #a0, a1, a2, a3, a4, a5   ; nessa ordem

        ##Criando uma variavel para guardar valores digitados anteriormente,este só vai calcular as coisas novamente se
        # e somente se parâmetros de entrada diferentes forem colocados
        #constAnterior = const
        #print "Valores",const
        #print "Valores anteriores",constAnterior
        #valAnteriorDif = True
        #flag_init = get_flagInit()

        #print "FLAG INIT",flag_init
        xT = get_xT()
        for i in range(len(const_orig)):
            const[i] = round(const_orig[i], prec)
        for i in range(len(cond_ini)):
            cond_ini[i] = round(cond_ini_orig[i], prec)

        try:
                print "Calculando edo_main"
                ##Adicionando os coefs a eq diferencial
                eq = sympify(const[5] * y(t).diff(t, 5) + const[4] * y(t).diff(t, 4) + const[3] * y(t).diff(t, 3) +
                const[2] * y(t).diff(t, 2) + const[1] * y(t).diff(t) + const[0] * y(t) - xT)
                Respostas[8] = eq


                #a5, a4, a3, a2, a1, a0, xT = input_coefs()
                ###Dif equation solver
                ##Sets if it is of homogenous or inhomogenous type and type of resolution method
                if Respostas[7] == 0:
                                solvedEq = dsolve(sympify(Respostas[8]), y(t), hint='nth_linear_constant_coeff_homogeneous',)
                                #elif (a3 != 0) or (a4 != 0) or (a5 != 0):
                                #solvedEq = dsolve(sympify(eq),y(t),hint='nth_linear_constant_coeff_variation_of_parameters')

                else:           # nth_linear_constant_coeff_variation_of_parameters
                                solvedEq = dsolve(sympify(Respostas[8]), y(t), hint='nth_linear_constant_coeff_undetermined_coefficients', returns='both')
                                #solvedEq = dsolve(sympify(Respostas[8]), y(t), hint='nth_linear_constant_coeff_variation_of_parameters_Integral')

                ##Transformação do tipo sympy_unity para o sympy_mul (mais operações permitidas)
                sepEq = solvedEq._args[1]
                #sepEq = sepEq.evalf(prec)
                #print "sepEq", sepEq

                if const[5] != 0:
                                RespPart = sepEq.subs([(C1, 0), (C2, 0), (C3, 0), (C4, 0), (C5, 0)])
                elif const[4] != 0:
                                RespPart = sepEq.subs([(C1, 0), (C2, 0), (C3, 0), (C4, 0)])
                elif const[3] != 0:
                                RespPart = sepEq.subs([(C1, 0), (C2, 0), (C3, 0)])
                elif const[2] != 0:
                                RespPart = sepEq.subs([(C1, 0), (C2, 0)])
                elif const[1] != 0:
                                RespPart = sepEq.subs(C1, 0)


                ##Resposta transitória alocada em  RespTran, natural em RespNat
                #print "Equacao:",sepEq
                #print "RespPart",RespPart
                Respostas[3] = RespPart #.evalf(prec)
                sepEq = expand(sepEq) #conserta o erro das raizes iguais com entrada igual
                #a eq vinha simplificada e o metodo subs nao reconhecia o RespPart na sepEq, por isso dava erro
                #print "Equacao:",sepEq
                formaNatural = sepEq - RespPart #usar o metodo subs aqui da problema em algumas situações
                #print "FN=",formaNatural

                raizes()
                #print Respostas[0]
                cte_tempo()

                str_fn = str(formaNatural)

                if str_fn.find("RootOf") != -1:
                    formaNatural = subs_rootof(formaNatural)

                ## fN é a mesma coisa, mas usado por um bug bizarro do Sympy que exige uma variável sem alocações prévias quando diferenciando
                ##isso é válido no método conds_iniciais_aplicadas
                # 0- Raizes; 1- Forma Natural da respsota; 2- Resposta Natural;
                # 3- Resposta Particular; 4- Resposta Transitoria; 5- Respsota Forcada
                # 6- Resposta Completa; 7- xT; 8- eq

                fN = formaNatural


                Respostas[1] = formaNatural #Adicionando Forma natural de resposta na lista de respostas


                rP = RespPart.evalf(prec)
                conds_iniciais_aplicadas(fN, rP)

                respForc = Respostas[4] + Respostas[3] #Yf = Yt + Yp
                Respostas[5] = respForc #.evalf(prec)   #Adiciona Resposta Forcada a lista de respostas


                respComp = Respostas[2]  #Resposta completa p/ eqs. homogeneas
                if(Respostas[7] != 0): #Eqs. nao homogeneas
                                respComp = Respostas[2] + Respostas[5]  #Respsota completa p/ eqs. nao-homogeneas

                Respostas[6] = respComp #.evalf(prec)  #Adiciona Resposta Completa a lista de respostas


                for i in range(len(Respostas)): #arruma precisao

                        #print "Loop",i

                        #Respostas[i] = sympy.expand(Respostas[i])
                        #Respostas[i] = sympy.powsimp(Respostas[i])
                        #Respostas[i] = sympy.trigsimp(Respostas[i])
                        #Respostas[i] = sympy.radsimp(Respostas[i])
                        if i == 0: None#Respostas[i] = sympy.powsimp(Respostas[i])
                        else: Respostas[i] = sympy.powsimp(Respostas[i]).evalf(prec,chop = True)

                        #Respostas[i] = nsimplify(Respostas[i],tolerance = 0.1, full = True, rational = False).evalf(2)


                        #Respostas[i] = sympy.collect(Respostas[i], t )

        except:
                pass



