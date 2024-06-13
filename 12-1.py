import re

def isValid(condition, group):
    match = "\.*"
    for i in group:
        match += '#{' + str(i) + '}' + '\.+'
    match = match[0:len(match)-1] + '*'
    x = re.search(match, condition)
    if x == None or len(x.group()) != len(condition):
        return False
    return True

f = open("input.txt")

total = 0
linenum = 0

for line in f:
    if linenum % 100 == 0: 
        print(linenum)
    line = line.strip()
    condition = line.split(" ")[0]
    group = [int(i) for i in line.split(" ")[1].split(",")]
    possible = []
    possible.append(condition)
    while True:
        curr = possible.pop(0)
        if '?' not in curr:
            possible.append(curr)
            break
        for i in range(len(curr)):
            if curr[i] == '?':
                one = curr[0:i] + '.' + curr[i+1:]
                two = curr[0:i] + '#' + curr[i+1:]
                x = re.search('#{' + str((max(group) + 1)) + '}', two)
                
                match = "\.*"
                for i in group:
                    match += '(#|\?){' + str(i) + '}' + '(\.|\?)+'
                match = match[0:len(match)-1] + '*'
                y = re.search(match, one)
                z = re.search(match, two)

                if one.count('?') + one.count('#') >= sum(group) and y != None:
                    possible.append(one)
                if two.count('#') <= sum(group) and x == None and z != None:
                    possible.append(two)
                break
        continue
    count = 0
    linenum += 1
    for i in possible:
        # print(i, group, isValid(i, group))
        if isValid(i, group):
            count += 1

    total += count
print(total)