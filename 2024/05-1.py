f = open('inputs/5.txt')

total = 0

rules = {}

for line in f:
    if line == "\n": break
    left, right = line.strip().split("|")
    if left in rules:
        rules[left].append(right)
    else:
        rules[left] = [right]

for line in f:
    seen = []
    nums = line.strip().split(',')
    flag = True
    for num in nums:
        if flag == False: break
        if num in rules:
            for check in rules[num]:
                if check in seen:
                    flag = False
                    break
        seen.append(num)
    if flag == True:
        total += int(nums[len(nums)//2])

print(total)
