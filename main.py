# My name is Anthony O'Neal and this is my work
# Green's Function and ODE with IVP

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import odeint


#homogenous solutions
#number1 solution and plot
def yfun(x):
    return 1+.75*(math.e**(-2*x))

x = np.linspace(0,1,1000)
x=np.array(x).flatten()
ys=[]
for i in range(1000):
    ys.append(yfun(x[i]))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Greens Function solutions 1")
plt.plot(x,ys)
plt.show()

########################################
#number2 solution and plot
def yfun2(x):
    return 4*(math.e**(-x))+1

x = np.linspace(0,1,1000)
x=np.array(x).flatten()
ys=[]
for i in range(1000):
    ys.append(yfun2(x[i]))

plt.xlabel("x")
plt.ylabel("y")
plt.title("Greens Function solutions 2")
plt.plot(x,ys)
plt.show()
