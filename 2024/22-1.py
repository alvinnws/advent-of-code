f = open("inputs/22.txt")

total = 0

for line in f:
    secret = int(line.strip())
    for i in range(2000):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret//32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
    total += secret

print(total)