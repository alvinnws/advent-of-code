f = open('inputs/5.txt')

freshies = []

for line in f:
    if line.strip() == '': break
    dash = line.find('-')
    freshies.append((int(line[0:dash]), int(line[dash+1:])))

freshies.sort(key=lambda x: x[0])

print(len(freshies))
deleted = True
while deleted:
    deleted = False
    for i in range(len(freshies)-1):
        if freshies[i][1]+1 >= freshies[i+1][0]:
            if freshies[i+1][1] > freshies[i][1]:
                freshies[i] = (freshies[i][0], freshies[i+1][1])
            freshies.pop(i+1)
            deleted = True
            break

print(len(freshies))

count = 0
for a,b in freshies:
    count += b-a+1

print(count)