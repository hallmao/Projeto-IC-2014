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

from sympy.mpmath import mp


###Parâmetros a serem considerados

###Precisão Decimal
prec = 2 ## Numero de digitos decimais de precisão mostrados no log de dados
mp.dps = prec
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
const = [0]*6 #a0, a1, a2, a3, a4, a5   ; nessa ordem
cond_ini = [0]*5 #y0, dy0, d2y0, d3y0, d4y0     ; nessa ordem
xT = 0
#----------------------Tal - constante de tempo, para cálculo do coef de amortecimento
tal = []
maiorTal = 0#5*tal
limx_min = 0
limx_max = maiorTal
##a2 = None
##a1 = 0
##a0 = 0
##xT = 0
##eq = 0
##fN = 0
##rP = 0
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

def set_a2(cte):
        try:
                const[2] = float(cte)
        except:
                pass
        
        
def set_a1(cte):
        try:
                const[1] = float(cte)
        except:
                pass
        
def set_a0(cte):
        try:
                const[0] = float(cte)
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
        
        try:
               Respostas[7] = xT = float(expr)
        except:
                pass
        
        
        
def set_y0(cte):
        try:
                cond_ini[0] = float(cte)
        except:
                pass
        
def set_dy0(cte):
        try:
                cond_ini[1] = float(cte)
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
def init(a2, a1, a0, xT, y0, dy0):

        set_xT(xT)
        set_a0(a0)
        set_a1(a1)
        set_a2(a2)
        set_y0(y0)
        set_dy0(dy0)
        Respostas[7] = get_xT()
        edo_main()
        

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

                Respostas[0] = roots

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
                ##----Pega o maior valor de tal e calcula o coef de amortecimento
                maiorTal = int(5*tal[-1])
                if maiorTal > 100e3:
                        maiorTal = int(maiorTal/100e5)
                print "Raizes, reais inversas  (tal)",tal
                print "5 Tal = ",int(maiorTal)
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

                                respNatural = fN.subs(C1,nC1).evalf(prec)
                                Respostas[2] = respNatural #Adiciona Resposta Natural na lista de respostas

                                ##Tenta resolver parâmetros não terminados, se possível



                                ##Saida da Resposta Natural no console
                                #print "Resposta Natural:"
                                #pprint(respNatural)

                                if(Respostas[7] != 0):    #Eq. nao homogenea
                                                yt = fN + rP #Yt(t) = Yfn(t) + Yp
                                                yt = sympify(yt, rational = False,evaluate= False).evalf(prec)
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



                #Ordem 2
                elif ((const[5] == 0) and (const[4] == 0)
                   and (const[3] == 0)):
                                y0 = cond_ini[0]
                                dy0 = cond_ini[1]

                                ##Primeiramente a resposta Natural
                                ##Solucao geral é : formaNat
                                #antes de aplicar as conds iniciais é necessário ter y'(t) e y(t) da resp natural

                                #Forma natural é derivada uma vez
                                ylinhaNat = sympify(fN.diff(t), rational = False, evaluate = False).evalf(prec)
                                formaNatural  = sympify(fN, rational = False,evaluate= False).evalf(prec)
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

                                respNatural = fN.subs([(C1,nC1),(C2,nC2)]).evalf(prec)
                                Respostas[2] = respNatural #Adiciona Resposta Natural na lista de respostas

                                ##Tenta resolver parâmetros não terminados, se possível


                                #print "Resposta Natural:"
                                #pprint(respNatural)

                                if(Respostas[7] != 0): #Eq. nao homogenea
                                                yt = fN + rP #Yt(t) = Yfn(t) + Yp

                                                #Resposta Transitoria é derivada uma vez
                                                ylinhaTran = sympify(yt.diff(t), rational = False, evaluate = False).evalf(prec)
                                                yt  = sympify(yt, rational = False,evaluate= False).evalf(prec)
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

                                                respTrans = yt.subs([(C1,tC1),(C2,tC2)]).evalf(prec)
                                                Respostas[4] = respTrans.evalf(prec) #Adiciona Resposta Transitoria a lista de respostas
                                                #print "Respsota Transitoria:"
                                                #pprint(respTrans)



                #Ordem 3
                elif ((const[5] == 0) and (const[4] == 0)):
                                y0 = cond_ini[0]
                                dy0 = cond_ini[1]
                                d2y0 = cond_ini[2]


                                ##Primeiramente a resposta Natural
                                ##Solucao geral é : formaNat
                                #antes de aplicar as conds iniciais é necessário ter y''(t) y'(t) e y(t) da resp natural

                                #Forma natural é derivada a primeira e à segunda
                                y2linhaNat = sympify(fN.diff(t,2), rational = False, evaluate = False).evalf(prec)
                                ylinhaNat = sympify(fN.diff(t), rational = False, evaluate = False).evalf(prec)
                                formaNatural  = sympify(fN, rational = False,evaluate= False).evalf(prec)
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

                                respNatural = fN.subs([(C1,nC1),(C2,nC2),(C3,nC3)]).evalf(prec)
                                Respostas[2] = respNatural #Adiciona Resposta Natural na lista de respostas

                                ##Tenta resolver parâmetros não terminados, se possível


                                #print "Resposta Natural:"
                                #pprint(respNatural)


                                if(Respostas[7] != 0): #Eq. nao homogenea
                                                yt = fN + rP #Yt(t) = Yfn(t) + Yp

                                                #Resposta Transitoria é derivada a primeira e à segunda
                                                y2linhaTran = sympify(yt.diff(t,2), rational = False, evaluate = False).evalf(prec)
                                                ylinhaTran = sympify(yt.diff(t), rational = False, evaluate = False).evalf(prec)
                                                yt  = sympify(yt, rational = False,evaluate= False).evalf(prec)
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

                                                respTrans = yt.subs([(C1,tC1),(C2,tC2),(C3,tC3)]).evalf(prec)
                                                Respostas[4] = respTrans #Adiciona Resposta Transitoria a lista de respostas

                                                #print "Respsota Transitoria:"
                                           # pprint(respTrans)


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
                                y3linhaNat = sympify(fN.diff(t,3), rational = False, evaluate = False).evalf(prec)
                                y2linhaNat = sympify(fN.diff(t,2), rational = False, evaluate = False).evalf(prec)
                                ylinhaNat = sympify(fN.diff(t), rational = False, evaluate = False).evalf(prec)
                                formaNatural  = sympify(fN, rational = False,evaluate= False).evalf(prec)
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

                                respNatural = fN.subs([(C1,nC1),(C2,nC2),(C3,nC3),(C4,nC4)]).evalf(prec)
                                Respostas[2] = respNatural #Adiciona Resposta Natural na lista de respostas

                           # print "Resposta Natural:"
                                #pprint(respNatural)

                                if(Respostas[7] != 0): #Eq. nao homogenea
                                                yt = fN + rP #Yt(t) = Yfn(t) + Yp

                                                #Resposta Transitoria é derivada a primeira , segunda e terceira
                                                y3linhaTran = sympify(yt.diff(t,3), rational = False, evaluate = False).evalf(prec)
                                                y2linhaTran = sympify(yt.diff(t,2), rational = False, evaluate = False).evalf(prec)
                                                ylinhaTran = sympify(yt.diff(t), rational = False, evaluate = False).evalf(prec)
                                                yt = sympify(yt, rational = False,evaluate= False).evalf(prec)
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

                                                respTrans = yt.subs([(C1,tC1),(C2,tC2),(C3,tC3),(C4,tC4)]).evalf(prec)
                                                Respostas[4] = respTrans #Adiciona Resposta Transitoria a lista de respostas

                                                #print "Respsota Transitoria:"
                                           # pprint(respTrans)


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
                                y4linhaNat = sympify(fN.diff(t,4), rational = False, evaluate = False).evalf(prec)
                                y3linhaNat = sympify(fN.diff(t,3), rational = False, evaluate = False).evalf(prec)
                                y2linhaNat = sympify(fN.diff(t,2), rational = False, evaluate = False).evalf(prec)
                                ylinhaNat = sympify(fN.diff(t), rational = False, evaluate = False).evalf(prec)
                                formaNatural  = sympify(fN, rational = False,evaluate= False).evalf(prec)
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

                                respNatural = fN.subs([(C1,nC1),(C2,nC2),(C3,nC3),(C4,nC4),(C5,nC5)]).evalf(prec)
                                Respostas[2] = respNatural #Adiciona Resposta Natural na lista de respostas

                           # print "Resposta Natural:"
                           # pprint(respNatural)

                                if(Respostas[7] != 0): #Eq. nao homogenea
                                                yt = fN + rP #Yt(t) = Yfn(t) + Yp

                                                #Resposta transitoria é derivada a primeira , segunda, terceira e quarta
                                                y4linhaTran = sympify(yt.diff(t,4), rational = False, evaluate = False).evalf(prec)
                                                y3linhaTran = sympify(yt.diff(t,3), rational = False, evaluate = False).evalf(prec)
                                                y2linhaTran = sympify(yt.diff(t,2), rational = False, evaluate = False).evalf(prec)
                                                ylinhaTran = sympify(yt.diff(t), rational = False, evaluate = False).evalf(prec)
                                                yt  = sympify(yt, rational = False,evaluate= False).evalf(prec)
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

                                                respTrans = yt.subs([(C1,tC1),(C2,tC2),(C3,tC3),(C4,tC4),(C5,tC5)]).evalf(prec)
                                                Respostas[4] = respTrans #Adiciona Resposta Transitoria a lista de respostas

                                                #print "Respsota Transitoria:"
                                                #pprint(respTrans)



                #print "Valor das constantes com t = 0",valorConstantesT0

