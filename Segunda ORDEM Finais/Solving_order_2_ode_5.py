from sympy import Function, dsolve, pprint, exp, cos
from sympy.abc import t
from sympy import *



##Loop para testes
while True:

    #Entrada pelo console
    def input_coefs():
        global a5,a4,a3,a2,a1,a0,xT
        print "Insira os coefs e entrada para uma EDO do tipo: "
        print "a5*y'''''(t) + a4*y''''(t) + a3*y'''(t)  + a2*y''(t) +a1*y'(t) +a0*y(t) = x(t)"
        a5 = input("a5:")
        a4 = input("a4:")
        a3 = input("a3:")
        a2 = input("a2:")
        a1 = input("a1:")
        a0 = input("a0:")   
        xT = input("x(t):")



    input_coefs()

    try :
        xT = float(xT)
    except :
        pass
    print type(xT)

    ##Defining our function
    y = Function('y')

    ##Adicionando os coefs a eq diferencial
    eq =sympify(a5*y(t).diff(t,5)+ a4*y(t).diff(t,4) + a3*y(t).diff(t,3)+ a2*y(t).diff(t,2) + a1*y(t).diff(t) +a0*y(t) -xT)



    pprint(eq)
    print ""

    ###Dif equation solver

    ##Sets if it is of homogenous or inhomogenous type and type of resolution method
    if xT == 0:
        solvedEq = dsolve(sympify(eq),y(t),hint='nth_linear_constant_coeff_homogeneous')
    elif (a3 != 0) or (a4 != 0) or (a5 != 0):
        #solvedEq = dsolve(sympify(eq),y(t),hint='nth_linear_constant_coeff_variation_of_parameters')
        pass
    else:
        solvedEq = dsolve(sympify(eq),y(t),hint='nth_linear_constant_coeff_undetermined_coefficients')

    ##Transformação do tipo sympy_unity para o sympy_mul (mais operações permitidas)
    sepEq = solvedEq._args[1]

    print(sympify(solvedEq, rational = False , evaluate = False).evalf(2))

    ##PRocesso de separação de resp natural e resposta transitória ---
    #SEPARACAO FUNCIONAL SOMENTE PARA GRAU 1 E 2
    #elementosEq = sepEq.atoms(Symbol)
    #C1 = elementosEq.pop()
    #C2 = elementosEq.pop()

    C1,C2,C3,C4,C5 = symbols("C1 C2 C3 C4 C5")

    print C1,C2

    if   a5 != 0:
        RespTran =  sepEq.subs([(C1,0),(C2,0),(C3,0),(C4,0),(C5,0)])
    elif a4 != 0:
        RespTran =  sepEq.subs([(C1,0),(C2,0),(C3,0),(C4,0)])
    elif a3 != 0:
        RespTran =  sepEq.subs([(C1,0),(C2,0),(C3,0)])
    elif a2 != 0:
        RespTran =  sepEq.subs([(C1,0),(C2,0)])
    elif a1 != 0:
        RespTran =  sepEq.subs(C1,0)

##    if C2 != t :
##        #print "Tem c2"
##        RespTran =  sepEq.subs([(C2,0),(C1,0)])
##        
##        
##    else:
##        RespTran =  sepEq.subs(C1,0)
        
    ##Resposta transitória alocada em  RespTran, natural em RespNat

    RespNat  =  sepEq.subs(RespTran,0)

    print (RespTran)
    print (RespNat)


    ##Saida
    
