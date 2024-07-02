def getNextDiff(ls):
    tmp = []
    allZero = True
    for i in range(len(ls) - 1):
        diff = ls[i+1] - ls[i]
        if not diff == 0:
            allZero = False
        tmp.append(diff)
    
    if allZero:
        return ls[-1]
    else:
        return ls[-1] + getNextDiff(tmp)

f = open("input.txt")
total = 0
for line in f:
    ls = []
    for i in line.strip().split(' '):
        ls.append(int(i))
    total += getNextDiff(ls)

print(total)
    