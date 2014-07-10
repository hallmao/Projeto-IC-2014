import matplotlib.pyplot as plt
from math import e
from numpy import array,sin,cos,exp
from numpy import arange



#-----EDO Linear 2ªOrdem c/ coeficientes constantes----------------------------
# Eq. Geral: a2*y"(t) + a1*y'(t) + a0*y(t) = b0(t)
#
# Eq. Homogênea: a2*y"(t) + a1*y'(t) + a0*y(t) = 0
# Eq. caracteristica: a2*r² + a1*r + a0 = 0
#
# --Raízes:
# Delta: a1² - 4*a2*a0      ==> Delta > 0 : Raizes reais e distintas
#                               Delta = 0 : Raizes repetidas, r=r1=r2
#                               Delta < 0 : Raizes complexas
#
# Bhaskara: r1 = ((-a1)+sqr(delta))/(2*a2)      r2 = ((-a1)-sqr(delta))/(2*a2)
#
###Delta > 0 : Raizes reais e distintas
#    ---Forma natural de resposta: Yfn(t) = C1*e^(r1*t) + C2*e^(r2*t)
#    ---Resposta natural:
#                   condicao inicial: y(0) = y0 ; y'(0) = dy0
#                   y'(t) = r1*C1*e^(r1*t) + r2*C2*e^(r2*t)
#
#                   y(0) = y0 => y0 = C1*e^(r1*0) + C2*e^(r2*0) => y0 = C1 + C2
#                   y'(0) = dy0 => dy0 = r1*C1*e^(r1*0) + r2*C2*e^(r2*0) => dy0 = r1*C1 + r2*C2
#
#                   C1 = y0 - C2    |   r1*(y0-C2) + r2*C2 = dy0
#                                   |   r1*y0 - r1*C2 + r2*C2 = dy0
#                                   |   C2*(r2-r1) = dy0 - r1*y0
#                                   |   C2 = (dy0 - r1*y0)/(r2-r1) ##var c2
#                   C1 = y0 - (dy0 - r1*y0)/(r2-r1) ##var c1
#
#       Ynat(t) = c1*e^(r1*t) + c2*e^(r2*t)
#
###Delta = 0 : Raizes repetidas, r=r1=r2
#   r = -b/(2*a2)  ##bhaskara simplificado
#   y1(t) = e^(r*t)
#   Precisa achar uma segunda solução que é linearmente independente da primeira
#   y(t) = v(t)*y1(t) = v(t)*e^(r*t)
#   y'(t) = v'(t)*e^(r*t) + r*v(t)*e^(r*t)
#   y"(t) = v"(t)*e^(r*t) + 2r*v'(t)*e^(r*t) + r²*v(t)*e^(r*t)
#   Substituir na eq. homogênea:
#       a2*(v"(t)*e^(r*t) + 2r*v'(t)*e^(r*t) + r²*v(t)*e^(r*t)) + a1*(v'(t)*e^(r*t) + r*v(t)*e^(r*t)) + a0*(v(t)*e^(r*t)) = 0
#       v"(t) = 0 ; v'(t) = C1 ; v(t) = C1 + C2*t
#   
#    ---Forma natural de resposta: Yfn(t) = C1*e^(r*t) + C2*t*e^(r*t)
#    ---Resposta natural:
#                   condicao inicial: y(0) = y0 ; y'(0) = dy0
#                   y'(t) = C1*r*e^(r*t) + C2*e^(r*t) + C2*t*r*e^(r*t)
#
#                   y(0) = y0 => y0 = C1*e^(r*0) + C2*0*e^(r*0) => C1 = y0  ##var c1
#                   y'(0) = dy0 => dy0 = C1*r*e^(r*0) + C2*e^(r*0) + C2*0*r*e^(r*0)
#                               => dy0 = y0*r + C2
#                               => C2 = dy0 - y0*r  ##var c2
#       Ynat(t) = c1*e^(r*t) + c2*t*e^(r*t)
#
###Delta < 0 : Raizes complexas
#   r1 = r + u*i ; r2 = r - u*i
#   y1 = C1*e^(r1*t) ; y2 = C2*e^(r2*t)
#   y = y1 + y2 = e^(r*t)*[Ca*e^(u*i*t) + Cb*e^(-u*i*t)]
#   Usando a Fórmula de Euler: e^(i*t) = cos(t) + i*sen(t)
#                              e^(-i*t) = cos(t) - i*sen(t)
#
#   y = e^(r*t)*[(Ca+Cb)*cos(u*t) + (Ca-Cb)*i*sen(u*t)] ; (Ca+Cb) = C1 ; (Ca-Cb) = C2
#   y = e^(r*t)*[C1*cos(u*t) + C2*i*sen(u*t)]
#   Se y1 e y2 são soluções da eq., então qualquer combinação linear de y1 e y2
#   também é solução.
#   u(t) = e^(r*t)*cos(u*t); v(t) = e^(r*t)*sen(u*t)
#   Se o wronskiano W(u,v)(t) for diferente de 0 a solução geral da eq. pode ser
#   escrita como:
#    ---Forma natural de resposta: Yfn(t) = e^(r*t)*[C1*cos(u*t) + C2*sen(u*t)]
#    ---Resposta natural:
#             condicao inicial: y(0) = y0 ; y'(0) = dy0
#             y'(t) = e^(r*t)*[sen(u*t)*(C2*r - C1*u) + cos(u*t)*(C1*r + C2*u)]
#
#               y(0) = y0 => y0 = e^(r*0)*[C1*cos(u*0) + C2*sen(u*0]
#                         => y0 = C1    ##var c1
#               y'(0) = dy0 => dy0 = e^(r*0)*[sen(u*0)*(C2*r - C1*u) + cos(u*0)*(C1*r + C2*u)]
#                           => dy0 = y0*r + C2*u
#                           => C2 = (dy0 - y0*r)/u  ##var c2
#       Ynat(t) = e^(r*t)*[c1*cos(u*t) + c2*sen(u*t)]
#

