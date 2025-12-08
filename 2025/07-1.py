arr = [[c for c in line.strip()] for line in open('inputs/7.txt')]

for j in range(len(arr[0])):
    if arr[0][j] == 'S':
        start = (1,j)
        break

def beam(arr, pos, hist):
    if pos in hist:
        return hist[pos]
    if pos[0] == len(arr):
        hist[pos] = 0
        return hist[pos]
    if arr[pos[0]][pos[1]] == '.':
        hist[pos] = beam(arr, (pos[0]+1, pos[1]), hist)
        return hist[pos]
    else:
        left = beam(arr, (pos[0], pos[1]-1), hist)
        right = beam(arr, (pos[0], pos[1]+1), hist)
        hist[pos] = left + right + 1
        return hist[pos]

hist = {}

counter = 0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == '^':
            if (i,j) in hist:
                counter += 1
                arr[i][j] = str(hist[(i, j)])

print(counter)