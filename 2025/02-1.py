f = open('inputs/2.txt')

def get_dash(s):
    for i in range(len(s)):
        if s[i] == '-': return i

count = 0
for line in f:
    for s in line.split(','):
        dash = get_dash(s)
        first = int(s[0:dash])
        second = int(s[dash+1:])
        for i in range(first, second+1):
            ilen = len(str(i))
            if ilen % 2 == 1: continue
            if str(i)[0:ilen//2] == str(i)[ilen//2:]:
                count += i

print(count)