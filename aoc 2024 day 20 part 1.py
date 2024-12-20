import time
NORTH = (-1,0)
SOUTH = (1,0)
EAST = (0,1)
WEST = (0,-1)
filename = 'input.txt'
size = 0
threshold = 100

def move(location, direction):
    return ((location[0] + direction[0], location[1] + direction[1]))

def get_neighbors(location):
    return (move(location, NORTH), move(location, SOUTH), move(location, EAST), move(location, WEST))

def get_walls(filename):
    global size
    walls = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        size = len(lines)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                walls.append((i,j))
    return tuple(walls)

def get_start(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                return((i,j))   

def get_finish(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "E":
                return((i,j))


    
def track_run(start, finish, walls):
    visited = [start]
    steps = 0
    location = start
    while location != finish:
        for neighbor in get_neighbors(location):
            if neighbor not in walls and neighbor not in visited:
                location = neighbor
                steps += 1
        visited.append(location)
    return visited


def main():
    walls = get_walls(filename)
    start = get_start(filename)
    finish = get_finish(filename)
    visited = track_run(start, finish, walls)
    cheats = 0
    i = 0
    for wall in walls:
        if move(wall, SOUTH) in visited and move(wall, NORTH) in visited and abs(visited.index(move(wall, SOUTH)) - visited.index(move(wall, NORTH))) >= threshold+2:
            cheats += 1
        if move(wall, EAST) in visited and move(wall, WEST) in visited and abs(visited.index(move(wall, EAST)) - visited.index(move(wall, WEST))) >= threshold+2:
            cheats += 1
        i += 1
    print(cheats)



start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")
