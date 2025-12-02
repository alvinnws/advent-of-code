f = open('inputs/2.txt')

def get_dash(s):
    for i in range(len(s)):
        if s[i] == '-': return i

def get_multiples(n, hist):
    if n in hist: return hist[n]
    ls = []
    for i in range(1,n):
        if n % i == 0: ls.append(i)
    hist[n] = ls
    return hist[n]

def has_repeats(s, i):
    base = s[0:i]
    start = i
    while start < len(s):
        if s[start:start+i] != base:
            return False
        start += i
    return True

count = 0
hist = {}
for line in f:
    for s in line.split(','):
        dash = get_dash(s)
        first = int(s[0:dash])
        second = int(s[dash+1:])
        for i in range(first, second+1):
            ilen = len(str(i))
            multiples = get_multiples(ilen, hist)
            for multiple in multiples:
                if has_repeats(str(i), multiple): 
                    count += i
                    break


print(count)