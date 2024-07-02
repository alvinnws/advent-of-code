def evalPart(part, rules, curr):
    if curr == 'A': return 'A'
    elif curr == 'R': return 'R'
    for con in rules[curr]:
        if con == 'A': return 'A'
        elif con == 'R': return 'R'
        if type(con) == type(''):
            return evalPart(part, rules, con)
        if con["comp"] == '<':
            if part[con["cat"]] < con["num"]:
                return evalPart(part, rules, con["res"])
        elif part[con["cat"]] > con["num"]:
                return evalPart(part, rules, con["res"])


f = open("input.txt")

rules  = {}

parts = []

finRules = False
for line in f:
    if line.strip() == '': finRules = True
    elif finRules:
        cats = line.strip().replace('{', '').replace('}','').split(',')
        newP = {}
        for cat in cats:
            newP[cat.split('=')[0]] = int(cat.split('=')[1])
        parts.append(newP)
    else:
        name = line.split('{')[0]
        cons = line.split('{')[1].strip().replace('}','').split(',')
        rls = []
        for con in cons:
            if con == 'A': 
                rls.append('A')
            elif con == 'R':
                rls.append('R')
            elif ':' not in con:
                rls.append(con)
            else:
                cat = con.split('<')[0].split('>')[0]
                comp = '<' if '<' in con else '>'
                num = int(con.split(comp)[1].split(':')[0])
                res = con.split(':')[1]
                rls.append({"cat": cat, "comp": comp, "num": num, "res":res})
        rules[name] = rls

tots = 0
for part in parts:
    if evalPart(part, rules, "in") == 'A':
        for x in part:
            tots += part[x]

print(tots)