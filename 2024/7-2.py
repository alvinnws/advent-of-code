f = open('inputs/7.txt')

def solver(target, vals, ops = []):
    if len(ops) == len(vals)-1:
        s = vals[0]
        for i in range(len(ops)):
            if ops[i] == '||':
                s = int(str(s) + str(vals[i+1]))
            else:
                s = s + vals[i+1] if ops[i] == '+' else s * vals[i+1]
        if s == target:
            return True
        else:
            return False
    return solver(target, vals, ops + ['+']) or solver(target, vals, ops + ['*']) or solver(target, vals, ops+['||'])

total = 0
for line in f:
    line = line.strip()
    target = int(line.split(':')[0])
    vals = line.split(':')[1].strip().split()
    for i in range(len(vals)):
        vals[i] = int(vals[i])
    if solver(target, vals):
        total += target

print(total)