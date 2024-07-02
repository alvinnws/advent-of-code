class Hand:
    cards = []
    five = False
    four = False
    three = False
    two = False
    twotwo = False
    strength = 0
    bid = 0

    def __init__(self, cards, bid):
        ls = []
        translation = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 11,
            'T': 10
        }
        for c in cards:
            if c in ['9', '8', '7', '6', '5', '4', '3', '2']:
                ls.append(int(c))
            else:
                ls.append(translation[c])
        self.cards = ls
        self.bid = bid
        self.strength = self.strong(cards)


    def strong(self, cards):
        counts = {}
        for card in cards:
            if card not in counts:
                counts[card] = 1
            else:
                counts[card] += 1
        
        for card in counts:
            if counts[card] == 5:
                return 5
            if counts[card] == 4:
                return 4
            if counts[card] == 3:
                self.three = True
            if counts[card] == 2:
                if self.two == True:
                    self.twotwo = True
                else:
                    self.two = True
        
        if self.three == True:
            if self.two == True:
                return 3
            else:
                return 2
        elif self.twotwo == True:
            return 1
        elif self.two == True:
            return 0
        else:
            return -1
        
def sorthand(hands):
    for i in range(len(hands)):
        for j in range(len(hands) - i - 1):
            if hands[j].strength > hands[j+1].strength:
                tmp = hands[j]
                hands[j] = hands[j+1]
                hands[j+1] = tmp
            elif hands[j].strength == hands[j+1].strength:
                for k in range(5):
                    if hands[j].cards[k] > hands[j+1].cards[k]:
                        tmp = hands[j]
                        hands[j] = hands[j+1]
                        hands[j+1] = tmp
                        break
                    elif hands[j].cards[k] < hands[j+1].cards[k]:
                        break
            else:
                continue

f = open("7.txt")
hands = []
for line in f:
    cards = line.split(" ")[0]
    bid = line.split(" ")[1].strip()
    hands.append(Hand(cards, bid))

sorthand(hands)

sum = 0
for i in range(len(hands)):
    sum += int(hands[i].bid) * (i + 1)
print(sum)
