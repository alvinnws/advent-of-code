class Hailstone():
    def __init__(self, input):
        self.pos = list(map(int, input.split(' @ ')[0].split(', ')))
        self.velocity = list(map(int, input.split(' @ ')[1].split(', ')))
    
    def __str__(self):
        s = str(self.pos[0])
        for i in self.pos[1:]:
            s += ', ' + str(i)
        s += ' @ ' + str(self.velocity[0])
        for i in self.velocity[1:]:
            s += ', ' + str(i)
        return s

    def collides_within(self, other, range):
        n = other.velocity[1] * (self.pos[0] - other.pos[0]) - other.velocity[0] * (self.pos[1] - other.pos[1])
        d = self.velocity[1]*other.velocity[0] - self.velocity[0] * other.velocity[1]
        if d == 0: return False
        a = n / d
        x = self.pos[0] + a * self.velocity[0]
        y = self.pos[1] + a * self.velocity[1]
        b = (x - other.pos[0]) / other.velocity[0]
        if a < 0 or b < 0: return False
        if range[0] <= x <= range[1] and range[0] <= y <= range[1]:
            return True
        return False

RANGE = (200000000000000, 400000000000000)

f = open('input.txt')

hailstones = []
for line in f:
    hailstones.append(Hailstone(line.strip()))

collisions = 0
for i in range(len(hailstones)):
    for j in range(i+1, len(hailstones)):
        #print(hailstones[i])
        #print(hailstones[j])
        #print(hailstones[i].collides_within(hailstones[j], RANGE))
        #print('')
        if hailstones[i].collides_within(hailstones[j], RANGE):
            collisions += 1

print(collisions)