import re
from time import sleep
import string

input = list(open("input.txt").read().strip())

def should_react(unit):
    if unit[0].lower() == unit[1].lower() and unit[0] != unit[1]:
        return True
    else:
        return False

def react_polymer(polymer):
    idx = 0
    while idx < len(polymer) - 1:

        unit = polymer[idx:idx+2]
        # print(unit, polymer[0:20])

        if should_react(unit):
            del polymer[idx:idx+2]
            if idx > 0:
                idx -= 1
        else:
            # print(idx, unit)
            idx += 1
        # print(polymer[0:10])
        # sleep(1)
    return len(polymer)


tests = {}
for letter in string.ascii_lowercase:
    test = "".join(input).replace(letter, "").replace(letter.upper(), "")
    result = react_polymer(list(test))
    print(letter, result)
    tests[letter] = result

print(tests)
