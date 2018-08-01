# import numpy as np (need to use np.zeros(10,1))
# from numpy import * (zeros(10,1))

from numpy import *
# import matplotlib.pyplot as plt
from matplotlib.pyplot import *

#Linspace
a = 0
b = 1
N = 12

A = linspace(a,b,N)
delta = (b-a)/(N-1)

print("delta is " + str(delta))

#Vector plot
aV = 0
bV = 5
NV = 100

x = linspace(aV,bV,NV)
y = (x**2) * log(x) * sin(x)

f1 = figure(1)
plot(x,y)
xlabel('x-axis')
ylabel('y-axis')
title('y-axis vs x-axis')

show()

# see how to show multiple plots
# see how to run sections of code