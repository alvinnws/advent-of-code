def explore(garden, pos, steps):
    last = [pos]
    for i in range(steps):
        last = bfssingle(garden, last)
        #print(last)
    return last

def bfssingle(garden, poss):
    next = []
    for pos in poss:
        for neighbour in garden[pos]:
            if neighbour not in next:
                next.append(neighbour)
    return next

f = open('input.txt')

fullgarden = []

gfound = False

y = x = 0
for line in f:
    row = []
    if not gfound: x = 0
    for c in line.strip():
        if c == 'S': gfound = True
        if not gfound: x += 1
        row.append(c)
    fullgarden.append(row)
    if not gfound: y += 1

starty = y
startx = x

neighbours = {}
for y in range(len(fullgarden)):
    for x in range(len(fullgarden[0])):
        neighbours[(y,x)] = []
        if y != 0 and fullgarden[y-1][x] != '#': neighbours[(y,x)].append((y-1, x))
        if x != 0 and fullgarden[y][x-1] != '#': neighbours[(y,x)].append((y, x-1))
        if y != len(fullgarden   )-1 and fullgarden[y+1][x] != '#': neighbours[(y,x)].append((y+1, x))
        if x != len(fullgarden[0])-1 and fullgarden[y][x+1] != '#': neighbours[(y,x)].append((y, x+1))

#for i in neighbours:
    #print(i, neighbours[i])

found = explore(neighbours, (starty, startx), 64)
for y in range(len(fullgarden)):
    for x in range(len(fullgarden[0])):
        if (y,x) in found:
            print('O', end='')
        else:
            print(fullgarden[y][x], end='')
    print('')

print(len(found))