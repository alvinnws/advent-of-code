f = open("input.txt")

maze = []
for line in f:
    row = []
    for column in line.strip():
        row.append(column)
    maze.append(row)

for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == 'S':
            starting = (x, y)

end = False
currx = starting[0]
curry = starting[1]
count = 0
state = 0
while not end:
    if state == 0:
        if maze[curry - 1][currx] in ['|','7','F']:
            curry -= 1
            state = 1
        elif maze[curry + 1][currx] in ['|', 'J', 'L']:
            curry += 1
            state = 2
        elif maze[curry][currx - 1] in ['-','L','F']:
            currx -= 1
            state = 3
        else:
            currx += 1
            state = 4
        count += 1
        continue
    if state == 1:
        if maze[curry][currx] == '|':
            curry -= 1
        elif maze[curry][currx] == '7':
            currx -= 1
            state = 3
        else:
            currx += 1
            state = 4
    elif state == 2:
        if maze[curry][currx] == '|':
            curry += 1
        elif maze[curry][currx] == 'J':
            currx -= 1
            state = 3
        else:
            currx += 1
            state = 4
    elif state == 3:
        if maze[curry][currx] == '-':
            currx -= 1
        elif maze[curry][currx] == 'L':
            curry -= 1
            state = 1
        else:
            curry += 1
            state = 2
    elif state == 4:
        if maze[curry][currx] == '-':
            currx += 1
        elif maze[curry][currx] == 'J':
            curry -= 1
            state = 1
        else:
            curry += 1
            state = 2
    count += 1
    if maze[curry][currx] == 'S':
        end = True

print(count/2)