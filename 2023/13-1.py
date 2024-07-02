def isValid(s):
    half = len(s)/2 + 1
    if len(s) % 2 == 1:
        half -= 0.5
        half = half
    for i in range(int(half)):
        if s[i] != s[-i-1]:
            return False
    return True

class pattern():
    def __init__(self, pattern):
        self.pattern = pattern

    def getMirrorPos(self):
        left = 0
        right = 0
        s, e = -1, len(self.pattern[0])
        rightflag = False
        while s != len(self.pattern[0]) - 2 and not rightflag:
            s += 1
            found = True
            for i in self.pattern:
                if not isValid(i[s:e]):
                    found = False
            
            if found:
                rightflag = True
                right = len(self.pattern[0]) - (e-s)/2
                if right % 1 == 0.5:
                    right = 0
        s, e = 0, len(self.pattern[0]) + 1
        leftflag = False
        while e != 2 and not leftflag:
            e -= 1
            found = True
            for i in self.pattern:
                if not isValid(i[s:e]):
                    found = False
            if found:
                leftflag = True
                left = (e-s)/2
                if left % 1 == 0.5:
                    left = 0
        return max(left, right)

f = open("input.txt")

total = 0
ptrn = []
for line in f:
    if line.strip() == '':
        p = pattern(ptrn)
        total += p.getMirrorPos()

        flip = []
        for i in range(len(ptrn[0])):
            row = []
            for j in range(len(ptrn)):
                row.append(ptrn[j][i])
            flip.append(row)

        p = pattern(flip)

        total += p.getMirrorPos() * 100

        ptrn = []
        continue
    ptrn.append(line.strip())

p = pattern(ptrn)
total += p.getMirrorPos()

flip = []
for i in range(len(ptrn[0])):
    row = []
    for j in range(len(ptrn)):
        row.append(ptrn[j][i])
    flip.append(row)
p = pattern(flip)
total += p.getMirrorPos() * 100
ptrn = []

print(total)