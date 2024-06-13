import functools

@functools.lru_cache(maxsize=None)
def calc(condition, groupnum, group):
    if groupnum == len(group):
        if '#' in condition:
            return 0
        return 1
    
    if not condition:
        return 0
    
    if condition[0] == '.':
        count = calc(condition[1:], groupnum, group)
    
    if condition[0] == '#':
        next = condition[0:group[groupnum]].replace('?','#')
        if next != group[groupnum] * '#':
            return 0
        if len(next) == len(condition):
            if groupnum == len(group) - 1:
                return 1
            return 0
        if condition[group[groupnum]] == '#':
            return 0
        count = calc(condition[group[groupnum] + 1:], groupnum + 1, group)

    if condition[0] == '?':
        count = calc('.' + condition[1:], groupnum, group) + calc('#' + condition[1:], groupnum, group) 
    
    return count    

f = open("input.txt")

total = 0
linenum = 0

for line in f:
    line = line.strip()
    condition = line.split(" ")[0]
    group = [int(i) for i in line.split(" ")[1].split(",")]

    for i in range(4):
        condition += '?' + line.split(" ")[0]
        group += [int(i) for i in line.split(" ")[1].split(",")]


    total += calc(condition, 0, tuple(group))

    
    linenum += 1

print(total)