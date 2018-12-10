import string

file = open("./input.txt")
twos = 0
threes = 0
for line in file:
    id = line.strip()

    found_two = False
    found_three = False

    for letter in list(string.ascii_lowercase):
        if id.count(letter) == 2:
            found_two = True
        if id.count(letter) == 3:
            found_three = True

    if found_two:
        twos += 1

    if found_three:
        threes += 1

print(twos * threes)
