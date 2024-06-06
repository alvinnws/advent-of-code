soil, fert, water, light, temp, humid, location = {}, {}, {}, {}, {}, {}, {}

f = open("inputs/5.txt")
seeds = f.readline().split(":")[1].strip().split(" ")
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
curr = int(seeds[0])
for seed in seeds:
    curr = int(seed)
    for i in range(len(modes)):
        for s, e in modes[i]:
            if s <= curr <= e:
                curr = curr + modes[i][(s, e)]
                break
    if curmin == None:
        curmin = curr
    curmin = min(curmin, curr)

print(curmin)