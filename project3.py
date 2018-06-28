# cd C:\Users\avela\python
# mth5500proj3.py

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
for i in range(0,100):
    x_axis.append(i/100)


sigma1 = 1
F1 = 0.05
beta = 0.5
# these are my intial values



# PART A
paths = 10
sigma_paths = []
# this will hold all of our paths for sigma
for j in range(0,paths):
    sigma_list = []
    sigma  = sigma1
    sigma_list.append(sigma)
    # sigma always starts a 1
    path = 0
    i = 0
    while(i<99):
        # i use a while loop here because i want to continue only if sigma stays positive
        path  = normal(0,.1)
        # we dont have to simulate brownian motion just every increment
        if sigma + sigma*(path) > 0:
            sigma = sigma + sigma*(path)
            sigma_list.append(sigma)
            # we will append every sigma to a list so that we can create a path
            i = i+1
    sigma_paths.append(sigma_list)
    # we will append every path to this list so that we have a collection of them

for i in range(0,paths):
    plt.plot(x_axis, sigma_paths[i])
plt.title('100 paths of sigma')
plt.show()



# PART B
F_paths = []
for j in range(0,paths):

    F_list = []
    F = F1
    F_list.append(F)
    # every F will start with a 0.05
    i = 0
    while(i<99):
        # same reason i will use a while loop so that there is no negatives
        path  = normal(0,.1)
        if F + sigma_paths[j][i]*(F**(0.5))*(path) > 0:
            F = F + sigma_paths[j][i]*(F**(0.5))*(path)
            # this is simply the formula given
            F_list.append(F)
            i = i+1
    F_paths.append(F_list)

for i in range(0,paths):
    plt.plot(x_axis, F_paths[i])
plt.title('100 paths of F')
plt.show()



# PART C
F_histo = []
for i in range(0,paths):
    F_histo.append(F_paths[i][-1])
    # this will take the last value of all of our paths of F
plt.hist(F_histo, bins = 20)
plt.title('F values histogram')
plt.show()




#PART D
expected = 0
k = 0.03
for i in range(0,paths):
    if F_histo[i] > k:
        expected += F_histo[i] - k
expected = expected/paths
print(expected)
# i will take the average of all the F1 values minus the strike price
# I usually get about 0.28
