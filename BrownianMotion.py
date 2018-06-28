# cd C:\Users\avela\python
# mth5500proj1.py

import random
from math import *
import matplotlib.pyplot as plt

def normal(mean, sigma):
    # this will create 2 psuedo random variables between 0 and 1
    x = random.random()
    y = random.random()
    # there aare 2 ways to do the box ueler method this is both, but i will only use 1
    # Z1 = sqrt(-2 * log(x)) * cos(2 * pi * y)
    Z0 = sqrt(-2 * log(x)) * sin(2 * pi * y)

    A0 = mean + Z0*sigma
    return A0

x_axis = []
for i in range(0,101):
    x_axis.append(i/100)




# PART A
# this loop while just sample 100 independent standard Gaussians
normal_list = []
for i in range (0, 100):
    x = normal(0,1)
    normal_list.append(x)
print(normal_list)



# PART B
paths = 100
Brownian_paths = []
for j in range(0,paths):
    brown = []
    path = 0
    for i in range(0,101):
        path += normal(0,1)
        # each increment of the path is normal with mean 0 and standard deviation 1
        brown.append(path)
    Brownian_paths.append(brown)

for j in range(0,number):
    plt.plot(Brownian_paths[j])
plt.title('Integer Brownian motion')
plt.show()




# PART C
Brownian_paths_small = []
# like Integer brownian path but smaller
for j in range(0,paths):
    brown_small = []
    path = 0
    for i in range(0,101):
        path += normal(0,0.1)
        # each increment in this case is normal with mean 0 and standard deviation 0.01
        brown_small.append(path)
    Brownian_paths_small.append(brown_small)

for j in range(0,paths):
    plt.plot(x_axis,Brownian_paths_small[j])
plt.title('Brownian motion')
plt.show()



# PART D
Brownian_bridge_paths = []
for j in range(0,paths):
    brownian_bridge = []
    path = 0
    for i in range(0,101):
        path = Brownian_paths_small[j][i] - (i/100)*Brownian_paths_small[j][-1]
        # I used the data from Brownian _paths_small in order to create the brownian bridge
        brownian_bridge.append(path)
    Brownian_bridge_paths.append(brownian_bridge)

for j in range(0,number):
    plt.plot(x_axis,Brownian_bridge_paths[j])
plt.title('Brownian Bridge')
plt.show()


################################################################################
# PART 2

paths_1000 = []

for i in range(0,100000):
    browny = []
    # I ran out of names for my path so i just named this one browny
    path = 0
    j = 0
    while(abs(path) < 1 and j < 301):
        # this path will stop either when it hits 1 or negative 1 or when j = 300 i.e 3
        path += normal(0, 0.1)
        browny.append(path)
        j += 1
    if j != 301:
        paths_1000.append(j/100)
plt.hist(paths_1000, bins = 100)
plt.title("Histogram of stopping time")
plt.show()
