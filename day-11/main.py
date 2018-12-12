import numpy as np

grid_serial_number = 9995
interface = np.zeros([300,300]).astype(int)

for x,row in enumerate(interface):
    for y,col in enumerate(row):
        X = x+1
        Y = y+1
        rack_id = X + 10
        # Begin with a power level of the rack ID times the Y coordinate.
        power_level = rack_id * Y
        # Increase the power level by the value of the grid serial number (your puzzle input).
        power_level += grid_serial_number
        # Set the power level to itself multiplied by the rack ID.
        power_level *= rack_id
        # Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
        power_level = power_level // 10**2 % 10
        # Subtract 5 from the power level.
        power_level -= 5
        # print(X,Y,power_level)
        interface[x,y] = int(power_level)

scores = np.zeros([298,298]).astype(int)

for x,row in enumerate(scores):
    for y,col in enumerate(row):
        scores[x,y] = sum(interface[x:x+3,y:y+3].flatten())

i,j = np.unravel_index(scores.argmax(), scores.shape)

assert scores[i,j] == scores.max()

print i+1,j+1
