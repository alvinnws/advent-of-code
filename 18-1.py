up = 0
right = 0
down = 0
left = 0

f = open("input.txt")
trench = [['#']]
x = y = 0
for line in f:
    if line[0] == "U":
        for i in range(int(line.split(' ')[1])):
            if y == 0:
                row = []
                for j in range(len(trench[0])):
                    if j == x:
                        row.append('#')
                    else:
                        row.append('.')
                trench.insert(0, row)
            else:
                y -= 1
                trench[y][x] = '#'
        
    elif line[0] == "R":
        for i in range(int(line.split(' ')[1])):
            if x == len(trench[0]) - 1:
                for j in range(len(trench)):
                    if j == y:
                        trench[j].append('#')
                    else:
                        trench[j].append('.')
                x += 1
            else:
                    x += 1
                    trench[y][x] = '#'

    elif line[0] == "L":
        for i in range(int(line.split(' ')[1])):
            if x == 0:
                for j in range(len(trench)):
                    if j == y:
                        trench[j].insert(0,'#')
                    else:
                        trench[j].insert(0,'.')
            else:
                x -= 1
                trench[y][x] = '#'

    else:
        for i in range(int(line.split(' ')[1])):
            if y == len(trench) - 1:
                row = []
                for j in range(len(trench[0])):
                    if j == x:
                        row.append('#')
                    else:
                        row.append('.')
                trench.append(row)
                y += 1
            else:
                y += 1
                trench[y][x] = '#'

print(y, x)
x+=2
queue = [(y, x)]
while queue:
    curr = queue.pop(0)
    y = curr[0]
    x = curr[1]
    if y-1 >= 0 and trench[y-1][x] == '.':
        trench[y-1][x] = '#'
        queue.append((y-1,x))
    if y+1 <= len(trench) and trench[y+1][x] == '.':
        trench[y+1][x] = '#'
        queue.append((y+1,x))
    if x+1 <= len(trench[0]) and trench[y][x+1] == '.':
        trench[y][x+1] = '#'
        queue.append((y,x+1))
    if x-1 >= 0 and trench[y][x-1] == '.':
        trench[y][x-1] = '#'
        queue.append((y,x-1))


count = 0
g = open("outs.txt", "w")
for l in trench:
    s = ''
    for j in l:
        if j == '#':
            count += 1
        s += j
    g.write(s)
    g.write('\n')
g.close()
print(count)