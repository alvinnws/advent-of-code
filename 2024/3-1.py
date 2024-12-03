f = open('inputs/3.txt')

total = 0

for line in f:
    for i in range(len(line)):
        if line[i:i+4] == 'mul(':
            j = i+1
            while line[j] != ')':
                j += 1
            n = line[i+4:j].split(',')
            if len(n) != 2: continue
            try:
                int(n[0])
                int(n[1])
            except:
                continue
            total += int(n[0]) * int(n[1])

print(total)
