import time
NORTH = (-1,0)
SOUTH = (1,0)
EAST = (0,1)
WEST = (0,-1)

def initialize_warehouse():
    inputs = [[]]
    with open('input.txt', 'r') as file:
        for line in file:
            if line[0] == '#':
                inputs[0].append(list(line.strip()))
            if line[0] == "<" or line[0] == ">" or line[0] == "^" or line[0] == "v":
                inputs.append(line.strip())
    return inputs

def initialize_robot(warehouse):
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == '@':
                return [i,j]

def move(point, direction, times=1):
    point = [point[0] + (times * direction[0]), point[1] + (times * direction[1])]
    return point

def check_spot(warehouse, point):
    return warehouse[point[0]][point[1]]

def set_spot(warehouse, point, symbol):
    warehouse[point[0]][point[1]] = symbol
    return warehouse

def move_robot(warehouse,command):
    robot = initialize_robot(warehouse)
    if command == '<': direction = WEST
    if command == '>': direction = EAST
    if command == '^': direction = NORTH
    if command == 'v': direction = SOUTH
    if check_spot(warehouse, move(robot, direction)) == '.':
        warehouse = set_spot(warehouse, robot, ".")
        robot = move(robot, direction)
        warehouse = set_spot(warehouse, robot, "@")
    elif check_spot(warehouse, move(robot, direction)) == 'O':
        push_spot = move(robot, direction)
        while check_spot(warehouse, push_spot) == 'O':
            push_spot = move(push_spot, direction)
        if check_spot(warehouse, push_spot) == '.':
            warehouse = set_spot(warehouse, push_spot, 'O')
            warehouse = set_spot(warehouse, robot, ".")
            robot = move(robot, direction)
            warehouse = set_spot(warehouse, robot, "@")                
    return warehouse

def get_gps(warehouse):
    gps = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == 'O':
                gps += 100 * i + j
    return gps

def main():
    inputs = initialize_warehouse()
    warehouse = inputs[0]
    commands = ""
    for i in range(1, len(inputs)):
        commands += inputs[i]
    for command in commands:
        warehouse = move_robot(warehouse,command)
    gps = get_gps(warehouse)
    print(gps)
    
start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")


