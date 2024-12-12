f = open("inputs/12.txt")

ls = []
for line in f:
    row = []
    for c in line.strip():
        row.append(c)
    ls.append(row)

def explore(ls, p, explored):
    dirs = [
        (0,1,1),
        (0,-1,3),
        (1,0,2),
        (-1,0,0)
    ]
    queue = [p]
    area = 1
    sides = 0
    seen_sides = []
    while queue:
        curr = queue.pop()
        explored[curr[0]][curr[1]] = True
        for i in dirs:
            if curr[0] + i[0] >= 0 and curr[0] + i[0] < len(ls) and curr[1] + i[1] >= 0 and curr[1] + i[1] < len(ls[0]):
                if ls[curr[0]+i[0]][curr[1]+i[1]] == ls[curr[0]][curr[1]] and not explored[curr[0]+i[0]][curr[1]+i[1]] and (curr[0]+i[0],curr[1]+i[1]) not in queue:
                    queue.append((curr[0]+i[0],curr[1]+i[1]))
                    area += 1
                elif ls[curr[0]+i[0]][curr[1]+i[1]] != ls[curr[0]][curr[1]]:
                    seen_sides.append((curr[0]+i[0],curr[1]+i[1], i[2]))
            else:
                seen_sides.append((curr[0]+i[0],curr[1]+i[1], i[2]))

    sods = [[["." for i in range(len(ls[0])+2)] for j in range(len(ls)+2)] for k in range(4)]
    expsods = [[[False for i in range(len(ls[0])+2)] for j in range(len(ls)+2)] for k in range(4)]

    for x,y,z in seen_sides:
        sods[z][x+1][y+1] = "O"
    
    dors = {
        0: [(0,-1),(0,1)],
        1: [(-1,0),(1,0)],
        2: [(0,-1),(0,1)],
        3: [(-1,0),(1,0)]
    }

    for i in range(4):
        for x in range(len(sods[0])):
            for y in range(len(sods[0][0])):
                if sods[i][x][y] == "." or expsods[i][x][y]: continue
                q = [(x,y)]
                sides += 1
                while q:
                    curr = q.pop(0)
                    expsods[i][curr[0]][curr[1]] = True
                    for nx in dors[i]:
                        nxc = (curr[0]+nx[0], curr[1]+nx[1])
                        if nxc[0] >= 0 and nxc[1] >= 0 and nxc[0] < len(sods[0]) and nxc[1] < len(sods[0][0]):
                            if not expsods[i][nxc[0]][nxc[1]] and nxc not in q and sods[i][nxc[0]][nxc[1]] == "O":
                                q.append(nxc)
    
    return area * sides

explored = [[False for i in range(len(ls[0]))] for j in range(len(ls))]
total = 0
for i in range(len(ls)):
    for j in range(len(ls[0])):
        if not explored[i][j]:
            total += explore(ls, (i, j), explored)

print(total)