f = open('inputs/9.txt')

total = 0

line = f.readline()
line = line.strip()

str = []
dots = []
file = True
count = 0
for i in line:
    if file:
        for i in range(int(i)):
            str.append(count)
        count += 1
        file = False
    else:
        for i in range(int(i)):
            str.append('.')
        file = True

curr = len(str)-1
i = 0
while i < curr:
    if str[i] == '.':
        str[i] = str[curr]
        str[curr] = '.'
        while str[curr] == '.':
            curr -=1
    i += 1

for i in range(curr+1):
    total += i * int(str[i])

print(total)

f.close()