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
    

def get_score(point, trail_map):
    score = 0
    points_to_test = [(point[0]+1, point[1]), (point[0]-1, point[1]), (point[0], point[1]+1), (point[0], point[1]-1)]
    for test_point in points_to_test:
        if 0 <= test_point[0] < len(trail_map) and 0 <= test_point[1] < len(trail_map) and trail_map[test_point[0]][test_point[1]] == trail_map[point[0]][point[1]] + 1:
            if trail_map[point[0]][point[1]] == 8:
                score += 1
            else:
                score += get_score(test_point, trail_map)
    return score
        

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
