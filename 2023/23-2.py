import sys
sys.setrecursionlimit(10000)

def dfs_rec(maze, jedges, curr, end, history, count):
    visited = history.copy()
    visited[(curr)] = True
    running = 0
    for i in range(len(jedges[curr])):
        neighbour = jedges[curr][i]
        if neighbour[0] in visited: continue
        if neighbour[0] == end: 
            return count + jedges[curr][i][1]
        running = max(running, dfs_rec(maze, jedges, neighbour[0], end, visited, count + jedges[curr][i][1]))
    return running
        
def junction_digger(jedges, edges, junctions, curr):
    q = []
    hist = {}
    q.append((curr, hist, 0))
    while q:
        ch = q.pop(0)
        c = ch[0]
        h = ch[1].copy()
        h[c] = True
        for neigh in edges[c]:
            if neigh not in h and neigh in junctions:
                jedges[curr].append((neigh, ch[2]+1))
                continue
            if neigh not in h:
                q.append((neigh, h, ch[2]+1))

f = open('input.txt')

maze = []
for line in f:
    row = []
    for c in line.strip():
        row.append(c)
    maze.append(row)

edges = {}
junctions = [(0,1),((len(maze) - 1, len(maze[0]) - 2))]
count = 0
for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] == '#': continue
        count += 1
        edges[(y,x)] = []
        if y > 0 and maze[y-1][x] in '.v': edges[(y,x)].append((y-1,x))
        if x > 0 and maze[y][x-1] in '.>': edges[(y,x)].append((y,x-1))
        if y < len(maze) - 1 and maze[y+1][x] in '.v': edges[(y,x)].append((y+1,x))
        if x < len(maze[0]) - 1 and maze[y][x+1] in '.>': edges[(y,x)].append((y,x+1))
        if len(edges[(y,x)]) > 2: junctions.append((y,x))

jedges = {}
for i in junctions:
    jedges[i] = []

for junction in junctions:
    junction_digger(jedges, edges, junctions, junction)

print("This will take a while.")
print(dfs_rec(maze, jedges, junctions[0], junctions[1], {}, 0))
