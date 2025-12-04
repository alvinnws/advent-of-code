f = open('inputs/3.txt')

count = 0
for line in f:
    l,r = 0,0
    for i in range(len(line.strip())):
        n = int(line[i])
        if n>l and i < len(line)-2:
            l = n
            r = int(line[i+1])
        elif n>r:
            r = n
    count += int(''.join([str(l),str(r)]))

print(count)