import time

found = None
frequency = 0
visited = set()
while found is None:
    file = open("./input.txt")
    for line in file:
        number = int(line.strip())
        new_frequency = frequency + number
        frequency = new_frequency
        if frequency in visited:
            found = frequency
            break
        visited.add(frequency)
    print("frequency", frequency)
    # time.sleep(0.5)
print(found)
