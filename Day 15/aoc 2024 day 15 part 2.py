import time
import copy
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
    elongated_warehouse = []
    i = 0
    for row in inputs[0]:
        elongated_warehouse.append([])
        for space in row:
            if space == '#':
                elongated_warehouse[i].append('#')
                elongated_warehouse[i].append('#')
            if space == 'O':
                elongated_warehouse[i].append('[')
                elongated_warehouse[i].append(']')
            if space == '.':
                elongated_warehouse[i].append('.')
                elongated_warehouse[i].append('.')
            if space == '@':
                elongated_warehouse[i].append('@')
                elongated_warehouse[i].append('.')
        i += 1
    inputs[0] = elongated_warehouse
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

def get_push_spots(warehouse, robot, direction):
    push_spots = [robot]
    i = 0
    while i < len(push_spots):
        spot = move(push_spots[i], direction)
        if check_spot(warehouse, spot) == '#':
            return []
        if check_spot(warehouse, spot) == '[':
            push_spots.append(spot)
            if direction == NORTH or direction == SOUTH:
                push_spots.append(move(spot, EAST))
        if check_spot(warehouse, spot) == ']':
            push_spots.append(spot)
            if direction == NORTH or direction == SOUTH:
                push_spots.append(move(spot, WEST))
        i += 1
    return push_spots

def reverse(direction):
    return (-1 * direction[0], -1 * direction[1])
        
def move_everything(warehouse, push_spots, direction):
    old_warehouse = copy.deepcopy(warehouse)
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            spot = [i,j]        
            if move(spot, reverse(direction)) in push_spots:
                old_spot = move(spot, reverse(direction))
                set_spot(warehouse, spot, check_spot(old_warehouse, old_spot))
            elif spot in push_spots:         
                set_spot(warehouse, spot, ".")
    return warehouse

def print_warehouse(warehouse):
    for row in warehouse:
        print(''.join(row))

def move_robot(warehouse,command):
    robot = initialize_robot(warehouse)
    if command == '<': direction = WEST
    if command == '>': direction = EAST
    if command == '^': direction = NORTH
    if command == 'v': direction = SOUTH
    push_spots = get_push_spots(warehouse, robot, direction)
    warehouse = move_everything(warehouse, push_spots, direction)
    return warehouse

def get_gps(warehouse):
    gps = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == '[':
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


