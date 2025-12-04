f = open('inputs/3.txt')

def cascade(ls, pos):
    if pos+1 < len(ls) and ls[pos] >= ls[pos+1]:
        cascade(ls, pos+1)
        ls[pos+1] = ls[pos]

count = 0

for line in f:
    bank = [int(i) for i in line.strip()]
    ls = bank[-12:]
    pos = len(bank)-13
    while pos >= 0:
        if bank[pos] >= ls[0]:
            cascade(ls, 0)
            ls[0] = bank[pos]
        pos -= 1
    count += int(''.join([str(i) for i in ls]))

print(count)