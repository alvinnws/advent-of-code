def search(devices, state, storage):
    current = state[0]
    fft = state[1] # Tuples are immutable
    dac = state[2]
    if state in storage: return storage[state] # Only immutable types can be used as keys in dictionary
    elif current == 'out':
        if fft and dac: return 1
        else: return 0
    else:
        count = 0
        if current == 'fft': fft = True
        if current == 'dac': dac = True
        for n in devices[current]:
            count += search(devices, (n, fft, dac), storage)
        storage[(current, fft, dac)] = count
        return storage[(current, fft, dac)]
        
f = open('inputs/11.txt')

devices = {}

for line in f:
    devices[line.split(':')[0]] = set([out for out in line.split(':')[1].strip().split(' ')])

print(search(devices, ('svr', False, False), {}))