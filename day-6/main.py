import pandas as pd
import itertools
import string

# input = open("test.txt")
input = open("input.txt")

ids = itertools.product(string.ascii_lowercase.upper(), string.ascii_lowercase.upper())

points = []
for line in input:
    line = line.strip()
    comma = line.find(',')
    x = int(line[0:comma])
    y = int(line[comma+1:])
    points.append({'x': x, 'y': y, 'id': "".join(ids.next())})

points = pd.DataFrame(points)

print("--------------------------")
print("POINTS")
print(points)

print("--------------------------")
print("MIN")
print("--------------------------")
print(points.min())
print("--------------------------")
print("MAX")
print("--------------------------")
print(points.max())
print("--------------------------")

# Create initial grid data
rows = []
for x in range(0,400):
    row = []
    for y in range(0,400):
        row.append(".")
    rows.append(row)

# Create grid and set points
grid = pd.DataFrame(rows)
for idx, row in points.iterrows():
    grid[row['x']][row['y']] = row['id']

def manhatten_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

for x in grid:
    for y, value in grid[x].iteritems():
        if value != '.':
            continue

        if y % 100 == 0:
            print(x, y)

        best_point = None
        best_score = 2**32
        for idx, point in points.iterrows():
            score = manhatten_distance(x, y, point['x'], point['y'])
            if score < best_score:
                best_score = score
                best_point = point
            elif score == best_score:
                best_point = None

        if best_point is not None:
            grid[x][y] = best_point['id'].lower()

print(grid)

first_col = grid[0]
first_row = grid.iloc[0]
last_col = grid[len(grid)-1]
last_row = grid.iloc[-1]

infinites = set()

for value in first_col:
    if value == ".":
        continue
    if value not in infinites:
        infinites.add(value.lower())
for value in first_row:
    if value == ".":
        continue
    if value not in infinites:
        infinites.add(value.lower())
for value in last_col:
    if value == ".":
        continue
    if value not in infinites:
        infinites.add(value.lower())
for value in last_row:
    if value == ".":
        continue
    if value not in infinites:
        infinites.add(value.lower())
print("")
print("AFTER REMOVING INFINITES", infinites)
print("")

non_infinites = {}

for x in grid:
    for y, value in grid[x].iteritems():
        if value == ".":
            continue
        if value.lower() in infinites:
            grid[x][y] = "."
        else:
            grid[x][y] = grid[x][y].upper()
            if grid[x][y] not in non_infinites:
                non_infinites[grid[x][y].upper()] = 0

print(grid)
print(non_infinites)

for x in grid:
    for y, value in grid[x].iteritems():
        if value == ".":
            continue
        non_infinites[value] += 1

print(non_infinites)
