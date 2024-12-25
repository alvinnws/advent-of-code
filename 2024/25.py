f = open("inputs/25.txt")

curr = 0
locks = []
keys = []
build = [0,0,0,0,0]
key = True
for line in f:
    if curr == 0:
        if line.strip() == "#####":
            key = False
            build = [0,0,0,0,0]
        else:
            key = True
            build = [5,5,5,5,5]
        curr += 1
    elif curr < 7:
        for c in range(len(line.strip())):
            if line[c] == "." and key:
                build[c] -= 1
            elif line[c] == "#" and not key:
                build[c] += 1
        curr += 1
    else:
        if key:
            keys.append(build)
        else:
            locks.append(build)
        curr = 0

if key:
    keys.append(build)
else:
    locks.append(build)

total = 0

for lock in locks:
    for key in keys:
        for pin in range(len(key)):
            if lock[pin] + key[pin] > 5:
                total -= 1
                break
        total += 1

print(total)