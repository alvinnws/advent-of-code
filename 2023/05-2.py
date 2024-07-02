soil, fert, water, light, temp, humid, location = {}, {}, {}, {}, {}, {}, {}

f = open("inputs/5.txt")
seedpairs = f.readline().split(":")[1].strip().split(" ")
seeds = []
for i in range(0,len(seedpairs),2):
    seeds.append((int(seedpairs[i]), int(seedpairs[i+1])))
print(seeds)
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
    modes[mode][(int(source), int(source)+int(length)-1)] = int(dest) - int(source)

curmin = None
while len(seeds) > 0:
    seedpair = seeds.pop(0)
    seed = seedpair[0]
    end = seedpair[1]
    curr = int(seed)
    if len(seeds) % 10000 == 0:
        print(len(seeds), curmin)
    for i in range(len(modes)):
        for s, e in modes[i]:
            if s <= curr <= e:
                if curr + end - 1 > e:
                    seeds.append((seed+e-curr+1, end-(e-curr)-1))
                curr = curr + modes[i][(s, e)]
                break
    if curmin == None:
        curmin = curr
    curmin = min(curmin, curr)

print(curmin)