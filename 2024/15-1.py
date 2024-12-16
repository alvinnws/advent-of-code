f = open("inputs/15.txt")

l = f.readline()
ls = []
while l[0] == "#":
    row = [c for c in l.strip()]
    ls.append(row)
    l = f.readline()

instructions = []
for l in f:
    for c in l.strip():
        instructions.append(c)

for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == "@":
            pos = (i, j)

dirs = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

def move(ls, pos, dir):
    if ls[pos[0]+dir[0]][pos[1]+dir[1]] == '#':
        return False
    elif ls[pos[0]+dir[0]][pos[1]+dir[1]] == '.':
        ls[pos[0]+dir[0]][pos[1]+dir[1]] = ls[pos[0]][pos[1]]
        ls[pos[0]][pos[1]] = '.'
        return True
    else:
        movebool = move(ls, (pos[0]+dir[0],pos[1]+dir[1]), dir)
        if movebool:
            ls[pos[0]+dir[0]][pos[1]+dir[1]] = ls[pos[0]][pos[1]]
            ls[pos[0]][pos[1]] = '.'
        return movebool

for i in instructions:
    movebool = move(ls, pos, dirs[i])
    if movebool:
        pos = (pos[0]+dirs[i][0], pos[1]+dirs[i][1])


total = 0

for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == 'O':
            total += 100*i + j


print(total)
