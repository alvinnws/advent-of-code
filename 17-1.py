f = open("input.txt")

neigh = {}
stox = {}
weights = []

for line in f:
    row = []
    for c in line.strip():
        row.append(int(c))
    weights.append(row)

for y in range(len(weights)):
    for x in range(len(weights[0])):
        for dir in range(4):
            for st in range(3):
                ls = []
                if st != 2:
                    nx = x
                    ny = y
                    if dir == 0: ny -= 1
                    elif dir == 1: nx += 1
                    elif dir == 2: ny += 1
                    else: nx -= 1
                    if (0 <= nx <= len(weights[0])-1) and (0 <= ny <= len(weights) - 1):
                        ls.append((ny, nx, dir, st+1))
                if dir % 2 == 0:
                    if x > 0: ls.append((y, x-1, 3, 0))
                    if x < len(weights[0])-1: ls.append((y, x+1, 1, 0))
                else:
                    if y > 0: ls.append((y-1, x, 0, 0))
                    if y < len(weights) - 1: ls.append((y+1, x, 2, 0))
                neigh[(y, x, dir, st)] = ls
                stox[(y, x, dir, st)] = float('inf')
                print((y, x, dir, st), ls)

stox[(0, 0, 1, 0)] = 0
stox[(0, 0, 2, 0)] = 0
stox[(0, 0, 3, 0)] = 0
stox[(0, 0, 4, 0)] = 0

for y in range(1):
    for x in range(len(weights[0])):
        for dir in range(4):
            for st in range(3):
                print((y, x, dir, st), neigh[(y, x, dir, st)])


q = []
q.append((0,0,1,0))
q.append((0,0,2,0))
while q:
    curr = q.pop(0)
    for n in neigh[curr]:
        if weights[n[0]][n[1]] + stox[curr] < stox[n]:
            stox[n] = min(weights[n[0]][n[1]] + stox[curr], stox[n])
            q.append(n)

for y in range(len(weights)):
    for x in range(len(weights[0])):
        mns = float('inf')
        for dir in range(4):
            for st in range(3):
                mns = min(mns, stox[(y, x, dir, st)])
        print(mns, end=' ')
    print('')