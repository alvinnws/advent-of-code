import sys
sys.setrecursionlimit(10000)

def dfs_rec(edges, curr, end, history, count):
    visited = history.copy()
    visited.append(curr)
    count += 1
    running = 0
    for neighbour in edges[curr]:
        if neighbour in visited: continue
        if neighbour == end: return count + 1
        running = max(running, dfs_rec(edges, neighbour, end, visited, count))
    return running

f = open('input.txt')

maze = []
for line in f:
    row = []
    for c in line.strip():
        row.append(c)
    maze.append(row)

edges = {}

for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] == '#': continue
        edges[(y,x)] = []
        if y > 0 and maze[y-1][x] == '.' and maze[y][x] != 'V': edges[(y,x)].append((y-1,x))
        if x > 0 and maze[y][x-1] == '.' and maze[y][x] != '>': edges[(y,x)].append((y,x-1))
        if y < len(maze) - 1 and maze[y+1][x] in '.v': edges[(y,x)].append((y+1,x))
        if x < len(maze[0]) - 1 and maze[y][x+1] in '.>': edges[(y,x)].append((y,x+1))

print("Please be patient, it might take a couple seconds")
print(dfs_rec(edges, (0,1), (len(maze) - 1, len(maze[0]) - 2), [], -1))