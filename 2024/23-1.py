from collections import defaultdict
f = open("inputs/23.txt")

connections = defaultdict(set)

for line in f:
    left = line.strip().split("-")[0]
    rght = line.strip().split("-")[1]
    connections[left].add(rght)
    connections[rght].add(left)

total = 0

for i in connections:
    for j in connections:
        if i == j: continue
        if j not in connections[i]: continue
        for k in connections:
            if j == k or k == i: continue
            if k in connections[i] and k in connections[j]: 
                if i[0] == "t" or j[0] == "t" or k[0] == "t":
                    total += 1

total //= 6
print(total)