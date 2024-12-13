import time
import numpy as np

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

def calibrate_claw_machines(claw_machines):
    for machine in claw_machines:
        machine[2] = (machine[2][0]+10000000000000, machine[2][1]+10000000000000)
    return claw_machines

def token_cost(claw_machine):
    buttonA = claw_machine[0]
    buttonB = claw_machine[1]
    prize = claw_machine[2]
    left = np.array([[buttonA[0], buttonB[0]],[buttonA[1], buttonB[1]]])
    right = np.array([prize[0], prize[1]])
    solution = np.linalg.solve(left, right)
    combination = list(map(round, solution))
    if combination[0] * buttonA[0] + combination[1] * buttonB[0] == prize[0] and combination[0] * buttonA[1] + combination[1] * buttonB[1] == prize[1]:
        return 3 * solution[0] + solution[1]
    else:
        return 0

def main():
    claw_machines = initialize_claw_machines()
    claw_machines = calibrate_claw_machines(claw_machines)
    tokens = 0
    for claw_machine in claw_machines:
        cost = token_cost(claw_machine)
        tokens += cost
    print(tokens)

start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")
