def findnum(num, schem, y, x, digits, explored):
    if schem[y][x] in digits and explored[y][x] == False:
        explored[y][x] = True
        num = schem[y][x]
        if x != 0:
            num = findnum('', schem, y, x-1, digits, explored) + num
        if x != len(schem[y]) - 1:
            num = num + findnum('', schem, y, x+1, digits, explored)
    return num

def main():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    f = open("inputs/3.txt")
    schematics = []
    explored = []
    for l in f:
        line = []
        exline = []
        for c in l:
            if c == '\n':
                continue
            line.append(c)
            exline.append(False)
        schematics.append(line)
        explored.append(exline)

    total = 0
    for y in range(len(schematics)):
        for x in range(len(schematics)):
            if schematics[y][x] == '.' or schematics[y][x] in digits:
                continue
            for adjy in range(-1,2):
                for adjx in range(-1,2):
                    if adjy == 0 and adjx == 0:
                        continue
                    if schematics[y+adjy][x+adjx] in digits and explored[y+adjy][x+adjx] == False:
                        number = findnum('', schematics, y+adjy, x+adjx, digits, explored)
                        if number == '':
                            continue
                        total += int(number)
    print(total)

main()
            


