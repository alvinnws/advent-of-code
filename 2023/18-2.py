up = 0
right = 0
down = 0
left = 0

f = open("input.txt")
coords = [(0,0)]
peri = 0
x = y = 0
for line in f:
    dist = int(line.split(' ')[2][2:-3], 16)
    if line[-3] == "3":
        y -= dist
        
    elif line[-3] == "0":
        x += dist

    elif line[-3] == "2":
        x -= dist

    else: 
        y += dist
    coords.append((y,x))
    peri += dist

count = 0
coords.append(coords[0])

for i in range(len(coords) - 1):
    count += coords[i][0] * coords[i+1][1] - coords[i][1] * coords[i+1][0]

count /= 2
if count < 0:
    count -= 2*count
print(int(count + peri/2 + 1))