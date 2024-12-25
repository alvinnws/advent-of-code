from collections import defaultdict
f = open("inputs/23.txt")

connections = defaultdict(set)

for line in f:
    left = line.strip().split("-")[0]
    rght = line.strip().split("-")[1]
    connections[left].add(rght)
    connections[rght].add(left)

sets = set()

for i in connections:
    for j in connections:
        if i == j: continue
        if j not in connections[i]: continue
        for k in connections:
            if j == k or k == i: continue
            if k in connections[i] and k in connections[j]: 
                sets.add(tuple(sorted([i,j,k])))

while len(sets) > 1:
    curr_sets = list(sets)
    i = 0
    while i < len(curr_sets):
        curr = curr_sets[i]
        sets.remove(curr)
        curr = list(curr)

        for j in connections:
            if j in curr: continue
            match = True
            for k in curr:
                if j not in connections[k]:
                    match = False
                    break
            if match:
                curr.append(j)
                sets.add(tuple(sorted(curr)))
                curr.pop()
        i += 1
        
print("".join(item + "," for item in list(sets)[0])[:-1])