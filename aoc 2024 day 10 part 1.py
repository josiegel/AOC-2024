import time

def initialize_map():
    trail_map = []
    with open('input.txt', 'r') as file:
        for line in file:
            trail_map.append(list(map(int, (line.strip()))))
    return trail_map

def get_trailheads(trail_map):
    trail_heads = []
    for i in range(len(trail_map)):
        for j in range(len(trail_map[0])):
            if trail_map[i][j] == 0:
                trail_heads.append([i, j])
    return trail_heads
    

def get_score(trail_head, trail_map):
    points = {(trail_head[0], trail_head[1])}       
    for elevation in range(9):
        next_steps = set()
        for point in points:
            if point[0]+1 < len(trail_map) and trail_map[point[0]+1][point[1]] == elevation + 1:
                    next_steps.add((point[0]+1,point[1]))
            if point[1]+1 < len(trail_map[0]) and trail_map[point[0]][point[1]+1] == elevation + 1:
                    next_steps.add((point[0],point[1]+1))
            if point[0]-1 >= 0 and trail_map[point[0]-1][point[1]] == elevation + 1:
                    next_steps.add((point[0]-1,point[1]))
            if point[1]-1 >= 0 and trail_map[point[0]][point[1]-1] == elevation + 1:
                    next_steps.add((point[0],point[1]-1))
        points = next_steps.copy()
    return len(points)

def main():
    trails = 0
    trail_map = initialize_map()
    trail_heads = get_trailheads(trail_map)
    for trail_head in trail_heads:
        trails += get_score(trail_head, trail_map)
    print(trails)


start_time = time.time()
main()
end_time = time.time()
print(end_time - start_time, " seconds")
