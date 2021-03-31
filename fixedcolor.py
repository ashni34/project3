import numpy as np
import queue
import sys
import matplotlib.pyplot as mpl
import math as math
import matplotlib as m
import random
from collections import deque
import random

# create matrix
n = 50
p = 0.25
#start = (0,0)
#goal = (n-1, n-1)
greycounter = 0
lightgreycounter = 0
greencounter = 0
blackcounter = 0


colors = [mpl.cm.ocean(1),mpl.cm.binary(0),mpl.cm.binary(0.4),
          mpl.cm.binary(0.7)]

cmap = m.colors.ListedColormap(colors)

newmatrix = np.zeros((n,n))
numBlocks = math.ceil(n*n*p)
print(numBlocks)
matrix = np.zeros((n,n))

cmap= m.colors.ListedColormap(colors)

## 6,12,13,14
num_arr = []
for i in range(numBlocks):
    num_arr.append(1)
    num_arr.append(2)
    num_arr.append(3)
    num_arr.append(4)

print(num_arr)
random.shuffle(num_arr)
print(num_arr)

counter = 0
l=0
x = n*n
while l < x:
    for i in range(n):
        for j in range(n):
            print("l value = ", l, "n value", i,j)
            newmatrix[i,j] = num_arr[l]
            l+=1

print(newmatrix)

x = np.random.randint(0,n-1)
y = np.random.randint(0,n-1)
print("This is the target:",(x,y))


#mpl.imshow(matrix,cmap='Greys',interpolation='nearest')

#print(matrix)
mpl.imshow(newmatrix,cmap = cmap,interpolation='nearest')
mpl.show()
