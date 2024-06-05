f = open("inputs/4.txt")
total = 0
for line in f:
    cardpoints = 0
    winning = line.split(": ")[1].strip().split(" |")[0].split(" ")
    elfs = line.split("| ")[1].strip().split(" ")
    visited = []
    for card in elfs:
        if card == "":
            continue
        if card in winning:
            if cardpoints == 0:
                cardpoints = 1
            else:
                cardpoints *= 2
        visited.append(card)
    total += cardpoints

print(total)
            