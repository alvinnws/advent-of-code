f = open("inputs/20.txt")

maze = [[c for c in l.strip()] for l in f]

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            start = (i,j)
        elif maze[i][j] == "E":
            end = (i,j)

dirs = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
]

queue = [start]
visited = []
while queue:
    curr = queue.pop()
    visited.append(curr)
    for dir in dirs:
        if maze[curr[0]+dir[0]][curr[1]+dir[1]] == "E":
            break
        if maze[curr[0]+dir[0]][curr[1]+dir[1]] == "." and (curr[0]+dir[0],curr[1]+dir[1]) not in visited:
            queue.append((curr[0]+dir[0],curr[1]+dir[1]))
        
quota = len(visited)

steps = {}
step2 = {}
for i in range(len(visited)):
    step2[visited[i]] = visited[i+1:]
    if i == len(visited)-1: 
        steps[visited[i]] = end
    else: 
        steps[visited[i]] = visited[i+1]

queue = [(start, [], [])]

cheats = {}

used = set()
while queue:
    curr, state, visited = queue.pop(0)
    if len(visited) > quota: continue
    visited.append(curr)
    for dir in dirs:
        next = (curr[0]+dir[0],curr[1]+dir[1])
        if next[0] < 0 or next[0] >= len(maze) or next[1] < 0 or next[1] >= len(maze[0]) or len(visited) == quota: continue
        if maze[curr[0]+dir[0]][curr[1]+dir[1]] == "E":
            if len(state) == 1:
                state.append(end)
            if len(state) == 2 and (state[0], state[1]) in used: continue
            elif len(state) == 2:
                used.add(((state[0], state[1]),len(visited)))
            if len(visited) in cheats:
                cheats[len(visited)] += 1
            else:
                cheats[len(visited)] = 1


            break
        if next not in visited:
            if maze[curr[0]+dir[0]][curr[1]+dir[1]] == ".":
                state2 = state.copy()

                if len(state2) == 2 and maze[curr[0]][curr[1]] == "." and next != steps[curr]: continue
                elif len(state2) == 2 and maze[curr[0]][curr[1]] == "." and next == steps[curr]:
                    visited += step2[curr]
                    used.add(((state2[0], state[1]), len(visited)))
                    if len(visited) in cheats:
                        cheats[len(visited)] += 1
                    else:
                        cheats[len(visited)] = 1
                    continue


                if len(state) == 1:
                    state2.append(next)
                queue.append((next, state2, visited.copy()))
            elif len(state) == 1 and maze[next[0]][next[1]] == ".":
                state2 = state.copy()
                state2.append(next)
                queue.append((next,state2,visited.copy()))
            elif len(state) == 0:
                state2 = state.copy()
                state2.append(next)
                queue.append((next,state2,visited.copy()))


total = 0
for i in cheats:
    if quota - i < 100: continue
    total += cheats[i]

print(total)