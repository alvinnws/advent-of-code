def flip2d(arr):
    flipped = []
    for x in range(len(arr[0])):
        row = []
        for y in range(len(arr)):
            row.append(arr[y][x])
        flipped.append(row)
    return flipped

f = open("input.txt")

rocks = []
for line in f:
    rocks.append(line.strip())

rocks = flip2d(rocks)

moves = True
while moves:
    moves = False
    for line in rocks:
        for i in range(len(line)-1):
            if line[i] == '.' and line[i+1] == 'O':
                line[i+1] = '.'
                line[i] = 'O'
                moves = True

total = 0
for line in rocks:
    for i in range(len(line)):
        if line[i] == 'O':
            total += len(line) - i
print(total)