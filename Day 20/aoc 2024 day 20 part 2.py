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

def distance(pointA, pointB):
    return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])

def main():
    walls = get_walls(filename)
    start = get_start(filename)
    finish = get_finish(filename)
    visited = track_run(start, finish, walls)
    cheats = 0
    for i in range(0, len(visited)-threshold):
        for j in range(i+threshold, len(visited)):
            if distance(visited[i], visited[j]) <= 20 and j - i >= threshold + distance(visited[i], visited[j]):
                cheats += 1            
    print(cheats)




start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")
