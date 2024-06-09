class node():
    def __init__(self, left, right):
        self.left = left
        self.right = right

f = open("input.txt")
first = f.readline().strip()
instructions = []
for c in first:
    instructions.append(c)
f.readline()

nodes = {}
for line in f:
    curr = line.split(" = ")[0]
    left = line.split("(")[1].split(", ")[0]
    right = line.split(", ")[1].split(")")[0]
    nodes[curr] = node(left, right)

count = 0
curr = 'AAA'
instrdupe = instructions.copy()
while curr != 'ZZZ':
    if len(instrdupe) == 0:
        instrdupe = instructions.copy()
    instr = instrdupe.pop(0)
    if instr == 'L':
        curr = nodes[curr].left
    else:
        curr = nodes[curr].right
    count += 1

print(count)
