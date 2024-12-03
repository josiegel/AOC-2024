input = ''
muls = []
sum = 0


with open('input.txt', 'r') as file:
    input = file.read()

# First create muls, a list of all groups that are potentially being multiplied
for i in range(len(input)):
    if input[i:i+4] == 'mul(':
        for j in range(i+4, len(input)):
            if input[j] == ')':
                muls.append(input[i+4:j])
                break
# For each possible mul, try to multiply it. If it works, add it to the sum
for i in range(len(muls)):
    muls[i] = muls[i].split(',')
    try:
        sum += (int(muls[i][0]) * int(muls[i][1]))
    except:
        pass

print(sum)                




        
