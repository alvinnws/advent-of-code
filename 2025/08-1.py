import math

class JunctionBox():
    def __init__(self, str_pos):
        pos = list(map(int, str_pos.strip().split(',')))
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
    
    def distance_to(self, other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
    
f = open('inputs/8.txt')

junc_boxes = []
for line in f:
    junc_boxes.append(JunctionBox(line))

distances = []
for i in range(len(junc_boxes)):
    for j in range(i+1, len(junc_boxes)):
        distances.append((i, j, junc_boxes[i].distance_to(junc_boxes[j])))

distances.sort(key=lambda x: -x[2])

parent = list(range(len(junc_boxes)))

def find(p):
    if p == parent[p]:
        return p
    
    parent[p] = find(parent[p])
    return parent[p]

def union(p, q):
    root_p = find(p)
    root_q = find(q)

    if root_p != root_q:
        parent[root_q] = root_p

for i in range(1000):
    p, q, dist = distances.pop()
    union(p, q)

counts = [0]*len(parent)

for i in range(len(parent)):
    counts[find(i)] += 1

counts.sort()
print(counts)

print(counts[-1]*counts[-2]*counts[-3])
