soil, fert, water, light, temp, humid, location = {}, {}, {}, {}, {}, {}, {}

f = open("inputs/5.txt")
seedpairs = f.readline().split(":")[1].strip().split(" ")
seeds = []
for i in range(0,len(seedpairs),2):
    seeds.append((int(seedpairs[i]), int(seedpairs[i+1])))
modes = [soil, fert, water, light, temp, humid, location]
mode = -1

f.readline()
for line in f:
    line = line.strip()
    if ':' in line:
        mode += 1
        continue
    if line == '':
        continue
    dest, source, length = line.split(" ")
    modes[mode][(int(dest), int(dest)+int(length)-1)] = int(dest) - int(source)

final = None
checking = 0
modes.reverse()
while final == None:
    zao = False
    curr = checking
    if checking % 10000 == 0:
        print(checking)
    for i in range(len(modes)):
        for s, e in modes[i]:
            if s <= curr <= e:
                curr = curr - modes[i][(s, e)]
                break
    checking += 1
    for s, e in seeds:
        if s <= curr <= s+e-1:
            final = curr

print(checking - 1)