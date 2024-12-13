import time

def move(point, direction):
    return (point[0] + direction[0], point[1] + direction[1])


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
    tokenZ = get_token_cost(claw_machine, (0,0), 0, 0, [])
    if tokenZ >= 999:
        return 0
    else:
        return tokenZ

def get_token_cost(claw_machine, location = (0, 0), Apresses = 0, Bpresses = 0, already_checked = []):
    already_checked.append((Apresses, Bpresses))
    buttonA = claw_machine[0]
    buttonB = claw_machine[1]
    prize = claw_machine[2]
    if location[0] == prize[0] and location[1] == prize[1]:
        return 0
    elif location[0] > prize[0] or location[1] > prize[1]:
        return 999
    elif Apresses == 100 and Bpresses == 100:
        return 999
    elif (Apresses + 1, Bpresses) in already_checked and (Apresses, Bpresses + 1) in already_checked:
        print("Both possibilities already checked!")
        return 999
    elif (Apresses == 100 and (Apresses, Bpresses + 1) not in already_checked) or (Apresses + 1, Bpresses) in already_checked:
        return get_token_cost(claw_machine, move(location, buttonB), Apresses, Bpresses + 1, already_checked) + 1
    elif (Bpresses == 100 and (Apresses + 1, Bpresses) not in already_checked) or (Apresses, Bpresses + 1) in already_checked:
        return get_token_cost(claw_machine, move(location, buttonB), Apresses + 1, Bpresses, already_checked) + 3
    else:
        return min(get_token_cost(claw_machine, move(location, buttonA), Apresses + 1, Bpresses, already_checked) + 3, get_token_cost(claw_machine, move(location, buttonB), Apresses, Bpresses+1, already_checked) + 1)

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
