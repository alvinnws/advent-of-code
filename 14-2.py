def rotatecw(arr):
    flipped = []
    for x in range(len(arr[0])):
        row = []
        for y in range(len(arr)):
            row.append(arr[y][x])
        row.reverse()
        flipped.append(row)
    return flipped

def pushright(rocks):
    moves = True
    while moves:
        moves = False
        for line in rocks:
            for i in range(len(line)-1):
                if line[i+1] == '.' and line[i] == 'O':
                    line[i] = '.'
                    line[i+1] = 'O'
                    moves = True

f = open("input.txt")

rocks = []
for line in f:
    rocks.append(line.strip())

cycles = 1000000000
for i in range(cycles):
    if i % 10000 == 0:
        print(i)
    for j in range(4):
        rocks = rotatecw(rocks)
        pushright(rocks)

    rocks = rotatecw(rocks)
    total = 0
    for line in rocks:
        for j in range(len(line)):
            if line[j] == 'O':
                total += j + 1
    print(total, i)
    rocks = rotatecw(rocks)
    rocks = rotatecw(rocks)
    rocks = rotatecw(rocks)