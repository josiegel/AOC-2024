input = ''
muls = []
sum = 0
doing = True

with open('input.txt', 'r') as file:
    input = file.read()

# First create muls, a list of all groups that are potentially being multiplied
# new variable doing tracks whether we should currently look for muls or not
for i in range(len(input)):
    if input[i:i+4] == 'do()': doing = True
    if input[i:i+7] == "don't()": doing = False
    if doing and input[i:i+4] == 'mul(':
        for j in range(i+4, len(input)):
            if input[j] == ')':
                muls.append(input[i+4:j])
                break
            
# For each potential mul, try to multiply it. If it works, add it to the sum
for i in range(len(muls)):
    muls[i] = muls[i].split(',')
    try:
        sum += (int(muls[i][0]) * int(muls[i][1]))
    except:
        pass

print(sum)                




        
