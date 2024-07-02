def flip2d(arr):
    tmp = []
    for x in range(len(arr[0])):
        row = ''
        for y in range(len(arr)):
            row += arr[y][x]
        tmp.append(row)
    return tmp

def f(p, s):
    for i in range(len(p)):
        if sum(c != d for l,m in zip(p[i-1::-1], p[i:])
                      for c,d in zip(l, m)) == s: return i
    else: return 0

def columnpalin(pattern):
    print('')
    lp = len(pattern)
    s = -2 if lp % 2 == 0 else -1
    solved = False
    while s < lp - 2 and not solved:
        s += 2
        print(s, "-"*20)
        smudges = 0
        for i in range(s,lp):
            print(smudges, pattern[i], pattern[lp-1-i+s], pattern[i] == pattern[lp-1-i+s])
            if pattern[i] == pattern[lp-1-i+s]:
                continue
            for c in range(len(pattern[i])):
                if pattern[i][c] == pattern[lp-1-i+s][c]:
                    continue
                smudges += 1
                if smudges > 2:
                    break
            if smudges > 2:
                break
        if smudges == 2:
            solved = True
    if solved:
        return s
    return -1

f = open("input.txt")

total = 0
tots2 = 0
pattern = []
reverse = []
for line in f:
    if line.strip() != '':
        pattern.append(line.strip())
        reverse.insert(0, line.strip())
        continue
    
    rowsp = columnpalin(pattern)
    rowsr = columnpalin(reverse)
    calcp = (len(pattern) - rowsp)/2 + rowsp if rowsp > -1 else 0
    calcr = (len(pattern) - rowsr)/2 if rowsr > -1 else 0
    total += max(calcp, calcr) * 100
    pattern = flip2d(pattern)
    reverse = []
    for i in pattern:
        reverse.insert(0, i)
    rowsp = columnpalin(pattern)
    rowsr = columnpalin(reverse)
    calcp = (len(pattern) - rowsp)/2 + rowsp if rowsp > -1 else 0
    calcr = (len(pattern) - rowsr)/2 if rowsr > -1 else 0
    #print(calcp, calcr)
    total += max(calcp, calcr)
    pattern = []
    reverse = []
    #tots2 += 100 * f(pattern) + f([*zip(*pattern)])
    print(int(total))

rowsp = columnpalin(pattern)
rowsr = columnpalin(reverse)
calcp = (len(pattern) - rowsp)/2 + rowsp if rowsp > -1 else 0
calcr = (len(pattern) - rowsr)/2 if rowsr > -1 else 0
total += max(calcp, calcr) * 100
pattern = flip2d(pattern)
reverse = []
for i in pattern:
    reverse.insert(0, i)
rowsp = columnpalin(pattern)
rowsr = columnpalin(reverse)
calcp = (len(pattern) - rowsp)/2 + rowsp if rowsp > -1 else 0
calcr = (len(pattern) - rowsr)/2 if rowsr > -1 else 0
total += max(calcp, calcr)
print(int(total))

