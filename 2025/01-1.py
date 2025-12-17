f = open('inputs/1.txt')

zeroes, current, rl = 0, 50, {"L": -1, "R": 1}

for line in f:
    current = (current + rl[line[0]]*int(line.strip()[1:])) % 100
    if current == 0: zeroes += 1

print(zeroes)