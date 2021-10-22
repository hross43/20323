
from Functions import *


print('Problem #1:')
qf1(0.001, 1000, 0.001)
qf2(0.001, 1000, 0.001)
qf3(0.001, 1000, 0.001)
print('\n')

print('Problem #2:')
Simpsons(0, 2, 10)
Simpsons(0, 2, 100)
Simpsons(0, 2, 1000)
print('\n')

print('Problem #3:')
Cv_list = []
Tvals = range(5, 501)
for i in Tvals:
    temp = Cv(i)
    Cv_list.append(temp)

plot_Cv(Tvals, Cv_list)