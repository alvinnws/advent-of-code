f = open('inputs/11.txt')

devices = {}

for line in f:
    devices[line.split(':')[0]] = [out for out in line.split(':')[1].strip().split(' ')]

q = [('you', set())]
count = 0
while q:
    curr, hist = q.pop(0)
    hist.add(curr)
    for n in devices[curr]:
        if n in hist: continue
        if n == 'out':
            count += 1
            continue
        his2 = hist.copy()
        q.append((n, his2))

print(count)