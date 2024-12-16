f = open("inputs/16.txt")

maze = [[c for c in l.strip()] for l in f]

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            pos = (i,j)

dir = 1

dirs = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

queue = [(pos, dir, 0)]

best = [[-1 for i in range(len(maze[0]))] for j in range(len(maze))]

while True:
    curr = queue.pop(0)
    if best[curr[0][0]][curr[0][1]] == -1:
        best[curr[0][0]][curr[0][1]] = curr[2]
    elif best[curr[0][0]][curr[0][1]] < curr[2]:
        continue
    if maze[curr[0][0]][curr[0][1]] == "E":
        print(curr[2])
        quit()
    for dir in dirs:
        if maze[curr[0][0]+dirs[dir][0]][curr[0][1]+dirs[dir][1]] == "#":
            continue
        elif dir == curr[1]:
            if ((curr[0][0]+dirs[dir][0], curr[0][1]+dirs[dir][1]), dir, curr[2] + 1) not in queue:
                queue.append(((curr[0][0]+dirs[dir][0], curr[0][1]+dirs[dir][1]), dir, curr[2] + 1))
        else:
            if ((curr[0][0]+dirs[dir][0], curr[0][1]+dirs[dir][1]), dir, curr[2] + 1001) not in queue:
                queue.append(((curr[0][0]+dirs[dir][0], curr[0][1]+dirs[dir][1]), dir, curr[2] + 1001))
    queue.sort(key=lambda x: x[2])
    