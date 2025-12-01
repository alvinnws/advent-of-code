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

    sorts = False
    while not sorts:
        seen = []
        sorts = True
        for i in range(len(nums)):
            if sorts == False: break
            if nums[i] in rules:
                for check in rules[nums[i]]:
                    if check in seen:
                        sorts = False
                        tmp = nums[i]
                        nums[i] = nums[i-1]
                        nums[i-1] = tmp
                        break
            seen.append(nums[i])


    if flag == False:
        total += int(nums[len(nums)//2])

print(total)
