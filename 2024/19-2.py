from functools import cache

f = open("inputs/19.txt")
 
patterns = f.readline().strip().split(", ")
patterns.sort()

firsts = {}

for pattern in patterns:
    if pattern[0] in firsts:
        firsts[pattern[0]].append(pattern)
    else:
        firsts[pattern[0]] = [pattern]

total = 0

@cache
def explore(word, index):
    count = 0
    if index == len(word):
        return 1
    if word[index] not in firsts: return 0

    for pattern in firsts[word[index]]:
        if index+len(pattern) > len(word): continue
        if word[index:index+len(pattern)] == pattern:
            count += explore(word, index+len(pattern))
    return count

f.readline()

count = 0
for matchy in f:
    total += explore(matchy.strip(), 0)
    count += 1

print(total)