from random import random

def bfs(edges, start, end):
    q = [[start]]
    v = []
    while q:
        curr = q.pop(0)
        if curr[-1] in v: continue
        if curr[-1] == end: return curr
        v.append(curr[-1])
        for n in edges[curr[-1]]:
            if n in v: continue
            new_path = curr.copy()
            new_path.append(n)
            q.append(new_path)

edges = {}
f = open("input.txt")

ls = []
for line in f:
    left = line.split(":")[0]
    right = line.strip().split(": ")[1].split(" ")
    if left not in edges: edges[left] = []
    if left not in ls: ls.append(left)
    for r in right:
        if r not in edges: edges[r] = []
        if r not in ls: ls.append(r)
        edges[left].append(r)
        edges[r].append(left)

freqs = {}
for i in range(1000):
    print(i)
    start = int(random()*len(ls)) - 1
    end = int(random()*len(ls)) - 1
    path = bfs(edges, ls[start], ls[end])
    for i in range(len(path)-1):
        ed =[path[i], path[i+1]]
        ed.sort()
        word = str(ed[0]) + str(ed[1])
        if word not in freqs:
            freqs[word] = 0
        freqs[word] += 1

res = sorted(freqs.items(), key=lambda item: item[1], reverse=True)
q = []
v = []
q.append("ctq")
while q:
    curr = q.pop(0)
    if curr in v: continue
    v.append(curr)
    for n in edges[curr]:
        if n in v: continue
        q.append(n)
tc = len(v)

for i in res[0:3]:
    edges[i[0][0:3]].remove(i[0][3:])
    edges[i[0][3:]].remove(i[0][0:3])

q = []
v = []
q.append("ctq")
while q:
    curr = q.pop(0)
    if curr in v: continue
    v.append(curr)
    for n in edges[curr]:
        if n in v: continue
        q.append(n)
cnow = len(v)
total = cnow * (tc - cnow)
print(total)