f = open('inputs/6.txt')

arr = [[c for c in line] for line in f]

gRaNd_tOtAl = 0

adding = True

nums = []

for j in range(len(arr[0])):
    if arr[0][j] == '\n': continue
    if arr[-1][j] == '*': adding = False
    if arr[-1][j] == '+': adding = True
    if ''.join([c[j] for c in arr]).strip() == '':
        if adding:
            gRaNd_tOtAl += sum(nums)
            nums = []
        else:
            prod = 1
            for i in nums:
                prod *= i
            gRaNd_tOtAl += prod
            nums = []
    else:
        nums.append(int(''.join([c[j] for c in arr[:-1]])))
    
if adding:
    gRaNd_tOtAl += sum(nums)
    nums = []
else:
    prod = 1
    for i in nums:
        prod *= i
    gRaNd_tOtAl += prod
    nums = []


print(gRaNd_tOtAl)