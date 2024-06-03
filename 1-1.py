total = 0
with open("./1-1input.txt") as f:
    for line in f:
        front = 0
        ffound = False
        back = len(line) - 1
        bfound = False
        while not (ffound and bfound):
            if not ffound:
                if line[front] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    ffound = True
                else:
                    front += 1
            if not bfound:
                if line[back] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    bfound = True
                else:
                    back -= 1
        total += int(line[front] + line[back]) 
print(total)
