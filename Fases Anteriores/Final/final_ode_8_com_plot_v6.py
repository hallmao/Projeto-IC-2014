from numpy.core.defchararray import decode, replace
import sympy.assumptions.handlers.calculus
import sympy.assumptions.handlers.ntheory
import sympy.assumptions.handlers.order
import sympy.assumptions.handlers.sets
from sympy import Function, pprint, exp, cos, init_printing, sympify, dsolve, symbols,mpmath, solve, lambdify, sin, im, \
        re, latex
from sympy.abc import t
import matplotlib.pyplot as plt
from numpy import  arange



###Parâmetros a serem considerados

###Precisão Decimal
prec = 2 ## Numero de digitos decimais de precisão mostrados no log de dados
###Configurações do pprint, registradas somente uma vez

#setattr(pprint,'num_columns',5)
#setattr(pprint,'use_unicode',True)
#setattr(pprint,'order','none')


        #("num_columns = 100,use_unicode = True,order = 'none'")




###Uses the best printing available for pprint
init_printing( use_latex=True)



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
# 6- Resposta Completa
Respostas = [0]*7

#Entrada pelo console
def input_coefs():
                global a5, a4, a3, a2, a1, a0, xT
                print "Insira os coefs e entrada para uma EDO do tipo: "
                print "a5*y'''''(t) + a4*y''''(t) + a3*y'''(t)  + a2*y''(t) +a1*y'(t) +a0*y(t) = x(t)"
                #a5 = input("a5:")
                #a4 = input("a4:")
                #a3 = input("a3:")
                a2 = input("a2:")
                a1 = input("a1:")
                a0 = input("a0:")
                xT = input("x(t):")

input_coefs()

try:
                xT = float(xT)
except:
                pass
#print type(xT)

##Defining our function
y = Function('y')

#### THERMS a3 to a5 DISABLED !!
a5 = a4 = a3 = 0

##Adicionando os coefs a eq diferencial
eq = sympify(
                a5 * y(t).diff(t, 5) + a4 * y(t).diff(t, 4) + a3 * y(t).diff(t, 3) + a2 * y(t).diff(t, 2) + a1 * y(t).diff(
                                t) + a0 * y(t) - xT)





###Dif equation solver

##Sets if it is of homogenous or inhomogenous type and type of resolution method
if xT == 0:
                solvedEq = dsolve(sympify(eq), y(t), hint='nth_linear_constant_coeff_homogeneous')
                #elif (a3 != 0) or (a4 != 0) or (a5 != 0):
                #solvedEq = dsolve(sympify(eq),y(t),hint='nth_linear_constant_coeff_variation_of_parameters')

else:
                solvedEq = dsolve(sympify(eq), y(t), hint='nth_linear_constant_coeff_undetermined_coefficients')

##Transformação do tipo sympy_unity para o sympy_mul (mais operações permitidas)
sepEq = solvedEq._args[1]


C1, C2, C3, C4, C5 = symbols("C1 C2 C3 C4 C5")


if a5 != 0:
                RespPart = sepEq.subs([(C1, 0), (C2, 0), (C3, 0), (C4, 0), (C5, 0)])
elif a4 != 0:
                RespPart = sepEq.subs([(C1, 0), (C2, 0), (C3, 0), (C4, 0)])
elif a3 != 0:
                RespPart = sepEq.subs([(C1, 0), (C2, 0), (C3, 0)])
elif a2 != 0:
                RespPart = sepEq.subs([(C1, 0), (C2, 0)])
elif a1 != 0:
                RespPart = sepEq.subs(C1, 0)



##Resposta transitória alocada em  RespTran, natural em RespNat


Respostas[3] = RespPart.evalf(prec)
formaNatural = sepEq.subs(RespPart, 0)
Respostas[1] = formaNatural #Adicionando Forma natural de resposta na lista de respostas
## fN é a mesma coisa, mas usado por um bug bizarro do Sympy que exige uma variável sem alocações prévias quando diferenciando
##isso é válido no método conds_iniciais_aplicadas
fN = formaNatural
rP = RespPart.evalf(prec)



