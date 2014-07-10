import matplotlib.pyplot as plt
from math import e
from numpy import array,sin,cos,exp
from numpy import arange
from sympy import *
from scipy.integrate import quad
import scipy.integrate.odeint as integrate
x = Symbol('x')

y1 = cos(x)
y2 = sin(x)
gx = 1 + tan(x)
dy1 = y1.diff(x)
dy2 = y2.diff(x)

W = y1*dy2 - y2*dy1
W = simplify(W)

du1 = (y2*gx)/W

print du1
u1 = integrate(du1)
##func = lambda du1 : du1
##u1 = quad(func)

print u1
