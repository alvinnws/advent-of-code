f = open('inputs/4.txt')

def get_rolls(arr, pos):
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0: continue
            if pos[0] + i < 0 or pos[0] + i >= len(arr) or pos[1] + j < 0 or pos[1] + j >= len(arr[0]): continue
            if arr[pos[0]+i][pos[1]+j] == '@': count += 1
    return count

arr = [[c for c in line.strip()] for line in f]

count = 0

removal = True
while removal:
    removal = False
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '@' and get_rolls(arr, (i,j)) < 4:
                removal = True
                arr[i][j] = '.'
                count += 1

print(count)
        