def raizes():
                #polyroots retorna uma lista
                if(a5 != 0):
                                roots = mpmath.polyroots([a5, a4, a3, a2, a1, a0])
                           # print roots[0], roots[1], roots[2], roots[3], roots[4]
                elif((a5 == 0) and (a4 !=0)):
                                roots = mpmath.polyroots([a4, a3, a2, a1, a0])
                           # print roots[0], roots[1], roots[2], roots[3]
                elif((a4 == 0) and (a3 !=0)):
                                roots = mpmath.polyroots([a3, a2, a1, a0])
                           # print roots[0], roots[1], roots[2]
                elif((a3 == 0) and (a2 !=0)):
                                roots = mpmath.polyroots([a2, a1, a0])
                           # print roots[0], roots[1]
                elif((a2 == 0) and (a1 !=0)):
                                roots = mpmath.polyroots([a1, a0])
                           # print roots[0]


                Respostas[0] = roots

raizes()


def conds_iniciais_aplicadas():

                print "Favor inserir as conds iniciais y(0) e y'(0)...:"

                ##Verificando a ordem da EDO para se ter o numero correto de conds Iniciais e
                #uma resolução própria

                #Ordem 1
                if ((a5 == 0) and (a4 == 0)
                   and (a3 == 0) and (a2 == 0)):
                                #Entrada cond inicial:
                                y0 = input("y(0): ")
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

                                if(xT != 0):    #Eq. nao homogenea
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
                elif ((a5 == 0) and (a4 == 0)
                   and (a3 == 0)):
                                y0 = input("y(0): ")
                                dy0 = input("y'(0): ")

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

                                if(xT != 0): #Eq. nao homogenea
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
                elif ((a5 == 0) and (a4 == 0)):
                                y0 = input("y(0): ")
                                dy0 = input("y'(0): ")
                                d2y0 = input("y''(0): ")


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


                                if(xT != 0): #Eq. nao homogenea
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
                elif ((a5 == 0)):
                                y0 = input("y(0): ")
                                dy0 = input("y'(0): ")
                                d2y0 = input("y''(0): ")
                                d3y0 = input("y'''(0): ")


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

                                if(xT != 0): #Eq. nao homogenea
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
                                y0 = input("y(0): ")
                                dy0 = input("y'(0): ")
                                d2y0 = input("y''(0): ")
                                d3y0 = input("y'''(0): ")
                                d4y0 = input("y''''(0): ")

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

                                if(xT != 0): #Eq. nao homogenea
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


conds_iniciais_aplicadas()

respForc = Respostas[4] + Respostas[3] #Yf = Yt + Yp
Respostas[5] = respForc.evalf(prec)   #Adiciona Resposta Forcada a lista de respostas


respComp = Respostas[2]  #Resposta completa p/ eqs. homogeneas
if(xT != 0): #Eqs. nao homogeneas
                respComp = Respostas[2] + Respostas[5]  #Respsota completa p/ eqs. nao-homogeneas

Respostas[6] = respComp.evalf(prec)  #Adiciona Resposta Completa a lista de respostas


def log_print():
        equacao = eq + xT
        equacao = equacao.subs("Derivative(y(t), t)","dy(t)")
        equacao = equacao.subs("Derivative(dy(t), t)","d2y(t)")
        equacao = equacao.subs("Derivative(d2y(t), t)","d3y(t)")
        equacao = equacao.subs("Derivative(d3y(t), t)","d4y(t)")
        equacao = equacao.subs("Derivative(d4y(t), t)","d5y(t)")

        equacao = str(equacao)
        equacao = "Equacao: "+equacao+" = "+str(xT)
        #print equacao

        str_raiz = "Raiz(es):"
        count = 0
        while(count < len(Respostas[0])):
                str_raiz = str_raiz+"\tr"+str(count+1)+"= "+str(Respostas[0][count])
                count = count+ 1
        #print str_raiz

        str_yfn = "Forma natural de resposta: Yfn(t) = "+str(Respostas[1])
        #print str_yfn

        str_yn = "Resposta natural: Yn(t) = "+str(Respostas[2])
        #print str_yn

        if(xT != 0):
            str_yp = "Resposta particular: Yp(t) = "+str(Respostas[3])
            #print str_yp
            
            str_ytrans = "Resposta Transitoria: Ytrans(t) = "+str(Respostas[4])
            #print str_ytrans

            str_yforc = "Resposta forcada: Yforc(t) = "+str(Respostas[5])
            #print str_yforc
        else:
            str_yp = ""
            str_ytrans = ""
            str_yforc = ""

        
        str_yc = "Resposta completa: Yc(t) = "+str(Respostas[6])
        #print str_yc

        str_resp = equacao+"\n"+str_raiz+"\n"+str_yfn+"\n"+str_yn+"\n"+str_yp+"\n"+str_ytrans+"\n"+str_yforc+"\n"+str_yc
        print str_resp

        #return c tds as respostas em uma variavel
        return str_resp

        ##return c cada resposta sendo uma variavel
        #return equacao, str_raiz, str_yfn, str_yn, str_yp, str_ytrans, str_yforc, str_yc


