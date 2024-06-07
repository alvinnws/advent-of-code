import math

f = open("inputs/6.txt")
times = f.readline().split(":")[1].strip().split(" ")
distances = f.readline().split(":")[1].strip().split(" ")
while '' in times or '' in distances:
    if '' in times:
        times.remove('')
    if '' in distances:
        distances.remove('')

def formula (t, d):
    t = float(t)
    d = float(d)
    lower = (t/2) - math.sqrt(((t*t)/4)-d)
    upper = (t/2) + math.sqrt(((t*t)/4)-d)
    return (lower, upper)

ways = 1
for i in range(len(times)):
    range = formula(times[i], distances[i])
    upper = int(range[1] - range[1] % 1)
    if range[1] % 1 == 0:
        upper = upper - 1
    lower = int(range[0] - range[0] % 1)
    ways *= (upper - lower)

print(ways)