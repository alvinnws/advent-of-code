total = 0
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
threelong = ['one', 'two', 'six']
fourlong = ['four', 'five', 'nine']
fivelong = ['three', 'seven', 'eight']
wordtodigit = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
with open("./1-1input.txt") as f:
    for line in f:
        front = 0
        ffound = False
        fword = None
        back = len(line) - 1
        bfound = False
        bword = None
        while not (ffound and bfound):
            if not ffound:
                if line[front] in digits:
                    ffound = True
                elif front + 3 < len(line) - 1 and line[front:front+3] in threelong:
                    ffound = True
                    fword = 3
                elif front + 4 < len(line) - 1 and line[front:front+4] in fourlong:
                    ffound = True
                    fword = 4
                elif front + 5 < len(line) - 1 and line[front:front+5] in fivelong:
                    ffound = True
                    fword = 5
                else:
                    front += 1
            if not bfound:
                if line[back] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    bfound = True
                elif back - 2 > -1 and line[back - 2: back + 1] in threelong:
                    bfound = True
                    bword = 3
                elif back - 3 > -1 and line[back - 3: back + 1] in fourlong:
                    bfound = True
                    bword = 4
                elif back - 4 > -1 and line[back - 4: back + 1] in fivelong:
                    bfound = True
                    bword = 5
                else:
                    back -= 1
        if fword is None:
            front = line[front]
        else:
            front = wordtodigit[line[front:front+fword]]
        if bword is None:
            back = line[back]
        else:
            back = wordtodigit[line[back - bword + 1:back + 1]]
        total += int(front + back)
print(total)
