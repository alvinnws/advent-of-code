def hasher(s):
    curr = 0
    for c in s:
        curr += ord(c)
        curr *= 17
        curr = (curr % 256)
    return curr

f = open("input.txt")

total = 0
for s in f.readline().strip().split(','):
    total += hasher(s)
print(total)