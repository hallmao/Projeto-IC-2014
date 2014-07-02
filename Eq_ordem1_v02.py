import matplotlib.pyplot as plt
from   math  import sin,cos,e,exp 
from   numpy import array
from   numpy import arange

###Funções renomeadas para facilitar digitação




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

print "Entre com os coefs para uma EDO do tipo a1*y´(t) + a0*(t)  = b0*x(t)"

#Entrada porca no console (só pra testes,claro !)
a1 = float(input("a1 = "))
a0 = float(input("a0 = "))
b0 = float(input("b0 = "))
y0 = float(input("Condicao Inicial de y(0) =  "))
print "Entrada x(t),favor inserir no formato e(q*t),sin(q*t),cos(q*t) onde q é uma cte:"
xT = raw_input("x(t) = ")

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
    print "Forma natural da resposta:\n"+"yfn(t)= " + "C*e^("+str(r)+"t)*u(t)"
##Resposta forma natural com conds iniciais
    print "\nResposta natural:\n"+"ynat(t)= " +str(y0)+"*e^("+str(r)+"t)*u(t)"
    ##Resposta completa
    if b0 == 0:
        print "\nResposta completa : yc(t) = ynat(t) + yfor(t)"
        print "yc(t) = ("+str(y0)+"*"+"e^("+str(r)+"t)*u(t)"

    
    if b0 != 0 :
        print "\nResposta forçada"
        print "ypart(t) ="+str((b0/a0))+"*("+xT+")*u(t)"
        ##ytran(t)
        print "ytran(t) = "+str((-b0/a0))+"*("+xT+")*e^("+str(r)+"t)*u(t)"
        ## Yforçada(t)
        print "yfor(t) = ytran(t) + ypart(t)"
        print "yfor(t) = "+str((-b0/a0))+"*("+xT+")*e^("+str(r)+"t)*u(t) + "+str((b0/a0))+"*"+xT+"*u(t)"
        ###Resposta completa
        print "\nResposta completa : yc(t) = ynat(t) + yfor(t)"
        print "yc(t) = ("+str(y0)+str(-b0/a0)+"*("+xT+")*e^("+str(r)+"t)*u(t) + "+str((b0/a0))+"*"+xT+"*u(t)"
    


#Print

log_print()


#def plot_and_show:



    


    
    
    
    
    











