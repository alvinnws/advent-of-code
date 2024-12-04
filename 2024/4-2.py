f = open('inputs/4.txt')

total = 0

ws = []
for line in f:
    l = []
    line = line.strip()
    for c in line:
        l.append(c)
    ws.append(l)

for i in range(1, len(ws)-1):
    for j in range(1, len(ws[i])-1):
        if ws[i][j] == 'A':
            d1, d2 = (-1,-1), (1, 1)
            d3, d4 = (-1, 1), (1,-1)
            if     (ws[i+d1[0]][j+d1[1]] == 'M' and ws[i+d2[0]][j+d2[1]] == 'S') or (ws[i+d2[0]][j+d2[1]] == 'M' and ws[i+d1[0]][j+d1[1]] == 'S'):
                if (ws[i+d3[0]][j+d3[1]] == 'M' and ws[i+d4[0]][j+d4[1]] == 'S') or (ws[i+d4[0]][j+d4[1]] == 'M' and ws[i+d3[0]][j+d3[1]] == 'S'):
                    total += 1

print(total)
