from copy import deepcopy

f = open('inputs/8.txt')

total = 0

ls = []
freq_occurance = {}
for line in f:
    row = []
    for c in line.strip():
        row.append(c)
        if c != '.': 
            if c in freq_occurance:
                freq_occurance[c] += 1
            else:
                freq_occurance[c] = 1
    ls.append(row)

locs = {}
for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] in freq_occurance:
            if ls[i][j] in locs:
                locs[ls[i][j]].append((i, j))
            else:
                locs[ls[i][j]] = [(i, j)]

def count_antinodes(ls, original, freq, seen, loc):
    locs = loc[freq]
    
    nodes = 0
    for i in range(len(locs)):
        f = locs[i]
        for j in range(len(locs)):
            s = locs[j]
            if f == s: continue

            pos1 = f[1] - (s[1] - f[1])
            pos2 = f[0] - (s[0] - f[0])
            walk1 = (s[1] - f[1])
            walk2 = (s[0] - f[0])
            while  pos1 < len(original[0]) and pos1 >= 0 and pos2 < len(original) and pos2 >= 0:
                ls[pos2][pos1] = '#'
                if (pos2, pos1) not in seen:
                    seen.add((pos2, pos1))
                    nodes += 1
                pos1 -= walk1
                pos2 -= walk2
    return nodes

original = deepcopy(ls)
seen = set()
for i in freq_occurance:
    total += count_antinodes(ls, original, i, seen, locs)

for i in ls:
    for c in i:
        if c in freq_occurance and len(locs[c]) > 1:
            total += 1

print(total)

f.close()