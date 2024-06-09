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
starts = []
for line in f:
    if line[2] == 'A':
        starts.append(line[0:3])
    curr = line.split(" = ")[0]
    left = line.split("(")[1].split(", ")[0]
    right = line.split(", ")[1].split(")")[0]
    nodes[curr] = node(left, right)

lengths = []

for i in starts:
    count = 0
    curr = i
    curr_instr = 0
    visited = []
    entered_cycle = False
    cycle_start = None
    exit_cycle = False
    cycle_length = 0

    while not exit_cycle:
        instr = instructions[curr_instr]
        if (curr, curr_instr) not in visited:
            visited.append((curr, curr_instr))
        if instr == 'L':
            curr = nodes[curr].left
        else:
            curr = nodes[curr].right
        count += 1

        if entered_cycle and (curr, curr_instr) == cycle_start:
            exit_cycle = True
            cycle_length = count - start_count
        if (curr, curr_instr) in visited and not entered_cycle:
            start_count = count
            entered_cycle = True
            cycle_start = (curr, curr_instr)

        curr_instr += 1
        if curr_instr == len(instructions):
            curr_instr = 0
    lengths.append(cycle_length)

divisors = {}
for i in lengths:
    divisor = 2
    curr = i
    while divisor < i/2:
        if curr/divisor % 1 == 0:
            curr = curr/divisor
            divisors[divisor] = True
        else:
            divisor += 1
    divisors[int(curr)] = True

count = 1
for i in divisors:
    count *= i

print(count)