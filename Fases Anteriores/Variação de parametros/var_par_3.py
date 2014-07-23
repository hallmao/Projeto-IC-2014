import matplotlib.pyplot as plt
from math import e
from numpy import array,sin,cos,exp
from numpy import arange
from sympy import *


x = Symbol('x')

y1 = cos(x)
y2 = sin(x)
gx = cos(x**2)

y1 = simplify(y1)
y2 = simplify(y2)
gx = simplify(gx)

dy1 = y1.diff(x)
dy2 = y2.diff(x)

dy1= simplify(dy1)
dy2= simplify(dy2)

print y1,y2,gx,dy1,dy2

W = y1*dy2 - y2*dy1
W = simplify(W)

du1 = (y2*gx)/W
du2 = (y1*gx)/W
u1 = Integral(du1,x)
##func = lambda du1 : du1
##u1 = quad(func)
u1 = u1.doit()

print u1
