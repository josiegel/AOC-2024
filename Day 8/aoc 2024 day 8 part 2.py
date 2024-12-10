import time

# set the starting grid
def initialize_grid():
    grid = []
    with open('input.txt', 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

# create a list of the possible symbols that can be creating antinodes
def find_symbols(grid):
    symbols = set()
    for line in grid:
        for item in line:
            if item != '.':
                symbols.add(item)
    return list(symbols)

# get all of the coordinates that a symbol appears at in the grid
def get_coordinates(symbol, grid):
    coords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == symbol:
                coords.append([i, j])
    return coords
            
    
# find the number of nodes created in the grid by a symbol with the given coordinates
def get_nodes(coords, grid):
    nodes = set()
    for i in range(len(coords)-1):
        for j in range(i+1, len(coords)):
            vector = [coords[i][0] - coords[j][0], coords[i][1] - coords[j][1]]
            vector_strength = 0
            while 0 <= coords[i][0] + (vector_strength * vector[0]) < len(grid) and 0 <= coords[i][1] + (vector_strength * vector[1]) < len(grid):
                nodes.add((coords[i][0] + (vector_strength * vector[0]), coords[i][1] + (vector_strength * vector[1])))
                vector_strength += 1
            vector_strength = 0
            while 0 <= coords[j][0] - (vector_strength * vector[0]) < len(grid) and 0 <= coords[j][1] - (vector_strength * vector[1]) < len(grid):
                nodes.add((coords[j][0] - (vector_strength * vector[0]), coords[j][1] - (vector_strength * vector[1])))
                vector_strength += 1
    return nodes
    
def main():
    grid = initialize_grid()
    symbols = find_symbols(grid)
    nodes = set()
    for symbol in symbols:
        nodes.update(get_nodes(get_coordinates(symbol, grid), grid))
    print(len(nodes))
    
main()

