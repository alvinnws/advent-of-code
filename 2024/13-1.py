f = open("inputs/13.txt")

total = 0

state = 0
a, b, x, y = None, None, None, None
for line in f:
    if state == 1:
        state = 0
        curr = 500
        for i in range(101):
            for j in range(101):
                if i*a[0]+j*b[0]==x and i*a[1]+j*b[1]==y:
                    curr = min(curr, 3*i+j)
        
        if curr != 500: total += curr
        continue
    if line[7] == "A":
        a = (int(line.split("+")[1].split(",")[0]), int(line.strip().split("+")[-1]))
    elif line[7] == "B":
        b = (int(line.split("+")[1].split(",")[0]), int(line.strip().split("+")[-1]))
    else:
        state = 1
        x = int(line.split("=")[1].split(",")[0])
        y = int(line.strip().split("=")[-1])
        
print(total)