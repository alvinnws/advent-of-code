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

@cache
def explore(word, index):
    if index == len(word): return True
    if word[index] not in firsts: return False

    for pattern in firsts[word[index]]:
        if index+len(pattern) > len(word): continue
        if word[index:index+len(pattern)] == pattern and explore(word, index+len(pattern)): return True
    return False

f.readline()

total = 0
for matchy in f:
    if explore(matchy.strip(), 0): total += 1

print(total)