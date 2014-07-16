from sympy import Function, dsolve, pprint, exp, cos
from sympy.abc import t
from sympy import *


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

    y = Function('y')

    ##Adicionando os coefs a eq diferencial
    eq =sympify(a2*y(t).diff(t,2) + a1*y(t).diff(t) +a0*y(t) -xT)

    pprint(eq)

    ###Dif equation solver
    solvedEq = dsolve(sympify(eq),y(t),hint='nth_linear_constant_coeff_undetermined_coefficients')

    ##Saida
    print(sympify(solvedEq, rational = False , evaluate = False).evalf(2))
