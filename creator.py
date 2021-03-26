import numpy as np
import queue
import sys
import imagesc as imagesc
import matplotlib.pyplot as mpl
import math as math
import matplotlib as m
from collections import deque

# create matrix
n = 8
p = 0.25
#start = (0,0)
#goal = (n-1, n-1)
greycounter = 0
lightgreycounter = 0
greencounter = 0
blackcounter = 0

newmatrix = np.zeros((n,n))
numBlocks = math.ceil(n*n*p)
print(numBlocks)
matrix = np.zeros((n,n))

colors = [mpl.cm.tab20c(6),mpl.cm.tab20c(12),mpl.cm.tab20c(13),
          mpl.cm.tab20c(14)]

cmap= m.colors.ListedColormap(colors)


## 6,12,13,14
num_arr = []
for i in range(numBlocks):
    num_arr.append(6)
    num_arr.append(12)
    num_arr.append(13)
    num_arr.append(14)

print(num_arr)
num_arr2  = np.random.shuffle(num_arr)
print(num_arr2)


#Generate random grey squares
for  k in range(numBlocks):
    x = np.random.randint(0,n-1)
    y = np.random.randint(0,n-1)
    if (matrix[x,y] == 0):
        matrix[x,y] = 12
    if (matrix[x,y] == 6 or matrix[x,y] == 14 or matrix[x,y] == 13 or matrix[x,y] == 12):
        k = k-1
    lightgreycounter +=1
    print(lightgreycounter)
    

#Generate random grey squares
for  k in range(numBlocks):
    x = np.random.randint(0,n-1)
    y = np.random.randint(0,n-1)
    if (matrix[x,y] == 0):
        matrix[x,y] = 13

    if (matrix[x,y] == 6 or matrix[x,y] == 14 or matrix[x,y] == 13 or matrix[x,y] == 12):
        k = k-1
    greycounter +=1
    print(greycounter)
    

#Generate random grey squares
for  k in range(numBlocks):
    x = np.random.randint(0,n-1)
    y = np.random.randint(0,n-1)
    if (matrix[x,y] == 0):
        matrix[x,y] = 14
    if (matrix[x,y] == 6 or matrix[x,y] == 14 or matrix[x,y] == 13 or matrix[x,y] == 12):
        k = k-1
    blackcounter +=1
    print(blackcounter)
    

#Generate random grey squares
for  k in range(numBlocks):
    x = np.random.randint(0,n-1)
    y = np.random.randint(0,n-1)
    if (matrix[x,y] == 0):
        matrix[x,y] = 6
    if (matrix[x,y] == 6 or matrix[x,y] == 14 or matrix[x,y] == 13 or matrix[x,y] == 12):
        k = k-1
    greencounter +=1
    print(greencounter)



#mpl.imshow(matrix,cmap='Greys',interpolation='nearest')

#print(matrix)
mpl.imshow(matrix,cmap = 'tab20c',interpolation='nearest')
mpl.show()
