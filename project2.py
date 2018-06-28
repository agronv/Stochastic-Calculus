# cd C:\Users\avela\python
# mth5500proj2.py

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




# PART A
paths = 100
Xt_10 = []
# this will store all of our paths for Xt
for i in range(0,paths):
    path  = 0;
    Xt = 0
    brown = []
    for j in range(0,100):
        path += normal(0, 0.1)
        # this part is basically the brownian motion part
        Xt =  (1/sqrt(1-(j/100)))*exp( (-1*(path**2)) / (2*(1-(j/100))) )
        # I simply applied the fromula
        brown.append(Xt)
        # we will append each Xt value to the path brown

    plt.plot(x_axis,brown)
    Xt_10.append(brown)
    # we will append each path to the list of paths
plt.title('Xt')
plt.show()



# PART B
Yt_10 = []
# this will store all of our paths for Yt
for i in range(0,paths):
    Yt = []
    Yt.append(1)
    # the first value for every path is 1
    yt = 1

    Bt = []
    path = 0
    for k in range(0,101):
        path += normal(0, 0.1)
        Bt.append(path)
        # the 5 lines above is just used to create a brownian motion path it is from
        # 0 to 101 beacuse in the line below i use Bt[j+1]

    for j in range(0,99):
        yt -= Bt[j]*yt*(Bt[j+1] - Bt[j])/((1-(j/100))**(1))
        # we cannot use the actual integral so we have to use an apporximation
        Yt.append(yt)
        # we will append the yt values to the Yt path
    plt.plot(x_axis,Yt)
    Yt_10.append(Yt)
    # we will append every path to a list of paths
plt.title("Yt")
plt.show()



#PART C
t1_average = 0
t2_average = 0
t3_average = 0
t4_average = 0
for i in range(0,paths):
# all that i am doing is taking the average of the 5 time values
    t1_average += (abs(Xt_10[i][21] - Yt_10[i][21]))/paths
    t2_average += (abs(Xt_10[i][41] - Yt_10[i][41]))/paths
    t3_average += (abs(Xt_10[i][61] - Yt_10[i][61]))/paths
    t4_average += (abs(Xt_10[i][81] - Yt_10[i][81]))/paths
print("t20: ", t1_average, " t40: ", t2_average, " t60: ", t3_average, " t80: ", t4_average)



# PART D
t95 = 0
t96 = 0
t97 = 0
t98 = 0
t99 = 0
for i in range(0,paths):
# this will take the average of every time for the Yt path
    t95 += Yt_10[i][95]/paths
    t96 += Yt_10[i][96]/paths
    t97 += Yt_10[i][97]/paths
    t98 += Yt_10[i][98]/paths
    t99 += Yt_10[i][99]/paths
print("95: ", t95, " 96: ", t96, " 97: ", t97, " 98: ", t98, " 99: ", t99)
# I think that the limit of Yt goes to 0 because the exponential converges to 0
# faster than the sqrt does, also this was on HW#7, but it makes sense




# PART E
max_y = 0
for i in range(0,paths):
    # print(max(Yt_10[i]))
    max_y += max(Yt_10[i])/paths
print("EXPECTED MAXIMUM: ",max_y)
# all that i am doing is printing the average for the largest value in the path
# my guess is e
