import re
import numpy as np

np.set_printoptions(threshold=np.nan)

fabric = np.zeros((1000,1000))

input = open("input.txt")
for line in input:
    data = map(int, re.findall(r'\d+', line.strip()))
    x = data[1]
    y = data[2]
    w = data[3]
    h = data[4]

    print(x,y,w,h)

    fabric[x:x+w,y:y+h] += 1

overlapping = fabric >= 2
print(overlapping.sum())
