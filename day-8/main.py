# this isnt working for some reason :( only for test set

import sys
sys.setrecursionlimit(10000)

def solve_for(arr):
    if len(arr) == 0:
        return 0

    # print(arr)

    child_count = arr[0]
    meta_count = arr[1]

    if child_count == 0: # ex 0 1 9
        if len(arr) == 2 + meta_count: # ex 0 1 9
            return sum(arr[2:])
        else: # ex 0 1 9 2 3 ... 2 3
            return sum(arr[2:2+meta_count]) + solve_for(arr[2+meta_count:])
    elif child_count > 0:
        if meta_count == 0: # ex 1 0 0 1 9
            return solve_for(arr[2:])
        else: # ex 1 1 1 1 9 9
            return solve_for(arr[2:-meta_count]) + sum(arr[-meta_count:])


input = map(int, \
    open("input.txt") \
    .read() \
    .strip() \
    .split(" "))

answer = solve_for(input)

print(answer)
