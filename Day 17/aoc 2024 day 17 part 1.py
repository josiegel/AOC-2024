import time

def initialize_computer(input):
    computer = []
    with open(input, 'r') as file:
        computer.append(int(file.readline().strip()[12:]))
        computer.append(int(file.readline().strip()[12:]))
        computer.append(int(file.readline().strip()[12:]))
        file.readline()      
        computer.append(tuple(map(int, file.readline().strip()[9:].split(","))))
        computer.append(0)
        computer.append(())
        computer = tuple(computer)
    return computer

# computer[0] is Register A
# computer[1] is Register B
# computer[2] is Register C
# computer[3] is the Program list
# computer[4] is the instruction pointer
# computer[5] is the output list

def combo(operand, a, b, c):
    match operand:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c

def run_opcode(computer):
    a = computer[0]
    b = computer[1]
    c = computer[2]
    program = computer[3]
    pointer = computer[4]
    outputs = computer[5]
    opcode = program[pointer]
    operand = program[pointer+1]
    match opcode:
        case 0: #adv
            a = a // (2 ** combo(operand, a, b, c))
        case 1: #bxl
            b = b ^ operand
        case 2: #bst
            b = (combo(operand, a, b, c)) % 8
        case 3: #jnz
            if a == 0: pointer += 2
            else: pointer = operand
        case 4: #bxc
            b = b ^ c
        case 5: #out
            outputs = list(outputs)
            outputs.append((combo(operand, a, b, c)) % 8)
            outputs = tuple(outputs)
        case 6: #bdv
            b = a // (2 ** combo(operand, a, b, c))
        case 7: #cdv
            c = a // (2 ** combo(operand, a, b, c))
    if opcode != 3:
        pointer += 2
    return (a,b,c,program,pointer,outputs)
        
def display_output(computer):
    outputs = computer[5]
    ans = ""
    for num in outputs:
        ans = ans + str(num) + ","
    print(ans[:-1])    
    

def main():
    computer = initialize_computer("example.txt")
    while computer[4] < len(computer[3]):
        computer = run_opcode(computer)
    print(computer)
    display_output(computer)
        

start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")
