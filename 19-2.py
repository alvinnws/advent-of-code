def evalPart(start, end, rules, curr, i, ls):
    if curr == 'A':
        ls.append((start, end, True))
        return
    if curr == 'R': return
    if rules[curr][i] == "A":
        ls.append((start, end, True))
        return
    elif rules[curr][i] == "R": return
    elif type(rules[curr][i]) == type(''):
        evalPart(start, end, rules, rules[curr][i], 0, ls)
    else:
        if rules[curr][i]["comp"] == '<':
            ss = start.copy()
            se = end.copy()
            se[rules[curr][i]["cat"]] = rules[curr][i]["num"] - 1
            ss2 = start.copy()
            se2 = end.copy()
            ss2[rules[curr][i]["cat"]] = rules[curr][i]["num"]
            #print(ss, se, rules[curr][i]["num"])
            #print(ss2, se2, rules[curr][i]["num"])
            evalPart(ss, se, rules, rules[curr][i]["res"], 0, ls)
            evalPart(ss2, se2, rules, curr, i + 1, ls)
        else:
            ss = start.copy()
            se = end.copy()
            ss[rules[curr][i]["cat"]] = rules[curr][i]["num"] + 1
            ss2 = start.copy()
            se2 = end.copy()
            se2[rules[curr][i]["cat"]] = rules[curr][i]["num"]
            #print(ss, se, rules[curr][i]["num"])
            #print(ss2, se2, rules[curr][i]["num"])
            evalPart(ss, se, rules, rules[curr][i]["res"], 0, ls)
            evalPart(ss2, se2, rules, curr, i + 1, ls)




f = open("input.txt")

rules  = {}

parts = []

finRules = False
for line in f:
    if line.strip() == '': break
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
ls = []
evalPart({'x':1, 'm':1, 'a':1, 's': 1}, {'x':4000, 'm':4000, 'a':4000, 's': 4000}, rules, 'in', 0, ls)
for i in range(len(ls)):
    tots += (ls[i][1]['x'] - ls[i][0]['x']+1) * (ls[i][1]['m'] - ls[i][0]['m']+1) * (ls[i][1]['a'] - ls[i][0]['a']+1) * (ls[i][1]['s'] - ls[i][0]['s']+1)

print(tots)