f = open("inputs/4.txt")
total = 0
cards = {}
for line in f:
    cards[int(line[5:8].strip())] = 1
f = open("inputs/4.txt")
for line in f:
    cardnumber = int(line[5:8].strip())
    winning = line.split(": ")[1].strip().split(" |")[0].split(" ")
    elfs = line.split("| ")[1].strip().split(" ")
    visited = []
    matches = 0
    for card in elfs:
        if card == "" or card in visited:
            continue
        if card in winning:
            matches += 1
        visited.append(card)
    print(cardnumber, matches)
    for i in range(cardnumber + 1, cardnumber + matches + 1):
        cards[i] += cards[cardnumber]

for i in cards:
    total += cards[i]
print(total)
            