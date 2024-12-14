f = open("inputs/14.txt")

WIDTH = 101
HEIGHT = 103
SECONDS = 1

total = 0

class robot():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def next(self):
        x = (self.pos[0] + self.vel[0] * SECONDS) % WIDTH
        y = (self.pos[1] + self.vel[1] * SECONDS) % HEIGHT
        self.pos = (x,y)
            
def egg(robots):
    ls = [["." for i in range(WIDTH)] for j in range(HEIGHT)]

    for rob in robots:
        ls[rob.pos[1]][rob.pos[0]] = "O"

    for line in ls:
        for c in line:
            print(c,end="")
        print()
    return

quads = [0,0,0,0,0]

robots = []
for line in f:
    x = int(line.split("=")[1].split(",")[0])
    y = int(line.split(",")[1].split(" ")[0])
    v1 = int(line.split("=")[-1].split(",")[0])
    v2 = int(line.strip().split(",")[-1])
    pos = (x, y)
    vel = (v1,v2)
    robots.append(robot(pos, vel))

count = 0
while count < 8178:
    for r in robots:
        r.next()
    count += 1

for r in robots:
    r.next()
count += 1
egg(robots)
print(count)