f = open("inputs/14.txt")

WIDTH = 101
HEIGHT = 103
SECONDS = 100

total = 0

class robot():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def next(self):
        x = (self.pos[0] + self.vel[0] * SECONDS) % WIDTH
        y = (self.pos[1] + self.vel[1] * SECONDS) % HEIGHT
        self.pos = (x,y)

    def quadrant(self):
        if self.pos[0] < WIDTH//2:
            if self.pos[1] < HEIGHT//2:
                return 1
            elif self.pos[1] > HEIGHT//2:
                return 3
        elif self.pos[0] > WIDTH//2:
            if self.pos[1] < HEIGHT//2:
                return 2
            elif self.pos[1] > HEIGHT//2:
                return 4
        return 0
            

quads = [0,0,0,0,0]

for line in f:
    x = int(line.split("=")[1].split(",")[0])
    y = int(line.split(",")[1].split(" ")[0])
    v1 = int(line.split("=")[-1].split(",")[0])
    v2 = int(line.strip().split(",")[-1])
    pos = (x, y)
    vel = (v1,v2)
    rob = robot(pos, vel)
    rob.next()
    quads[rob.quadrant()] += 1

total = 1
for i in range(1,5):
    total *= quads[i]

print(total)