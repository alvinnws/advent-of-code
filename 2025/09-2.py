import matplotlib.pyplot as plt

class XmasFloor():
    def __init__(self):
        self.red_tiles = []
        self.x_lines = {}
        self.y_lines = {}
    
    def gen_lines(self):
        for i in range(len(self.red_tiles)):
            a = self.red_tiles[i]
            b = self.red_tiles[i-1]
            if a.x == b.x:
                if a.x in self.y_lines:
                    self.y_lines[a.x].append(tuple(sorted([a.y, b.y])))
                else:
                    self.y_lines[a.x] = [tuple(sorted([a.y, b.y]))]
            else:
                if a.y in self.x_lines:
                    self.x_lines[a.y].append(tuple(sorted([a.x, b.x])))
                else:
                    self.x_lines[a.y] = [tuple(sorted([a.x, b.x]))]
    
    def on_line(self, pos):
        if pos[0] in self.y_lines:
            for lower, upper in self.y_lines[pos[0]]:
                if lower <= pos[1] <= upper: return True
        if pos[1] in self.x_lines:
            for lower, upper in self.x_lines[pos[1]]:
                if lower <= pos[0] <= upper: return True
        return False
    
    def in_shape(self, pos):
        inside = False
        line = False
        skip = []
        pos = list(pos)
        for x in sorted(self.y_lines.keys()):
            if pos[0] <= x <= 100000:
                for lower, upper in self.y_lines[x]:
                    if (lower, upper) in skip:
                        skip.remove((lower, upper))
                        continue
                    if lower < pos[1] < upper:
                        inside = not inside
                    elif lower == pos[1] or upper == pos[1]:
                        if line == True:
                            line = False
                            continue
                        inside = not inside
                        line = True
                        for other1, other2 in self.y_lines[x]:
                            if other2 == lower or other1 == upper:
                                skip.append((other1, other2))
        return inside
    
    def is_valid(self, i, j):
        a = self.red_tiles[i]
        b = self.red_tiles[j]
        for y in range(min(a.y, b.y), max(a.y, b.y)+1):
            if not (self.on_line((a.x, y)) or self.in_shape((a.x, y))):
                return False
            elif not (self.on_line((b.x, y)) or self.in_shape((b.x, y))):
                return False
        for x in range(min(a.x, b.x), max(a.x, b.x)+1):
            if not (self.on_line((x, a.y)) or self.in_shape((x, a.y))):
                return False
            elif not (self.on_line((x, b.y)) or self.in_shape((x, b.y))):
                return False
        return True
    
    def quick_valid(self, i, j):
        a = self.red_tiles[i]
        b = self.red_tiles[j]
        lowy, highy = min(a.y, b.y), max(a.y, b.y)
        lowx, highx = min(a.x, b.x), max(a.x, b.x)
        for x in self.y_lines:
            if lowx<x<highx:
                for lower, higher in self.y_lines[x]:
                    if lower<a.y<higher or lower<b.y<higher: return False
        for y in self.x_lines:
            if lowy<y<highy:
                for lower, higher in self.x_lines[y]:
                    if lower<a.x<higher or lower<b.x<higher: return False
        return True

class RedTile():
    def __init__(self, str_inp):
        self.x, self.y = list(map(int, str_inp.strip().split(',')))

    def area(self, other):
        return (abs(self.x-other.x)+1)*(abs(self.y-other.y)+1)

f = open('/Users/alvinng/Documents/Code/VSCode/advent-of-code/2025/inputs/9.txt')

xs = []
ys = []

floor = XmasFloor()
for line in f:
    floor.red_tiles.append(RedTile(line))
    xs.append(floor.red_tiles[-1].x)
    ys.append(floor.red_tiles[-1].y)

tiles = floor.red_tiles

floor.gen_lines()

areas = []

for i in range(len(tiles)):
    for j in range(i+1, len(tiles)):
        areas.append((i, j, tiles[i].area(tiles[j])))

areas.sort(key=lambda x: -x[2])

for n in range(0,len(areas),1):
    i, j, area = areas[n]
    if floor.quick_valid(i, j) and floor.is_valid(i, j):
        print(area)
        break