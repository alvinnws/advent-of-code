class Hailstone():
    def __init__(self, input):
        self.pos = list(map(int, input.split(' @ ')[0].split(', ')))
        self.velocity = list(map(int, input.split(' @ ')[1].split(', ')))
    
def cross_prod(v1, v2):
    x = v1[1]*v2[2] - v1[2]*v2[1]
    y = v1[2]*v2[0] - v1[0]*v2[2]
    z = v1[0]*v2[1] - v1[1]*v2[0]
    return (x,y,z)

def dot_prod(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

f = open('input.txt')

hailstones = []
for line in f:
    hailstones.append(Hailstone(line.strip()))

def getter(hs0, hs1, hs2):
    """
    Solution taken from u/DaveBaum on reddit. I found this the most elegant solution.
    The explanation here is my own.
    
    Pick any 3 hailstones: hs0, hs1, hs2.
    Choose one to be at origin, then offset the other two hailstone's position and velocity vectors
    pos1 = hs1.pos - hs0.pos
    pos2 = hs2.pos - hs0.pos
    vel1 = hs1.vel - hs0.vel
    vel2 = hs2.vel - hs0.vel

    The position of hs1 relative to hs0 at time t1 is thus
    p1 = pos1 + t1 * vel1
    
    Similarly for hs2 relative to hs0
    p2 = pos2 + t2 * vel2

    The direction vector from hs0 to hs1 at t1 must be the same as
    the direction vector from hs0 to hs2 at t2, since the rock must hit all 3.
    Therefore, p1 is collinear with p2.
    Cross product of collinear vectors is 0.
    a x b = |a||b|sin(0) = 0
    p1 x p2 = 0

    (p1 + v1*t1) x (p2 + v2*t2) = 0
    p1 x p2 + t1*(v1 x p2) + t2*(p1 x v2) + t1*t2*(v1 x v2) = 0 -- (1)

    From here, we need to single out t1 and t2 to solve individually.
    The cross product of 2 vectors gives a vector perpendicular to the original 2,
    while the dot product of 2 perpendicular vectors is 0
    a (dot) b = |a||b|cos(90) = 0

    As a result, (a x b) (dot) b = 0
    
    Therefore taking (1) dot v2 or v1 can yield y1 or t2.
    (1) (dot) v2: (p1 x p2) (dot) v2 + t1 * (v1 x p2) (dot) v2 = 0
    t1 = - ((p1 x p2) (dot) v2) / ((v1 x p2) (dot) v2)

    (1) (dot) v1: (p1 x p2) (dot) v1 + t2 * (p1 x v2) (dot) v1 = 0
    t2 = - ((p1 x p2) (dot) v1) / ((p1 x v2) (dot) v1)

    Then, you can find the collision point of hs1 with the rock in absolute coordinates
    col1 = hs1.pos + hs1.vel * t1
    col2 = hs2.pos + hs2.vel * t2

    The velocity of the rock is thus the difference between col2 and col1, divided by the time difference
    rock.vel = (col2 - col1) / (t2 - t1)
    For the rock to reach the first collision point,
    col1 = rock.pos + rock.vel * t1
    => rock.pos = col1 - rock.vel * t1
    """
    pos1 = [0,0,0]
    pos1[0] = hs1.pos[0] - hs0.pos[0]
    pos1[1] = hs1.pos[1] - hs0.pos[1]
    pos1[2] = hs1.pos[2] - hs0.pos[2]

    pos2 = [0,0,0]
    pos2[0] = hs2.pos[0] - hs0.pos[0]
    pos2[1] = hs2.pos[1] - hs0.pos[1]
    pos2[2] = hs2.pos[2] - hs0.pos[2]

    vel1 = [0,0,0]
    vel1[0] = hs1.velocity[0] - hs0.velocity[0]
    vel1[1] = hs1.velocity[1] - hs0.velocity[1]
    vel1[2] = hs1.velocity[2] - hs0.velocity[2]

    vel2 = [0,0,0]
    vel2[0] = hs2.velocity[0] - hs0.velocity[0]
    vel2[1] = hs2.velocity[1] - hs0.velocity[1]
    vel2[2] = hs2.velocity[2] - hs0.velocity[2]

    
    t1 = 0-((dot_prod(cross_prod(pos1, pos2), vel2)) / dot_prod(cross_prod(vel1, pos2), vel2))
    t2 = 0-((dot_prod(cross_prod(pos1, pos2), vel1)) / dot_prod(cross_prod(pos1, vel2), vel1))

    col1 = [0,0,0]
    col1[0] = hs1.pos[0] + t1 * hs1.velocity[0]
    col1[1] = hs1.pos[1] + t1 * hs1.velocity[1]
    col1[2] = hs1.pos[2] + t1 * hs1.velocity[2]

    col2 = [0,0,0]
    col2[0] = hs2.pos[0] + t2 * hs2.velocity[0]
    col2[1] = hs2.pos[1] + t2 * hs2.velocity[1]
    col2[2] = hs2.pos[2] + t2 * hs2.velocity[2]

    x = col1[0] - ((col2[0] - col1[0]) / (t2 - t1)) * t1
    y = col1[1] - ((col2[1] - col1[1]) / (t2 - t1)) * t1
    z = col1[2] - ((col2[2] - col1[2]) / (t2 - t1)) * t1
    return int(x+y+z)

# Any combination should yield the same exact starting position, so these are just to test
print(getter(hailstones[0], hailstones[1], hailstones[2]))
print(getter(hailstones[10], hailstones[50], hailstones[75]))
print(getter(hailstones[123], hailstones[0], hailstones[234]))
