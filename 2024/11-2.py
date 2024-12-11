from functools import cache
import sys

print(sys.getrecursionlimit())

f = open('inputs/11.txt')

total = 0

stones = tuple(map(int, f.readline().strip().split()))

print(stones)

memo = {}

def get_n(stone, blink):
    if (stone, blink) in memo:
        return memo[(stone, blink)]
    if blink==0:
        return 1
    elif stone == 0:
        memo[(stone, blink)] = get_n(1, blink-1)
    elif len(str(stone)) % 2 == 0:
        memo[(stone, blink)] = get_n(int(str(stone)[len(str(stone))//2:]), blink-1) + get_n(int(str(stone)[:len(str(stone))//2]), blink-1)
    else: 
        memo[(stone, blink)] = get_n(2024*stone, blink-1)
    return memo[(stone, blink)]

print(sum(get_n(s, 75) for s in stones))

f.close()