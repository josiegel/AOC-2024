import time

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
        neighbors = [(region[i][0]+1, region[i][1]),(region[i][0]-1, region[i][1]),(region[i][0], region[i][1]+1),(region[i][0], region[i][1]-1)]
        for neighbor in neighbors:
            if neighbor not in region and 0 <= neighbor[0] < len(garden) and 0 <= neighbor[1] < len(garden) and garden[neighbor[0]][neighbor[1]] == crop:
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
                
def get_sides(region):
    sides = 0
    for plot in region:
        if (plot[0]-1, plot[1]) not in region and not ((plot[0], plot[1]-1) in region and (plot[0]-1, plot[1]-1) not in region):
                sides += 1
        if (plot[0], plot[1]-1) not in region and not ((plot[0]-1, plot[1]) in region and (plot[0]-1, plot[1]-1) not in region):
                sides += 1
        if (plot[0]+1, plot[1]) not in region and not ((plot[0], plot[1]-1) in region and (plot[0]+1, plot[1]-1) not in region):
                sides += 1
        if (plot[0], plot[1]+1) not in region and not ((plot[0]-1, plot[1]) in region and (plot[0]-1, plot[1]+1) not in region):
                sides += 1
    return sides


def get_price(region):
    sides = get_sides(region)
    area = len(region)
    return area * sides

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