def idioma_log_print():
    global lingua

    if(lingua==1):
        idi_eq = "Equacao diferencial: "
        idi_hom = "Equacao homogenea: "
        idi_car = "Equacao caracteristica: "
        if(len(Respostas[0])==1):
            idi_raiz = "Raiz: "
        else:
            idi_raiz = "Raizes: "
        if(len(tal)==1):
            idi_tal = "Constante de tempo: "
        else:
            idi_tal = "Constantes de tempo: "
        idi_yfn = "Forma natural de resposta: Yfn(t) = "
        idi_yn = "Resposta natural: Ynat(t) = "
        idi_yp = "Resposta particular: Ypart(t) = "
        idi_ytrans = "Resposta transitoria: Ytrans(t) = "
        idi_yf = "Resposta forcada: Yforc(t) = "
        idi_yc = "Resposta completa: Yc(t) = "
        idi_cond_sing = "Condicao inicial:  "
        idi_cond_pl = "Condicoes iniciais:  "
        return idi_eq, idi_hom, idi_car, idi_raiz, idi_tal, idi_yfn, idi_yn, idi_yp, idi_ytrans, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl

    elif(lingua==2):
        idi_eq = "Differential equation: "
        idi_hom = "Homogenous\ Equation: "
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
        idi_eq = "Ecuacion diferencial: "
        idi_hom = "Ecuacion homogenea: "
        idi_car = "Ecuacion caracteristica: "
        if(len(Respostas[0])==1):
            idi_raiz = "Raiz: "
        else:
            idi_raiz = "Raices: "
        if(len(tal)==1):
            idi_tal = "Constante de tiempo: "
        else:
            idi_tal = "Constantes de tiempo: "
        idi_yfn = "Solucion general: Ygen(t) = "
        idi_yn = "Respuesta natural: Ynat(t) = "
        idi_yp = "Solucion particular: Ypart(t) = "
        idi_ytrans = "Respuesta transitoria: Ytrans(t) = "
        idi_yf = "Respuesta forzada: Yforz(t) = "
        idi_yc = "Respuesta completa: Yc(t) = "
        idi_cond_sing = "Condicion inicial:  "
        idi_cond_pl = "Condiciones iniciales:  "
        return idi_eq, idi_hom, idi_car, idi_raiz, idi_tal, idi_yfn, idi_yn, idi_yp, idi_ytrans, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl

