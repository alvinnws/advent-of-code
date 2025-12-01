from copy import deepcopy

f = open('inputs/8.txt')

total = 0

ls = []
fres = {}
for line in f:
    row = []
    for c in line.strip():
        row.append(c)
        if c != '.': 
            if c in fres:
                fres[c] += 1
            else:
                fres[c] = 1
    ls.append(row)

locs = {}
for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] in fres:
            if ls[i][j] in locs:
                locs[ls[i][j]].append((i, j))
            else:
                locs[ls[i][j]] = [(i, j)]

def count_antinodes(ls, original, freq, seen, loc):
    locs = loc[freq]
    for i in range(len(ls)):
        for j in range(len(ls[0])):
            if ls[i][j] == freq:
                locs.append((i, j))
    
    nodes = 0
    for i in range(len(locs)):
        f = locs[i]
        for j in range(i+1, len(locs)):
            s = locs[j]
            if f == s: continue

            pos1 = f[1] - (s[1] - f[1])
            pos2 = f[0] - (s[0] - f[0])
            if  pos1 < len(ls[0]) and pos1 >= 0 and pos2 < len(ls) and pos2 >= 0 and (pos2, pos1) not in seen:
                original[pos2][pos1] = '#'
                seen.add((pos2, pos1))
                nodes += 1
            pos1 = s[1] - (f[1] - s[1])
            pos2 = s[0] - (f[0] - s[0])
            if  pos1 < len(ls[0]) and pos1 >= 0 and pos2 < len(ls) and pos2 >= 0 and (pos2, pos1) not in seen:
                original[pos2][pos1] = '#'
                seen.add((pos2, pos1))
                nodes += 1
    return nodes
original = deepcopy(ls)
seen = set()
for i in fres:
    total += count_antinodes(ls, original, i, seen, locs)
print(total)

f.close()