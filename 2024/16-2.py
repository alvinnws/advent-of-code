f = open("inputs/16.txt")

VISUALISE = False 

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

queue = [(pos, dir, 0, tuple())]

best = [[-1 for i in range(len(maze[0]))] for j in range(len(maze))]

best_score = False

sits = set()

while queue:
    curr = queue.pop(0)
    if best[curr[0][0]][curr[0][1]] == -1:
        best[curr[0][0]][curr[0][1]] = curr[2]
    elif best[curr[0][0]][curr[0][1]] + 2000 < curr[2]:
        continue
    if best_score and best_score < curr[2]:
        continue
    if maze[curr[0][0]][curr[0][1]] == "E":
        if not best_score:
            best_score = curr[2]
        for i in curr[3]:
            sits.add(i)

    for dir in dirs:
        if maze[curr[0][0]+dirs[dir][0]][curr[0][1]+dirs[dir][1]] == "#" or (curr[0][0]+dirs[dir][0], curr[0][1]+dirs[dir][1]) in curr[3]:
            continue
        
        if dir == curr[1]:
            if ((curr[0][0]+dirs[dir][0], curr[0][1]+dirs[dir][1]), dir, curr[2] + 1) not in queue:
                if curr[2]+1 > 66404: continue
                queue.append(((curr[0][0]+dirs[dir][0], curr[0][1]+dirs[dir][1]), dir, curr[2] + 1, (list(curr[3]) + [curr[0]])))
        else:
            if ((curr[0][0]+dirs[dir][0], curr[0][1]+dirs[dir][1]), dir, curr[2] + 1001) not in queue:
                if curr[2]+1000 > 66404: continue
                queue.append(((curr[0][0]+dirs[dir][0], curr[0][1]+dirs[dir][1]), dir, curr[2] + 1001, (list(curr[3]) + [curr[0]])))
    queue.sort(key=lambda x: x[2])
    
print(len(sits) + 1)

if VISUALISE:
    for i in sits:
        maze[i[0]][i[1]] = "O"

    for i in maze:
        for j in i:
            print(j, end="")
        print()