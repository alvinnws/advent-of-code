f = open('inputs/9.txt')

total = 0

line = f.readline()
line = line.strip()

files = []
dots = []
file = True
count = 0
no_fit = set()
for i in line:
    if file:
        for i in range(int(i)):
            files.append(count)
        count += 1
        file = False
    else:
        for i in range(int(i)):
            files.append('.')
        file = True

curr = count - 1
while curr > 0:
    k = len(files) -1
    while files[k] != curr:
        k -= 1
    l = k
    while files[l-1] == files[k]:
        l -= 1
    len_file = k - l + 1

    # FIND SPACE
    i, j, len_i = -1, -1, len_file - 1
    while len_i < len_file and j+1 < l:
        i = j + 1
        while files[i] != '.':
            i += 1
        j = i
        while files[j] == '.':
            j += 1
            if j >= len(files):
                break
        j -= 1
        len_i = j - i + 1
    if len_file <= len_i and j < l:
        for a in range(len_file):
            files[i+a] = files[k]
        for a in range(len_file):
            files[k-a] = '.'
    curr -= 1


for i in range(len(files)):
    if files[i] != '.':
        total += i * int(files[i])

print(total)

f.close()