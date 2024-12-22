f = open("inputs/22.txt")

total = 0
dicts = {}

for line in f:
    secret = int(line.strip())
    history = [secret % 10]
    changes = []
    seen = set()
    for i in range(2000):
        secret = ((secret *  64  ) ^ secret) % 16777216
        secret = ((secret // 32  ) ^ secret) % 16777216
        secret = ((secret *  2048) ^ secret) % 16777216
        changes.append((secret % 10) - history[-1])
        history.append(secret % 10)
        if i > 2:
            pattern = tuple(changes[-4:])
            if pattern in seen: continue
            seen.add(pattern)
            if pattern in dicts:
                dicts[pattern] += history[-1]
            else:
                dicts[pattern] = history[-1]

curmax = 0
for i in dicts:
    curmax = max(dicts[i], curmax)

print(curmax)