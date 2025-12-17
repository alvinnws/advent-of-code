from copy import deepcopy

class Machine():
    def __init__(self, str_input):
        self.target = [c == '#' for c in str_input[1:str_input.find(']')]]
        self.buttons = [list(map(int,c[1:-1].split(','))) for c in str_input.split(' ')[1:-1]]
        self.state = [False]*len(self.target)
        self.presses = 0

    def valid(self):
        for i in range(len(self.target)):
            if self.target[i] != self.state[i]:
                return False
        return True
    
    def __str__(self):
        return ''.join(['Presses: ', str(self.presses), " | State: ", str(self.state), '\n'])

f = open('inputs/10.txt')

count = 0

for line in f:
    m = Machine(line.strip())
    q = [m]
    visited = set()
    while q:
        m = q.pop(0)
        if m.valid():
            count += m.presses
            break
        for button in m.buttons:
            if (tuple(m.state), tuple(button)) in visited: continue
            n = deepcopy(m)
            visited.add((tuple(n.state), tuple(button)))
            for butt in button:
                n.state[butt] = not n.state[butt]
            n.presses += 1
            q.append(n)
        q.sort(key=lambda x: x.presses  )


print(count)