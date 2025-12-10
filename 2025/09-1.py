class RedTile():
    def __init__(self, str_inp):
        self.x, self.y = list(map(int, str_inp.strip().split(',')))

    def area(self, other):
        return (abs(self.x-other.x)+1)*(abs(self.y-other.y)+1)
    
f = open('inputs/9.txt')

tiles = []
for line in f:
    tiles.append(RedTile(line))

area = 0

for i in range(len(tiles)):
    for j in range(i+1, len(tiles)):
        area = max(area, tiles[i].area(tiles[j]))

print(area)