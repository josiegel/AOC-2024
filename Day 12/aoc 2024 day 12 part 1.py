import time
NORTH = (-1, 0)
SOUTH = (+1, 0)
EAST = (0, +1)
WEST = (0, -1)

def move(point, direction):
    return (point[0] + direction[0], point[1] + direction[1])

def get_neighbors(point, grid = []):
    neighbors = []
    for direction in [NORTH, SOUTH, EAST, WEST]:
        neighbor = move(point, direction)
        if grid == [] or (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])):
            neighbors.append(neighbor)
    return neighbors

def initialize_garden():
    garden = []
    with open('input.txt', 'r') as file:
        for line in file:
            garden.append(list(line.strip()))
    return garden

def prune_region(garden, region):
    for plot in region:
        garden[plot[0]][plot[1]] = '.'
    return garden

def find_region(garden, region):
    crop = garden[region[0][0]][region[0][1]]
    i = 0
    while i < len(region):
        neighbors = get_neighbors(region[i], garden)
        for neighbor in neighbors:
            if neighbor not in region and garden[neighbor[0]][neighbor[1]] == crop:
                region.append(neighbor)
        i += 1
    return region

def get_regions(garden):
    regions = []
    for i in range(len(garden)):
        for j in range(len(garden)):
            if garden[i][j] != '.':
                new_region = find_region(garden, [(i, j)])
                garden = prune_region(garden, new_region)
                regions.append(new_region)
    return regions
                

def get_price(region):
    perimeter = 0
    for plot in region:
        neighbors = get_neighbors(plot)
        for neighbor in neighbors:
            if neighbor not in region:
                perimeter += 1
    area = len(region)
    return area * perimeter

def main():
    garden = initialize_garden()
    regions = get_regions(garden)
    total_price = 0
    for region in regions:
        total_price += get_price(region)
    print(total_price)


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")
