import sys

def explore(pos, steps, full):
    last = []
    even = []
    odd = []
    new = [pos]
    udlr = [0,0,0,0,0,0]
    for i in range(steps):
        print(i)
        last = bfssingle(new, full)
        new = []
        for coord in last:
            if coord[0] == 0 and not udlr[0]:
                udlr[0] = (coord,i)
            if coord[0] == len(full)-1 and not udlr[1]:
                udlr[1] = (coord,i)
            if coord[1] == 0 and not udlr[2]:
                udlr[2] = (coord,i)
            if coord[1] == len(full[0])-1 and not udlr[3]:
                udlr[3] = (coord,i)
            if coord == (0,0) and not udlr[4]:
                udlr[4] = (coord,i)
            if coord == (len(full)-1, len(full[0])-1) and not udlr[5]:
                udlr[5] = (coord,i)
            if i%2 == 0 and coord not in odd:
                odd.append(coord)
                new.append(coord)
            elif i%2 == 1 and coord not in even:
                even.append(coord)
                new.append(coord)
    
    return [udlr, even, odd]

def bfssingle(poss, full):
    next = []
    for pos in poss:
        for new in [(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]-1),(pos[0],pos[1]+1)]:
            if new[0] < 0 or new[0] == len(full): continue
            if new[1] < 0 or new[1] == len(full[0]): continue
            if full[new[0] % len(full)][new[1] % len(full[0])] != '#' and (new[0], new[1]) not in next:
                next.append(new)
    return next

f = open('input.txt')

fullgarden = []

gfound = False

y = x = 0
for line in f:
    row = []
    if not gfound: x = 0
    for c in line.strip():
        if c == 'S': gfound = True
        if not gfound: x += 1
        row.append(c)
    fullgarden.append(row)
    if not gfound: y += 1

starty = y
startx = x

count = 0
count2 = 0
found = explore((starty, startx), int(sys.argv[1]), fullgarden)
for y in range(len(fullgarden)):
    if y == len(fullgarden): print('-'*len(fullgarden))
    for x in range(len(fullgarden[0])):
        if (y,x) in found[1]:
            print('O', end='')
            count +=1
        else:
            print(fullgarden[y%len(fullgarden)][x%len(fullgarden[0])], end='')
        
        if (y,x) in found[2]:
            count2 += 1
    print('')

squares = 1
n = 26501365//131
r = 26501365-((26501365//131)*131)
plots = ((n+1)**2)*count2 + (n**2)*count
plots += (count - len(explore((starty,startx), r, fullgarden)[1])) * n
plots -= (count2 - len(explore((starty,startx), r, fullgarden)[2])) * (n+1)

print(found[0])
print(count, count2)
print(plots)


print(len(fullgarden), len(fullgarden[0]))
print(len(found))