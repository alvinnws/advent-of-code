import math

f = open("inputs/6.txt")
times = f.readline().split(":")[1].strip().replace(" ","")
distances = f.readline().split(":")[1].strip().replace(" ","")

def formula (t, d):
    t = float(t)
    d = float(d)
    lower = (t/2) - math.sqrt(((t*t)/4)-d)
    upper = (t/2) + math.sqrt(((t*t)/4)-d)
    return (lower, upper)

ways = 1
range = formula(times, distances)
upper = int(range[1] - range[1] % 1)
if range[1] % 1 == 0:
    upper = upper - 1
lower = int(range[0] - range[0] % 1)
ways *= (upper - lower)

print(ways)