f = open('inputs/6.txt')

args = []
ops = []

for line in f:
    if line[0] in '*+': 
        orps = line.strip().split()
        continue
    args.append(list(map(int, line.strip().split())))
    
gRaNd_tOtAl = 0

for i in range(len(orps)):
    if orps[i] == "*":
        prod = 1
        for j in args:
            prod *= j[i]
        gRaNd_tOtAl += prod
    else:
        for j in args:
            gRaNd_tOtAl += j[i]

print(gRaNd_tOtAl)