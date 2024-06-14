def flip2d(arr):
    tmp = []
    for x in range(len(arr[0])):
        row = ''
        for y in range(len(arr)):
            row += arr[y][x]
        tmp.append(row)
    return tmp

def columnpalin(pattern):
    #print('-'*15)
    #for i in pattern:
     #   print(i)
    s, e, found, right = -1, len(pattern), False, 0
    while s != e - 2 and not found:
        s += 1
        #print(s, '-'*10)
        smudges = 0
        for i in range(s, e):
            #print(pattern[i], pattern[e - 1 - i + s])
            if pattern[i] == pattern[e - 1 - i + s]:
                continue
            for c in range(len(pattern[i])):
                if pattern[i][c] != pattern[e - 1 - i + s][c]:
                    smudges += 1
                if smudges > 2:
                    break
            if smudges > 2:
                break
        if smudges != 2:
            continue
        found = True
    #print(s-1, found)
    if found != True:
        return 0
    return s - 1

f = open("input.txt")

total = 0
pattern = []
reverse = []
for line in f:
    if line.strip() != '':
        pattern.append(line.strip())
        reverse.insert(0, line.strip())
        continue
    
    total += max(columnpalin(pattern), len(pattern) - columnpalin(reverse) - 2 if columnpalin(reverse) else 0) * 100
    pattern = flip2d(pattern)
    reverse = flip2d(reverse)
    total += max(columnpalin(pattern), len(pattern) - columnpalin(reverse) - 2 if columnpalin(reverse) else 0)
    pattern = []
    reverse = []
    print(total)

total += max(columnpalin(pattern), len(pattern) - columnpalin(reverse) - 2 if columnpalin(reverse) else 0) * 100
pattern = flip2d(pattern)
reverse = flip2d(reverse)
total += max(columnpalin(pattern), len(pattern) - columnpalin(reverse) - 2 if columnpalin(reverse) else 0)

print(total)
