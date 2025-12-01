f = open('inputs/1.txt')

left = []
right = []

for line in f:
    left.append(int(line.split('   ')[0]))
    right.append(int(line.split('   ')[1]))
left.sort()
right.sort()

total = 0


for i in range(len(left)):
    print(left[i], right[i])
    total += max(left[i], right[i]) - min(left[i], right[i])

print(total)