log_print()



def conversao_numpy(symbol):
        ###Transforma todas as respostas em funcoes Lambda
        #Compativeis de forma nativa no python e sem a necessidade de bibliotecas externas
        ##Array with same length as Respostas variable
        plots_numpy = [0]*len(Respostas)



### SIM SIM EU SEI USA UMA ITERACAO AKA FOR, mas ai...
## quem é que vai entender isso mês que vem ?
        ##Entrada x(t)
        plots_numpy[1] = lambdify(t,sympify(xT))
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





###Funcoes lambda compativeis com o numpy
plots_numpy = conversao_numpy(t)





def show_plots():


        ## Nossa variável de deslocamento t no eixo x
        #x_t = drange(0,10,0.00001)
        x_t  = arange(0.0,5.0,0.01)


        ###Nossas Variaveis de plot, todas tem o mesmo tamanho do vetor x_t
        ##Now they have equal length
        plotXt    = [0]*len(x_t)
        plotNat   = [0]*len(x_t)
        plotPar   = [0]*len(x_t)
        plotTran  = [0]*len(x_t)
        plotFor   = [0]*len(x_t)
        plotCom   = [0]*len(x_t)

        ##Separando parte real e imaginária das raízes
        plotRaizesT = (Respostas[0])
        plotRaizesC = [0]*len(plotRaizesT)
        plotRaizesR = [0]*len(plotRaizesT)

        for i in range(len(plotRaizesT)):

                plotRaizesC[i] = im(plotRaizesT[i])
                plotRaizesR[i] = re(plotRaizesT[i])


        print  len(plotRaizesC),plotRaizesC,type(plotRaizesC)
        print  len(plotRaizesR),plotRaizesR,type(plotRaizesR)               
        #menor raiz na primeira posicao e maior raiz na ultima posicao
        #necessario para o range do plot
        plotRaizesR.sort()
        plotRaizesC.sort()







        try:

                for i in range(len(x_t)):
                        plotXt[i]      = plots_numpy[1](x_t[i])
                        plotNat[i]     = plots_numpy[2](x_t[i])
                        plotPar[i]     = plots_numpy[3](x_t[i])
                        plotTran[i]    = plots_numpy[4](x_t[i])
                        plotFor[i]     = plots_numpy[5](x_t[i])
                        plotCom[i]     = plots_numpy[6](x_t[i])


        ###Setando o tamanho da fonte  para os plots
                font = {'family' : 'Arial',
                'weight' : 'normal',
                'size'   : 8}

                plt.rc('font', **font)



                outputPlots = plt.figure('Plots',facecolor='white')
                plt.subplot(333)
                plt.grid('on')
                plt.title("ynat(t)")
                plt.ylabel("Amplitude")
                plt.xlabel("t")
                respNatPlot = plt.plot(x_t,plotNat,lw = 2)

                plt.subplot(334)
                plt.grid('on')
                plt.title("Raizes")
                plt.xlabel("Real")
                plt.ylabel("Imaginario")
                #plt.scatter(plotRaizesR,plotRaizesC)
                #cli_on=False permite a marcacao 'o' sobrepor a borda do grafico
                #menor e maior raiz aparecendo sempre no limite da borda
                #nao dava pra ver o ponto
                #plt.annotate(xycoords = 'data',)
                plt.ylim(-abs(abs(float(plotRaizesC[0]))*2 +1),abs(abs(float(plotRaizesC[len(plotRaizesC)-1]))+ 1)  )
                plt.xlim(-abs(abs(float(plotRaizesR[0]))*2+1),abs(abs(float(plotRaizesR[len(plotRaizesR)-1]))+1)  )
                plt.axhline(0, color = 'black',lw =1)
                respRaizesPlot = plt.stem(plotRaizesR,plotRaizesC,markerfmt='bo',)

                plt.subplot(332)
                plt.grid('on')
                plt.title("ypar(t)")
                plt.xlabel("t")
                plt.ylabel("Amplitude")
                plt.axhline(0, color = 'black',lw =2)
                respParPlot = plt.plot(x_t,plotPar,lw = 2)

                plt.subplot(335)
                plt.grid('on')
                plt.title("ytran(t)")
                plt.xlabel("t")
                plt.ylabel("Amplitude")
                plt.axhline(0, color = 'black',lw =2)
                respTranPlot = plt.plot(x_t,plotTran,lw = 2)

                plt.subplot(336)
                plt.grid('on')
                plt.title("yfor(t)")
                plt.xlabel("t")
                plt.ylabel("Amplitude")
                plt.axhline(0, color = 'black',lw =2)
                respForPlot = plt.plot(x_t,plotFor,lw = 2)

                plt.subplot(338)
                plt.grid('on')
                plt.title("yfor(t)")
                plt.xlabel("t")
                plt.ylabel("Amplitude")
                plt.axhline(0, color = 'black',lw =2)
                respForPlot = plt.plot(x_t,plotFor,lw = 2)

                plt.subplot(339)
                plt.grid('on')
                plt.title("yc(t)")
                plt.xlabel("t")
                plt.ylabel("Amplitude")
                plt.axhline(0, color = 'black',lw =2)
                respComPlot = plt.plot(x_t,plotCom,lw = 2)

                plt.subplot(331)
                plt.grid('on')
                plt.title("x(t)")
                plt.xlabel("t")
                plt.ylabel("Amplitude")
                plt.axhline(0, color = 'black',lw =2)
                respXtPlot = plt.plot(x_t,plotXt,lw = 2)

                plt.subplots_adjust(left=0.05, bottom=0.10, right=0.97, top=0.95,
                                                wspace=0.46, hspace=0.64)


                #plt.tight_layout()#automaticamente ajusta os subplots para nao se sobreporem
                #e para caberem dentro da janela



                plt.show()
                return outputPlots

        except:
                pass

