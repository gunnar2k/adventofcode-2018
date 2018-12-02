file = open("./input.txt")
lines = set(file.read().strip().split("\n"))
for id1 in lines:
    for id2 in lines:
        if id1 == id2:
            continue
        wrongs = 0
        for idx, char in enumerate(id1):
            if char != id2[idx]:
                wrongs += 1
            if wrongs > 1:
                break
        if wrongs == 1:
            print(id1, id2)
            exit()
