##Taken from http://docs.sympy.org/latest/tutorial/calculus.html#integrals

from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

expr = Integral(log(x)**2, x)
expr


print expr.doit()
