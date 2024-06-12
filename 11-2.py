f = open("input.txt")
space = []
for line in f:
    space.append(line.strip())

spaceflip = []
gapsx = []
for j in range(len(space[0])):
    row = []
    for i in range(len(space)):
        row.append(space[i][j])
    if '#' not in row:
        gapsx.append(j)
    spaceflip.append(row)

space = []
galaxies = []
gapsy = []
for j in range(len(spaceflip[0])):
    row = []
    for i in range(len(spaceflip)):
        if spaceflip[i][j] == '#':
            galaxies.append((j, i))
        row.append(spaceflip[i][j])
    if '#' not in row:
        gapsy.append(j)
    space.append(row)

sums = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        distancex = galaxies[j][1] - galaxies[i][1]
        distancey = galaxies[j][0] - galaxies[i][0]
        if distancex < 0:
            distancex = -distancex
        if distancey < 0:
            distancey = -distancey
        for gap in gapsx:
            if galaxies[j][1] < gap < galaxies[i][1] or galaxies[i][1] < gap < galaxies[j][1]:
                distancex += 999999
        for gap in gapsy:
            if galaxies[j][0] < gap < galaxies[i][0] or galaxies[i][0] < gap < galaxies[j][0]:
                distancey += 999999
        sums += (distancey + distancex)
print(sums)