def print_latex():



        # 0- Raizes; 1- Forma Natural da respsota; 2- Resposta Natural;
        # 3- Resposta Particular; 4- Resposta Transitoria; 5- Respsota Forcada
        # 6- Resposta Completa
        # 7-Sinal de entrada x(t)
        ###
        eqDiferencialEntradaLatex = latex(eq)

        ##Perfumaria
        dif = 0.9 -0.77
        xdif = -0.15
        font = {'family' : 'Sans',
                'weight' : 'normal',
                'size'   : 18}

        plt.rc('font', **font)

        ##Obtendo as respostas em Latex
        RespostasEmLatex = [0]*(len(Respostas))
        raizEmLatex = [0]*(len(Respostas[0]))
        str_raizLatex =""
        for i in range(len(Respostas[0])):
                raizEmLatex[i] = '$'+str(latex(Respostas[0][i])) +'$'
        for i in range(len(raizEmLatex)):
                rn = "r"+str(i+1)+" = "
                rn = '$'+str(latex(rn)) +'$'
                str_raizLatex = str_raizLatex+"\t"+rn+raizEmLatex[i]
        ##print len(RespostasEmLatex)
        for i in range(len(Respostas)):
                RespostasEmLatex[i] = '$'+str(latex(Respostas[i])) +'$'
        #print RespostasEmLatex
        xTLatex = '$' + latex(xT) +'$'
        ###Preparando para imprimir
        log_figure = plt.figure("Representacao",facecolor='white')
        ax1 = plt.axes(frameon = False)
        ax1.get_xaxis().tick_bottom()
        ax1.get_xaxis().set_visible(False)
        ax1.axes.get_yaxis().set_visible(False)
        for i in range(0,8,1):
                plt.axhline(0.86-dif*i,xmin = -5,xmax = 5, color = 'black',lw =0.2, linestyle = ':')
        #log_figure.figure("Forma_Representativa:")
        plt.title("Eq dif:"+ur''+eqDiferencialEntradaLatex)
        plt.text(xdif,0.9,'Forma Natural:'+ur''+RespostasEmLatex[1])
        plt.text(xdif,0.9-dif,'yn(t) = '+ur''+RespostasEmLatex[2])
        plt.text(xdif,0.9-2*dif,'ypar(t) = '+ur''+RespostasEmLatex[3])
        plt.text(xdif,0.9-3*dif,'ytran(t) = '+ur''+RespostasEmLatex[4])
        plt.text(xdif,0.9-4*dif,'yfor(t) = '+ur''+RespostasEmLatex[5])
        plt.text(xdif,0.9-5*dif,'yc(t) = '+ur''+RespostasEmLatex[6])
        plt.text(xdif,0.9-6*dif,'x(t) = '+ur''+xTLatex)
        plt.text(xdif,0.9-7*dif,'Raiz(es): '+ur''+str_raizLatex)

        log_figure.show()








print_latex()
show_plots()




