f = open("input.txt")

space = []
for line in f:
    if '#' not in line:
        space.append(line.strip())
    space.append(line.strip())

spaceflip = []
for j in range(len(space[0])):
    row = []
    for i in range(len(space)):
        row.append(space[i][j])
    if '#' not in row:
        spaceflip.append(row)
    spaceflip.append(row)

space = []
galaxies = []
for j in range(len(spaceflip[0])):
    row = []
    for i in range(len(spaceflip)):
        if spaceflip[i][j] == '#':
            galaxies.append((j, i))
        row.append(spaceflip[i][j])
    space.append(row)
    print(row)
    
print(space[galaxies[1][0]][galaxies[1][1]])
sums = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        distancey = galaxies[j][1] - galaxies[i][1]
        distancex = galaxies[j][0] - galaxies[i][0]
        if distancex < 0:
            distancex = -distancex
        if distancey < 0:
            distancey = -distancey
        sums += (distancey + distancex)
print(sums)