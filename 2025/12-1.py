f = open('inputs/12.txt')

def check_repeat(shape, list):
    for other in list:
        if len(other) != len(shape): continue
        if len(other[0]) != len(shape[0]): continue
        sames = 0
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if shape[i][j] == other[i][j]: sames += 1
        if sames == len(shape)*len(shape[0]): return True
    return False

def rotate(shape):
    new = [[] for _ in range(len(shape[0]))]
    for i in range(len(shape)):
        for j in range(len(shape[0])):
            new[j].insert(0, shape[i][j])
    return new

def flip_v(shape):
    new = [c[::] for c in shape[::-1]]
    return new

def flip_h(shape):
    new = [c[::-1] for c in shape[::]]
    return new

def count(shape):
    return sum([sum(list(map(lambda x: 1 if x else 0, c))) for c in shape])

c = 0

shapes = []
for line in f:
    if line.strip() == '': 
        ls = shapes[-1]
        shape = ls[0]
        h = flip_h(shape)
        v = flip_v(shape)
        sps = [shape, h, v]
        for i in range(3):
            sps.append(rotate(sps[-3]))
            sps.append(rotate(sps[-3]))
            sps.append(rotate(sps[-3]))
        for s in sps:
            if not check_repeat(s, ls):
                ls.append(s)
    elif line[1] == ":": shapes.append([[]])
    elif line[1] in '0123456789':
        size = tuple(map(int, line.split(':')[0].split('x')))
        needed = list(map(int, line.split(':')[1].strip().split(' ')))
        sqs = 0
        for n in range(len(needed)):
            sqs += needed[n] * count(shapes[n][0])
        if size[0]*size[1] > sqs:
            c += 1
        #print(size[0]*size[1] > sqs)
        grid = [[False for _ in range(size[1])] for __ in range(size[0])]
    else: shapes[-1][-1].append([c == '#' for c in line.strip()])
    """
n = flip_h(shapes[0][0])
for i in shapes:
    print(count(i[0]))
for i in shapes[0][0]:
    print(i)
print(" ")
for i in n:
    print(i)
print()
o = flip_h(n)
for i in o:
    print(i)"""

print(c)