import numpy as np
import math
from matplotlib import pyplot as plt

####################################
#           Problem 1              #
####################################
def qf1(a, b, c):

    discrim = (b**2) - (4*a*c)

    if discrim < 0:
        print('No Real Roots')

    else:
        temp1 = -b + ( ((b**2) - (4*a*c)) ** 0.5)
        ret1 = temp1 / (2*a)

        temp2 = -b - ( ((b**2) - (4*a*c)) ** 0.5)
        ret2 = temp2 / (2*a)

        print('Part A Roots: ' + str(ret1) + ' ' + str(ret2))

def qf2(a, b, c):
    discrim = (b**2) - (4*a*c)
    if discrim < 0:
        print('No Real Roots')

    else:
        temp1 = -b + ( ((b**2) - (4*a*c)) ** 0.5)
        ret1 = (2*c) / temp1

        temp2 = -b - ( ((b**2) - (4*a*c)) ** 0.5)
        ret2 = (2*c) / temp1

        print('Part B Roots: ' + str(ret1) + ' ' + str(ret2))

def qf3(a, b, c):
    discrim = (b**2) - (4*a*c)

    if discrim < 0:
        print('No Real (Not Complex) Roots')
    elif a != 1:
        A = float(1 / a)
        B = A * b
        C = A * c

    temp1 = -B + ( ((B**2) - (4*A*C)) ** 0.5)
    ret1 = temp1 / (2*A)

    temp2 = -B - ( ((B**2) - (4*A*C)) ** 0.5)
    ret2 = temp2 / (2*A)

    print('Part C Roots: ' + str(ret1) + ' ' + str(ret2))

####################################
#           Problem 2              #
####################################
def f(x):
    retval = (x**4) - (2*x) + 1
    return retval

def Simpsons(a, b, n):
    
    h = (b - a) / n
    i = 0
    Nevens = []
    Nodds = []

    while i < n:
        if (i % 2) == 0:
            temp = f(i * h)
            Nevens.append(temp)
        elif (i % 2) != 0:
            temp = f(i * h)
            Nodds.append(temp)

        i += 1
    SumEvens = sum(Nevens)
    SumOdds = sum(Nodds)
    
    retval = (h / 3) * (f(a) + f(b) + (4*SumOdds) + (2*SumEvens))
    print('Simpsons Approximation for ' + str(n) + ' slices yeilds ' + str(retval))

####################################
#           Problem 3              #
####################################
def f2(x):
    if x == 0:
        return(0)
    else:
        numer = (x**4) * math.exp(x)
        denom = (math.exp(x) - 1) ** 2
        return (numer / denom)

def TrapizoidRule(b, a=0, N=1000):
    h = (b - a) / N
    s = (0.5 * f2(a)) + (0.5 * f2(b))

    for i in range(1, N):
        s += f2(a + i * h)

    return (s * h) 

def Cv(T):
    volume = 1000
    density = 6.022 * (10**28)
    boltz = 1.381 * (10**-23)
    debye = 428

    coeff = 9 * volume * density * boltz * ((T / debye) ** 3)

    upperlim = debye / T
    Trap_retval = TrapizoidRule(upperlim)

    return(coeff * Trap_retval)

def plot_Cv(T, Cv):
    fig1 = plt.figure(figsize=(20,10))
    ax1 = fig1.add_subplot(111)
    ax1.scatter(T, Cv, s=15, c='b', alpha=0.5)

    ax1.set_xlabel('$Temperature$ $(K^{o})$', size=20)
    ax1.set_ylabel('$C_{V}(T)$', size=20)

    ax1.xaxis.set_tick_params(labelsize=20)
    ax1.yaxis.set_tick_params(labelsize=20)
    plt.title('Heat Capacity of a Solid $C_{V}(T)$ Vs. Temperature $(K^{o})$', size=30)
    #plt.xlim(-1, 501)
    #plt.ylim(0, 2500000000)
    plt.savefig('scatter.jpg')
    
    print('Plot saved as scatter.jpg')

