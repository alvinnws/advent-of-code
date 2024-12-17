f = open("inputs/17.txt")

ls = []
for i in range(3):
    ls.append(int(f.readline().split(":")[1].strip()))

f.readline()

program = [int(i) for i in f.readline().split(": ")[1].strip().split(",")]

ints_ptr = 0

output = ""

while ints_ptr < len(program):
    print(output)
    ints = program[ints_ptr]
    combo = program[ints_ptr+1]
    
    ints_ptr += 2
    # adv A = A//2^combo
    if ints == 0:
        if combo > 3 and combo < 7:
            combo = ls[combo-4]
        elif combo == 7:
            print("WAT")
        
        ls[0] = ls[0] // (2**combo)

    # bxl B = XOR B
    elif ints == 1:
        ls[1] = ls[1] ^ combo
    
    # bst
    elif ints == 2:
        if combo > 3 and combo < 7:
            combo = ls[combo-4]
        elif combo == 7:
            print("WAT")
        
        ls[1] = combo % 8
        
    # jnz
    elif ints == 3:
        if ls[0] != 0:
            ints_ptr = combo
            
        
    # bxc
    elif ints == 4:
        ls[1] = ls[1] ^ ls[2]

    # out
    elif ints == 5:
        if combo > 3 and combo < 7:
            combo = ls[combo-4]
        elif combo == 7:
            print("WAT")
        output += str(combo % 8) + ","
        
    # bdv
    elif ints == 6:
        if combo > 3 and combo < 7:
            combo = ls[combo-4]
        elif combo == 7:
            print("WAT")
        ls[1] = ls[0] // (2**combo)
        
    # cdv
    elif ints == 7:
        if combo > 3 and combo < 7:
            combo = ls[combo-4]
        elif combo == 7:
            print("WAT")
        ls[2] = ls[0] // (2**combo)

output = output[:-1]        
print(output)