f = open('inputs/1.txt')

zeroes = 0
current = 50

for line in f:
    if line[0] == "L":
        for i in range(int(line.strip()[1:])):
            current -= 1
            if current == -1:
                current = 99
            if current == 0:
                zeroes += 1
    else:
        for i in range(int(line.strip()[1:])):
            current += 1
            if current == 100:
                current = 0
            if current == 0:
                zeroes += 1


print(zeroes)