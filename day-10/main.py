import os
import pandas as pd
import matplotlib.pyplot as plt

points = []
input = open("input.txt")

for line in input:
    line = line.strip()
    X = int(line[10:16])
    Y = int(line[18:24])
    vel_X = int(line[36:38])
    vel_Y = int(line[40:42])
    points.append({
        'X': X,
        'Y': -Y,
        'vel_X': vel_X,
        'vel_Y': vel_Y,
    })

df = pd.DataFrame(points)
def print_map(id):
    df.plot.scatter(x='X', y='Y', s=70)
    plt.show()

i = 0
while i < 11000:
    df['X'] += df['vel_X']
    df['Y'] -= df['vel_Y']

    if i == 10085:
        print_map(i)

    i += 1
