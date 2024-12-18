from copy import deepcopy

INPUT_DIR = 'inputs/6.txt'

def create_map(input_dir):
    f = open(input_dir)

    guard_map = []
    for line in f:
        row = []
        for c in line.strip():
            row.append(c)
        guard_map.append(row)
    
    f.close()

    return guard_map

def findstart(mapmap):
    pos = None
    for i in range(len(mapmap)):
        if pos: break
        for j in range(len(mapmap[0])):
            if mapmap[i][j] == '^':
                pos = [i, j]
                break
    return pos

def explore(mapmap, pos, cd, visited): 
    while True:
        if (pos[0], pos[1], cd) in visited:
            return True
        nextloop = [pos[0]+np[cd][0], pos[1]+np[cd][1]]
        visited.add((pos[0], pos[1], cd))

        if nextloop[0] < 0 or nextloop[1] == len(mapmap[1]) or nextloop[0] == len(mapmap) or nextloop[1] < 0:
            break
        if mapmap[nextloop[0]][nextloop[1]] == '#':
            cd = (cd + 1) % 4
        else: 
            pos = nextloop
    return False

mapmap = create_map(INPUT_DIR)

pos = findstart(mapmap)

# 0 UP 1 RIGHT 2 LEFT 3 DOWN
np = {
    0: (-1, 0),
    1: ( 0, 1),
    2: ( 1, 0),
    3: ( 0,-1)
}
cd = 0

visited = set()
steps = 0
blocks = set()
total = 0
while True:
    next = [pos[0]+np[cd][0], pos[1]+np[cd][1]]
    loopcheck = deepcopy(visited)
    visited.add((pos[0], pos[1], cd))
    loopmap = deepcopy(mapmap)

    if next[0] < 0 or next[1] == len(mapmap[1]) or next[0] == len(mapmap) or next[1] < 0:
        break
    if mapmap[next[0]][next[1]] == '#':
        cd = (cd + 1) % 4
    else: 
        loopmap[next[0]][next[1]] = "#"
        nocheck = False
        for i in range(4):
            if (next[0], next[1], i) in visited:
                nocheck = True
        if (not nocheck) and explore(loopmap, pos, cd, loopcheck):
            blocks.add((next[0], next[1]))
        pos = next
        steps += 1

print(len(blocks))
quit()