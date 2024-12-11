f = open('inputs/11.txt')

total = 0

stones = f.readline().strip().split()

for abc in range(25):
    i = 0
    while i < len(stones):
        if stones[i] == '0':
            stones[i] = '1'
        elif len(stones[i]) % 2 == 0:
            stones.insert(i+1, str(int(stones[i][len(stones[i])//2:])))
            stones[i] = stones[i][:len(stones[i])//2]
            i += 1
        else:
            stones[i] = str(int(stones[i])*2024)
        i += 1

print(len(stones))

f.close()