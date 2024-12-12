f = open("inputs/12.txt")

ls = []
for line in f:
    row = []
    for c in line.strip():
        row.append(c)
    ls.append(row)

def explore(ls, p, explored):
    dirs = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0)
    ]
    queue = [p]
    area = 1
    perim = 0
    while queue:
        curr = queue.pop()
        explored[curr[0]][curr[1]] = True
        for i in dirs:
            if curr[0] + i[0] >= 0 and curr[0] + i[0] < len(ls) and curr[1] + i[1] >= 0 and curr[1] + i[1] < len(ls[0]):
                if ls[curr[0]+i[0]][curr[1]+i[1]] == ls[curr[0]][curr[1]] and not explored[curr[0]+i[0]][curr[1]+i[1]] and (curr[0]+i[0],curr[1]+i[1]) not in queue:
                    queue.append((curr[0]+i[0],curr[1]+i[1]))
                    area += 1
                elif ls[curr[0]+i[0]][curr[1]+i[1]] != ls[curr[0]][curr[1]]:
                    perim += 1
            else:
                perim += 1 
    return area * perim

explored = [[False for i in range(len(ls[0]))] for j in range(len(ls))]
total = 0
for i in range(len(ls)):
    for j in range(len(ls[0])):
        if not explored[i][j]:
            total += explore(ls, (i, j), explored)

print(total)