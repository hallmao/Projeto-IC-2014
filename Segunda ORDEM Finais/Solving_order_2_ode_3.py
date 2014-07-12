from sympy import Function, dsolve, pprint, exp, cos
from sympy.abc import t
from sympy import *

#C1,C2 = symbols("C1 C2")


##Loop para testes
while True:

    #Entrada pelo console
    def input_coefs():
        global a2,a1,a0,xT
        print "Insira os coefs e entrada para uma EDO do tipo: "
        print "     a2*y''(t) +a1*y'(t) +a0*y(t) = x(t)"
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
    y = Function('y')

    ##Adicionando os coefs a eq diferencial
    eq =sympify(a2*y(t).diff(t,2) + a1*y(t).diff(t) +a0*y(t) -xT)



    pprint(eq)
    print ""

    ###Dif equation solver
    if xT == 0:
	    solvedEq = dsolve(sympify(eq),y(t),hint='nth_linear_constant_coeff_homogeneous')
    else:
        solvedEq = dsolve(sympify(eq),y(t),hint='nth_linear_constant_coeff_undetermined_coefficients')

    ##Transformação do tipo sympy_unity para o sympy_mul (mais operações permitidas)
    sepEq = solvedEq._args[1]

    ##PRocesso de separação de resp natural e resposta transitória
    elementosEq = sepEq.atoms(Symbol)
    C1 = elementosEq.pop()
    C2 = elementosEq.pop()

    print C1,C2

    if C2 != t :
        print "Tem c2"
        RespTran =  sepEq.subs([(C2,0),(C1,0)])
        
        
    else:
        RespTran =  sepEq.subs(C1,0)
        
    ##Resposta transitória alocada em  RespTran, natural em RespNat

    RespNat  =  sepEq.subs(RespTran,0)

    print RespTran
    print RespNat


    ##Saida
    print(sympify(solvedEq, rational = False , evaluate = False).evalf(2))
