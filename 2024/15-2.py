f = open("inputs/15.txt")

l = f.readline()
ls = []
while l[0] == "#":
    row = []
    for c in l.strip():
        if c == "@":
            row.append("@")
            row.append(".")
        elif c == "O":
            row.append("[")
            row.append("]")
        else:
            row.append(c)
            row.append(c)
    ls.append(row)
    l = f.readline()


for l in ls:
    for c in l:
        print(c, end='')
    print()
input()

instructions = []
for l in f:
    for c in l.strip():
        instructions.append(c)

for i in range(len(ls)):
    print(ls[i])
    for j in range(len(ls[0])):
        if ls[i][j] == "@":
            pos = (i, j)

print(pos)

dirs = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

def can_move(ls, pos, dir):
    if ls[pos[0]][pos[1]] == '.': return True
    elif ls[pos[0]][pos[1]] == '#': return False
    if ls[pos[0]][pos[1]] in "[]"  and not dir in [(0, 1), (0, -1)]:
        if ls[pos[0]][pos[1]] == "]":
            pos = (pos[0], pos[1]-1)
        return can_move(ls, (pos[0]+dir[0],pos[1]), dir) and can_move(ls, (pos[0]+dir[0],pos[1]+1), dir)
    else:
        if ls[pos[0]+dir[0]][pos[1]+dir[1]] == '#':
            return False
        elif ls[pos[0]+dir[0]][pos[1]+dir[1]] == '.':
            return True
        else:
            return can_move(ls, (pos[0]+dir[0],pos[1]+dir[1]), dir)

def move(ls, pos, dir):
    if ls[pos[0]][pos[1]] == '.': return
    if ls[pos[0]][pos[1]] in "[]" and not dir in [(0, 1), (0, -1)]:
        if ls[pos[0]][pos[1]] == "]":
            pos = (pos[0], pos[1]-1)

        if ls[pos[0]+dir[0]][pos[1]] == "]":
            move(ls, (pos[0]+dir[0],pos[1]  ), dir)
            move(ls, (pos[0]+dir[0],pos[1]+1), dir)
            ls[pos[0]+dir[0]][pos[1]] = '['
            ls[pos[0]+dir[0]][pos[1]+1] = ']'
            ls[pos[0]][pos[1]] = '.'
            ls[pos[0]][pos[1]+1] = '.'
        elif ls[pos[0]+dir[0]][pos[1]+1] == "[":
            move(ls, (pos[0]+dir[0],pos[1]  ), dir)
            move(ls, (pos[0]+dir[0],pos[1]+1), dir)
            ls[pos[0]+dir[0]][pos[1]] = '['
            ls[pos[0]+dir[0]][pos[1]+1] = ']'
            ls[pos[0]][pos[1]] = '.'
            ls[pos[0]][pos[1]+1] = '.'
        else:
            move(ls, (pos[0]+dir[0],pos[1]  ), dir)
            ls[pos[0]+dir[0]][pos[1]] = '['
            ls[pos[0]+dir[0]][pos[1]+1] = ']'
            ls[pos[0]][pos[1]] = '.'
            ls[pos[0]][pos[1]+1] = '.'
    else:
        if ls[pos[0]+dir[0]][pos[1]+dir[1]] != '.':
            move(ls, (pos[0]+dir[0],pos[1]+dir[1]), dir)
        ls[pos[0]+dir[0]][pos[1]+dir[1]] = ls[pos[0]][pos[1]]
        ls[pos[0]][pos[1]] = '.'


count = 0
for i in instructions:
    print(i, str(count)+"/"+str(len(instructions)))
    if can_move(ls, pos, dirs[i]):
        move(ls, pos, dirs[i])
        pos = (pos[0]+dirs[i][0], pos[1]+dirs[i][1])
    """for l in ls:
        for c in l:
            print(c, end='')
        print()
    input()"""
    count += 1


total = 0

for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == '[':
            total += 100*i + j


print(total)
