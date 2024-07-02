class machine():
    mods = {}
    q = []
    states = []
    pulses = [0,0]
    cycle = False
    tracked = {'dj': 0, 'rr':0,'pb':0,'nl':0}
    tracked2 = {'dc': 0, 'rv':0,'vp':0,'cq':0}

    def get_state(self):
        state = []
        for mod in self.mods:
            state.append(self.mods[mod].state())
        state = tuple(state)
        return state
    
    def update_state(self, state):
        self.states.append(state)
        return


    def button(self):
        self.q.append(('broadcaster', 0, ''))
        while self.q:
            curr = self.q.pop(0)
            self.pulses[curr[1]] += 1
            pulse = self.mods[curr[0]].press(curr[1], curr[2])
            if pulse != None:
                if pulse == 0 and curr[0] == 'nl':
                    self.cycle = True
                    break
                for out in self.mods[curr[0]].outputs:
                    self.q.append((out, pulse, curr[0]))
        state = self.get_state()
        if state in self.states:
            self.cycle = True
        else:
            self.states.append(state)


class flip():
    def __init__(self, outputs):
        self.last = 0
        self.outputs = outputs.copy()

    def press(self, pulse, x):
        # x is not needed
        if pulse:
            return None
        else:
            self.last = 0 if self.last else 1
            return self.last
        
    def state(self):
        return self.last

class con():
    def __init__(self, outputs):
        self.history = {}
        self.outputs = outputs.copy()

    def add_input(self, in_from):
        self.history[in_from] = 0

    def press(self, pulse, in_from):
        self.history[in_from] = pulse
        for x in self.history:
            if self.history[x] != 1:
                return 1
        return 0
    
    def state(self):
        his = []
        for x in self.history:
            his.append(self.history[x])
        return tuple(his)
        
class broadcaster():
    outputs = []

    def __init__(self, outputs):
        self.outputs = outputs.copy()
    
    def press(self, pulse, x):
        return pulse
    
    def state(self):
        return None

f = open("input.txt")

mac = machine()
for line in f:
    outputs = line.split('->')[1].strip().split(', ')
    name = line.split('->')[0].strip()[1:]
    if 'broadcaster' in line:
        mac.mods['broadcaster'] = broadcaster(line.split('->')[1].strip().split(', '))
        continue
    elif line[0] == '%':
        mac.mods[name] = flip(outputs)
    else:
        mac.mods[name] = con(outputs)
    
f.seek(0)
for line in f:
    outputs = line.split('->')[1].strip().split(', ')
    name = line.split('->')[0].strip()[1:]
    for mod in outputs:
        if mod not in mac.mods:
            mac.mods[mod] = flip([])
        if type(mac.mods[mod]) == type(con([])):
            mac.mods[mod].add_input(name)

i = 0
start = mac.get_state()
while not mac.cycle:
    i += 1
    mac.button()
print(i)
print(mac.pulses[0] * mac.pulses[1])