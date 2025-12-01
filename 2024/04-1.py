f = open('inputs/4.txt')

total = 0

ws = []
for line in f:
    l = []
    line = line.strip()
    for c in line:
        l.append(c)
    ws.append(l)

dirs = [
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,-1),
    (0,1),
    (1,-1),
    (1,0),
    (1,1)
]

xmas = {
    'M': 1,
    'A': 2,
    'S': 3
}

for i in range(len(ws)):
    for j in range(len(ws[i])):
        if ws[i][j] == 'X':
            for x,y in dirs:
                count = 0
                for c in xmas:
                    if i+(xmas[c]*x) > len(ws) - 1 or i+(xmas[c]*x) < 0: continue
                    if j+(xmas[c]*y) > len(ws[0]) - 1 or j+(xmas[c]*y) < 0: continue
                    if ws[i+xmas[c]*x][j+(xmas[c]*y)] == c: 
                        count += 1
                if count == 3: 
                    total += 1




print(total)