def log_print():

        idi_eq, idi_hom, idi_car, idi_raiz, idi_tal, idi_yfn, idi_yn, idi_yp, idi_ytrans, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl = idioma_log_print()
        equacao = Respostas[8] + Respostas[7]
        equacao = equacao.subs("Derivative(y(t), t)","dy(t)")
        equacao = equacao.subs("Derivative(dy(t), t)","d2y(t)")
        equacao = equacao.subs("Derivative(d2y(t), t)","d3y(t)")
        equacao = equacao.subs("Derivative(d3y(t), t)","d4y(t)")
        equacao = equacao.subs("Derivative(d4y(t), t)","d5y(t)")
        eqCar = equacao

        equacao = str(equacao)
        eqGer = idi_eq+equacao+" = "+str(Respostas[7])
        #print equacao
        str_xT = "x(t) = "
        str_xT = str_xT+"( "+str(Respostas[7])+" )*u(t)"

        eqHom = idi_hom+equacao+" = 0"

        eqCar = eqCar.subs("d2y(t)","r**(2)")
        eqCar = eqCar.subs("dy(t)","r")
        eqCar = eqCar.subs("y(t)","1")
        eqCar = str(eqCar)
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
            str_yp = idi_yp+"( "+str(Respostas[3])+" )*u(t)"
            #print str_yp

            str_ytrans = idi_ytrans+"( "+str(Respostas[4])+" )*u(t)"
            #print str_ytrans

            str_yforc = idi_yf+"( "+str(Respostas[5])+" )*u(t)"
            #print str_yforc
        else:
            str_yp = ""
            str_ytrans = ""
            str_yforc = ""

        str_yc = idi_yc+"( "+str(Respostas[6])+" )*u(t)"
        #print str_yc

        if ((const[5] == 0) and (const[4] == 0) and (const[3] == 0) and (const[2] == 0)):#eq ordem 1
            str_cond_ini = idi_cond_sing+"y(0) = "+str(cond_ini[0])
        else: #eq ordem 2
            str_cond_ini = idi_cond_pl+"y(0) = "+str(cond_ini[0])+"    y'(0) = "+str(cond_ini[1])

        str_resp = eqGer+"\n"+eqHom+"\n"+eqCar+"\n"+str_raiz+"\n"+str_tal+"\n"+str_yfn+"\n"+str_cond_ini+"\n"+str_yn+"\n"+str_xT+"\n"+str_yp+"\n"+str_ytrans+"\n"+str_yforc+"\n"+str_yc
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
    global lingua

    if(lingua==1):
        idi_amp = "Amplitude"
        idi_yn = "Ynat(t)"
        if(len(Respostas[0])==1):
            idi_raiz = "Raiz"
        else:
            idi_raiz = "Raizes"
        idi_real = "Real"
        idi_imag = "Imaginario"
        idi_yp = "Ypart(t)"
        idi_yt = "Ytrans(t)"
        idi_yf = "Yforc(t)"
        idi_yc = "Yc(t)"
        return idi_amp, idi_yn, idi_raiz, idi_real, idi_imag, idi_yp, idi_yt, idi_yf, idi_yc

    elif(lingua==2):
        idi_amp = "Amplitude"
        idi_yn = "Ynat(t)"
        if(len(Respostas[0])==1):
            idi_raiz = "Root"
        else:
            idi_raiz = "Roots"
        idi_real = "Real"
        idi_imag = "Imaginary"
        idi_yp = "Ypart(t)"
        idi_yt = "Ytrans(t)"
        idi_yf = "Yforc(t)"
        idi_yc = "Ycomplete(t)"
        return idi_amp, idi_yn, idi_raiz, idi_real, idi_imag, idi_yp, idi_yt, idi_yf, idi_yc

    else:
        idi_amp = "Amplitud"
        idi_yn = "ynat(t)"
        if(len(Respostas[0])==1):
            idi_raiz = "Raiz"
        else:
            idi_raiz = "Raices"
        idi_real = "Real"
        idi_imag = "Imaginario"
        idi_yp = "ypart(t)"
        idi_yt = "ytrans(t)"
        idi_yf = "yforz(t)"
        idi_yc = "yc(t)"
        return idi_amp, idi_yn, idi_raiz, idi_real, idi_imag, idi_yp, idi_yt, idi_yf, idi_yc


