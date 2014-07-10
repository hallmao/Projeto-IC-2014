import matplotlib.pyplot as plt
from math import e
from numpy import array,sin,cos,exp
from numpy import arange
from sympy import *
from scipy.integrate import quad
from scipy import Inf

x = Symbol('x')

y1 = cos(x)
y2 = sin(x)
gx = 1 + tan(x)
dy1 = y1.diff(x)
dy2 = y2.diff(x)

W = y1*dy2 - y2*dy1
W = simplify(W)

du1 = (y2*gx)/W

u1 = quad(2, 0, Inf)

print u1
