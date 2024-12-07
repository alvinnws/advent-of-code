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
    
mapmap = create_map(INPUT_DIR)
total = 0

pos = findstart(mapmap)

# 0 UP 1 RIGHT 2 LEFT 3 DOWN
np = {
    0: (-1, 0),
    1: ( 0, 1),
    2: ( 1, 0),
    3: ( 0,-1)
}
cd = 0

visited = []
uniques = set()
steps = 0
while True:
    visited.append((pos[0], pos[1], cd))
    uniques.add((pos[0],pos[1]))
    next = [pos[0]+np[cd][0], pos[1]+np[cd][1]]
    if next[0] < 0 or next[1] == len(mapmap[1]) or next[0] == len(mapmap) or next[1] < 0:
        break
    if mapmap[next[0]][next[1]] == '#':
        cd = (cd + 1) % 4
        pos = [pos[0]+np[cd][0], pos[1]+np[cd][1]]
    else: 
        pos = next
    steps += 1

print(len(uniques))
quit()