def show_plots():
        global tal, limx_max, limx_min
        idi_amp, idi_yn, idi_raiz, idi_real, idi_imag, idi_yp, idi_yt, idi_yf, idi_yc = idioma_show_plots()

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
        x_t  = drange(limx_min,limx_max,1e-3)

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




        ###Setando o tamanho da fonte  para os plots
        font = {'family' : 'Arial',
        'weight' : 'normal',
        'size'   : 8}

        plt.rc('font', **font)

     
        outputPlots = plt.figure('Plots',facecolor='white')
        plt.subplot(333)
        plt.grid('on')
        plt.title(idi_yn)
        plt.ylabel(idi_amp)
        plt.xlabel("t")
        respNatPlot = plt.plot(x_t,plotNat,lw = 2)

        plt.subplot(331)
        plt.grid('on')
        plt.title("x(t)")
        plt.xlabel("t")
        plt.ylabel(idi_amp)
        plt.axhline(0, color = 'black',lw =2)
        plt.axvline(-0.01, color = 'black',lw =2)
        if plotXt[1] == plotXt[-1]:
                plt.ylim(ymax = plotXt[0] + 0.2*plotXt[0])
        respXtPlot = plt.plot(x_t,plotXt,lw = 2)
   

        


        ax = plt.subplot(334)
        ax.grid('on')
        ax.set_title(idi_raiz)
        ax.set_xlabel(idi_real)
        ax.set_ylabel(idi_imag)
        #plt.scatter(plotRaizesR,plotRaizesC)
        #cli_on=False permite a marcacao 'o' sobrepor a borda do grafico
        #menor e maior raiz aparecendo sempre no limite da borda
        #nao dava pra ver o ponto
        #plt.annotate(xycoords = 'data',)
       # ax.set_ylim(-abs(abs(float(plotRaizesC[0])) +1),abs(abs(float(plotRaizesC[len(plotRaizesC)-1]))+ 1)  )
        #ax.set_xlim(-abs(abs(float(plotRaizesR[0]))+1),abs(abs(float(plotRaizesR[len(plotRaizesR)-1]))+1)  )
        if plotRaizesC[0] != 0:
                ax.set_ylim(float(-abs(plotRaizesC[0] + 0.2*plotRaizesC[0])),float(abs(plotRaizesC[-1]+ 0.2*plotRaizesC[-1]) ))
        else:
                ax.set_ylim(-1,1)
        ax.set_xlim(-(raizesRabs[-1]+ 0.1*raizesRabs[-1]),(raizesRabs[-1]+ 0.1*raizesRabs[-1]))
        respRaizesPlot = ax.plot(plotRaizesR,plotRaizesC,'bx', markersize = 9)
        #ax.axhline(0, color = 'black',lw =1)
        ax.spines['left'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('center')
        ax.spines['top'].set_color('none')
        ax.spines['left']#.set_smart_bounds(True)
        ax.spines['bottom']#.set_smart_bounds(True)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
         
                                              

        plt.subplot(332)
        plt.grid('on')
        plt.title(idi_yp)
        plt.xlabel("t")
        plt.ylabel(idi_amp)
        plt.axhline(0, color = 'black',lw =2)
        if plotPar[0] == plotXt[-1]:
                plt.ylim(ymax = plotPar[0] + 0.2*plotPar[0])
        respParPlot = plt.plot(x_t,plotPar,lw = 2)

        plt.subplot(335)
        plt.grid('on')
        plt.title(idi_yt)
        plt.xlabel("t")
        plt.ylabel(idi_amp)
        plt.axhline(0, color = 'black',lw =2)
        respTranPlot = plt.plot(x_t,plotTran,lw = 2)

        plt.subplot(336)
        plt.grid('on')
        plt.title(idi_yf)
        plt.xlabel("t")
        plt.ylabel(idi_amp)
        plt.axhline(0, color = 'black',lw =2)
        respForPlot = plt.plot(x_t,plotFor,lw = 2)

        plt.subplot(338)
        plt.grid('on')
        plt.title(idi_yf)
        plt.xlabel("t")
        plt.ylabel(idi_amp)
        plt.axhline(0, color = 'black',lw =2)
        respForPlot = plt.plot(x_t,plotFor,lw = 2)

        plt.subplot(339)
        plt.grid('on')
        plt.title(idi_yc)
        plt.xlabel("t")
        plt.ylabel(idi_amp)
        plt.axhline(0, color = 'black',lw =2)
        respComPlot = plt.plot(x_t,plotCom,lw = 2)



        

        plt.subplots_adjust(left=0.08, bottom=0.10, right=0.97, top=0.95,
                                        wspace=0.46, hspace=0.64)

 
        return outputPlots

def idioma_print_latex():
    global lingua

    if(lingua==1):
        if(len(Respostas[0])==1):
            idi_raiz = '$'+latex("Raiz: ")+'$'
        else:
            idi_raiz = '$'+latex("Raizes: ")+'$'
        if(len(tal)==1):
            idi_tal = '$'+latex("Constante\ de\ tempo:\ ")+'$'
        else:
            idi_tal = '$'+latex("Constantes\ de\ tempo:\ ")+'$'
        idi_eq = '$'+latex("Equacao\ diferencial:\ ")+'$'
        idi_hom = '$'+latex("Equacao\ homogenea:\ ")+'$'
        idi_car = '$'+latex("Equacao\ caracteristica:\ ")+ '$'
        idi_yfn = '$'+latex("Y_{fn}(t) = ")+'$'
        idi_yn = '$'+latex("Y_{nat}(t) = ")+'$'
        idi_yp = '$'+latex("Y_{part}(t) = ")+'$'
        idi_yt = '$'+latex("Y_{trans}(t) = ")+'$'
        idi_yf = '$'+latex("Y_{forc}(t) = ")+'$'
        idi_yc = '$'+latex("Y_c(t) = ")+'$'
        idi_cond_sing = latex("Condicao\ inicial:\ ")
        idi_cond_pl =   latex("Condicoes\ iniciais:\ ")
        str_xt = latex("Entrada\ ")
        return idi_raiz, idi_tal, idi_eq,idi_hom, idi_car, idi_yfn, idi_yn, idi_yp, idi_yt, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl, str_xt

    elif(lingua==2):
        if(len(Respostas[0])==1):
            idi_raiz = '$'+latex("Root: ")+'$'
        else:
            idi_raiz = '$'+latex("Roots: ")+'$'
        if(len(tal)==1):
            idi_tal = '$'+latex("Time\ constant:\ ")+'$'
        else:
            idi_tal = '$'+latex("Time\ constants:\ ") +'$'
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
        return idi_raiz, idi_tal, idi_eq, idi_hom, idi_car, idi_yfn, idi_yn, idi_yp, idi_yt, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl, str_xt

    else:
        if(len(Respostas[0])==1):
            idi_raiz = '$'+latex("Raiz: ")+'$'
        else:
            idi_raiz = '$'+latex("Raices: ")+'$'
        if(len(tal)==1):
            idi_tal = '$'+latex("Constante\ de\ tiempo:\ ")+'$'
        else:
            idi_tal = '$'+latex("Constantes\ de\ tiempo:\ ")+'$'
        idi_eq = '$'+latex("Ecuacion\ diferencial:\ ")+'$'
        idi_hom = '$'+latex("Ecuacion\ homogenea:\ ")+'$'
        idi_car = '$'+latex("Ecuacion\ caracteristica:\ ")+ '$'
        idi_yfn = '$'+latex("Y_{gen}(t) = ")+'$'
        idi_yn = '$'+latex("Y_{nat}(t) = ")+'$'
        idi_yp = '$'+latex("Y_{part}(t) = ")+'$'
        idi_yt = '$'+latex("Y_{trans}(t) = ")+'$'
        idi_yf = '$'+latex("Y_{forz}(t) = ")+'$'
        idi_yc = '$'+latex("Y_{c}(t) = ")+'$'
        idi_cond_sing = latex("Condicion\ inicial:\  ")
        idi_cond_pl = latex("Condiciones\ iniciales:\  ")
        str_xt = latex("Entrada\ ")
        return idi_raiz, idi_tal, idi_eq, idi_hom, idi_car, idi_yfn, idi_yn, idi_yp, idi_yt, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl, str_xt


def print_latex():
        global t


        idi_raiz, idi_tal, idi_eq, idi_hom, idi_car, idi_yfn, idi_yn, idi_yp, idi_yt, idi_yf, idi_yc, idi_cond_sing, idi_cond_pl, str_xt = idioma_print_latex()
        #plt.clf()
        #edo_main()

        # 0- Raizes; 1- Forma Natural da respsota; 2- Resposta Natural;
        # 3- Resposta Particular; 4- Resposta Transitoria; 5- Respsota Forcada
        # 6- Resposta Completa; 7-Sinal de entrada x(t); 8 - eq
        ###

        # eqD = Respostas[8] + Respostas[7] #xT esta negativo dentro da equacao, por isso a soma
        # eqDiferencialEntradaLatex = latex(eqD)

#-------------------Equacao em Latex na ordem correta-------------------------------
        eqD = str(const[2])+"\\frac{d^{2}}{d t^{2}}  y{\left (t \\right )}" # as partes escritas entre as aspas sao as formulas das derivadas em latex
        eqC = str(const[2])+"r^{2}"
        if(const[1]<0):
            eqD = eqD+str(const[1])+"\\frac{d}{d t} y{\left (t \\right )}"
            eqC = eqC+str(const[1])+"r"
        else:
            eqD = eqD+"+"+str(const[1])+"\\frac{d}{d t} y{\left (t \\right )}"
            eqC = eqC+"+"+str(const[1])+"r"
        if(const[0]<0):
            eqD = eqD+str(const[0])+"y{\left (t \\right )}"
            eqC = eqC+str(const[0])
        else:
            eqD = eqD+"+"+str(const[0])+"y{\left (t \\right )}"
            eqC = eqC+"+"+str(const[0])

        eqDiferencialEntradaLatex = latex(eqD)
        eqCaracEmLatex = latex(eqC)
#----------------------FIM-----------------------------------------------------------


        ##Perfumaria
        dif = 0.9 -0.77
        xdif = -0.15
        font = {'serif' : 'New Century Schoolbook',
                'weight' : 'normal',
                'size'   : 15}


        plt.rc('font', **font)

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
                        rn = "r"+str(i+1)+" = "
                        rn = '$'+str(latex(rn)) +'$'
                        str_raizLatex = str_raizLatex+"    "+rn+raizEmLatex[i]
                str_r = idi_raiz
        talEmLatex= [0]*(len(tal))
        str_talLatex=""
        for i in range(len(tal)):
                talEmLatex[i] = '$'+str(latex(round(tal[i],prec))) +'$'
        if(len(tal) == 1):
           taln = "\\tau = "
           taln = '$'+str(latex(taln)) +'$'
           str_talLatex = str_talLatex+taln+talEmLatex[0]
           str_t = idi_tal
        else:
                for i in range(len(talEmLatex)):
                        taln = "\\tau"+str(i+1)+" = "
                        taln = '$'+str(latex(taln)) +'$'
                        str_talLatex = str_talLatex+"    "+taln+talEmLatex[i]
                str_t = idi_tal
        ##print len(RespostasEmLatex)
        for i in range(1,8):
                RespostasEmLatex[i] = '$'+str(latex(sympy.powsimp(Respostas[i], combine="exp", deep=True, force=True))) +'$'
        #print RespostasEmLatex
        #xTLatex = '$' + latex(xT) +'$'
        ###Preparando para imprimir
        log_figure = plt.figure("Representacao",facecolor='white')
        ax1 = plt.axes(frameon = False)
        ax1.get_xaxis().tick_bottom()
        ax1.get_xaxis().set_visible(False)
        ax1.axes.get_yaxis().set_visible(False)
        for i in range(0,9,1):
            plt.axhline(0.86-dif*i,xmin = -10,xmax = 5, color = 'black',lw =0.2, linestyle = ':')
        plt.axhline(0.86-dif*4, color='black', lw=2)
        plt.axhline(0.86-dif*5, color='black', lw=2)
        #log_figure.figure("Forma_Representativa:")
        plt.title('')
        plt.text(xdif,0.89,idi_eq+
                 ur'$'+eqDiferencialEntradaLatex+'$'+"  "+
                 ur'$'+latex("=")+'$'+"  "+
                 ur''+RespostasEmLatex[7])

        plt.text(xdif, 0.9-dif,idi_hom+
                 ur'$'+eqDiferencialEntradaLatex+'$'+"  "+
                 ur'$'+latex("=\ 0")+'$'+"   "+
                 idi_car+ur'$'+eqCaracEmLatex+'$'+"  "+
                 ur'$'+latex("=\ 0")+'$')

        plt.text(xdif,0.9-2*dif,str_r+ur''+
                 str_raizLatex)

        plt.text(xdif,0.9-3*dif,str_t+ur''+str_talLatex)
        
        plt.text(xdif,0.9-4*dif,ur''+
                 idi_yfn+ur'$'+latex("(")+'$'+
                 ur''+RespostasEmLatex[1]+
                 ur'$'+latex(")u(t)")+'$')
        
        if((const[5] == 0) and (const[4] == 0) and (const[3] == 0) and (const[2] == 0)):#eq ordem 1
            plt.text(xdif,0.9-5*dif,ur'$'+idi_cond_sing+latex("y(0)= ")+latex(cond_ini[0]) +'$'+"   "
                     ur''+idi_yn+
                     ur'$'+latex("(")+'$'+
                     ur''+RespostasEmLatex[2]+
                     ur'$'+latex(")u(t)")+'$')
        else:
            plt.text(xdif,0.9-5*dif,ur'$'+latex(idi_cond_pl)+latex("y(0)=")+latex(str(cond_ini[0]))+'$'+
                     ur'$'+latex("\ \ \dot y(0)= ")+latex(cond_ini[1]) + '$'+"   "
                     ur''+idi_yn+
                     ur'$'+latex("(")+'$'+ur''+RespostasEmLatex[2]+
                     ur'$'+latex(")u(t)")+'$')


            
        plt.text(xdif,0.9-6*dif,ur'$'+str_xt+latex("x(t) = ($")+
                 ur''+RespostasEmLatex[7]+
                 ur'$'+latex(")u(t)")+'$'+"   "
                 ur''+idi_yp+
                 ur'$'+latex("(")+'$'+
                 ur''+RespostasEmLatex[3]+
                 ur'$'+latex(")u(t)")+'$'
                 )
        
        plt.text(xdif,0.9-7*dif,ur''+idi_yt+
                 ur'$'+latex("(")+'$'+
                 ur''+RespostasEmLatex[4]+
                 ur'$'+latex(")u(t)")+'$')
        
        plt.text(xdif,0.9-8*dif,ur''+idi_yf+
                 ur'$'+latex("(")+'$'+
                 ur''+RespostasEmLatex[5]+
                 ur'$'+latex(")u(t)")+'$')
        
        plt.text(xdif,0.9-9*dif,ur''+idi_yc+
                 ur'$'+latex("(")+'$'+
                 ur''+RespostasEmLatex[6]+
                 ur'$'+latex(")u(t)")+'$')
        #plt.text(xdif,0.9-7*dif,'x(t) = '+ur''+RespostasEmLatex[7])
        

        plt.subplots_adjust(left=0.12, bottom=0.14, right=0.53, top=0.93,
                                                wspace=0.22, hspace=0.21)





        ##log_figure.set_size_inches(19.2,10.8)
        #log_figure.show()
        #plt.show()

        return log_figure


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
                                solvedEq = dsolve(sympify(Respostas[8]), y(t), hint='nth_linear_constant_coeff_homogeneous')
                                #elif (a3 != 0) or (a4 != 0) or (a5 != 0):
                                #solvedEq = dsolve(sympify(eq),y(t),hint='nth_linear_constant_coeff_variation_of_parameters')

                else:           # nth_linear_constant_coeff_variation_of_parameters
                                solvedEq = dsolve(sympify(Respostas[8]), y(t), hint='nth_linear_constant_coeff_undetermined_coefficients')
                                #solvedEq = dsolve(sympify(Respostas[8]), y(t), hint='nth_linear_constant_coeff_variation_of_parameters_Integral')
        
                ##Transformação do tipo sympy_unity para o sympy_mul (mais operações permitidas)
                sepEq = solvedEq._args[1]
                sepEq = sepEq.evalf(prec)

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
                Respostas[3] = RespPart.evalf(prec)
                sepEq = expand(sepEq) #conserta o erro das raizes iguais com entrada igual
                #a eq vinha simplificada e o metodo subs nao reconhecia o RespPart na sepEq, por isso dava erro
                #print "Equacao:",sepEq
                formaNatural = sepEq.subs(RespPart, 0)
                #print "FN=",formaNatural
                
                
                ## fN é a mesma coisa, mas usado por um bug bizarro do Sympy que exige uma variável sem alocações prévias quando diferenciando
                ##isso é válido no método conds_iniciais_aplicadas
                # 0- Raizes; 1- Forma Natural da respsota; 2- Resposta Natural;
                # 3- Resposta Particular; 4- Resposta Transitoria; 5- Respsota Forcada
                # 6- Resposta Completa; 7- xT; 8- eq
                
                fN = formaNatural
##                ### Processamento adicional para o caso de resposta com raizes repetidas E entrada não-homogênea,caso a raiz seja igual a esta entrada esse
##                #processamento se faz necessário
##                if const[5] != 0:
##                                        valorEmT = fN.subs([(C1, 0), (C2, 0), (C3, 0), (C4, 0), (C5, 0)])
##                                        fN = fN.subs(valorEmT*xT,0)
## 
##                elif const[4] != 0:
##                                        valorEmT = fN.subs([(C1, 0), (C2, 0), (C3, 0), (C4, 0)])
##                                        fN = fN.subs(valorEmT*xT,0)
## 
##                elif const[3] != 0:
##                                         valorEmT = fN.subs([(C1, 0), (C2, 0), (C3, 0)])
##                                         fN = fN.subs(valorEmT*xT,0)
## 
##                elif const[2] != 0:
##                                         t = Symbol('t')
##                                         valorEmT = fN.subs([(C1, 0), (C2, 0)])
##                                         sympify(valorEmT)
##                                         print "fN: ",fN
##                                         fN = fN.subs(valorEmT,0.0)
##                                         print "Entrei"+ " ValoremT ",valorEmT,"Fn:",fN,type(valorEmT),type(fN)
##
##                elif const[1] != 0:
##                                         valorEmT = fN.subs([(C1, 0)])
##                                         print "fN: ",fN
##                                         fN = sympify(fN - valorEmT)
##                                         print "Entrei"+ " ValoremT ",valorEmT,"Fn:",fN,type(valorEmT),type(fN)
 
                Respostas[1] = formaNatural #Adicionando Forma natural de resposta na lista de respostas

                
                rP = RespPart.evalf(prec)
                raizes()
                cte_tempo()
                conds_iniciais_aplicadas(fN, rP)

                respForc = Respostas[4] + Respostas[3] #Yf = Yt + Yp
                Respostas[5] = respForc.evalf(prec)   #Adiciona Resposta Forcada a lista de respostas


                respComp = Respostas[2]  #Resposta completa p/ eqs. homogeneas
                if(Respostas[7] != 0): #Eqs. nao homogeneas
                                respComp = Respostas[2] + Respostas[5]  #Respsota completa p/ eqs. nao-homogeneas

                Respostas[6] = respComp.evalf(prec)  #Adiciona Resposta Completa a lista de respostas

                for i in range(1,7): #arruma precisao
                        # Respostas[i] = expand(Respostas[i])
                        Respostas[i] = nsimplify(Respostas[i], rational = True,tolerance = 0.05).evalf(prec)
        except:
                pass





