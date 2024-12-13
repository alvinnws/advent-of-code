from decimal import *

getcontext().prec = 30

f = open("inputs/13.txt")

total = 0

state = 0
a, b, x, y = None, None, None, None
for line in f:
    if state == 1:
        state = 0
        
        if (y*a[0]-(a[1]*x)) % (b[1]*a[0]-(a[1]*b[0])) == 0:
            bn = (y*a[0]-(a[1]*x))/(b[1]*a[0]-(a[1]*b[0]))
            if (x-b[0]*bn) % a[0] == 0:
                an = (x-b[0]*bn)/a[0]
                total += 3*an
                total += bn

        continue
    if line[7] == "A":
        a = (Decimal(line.split("+")[1].split(",")[0]), Decimal(line.strip().split("+")[-1]))
    elif line[7] == "B":
        b = (Decimal(line.split("+")[1].split(",")[0]), Decimal(line.strip().split("+")[-1]))
    else:
        state = 1
        x = Decimal(line.split("=")[1].split(",")[0])+10000000000000
        y = Decimal(line.strip().split("=")[-1])+10000000000000
        
print(int(total))