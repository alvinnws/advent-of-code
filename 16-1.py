def beam(states, map, dir, x, y):
    """
    States -> [[{
                0: None,
                1: None,
                2: None,
                3: None
                }, {...}, {...}],
                [{...}],[{...}], ...]
    map -> [[],[],[]]
    dir -> 0, 1, 2, 3
    x, y -> int
    0 <= x,y <= len(map), len(map[0])
    """
    def straight(states, map, dir, x, y):
        if dir == 0: y-=1
        elif dir == 1: x+=1
        elif dir == 2: y+=1
        else: x-=1
        beam(states, map, dir, x, y)
        return

    if x < 0 or y < 0: return
    if x > len(map[0]) - 1 or y > len(map) - 1: return 

    if states[y][x][dir] == True: return
        
    states[y][x][dir] = True

    if map[y][x] == '.':
        straight(states, map, dir, x, y)
        return
    
    elif map[y][x] == '|':
        if dir == 1 or dir == 3:
            beam(states, map, 0, x, y-1)
            beam(states, map, 2, x, y+1)
        else:
            straight(states, map, dir, x, y)
            return
    elif map[y][x] == '-':
        if dir == 0 or dir == 2:
            beam(states, map, 1, x+1, y)
            beam(states, map, 3, x-1, y)
        else:
            straight(states, map, dir, x, y)
    elif map[y][x] == '/':
        if dir == 0: beam(states, map, 1, x+1, y)
        elif dir == 1: beam(states, map, 0, x, y-1)
        elif dir == 2: beam(states, map, 3, x-1, y)
        else: beam(states, map, 2, x, y+1)
    else: # '\'
        if dir == 0: beam(states, map, 3, x-1, y)
        elif dir == 1: beam(states, map, 2, x, y+1)
        elif dir == 2: beam(states, map, 1, x+1, y)
        else: beam(states, map, 0, x, y-1)
    return

import sys
sys.setrecursionlimit(12100)

f = open("input.txt")

states = []
state = { 0: None, 1: None, 2: None, 3: None }
map = []

for line in f:
    row = []
    row2 = []
    for c in line.strip():
        row.append(c)
        row2.append(state.copy())
    map.append(row)
    states.append(row2)

beam(states, map, 1, 0, 0)

total = 0
for y in states:
    for x in y:
        if True in x.values():
            total += 1
print(total)