letters = []
xmas = 0

with open('input.txt', 'r') as file:
    for line in file:
        row = []
        for letter in range(len(line)):
            row.append(line[letter])
        letters.append(row)


for i in range(len(letters)):
    for j in range(len(letters[i])):
        if letters[i][j] == 'X':
            if j + 3 < len(letters):
                if (letters[i][j+1] == 'M' and letters[i][j+2] == 'A' and letters[i][j+3] == 'S'):
                    xmas += 1
            if i + 3 < len(letters):
                if (letters[i+1][j] == 'M' and letters[i+2][j] == 'A' and letters[i+3][j] == 'S'):
                    xmas += 1
            if j - 3 >= 0:
                if (letters[i][j-1] == 'M' and letters[i][j-2] == 'A' and letters[i][j-3] == 'S'):
                    xmas += 1
            if i - 3 >= 0:
                if (letters[i-1][j] == 'M' and letters[i-2][j] == 'A' and letters[i-3][j] == 'S'):
                    xmas += 1
            if i + 3 < len(letters) and j + 3 < len(letters):
                if (letters[i+1][j+1] == 'M' and letters[i+2][j+2] == 'A' and letters[i+3][j+3] == 'S'):
                    xmas += 1
            if i - 3 >= 0 and j - 3 >= 0:
                if (letters[i-1][j-1] == 'M' and letters[i-2][j-2] == 'A' and letters[i-3][j-3] == 'S'):
                    xmas += 1
            if i + 3 < len(letters) and j - 3 >= 0:
                if (letters[i+1][j-1] == 'M' and letters[i+2][j-2] == 'A' and letters[i+3][j-3] == 'S'):
                    xmas += 1
            if i - 3 >= 0 and j + 3 < len(letters):
                if (letters[i-1][j+1] == 'M' and letters[i-2][j+2] == 'A' and letters[i-3][j+3] == 'S'):
                    xmas += 1
print(xmas)
