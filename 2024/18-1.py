f = open("inputs/18.txt")

WIDTH = 71
FALLEN = 1024

maze = [["." for c in range(WIDTH)] for l in range(WIDTH)]

dirs = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

for i in range(FALLEN):
    pos = [int(i) for i in f.readline().strip().split(",")]
    maze[pos[1]][pos[0]] = "#"

queue = [((0,0),0,[])]

best = [[-1 for i in range(len(maze[0]))] for j in range(len(maze))]

visited = []
while True:
    curr, dis, visited = queue.pop(0)
    if best[curr[0]][curr[1]] == -1:
        best[curr[0]][curr[1]] = dis
    elif best[curr[0]][curr[1]] <= dis:
        continue
    else:
        best[curr[0]][curr[1]] = dis
    
    if curr == (WIDTH-1,WIDTH-1):
        print(dis)
        quit()
    
    for dir in dirs:
        next = (curr[0]+dir[0], curr[1]+dir[1])
        if 0 > next[0] or next[0] >= WIDTH or 0 > next[1] or next[1] >= WIDTH or maze[next[0]][next[1]] == "#" or next in visited:
            continue
        else:
            queue.append((next, dis+1, visited.copy() + [curr]))

    queue.sort(key=lambda x: x[1])
    