total = 0
with open("./inputs/2.txt") as f:
    for line in f:
        game_num = line.split(":")[0].replace("Game ","")
        sets = line.strip().split(": ")[1].split("; ")
        valid = True
        cur_min = {"red": 0, "green": 0,"blue": 0}
        for balls in sets:
            for ball in balls.split(", "):
                for colour in cur_min:
                    if colour not in ball:
                        continue
                    cur_min[colour] = max(cur_min[colour], int(ball.replace(colour, "")))
        total += cur_min["red"]*cur_min["blue"]*cur_min["green"]
print(total)