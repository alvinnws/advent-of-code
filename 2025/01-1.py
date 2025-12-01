f = open('inputs/1.txt')

zeroes = 0
current = 50

for line in f:
    if line[0] == "L":
        current = (current - int(line.strip()[1:])) % 100
    else:
        current = (current + int(line.strip()[1:])) % 100

    if current == 0:
        zeroes += 1

print(zeroes)