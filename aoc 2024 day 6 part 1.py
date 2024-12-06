grid = []
direction = [-1, 0]
location = []
loops = 0
loop_start = []

with open('input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '^':
            location = [i, j]

while location[0] >= 0 and location[0] < len(grid) and location[1] >=0 and location[1] < len(grid[0]):
    grid[location[0]][location[1]] = '^'
    if grid[location[0] + direction[0]][location[1] + direction[1]] == '#':
        if direction == [-1, 0]:
            direction = [0, 1]
        elif direction == [0, 1]:
            direction = [1, 0]
        elif direction == [1, 0]:
            direction = [0, -1]
        elif direction == [0, -1]:
            direction = [-1, 0]
    location[0] += direction[0]
    location[1] += direction[1]
    
spaces = 0
for row in grid:
    for item in row:
        if item == '^':
            spaces += 1
for row in grid:
    print(''.join(row))

print(spaces)
