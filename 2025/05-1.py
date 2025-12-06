f = open('inputs/5.txt')

freshies = []

count = 0

for line in f:
    if line.strip() == '': break
    dash = line.find('-')
    freshies.append((int(line[0:dash]), int(line[dash+1:])))

for line in f:
    val = int(line)
    for a, b in freshies:
        if a <= val <= b:
            count += 1
            break

print(count)