print "Entre com os coefs para uma EDO do tipo a2*y''(t) + a1*y'(t) + a0*y(t) = b0*x(t)"

a2 = float(input("a2 = "))
a1 = float(input("a1 = "))
a0 = float(input("a0 = "))
b0 = float(input("b0 = ")) #por enquanto só funciona com b0 = 0
y0 = float(input("Condicao inicial de y(0) = "))
dy0 = float(input("Condicao inicial de y'(0) = "))


#Delta
delta = ((a1*a1)-(4*a2*a0))

#tipo_r eh uma variavel auxiliar
#tipo_r = 0 --> raizes reais e distintas; delta > 0
#tipo_r = 1 --> raizes repetidas; delta = 0
#tipo_r = 2 --> raizes complexas conjugadas; delta < 0

#Raizes r1 e r2
if (delta > 0):
    tipo_r = 0
    #Fórmula de Bhaskara para achar as raizes
    r1 = ((-a1)+(delta**(0.5)))/(2*a2)
    r2 = ((-a1)-(delta**(0.5)))/(2*a2)
    # Yfn(t) = C1*e^(r1*t) + C2*e^(r2*t)

    #cond inicial
    c2 = (dy0 - r1*y0)/(r2-r1)
    c1 = y0 - c2
    # Ynat(t) = c1*e^(r1*t) + c2*e^(r2*t)

if (delta == 0):
    tipo_r = 1
    #r1=r2=r=(-a1)/(2*a2)
    r=(-a1)/(2*a2)
    # Yfn(t) = C1*e^(r*t) + C2*t*e^(r*t)

    #cond inicial
    c1 = y0
    c2 = dy0 - (y0*r)
    # Ynat(t) = c1*e^(r*t) + c2*t*e^(r*t)

if (delta < 0):
    tipo_r = 2
    r = (-a1)/(2*a2) #parte real das raizes
    r_u = (delta*(-1))**(0.5) #sqrt(-x) = sqrt(x)*sqrt(-1) = sqrt(x)*i //parte imaginaria
    #u eh a parte imaginaria das raizes
    u = r_u/(2*a2)
    # Yfn(t) = e^(r*t)*[C1*cos(u*t) + C2*sen(u*t)]

    #cond inicial
    c1 = y0
    c2 = (dy0-(c1*r))/u
    # Ynat(t) = e^(r*t)*[c1*cos(u*t) + c2*sen(u*t)]
    

def log_print():
    print "Eq diferencial:\n"+str(a2)+"*y''(t) + "+str(a1)+"y'(t) + "+str(a0)+"y(t) = "+str(b0)+"*x(t)\n"

    if (tipo_r == 0):
        print "Forma natural de resposta:\n"+"yfn(t) = C1*e^("+str(round(r1,2))+"*t) + C2*e^("+str(round(r2,2))+"*t)"
        #Resposta forma natural c/ conds iniciais
        print "\nResposta natural:\n"+"ynat(t) = "+str(round(c1,2))+"*e^("+str(round(r1,2))+"*t) + "+str(round(c2,2))+"*e^("+str(round(r2,2))+"*t)"

    if (tipo_r == 1):
        print "Forma natural de resposta:\n"+"yfn(t) = C1*e^("+str(round(r,2))+"*t) + C2*t*e^("+str(round(r,2))+"*t)"
        #Resposta forma natural c/ conds iniciais
        print "\nResposta natural:\n"+"ynat(t) = "+str(round(c1,2))+"*e^("+str(round(r,2))+"*t) + "+str(round(c2,2))+"*t*e^("+str(round(r,2))+"*t)"

    if (tipo_r == 2):
        print "Forma natural de resposta:\n"+"yfn(t) = e^("+str(round(r,2))+"*t)*[C1*cos("+str(round(u,2))+"*t) + C2*sen("+str(round(u,2))+"*t)]"
        #Resposta forma natural c/ conds iniciais
        print "\nResposta natural:\n"+"yfn(t) = e^("+str(round(r,2))+"*t)*["+str(round(c1,2))+"*cos("+str(round(u,2))+"*t) + "+str(round(c2,2))+"*sen("+str(round(u,2))+"*t)]"
        
log_print()
