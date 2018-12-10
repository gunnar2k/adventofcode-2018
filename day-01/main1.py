file = open("./input.txt")
frequency = 0
for line in file:
    frequency += int(line.strip())
print(frequency)
