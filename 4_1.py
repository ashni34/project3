import numpy as np
import queue
import sys
import matplotlib.pyplot as mpl
import math as math
import matplotlib as m
import random
from collections import deque
import random

n = 50
def create():
    # create matrix
    p = 0.25
    #start = (0,0)
    #goal = (n-1, n-1)
    greycounter = 0
    lightgreycounter = 0
    greencounter = 0
    blackcounter = 0

    ## 1= green -> forest
    ## 0 = white -> flat
    ## .4 = gray -> hilly
    ## .7 = dark gray -> cave
    colors = [mpl.cm.ocean(1),mpl.cm.binary(0),mpl.cm.binary(0.4),
              mpl.cm.binary(0.7)]

    cmap = m.colors.ListedColormap(colors)

    newmatrix = np.zeros((n,n))
    numBlocks = math.ceil(n*n*p)
    #print(numBlocks)
    matrix = np.zeros((n,n))

    cmap= m.colors.ListedColormap(colors)

    ## 6,12,13,14
    num_arr = []
    for i in range(numBlocks):
        num_arr.append(1)
        num_arr.append(2)
        num_arr.append(3)
        num_arr.append(4)

    #print(num_arr)
    random.shuffle(num_arr)
    #print(num_arr)

    counter = 0
    l=0
    x = n*n
    while l < x:
        for i in range(n):
            for j in range(n):
                #print("l value = ", l, "n value", i,j)
                newmatrix[i,j] = num_arr[l]
                l+=1

    print(newmatrix)
    return newmatrix

newmatrix = create()
x = np.random.randint(0,n-1)
y = np.random.randint(0,n-1)
print("This is the target:",(x,y))



#### using Bayes theorem

## go through the array and set probability to 1/(total number of cells)
prob_matrix = np.zeros((n,n))
## inital probability when all have equal chance
init_prob = 1/(n*n)
for i in range(n):
    for j in range(n):
        prob_matrix[i,j] = 1/(n*n)

    ## 1= green -> forest  =====> .7
    ## 2 = white -> flat ====> .1
    ## 3 = gray -> hilly =====> .3
    ## 4 = dark gray -> cave ===> .9
#for i in range(n):
    #for j in range(n):
        #flat

    
            

       
## if target not found, normalize
## The idea is that if you search a flat cell and its not the 
## target, then finding the target becomes harder because the remaining cells 
## have a higher false negative rate. 


## find highest probability:

def open_cell(newmatrix, prob_matrix, val):
    ## find maximum value in the matrix and open that 
    #maximum = np.max(prob_matrix)
    i= np.argmax(prob_matrx, axis = 0)
    j= np.argmax(prob_matrx, axis = 1)

    if (newmatrx[i,j] == 2):
        prob_matrix[i,j] = prob_matrix[i,j] * .1
        curr = prob_matrix[i,j]
    #forest
    if (newmatrx[i,j] == 1):
        prob_matrix[i,j] = prob_matrix[i,j] * .7
        curr = prob_matrix[i,j]
    #hilly 
    if (newmatrx[i,j] == 3):
        prob_matrix[i,j] = prob_matrix[i,j] * .3
        curr = prob_matrix[i,j]
    #cave   
    if (newmatrx[i,j] == 4):
        prob_matrix[i,j] = prob_matrix[i,j] * .9
        curr = prob_matrix[i,j]
    
    




#mpl.imshow(matrix,cmap='Greys',interpolation='nearest')

#print(matrix)
mpl.imshow(newmatrix,cmap = cmap,interpolation='nearest')
mpl.show()
