from typing import List

class Block():
    def __init__(self, pos: str) -> None:
        xyz1 = pos.split('~')[0].split(',')
        xyz2 = pos.split('~')[1].split(',')
        self.x = (int(xyz1[0]), int(xyz2[0]))
        self.y = (int(xyz1[1]), int(xyz2[1]))
        self.z = (int(xyz1[2]), int(xyz2[2]))
        self.below = []
        self.above = []
    
    def __str__(self) -> str:
        return str(((self.x[0], self.y[0], self.z[0]),(self.x[1], self.y[1], self.z[1])))
    
    def order(self) -> int:
        return min(self.z[0], self.z[1])
    
    def add_below(self, n: int) -> None:
        if n not in self.below: self.below.append(n)
        return
    
    def num_below(self) -> int:
        return len(self.below)
    
    def add_above(self, n: int) -> None:
        if n not in self.above: self.above.append(n)
        return
    
    def num_above(self) -> int:
        return len(self.above)
    
    def total_above(self, blocks: List[object], counted: List[int]) -> int:
        total = 0
        for block in self.above:
            counted[block] = 1
            l = blocks[block].total_above(blocks, counted)
        return sum(counted)

def check_sheet(stack: List[List[List[int]]], block, z) -> bool:
    for y in range(block.y[0], block.y[1]+1):
        for x in range(block.x[0], block.x[1]+1):
            if stack[z-1][y][x] != -1:
                return False
    return True

f = open("input.txt")

blocks = []
disintegratable = []
counted = []
x_min, x_max, y_min, y_max, z_min, z_max = 0,0,0,0,0,0
for line in f:
    blocks.append(Block(line.strip()))
    disintegratable.append(-1)
    counted.append(0)
    x_min = min(x_min, blocks[-1].x[0], blocks[-1].x[1])
    y_min = min(y_min, blocks[-1].y[0], blocks[-1].y[1])
    z_min = min(z_min, blocks[-1].z[0], blocks[-1].z[1])
    x_max = max(x_max, blocks[-1].x[0], blocks[-1].x[1])
    y_max = max(y_max, blocks[-1].y[0], blocks[-1].y[1])
    z_max = max(z_max, blocks[-1].z[0], blocks[-1].z[1])
x_width = x_max - x_min + 1
y_width = y_max - y_min + 1
z_width = z_max - z_min + 1

blocks.sort(key=lambda x: x.order())

stack = []
for i in range(z_width+1):
    sheet = []
    for j in range(y_width):
        line = []
        for z in range(x_width):
            if i == 0: line.append('-')
            else: line.append(-1)
        sheet.append(line)
    stack.append(sheet)

for i in range(len(blocks)):
    c = blocks[i]
    z = c.order()
    while check_sheet(stack, c, z):
        z-=1
    for y in range(c.y[0], c.y[1]+1):
        for x in range(c.x[0], c.x[1]+1):
            if stack[z-1][y][x] != -1:
                c.add_below(stack[z-1][y][x])
                if stack[z-1][y][x] != '-':
                    blocks[stack[z-1][y][x]].add_above(i)
            for ups in range(c.z[1] - c.z[0] + 1):
                stack[z+ups][y][x] = i

for i in range(len(blocks)):
    if blocks[i].num_below() == 1:
        if blocks[i].below[0] != '-':
            disintegratable[blocks[i].below[0]] = 0
    elif blocks[i].num_below() > 1:
        for j in blocks[i].below:
            if disintegratable[j] != 0:
                disintegratable[j] = 1
    if blocks[i].num_above() == 0:
        disintegratable[i] = 1

def rec_collapse(blocks, i, collapsed):
    if collapsed == 1: return 0
    for child in blocks[i].below:
        if collapsed[child] == 0:
            return 0
    collapsed[i] = 1
    total = 1
    for parent in blocks[i].above:
        total += rec_collapse(blocks, parent, collapsed)
    return total

count = 0
for i in range(len(blocks)):
    collapsed = counted.copy()
    if disintegratable[i] != 1:
        collapsed[i] = 1
        count += 0
        for parent in blocks[i].above:
            count += rec_collapse(blocks, parent, collapsed)
print(count)
