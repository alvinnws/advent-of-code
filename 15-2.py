def hasher(s):
    curr = 0
    for c in s:
        curr += ord(c)
        curr *= 17
        curr = (curr % 256)
    return curr

f = open("input.txt")

boxes = [[] for x in range(256)]
for s in f.readline().strip().split(','):
    label = s.split('=')[0].split('-')[0]
    if '-' in s:
        focal = s.split('-')[1]
        for i in range(len(boxes[hasher(label)])):
            if boxes[hasher(label)][i][0] == label:
                boxes[hasher(label)].pop(i)
                break
    else:
        focal = s.split('=')[1]
        added = False
        for i in range(len(boxes[hasher(label)])):
            if boxes[hasher(label)][i][0] == label:
                boxes[hasher(label)][i] = (label, focal)
                added = True
                break
        if not added:
            boxes[hasher(label)].append((label, focal))

        
total = 0
for i in range(len(boxes)):
    if boxes[i]:
        for j in range(len(boxes[i])):
            total += (i+1)*(j+1)*int(boxes[i][j][1])
print(total)