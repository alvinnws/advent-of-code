f = open('inputs/10.txt')

total = 0

ls = []
for line in f:
    row = []
    for c in line.strip():
        row.append(c)
    ls.append(row)

sps = []

for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == '0':
            sps.append((i, j))

def explore(ls, pos, explored=set()):
    dirs = [
        (0, 1),
        (0,-1),
        (1, 0),
        (-1,0)
    ]
    total = 0
    if ls[pos[0]][pos[1]] == "9":
        return 1
    else:
        for i in dirs:
            if 0 <= pos[0]+i[0] and pos[0]+i[0] < len(ls) and 0 <= pos[1]+i[1] and pos[1]+i[1] < len(ls[0]):
                # print((pos[0]+i[0], pos[1]+i[1]), int(ls[pos[0]+i[0]][pos[1]+i[1]]), int(ls[pos[0]][pos[1]]) + 1, int(ls[pos[0]+i[0]][pos[1]+i[1]]) == int(ls[pos[0]][pos[1]]) + 1)
                if int(ls[pos[0]+i[0]][pos[1]+i[1]]) == int(ls[pos[0]][pos[1]]) + 1:
                    # print((pos[0]+i[0], pos[1]+i[1]))
                    total += explore(ls, (pos[0]+i[0], pos[1]+i[1]), explored)
    return total

for sp in sps:
    total += explore(ls, sp, set())

print(total)

f.close()