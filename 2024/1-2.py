f = open('inputs/1.txt')

left = []
right = []

for line in f:
    left.append(int(line.split('   ')[0]))
    right.append(int(line.split('   ')[1]))

total = 0

for i in left:
    total += i * right.count(i)
    
print(total)