import time

def move(point, direction, times=1):
    return (point[0] + (times * direction[0]), point[1] + (times * direction[1]))


def initialize_claw_machines():
    claw_machines = [[]]
    lines = []
    with open('input.txt', 'r') as file:
        for line in file:
            lines.append(line.strip())
    index = 0
    for line in lines:
        if line.startswith("Button A"):
            claw_machines[index].append((int(line[line.find("X+")+2:line.find(",")]), int(line[line.find("Y+")+2:])))
        elif line.startswith("Button B"):
            claw_machines[index].append((int(line[line.find("X+")+2:line.find(",")]), int(line[line.find("Y+")+2:])))
        elif line.startswith("Prize"):
            claw_machines[index].append((int(line[line.find("X=")+2:line.find(",")]), int(line[line.find("Y=")+2:])))
        else:
            index += 1
            claw_machines.append([])
    return claw_machines



def token_cost(claw_machine):
    buttonA = claw_machine[0]
    buttonB = claw_machine[1]
    prize = claw_machine[2]
    tokens = 999
    location = (0, 0)
    maxA = 0
    maxB = 0
    while location[0] < prize[0] and location[1] < prize[1] and maxA < 100:
        location = move(location, buttonA)
        maxA += 1
    location = (0, 0)
    while location[0] < prize[0] and location[1] < prize[1] and maxB < 100:
        location = move(location, buttonB)
        maxB += 1
    location = (0, 0)
    combinations = []
    for a in range(maxA + 1):
        for b in range(maxB + 1):
            if prize == move(move(location, buttonA, a), buttonB, b):
                combinations.append((a, b))
    for combination in combinations:
        tokens = min(tokens, 3 * combination[0] + combination[1])
    if tokens == 999:
        return 0
    else:
        return tokens

        
            

def main():
    claw_machines = initialize_claw_machines()
    tokens = 0
    current_machine = 0
    for claw_machine in claw_machines:
        print("Beginning machine:",current_machine)
        cost = token_cost(claw_machine)
        tokens += cost
        current_machine += 1
    print(tokens)

start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")
