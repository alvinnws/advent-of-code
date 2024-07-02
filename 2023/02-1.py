total = 0
balls_in_bag = {"red": 12, "green": 13,"blue": 14}
with open("./inputs/2.txt") as f:
    for line in f:
        game_num = line.split(":")[0].replace("Game ","")
        sets = line.strip().split(": ")[1].split("; ")
        valid = True
        for balls in sets:
            for ball in balls.split(", "):
                for colour in balls_in_bag:
                    if colour not in ball:
                        continue
                    if int(ball.replace(colour,"")) > balls_in_bag[colour]:
                        valid = False
        if valid:
            total += int(game_num)
print(total)