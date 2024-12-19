import time
NORTH = (-1,0)
SOUTH = (1,0)
EAST = (0,1)
WEST = (0,-1)
SIZE = 15
INPUT = "input.txt"

def get_walls(input):
    walls = []
    with open(input, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                walls.append((i,j))
    return tuple(walls)

def get_start(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                return((i,j))

def get_finish(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "E":
                return((i,j))

def move(location, direction):
    return (location[0]+direction[0], location[1]+direction[1])

def left(direction):
    if direction == NORTH:
        return WEST
    elif direction == SOUTH:
        return EAST
    elif direction == EAST:
        return NORTH
    elif direction == WEST:
        return SOUTH

def right(direction):
    if direction == NORTH:
        return EAST
    elif direction == SOUTH:
        return WEST
    elif direction == EAST:
        return SOUTH
    elif direction == WEST:
        return NORTH        

def get_neighbors(node, walls):
    location = node[0]
    direction  = node[1]
    neighbors = []
    if move(location, direction) not in walls:
        neighbors.append((move(location,direction),direction))
    if move(location, left(direction)) not in walls:
        neighbors.append((location, left(direction)))
    if move(location, right(direction)) not in walls:
        neighbors.append((location, right(direction)))   
    return neighbors

def get_next_node(queue,scores):
    next_node = queue[0]
    for node in queue:
        if node in scores and scores[node] < scores[next_node]:
            next_node = node
    return next_node

def analyze_node(node, walls, scores):
    current_score = scores[node]
    for neighbor in get_neighbors(node, walls):
        if node[0] == neighbor[0]:
            scores[neighbor] = min(scores[neighbor], 1000 + current_score)
        else:
            scores[neighbor] = min(scores[neighbor], 1 + current_score)
    

def get_score(start, finish, walls):
    starting_node = (start, EAST)
    visited_nodes = []
    scores = {(starting_node):0}
    queue  = [starting_node] + get_neighbors(starting_node, walls)
    while queue:
        current = get_next_node(queue, scores)
        for node in get_neighbors(current,walls):
            if node not in scores:
                queue.append(node)
                scores[node] = float('inf')
        analyze_node(current, walls, scores)
        queue.remove(current)
    finishing_scores = []
    for direction in [NORTH, SOUTH, EAST, WEST]:
        finishing_scores.append((finish, direction))
    score = float('inf')
    for direction in finishing_scores:
        if direction in scores:
            score = min(score, scores[direction])
    return score




def main():
    input = "example.txt"
    walls = get_walls(INPUT)
    start = get_start(INPUT)
    finish = get_finish(INPUT)
    score = get_score(start, finish, walls)
    print(score)


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")
