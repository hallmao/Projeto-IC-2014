from sympy import Function, dsolve, pprint, exp, cos
from sympy.abc import t
from sympy import *



def input_coefs():
global a2,a1,a0,xT
print "Insira os coefs e entrada para uma EDO do tipo: "
print "     a2*y''(t) +a1*y'(t) +a0*y(t) = x(t)"
a2 = input("a2:")
a1 = input("a1:")
a0 = input("a0:")
xT = input("x(t):")


    

y = Function('y')

eq =sympify(a2*y(t).diff(t,2) + a1*y(t).diff(t) +a0*y(t) - 4*exp(-x)*x**2 + cos(2*x))

pprint(eq)

print (eq)




print(dsolve(sympify(eq),f(x),hint='nth_linear_constant_coeff_undetermined_coefficients'))
