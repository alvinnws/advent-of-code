def solver(state, memo, memo2):
    if any(i < 0 for i in state): return float('inf')
    if all(i == 0 for i in state): return 0
    if tuple(state) in memo2: return memo2[tuple(state)]
    odds = [1 if i % 2 == 1 else 0 for i in state]
    count = float('inf')
    if tuple(odds) not in memo: return float('inf')
    for minuses, presses in memo[tuple(odds)]:
        new_s = [(state[i]-minuses[i])//2 for i in range(len(state))]
        count = min(count, 2*solver(new_s, memo, memo2) + presses)
    memo2[tuple(state)] = count
    return memo2[tuple(state)]

def get_button_combinations(state, buttons, i, presses, memo):
    if i == len(buttons):
        odds = [1 if c % 2 == 1 else 0 for c in state]
        if tuple(odds) in memo: memo[tuple(odds)].append((tuple(state), presses))
        else: memo[tuple(odds)] = [(tuple(state), presses)]
        return
    new_s = state[::]
    get_button_combinations(new_s, buttons, i+1, presses, memo)
    for button in buttons[i]: new_s[button] += 1
    get_button_combinations(new_s, buttons, i+1, presses+1, memo)
    return

count = 0
f = open('inputs/10.txt')
for line in f:
    state = list(map(int, line.split('{')[1].split('}')[0].split(',')))
    buttons = [list(map(int, c[1:-1].split(','))) for c in line.split(' ')[1:-1]]
    memo = {}
    get_button_combinations([0 for _ in range(len(state))], buttons, 0, 0, memo)
    res = solver(state, memo, {})
    if res > 10000: print(line)
    count += res
print(count)
f.close()