import copy
starting_grid = []
starting_direction = [-1, 0]
starting_location = []

# set the starting grid
with open('input.txt', 'r') as file:
    for line in file:
        starting_grid.append(list(line.strip()))

# set the starting location
for i in range(len(starting_grid)):
    for j in range(len(starting_grid[i])):
        if starting_grid[i][j] == '^':
            starting_location = [i, j]

# check a given potential obstacle spot
def check_spot(i, j):
    location = starting_location.copy()
    direction = starting_direction.copy()
    grid = copy.deepcopy(starting_grid)
    grid[i][j] = '#'
    steps = 0
    while steps < 20000 and location[0] + direction[0] >= 0 and location[0] + direction[0] < len(grid) and location[1] + direction[1] >= 0 and location[1] + direction[1] < len(grid):
        if grid[location[0] + direction[0]][location[1] + direction[1]] == '#':
            if direction == [-1, 0]:
                direction = [0, 1]
            elif direction == [0, 1]:
                direction = [1, 0]
            elif direction == [1, 0]:
                direction = [0, -1]
            elif direction == [0, -1]:
                direction = [-1, 0]
        else:
            location[0] += direction[0]
            location[1] += direction[1]
            steps += 1
    # hey, it works
    if steps == 20000:
        return True
    else:
        return False

def main():
    loops = 0
    for i in range(len(starting_grid)):
        for j in range(len(starting_grid[0])):
            if starting_location != (i, j) and check_spot(i, j): loops += 1
    print(loops)

main()
            
