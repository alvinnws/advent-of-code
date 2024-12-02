f = open('inputs/2.txt')

total = 0

for line in f:
    line = line.strip()
    remove = None
    while remove == None or remove < len(line.split()):
        levels = []
        for i in range(len(line.split())):
            if i == remove: continue
            levels.append(int(line.split()[i]))
        mode = 1 if levels[1] > levels[0] else 0
        flag = True
        for i in range(len(levels)-1):
            test_mode = 1 if levels[i+1] > levels[i] else 0
            if test_mode != mode: 
                flag = False
                break
            if levels[i] == levels[i+1]:
                flag = False
                break
            if abs(int(levels[i+1]) - int(levels[i])) > 3:
                flag = False
                break
        if remove == None:
            remove = 0
        else:
            remove += 1
        if flag == True:
            total += 1
            break

print(total)
