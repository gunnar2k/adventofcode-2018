import re
import numpy as np

np.set_printoptions(edgeitems=100)

fabric = np.zeros((1000,1000), dtype=int)
claims = {}

input = open("input.txt")
for line in input:
    data = map(int, re.findall(r'\d+', line.strip()))
    id = int(data[0])
    x = data[1]
    y = data[2]
    w = data[3]
    h = data[4]

    claims[id] = 0

    # print(id,x,y,w,h)

    for i in fabric[x:x+w,y:y+h].flatten():
        if i != 0:
            claims[id] = 999
            claims[i] = 999

    fabric[x:x+w,y:y+h] = id

for key, claim in claims.items():
    if claim == 0:
        print(key)
        exit()
