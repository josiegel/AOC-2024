letters = []
xmas = 0

with open('input.txt', 'r') as file:
    for line in file:
        row = []
        for letter in range(len(line)):
            row.append(line[letter])
        letters.append(row)


for i in range(1, len(letters) - 1):
    for j in range(1, len(letters[i]) - 1):
        if letters[i][j] == 'A':
            if letters[i-1][j-1] == 'M' and letters[i-1][j+1] == 'M' and letters[i+1][j+1] == 'S' and letters[i+1][j-1] == 'S':
                xmas += 1
            if letters[i-1][j-1] == 'M' and letters[i+1][j-1] == 'M' and letters[i+1][j+1] == 'S' and letters[i-1][j+1] == 'S':
                xmas += 1
            if letters[i+1][j+1] == 'M' and letters[i+1][j-1] == 'M' and letters[i-1][j-1] == 'S' and letters[i-1][j+1] == 'S':
                xmas += 1
            if letters[i+1][j+1] == 'M' and letters[i-1][j+1] == 'M' and letters[i-1][j-1] == 'S' and letters[i+1][j-1] == 'S':
                xmas += 1
  
print(xmas)
