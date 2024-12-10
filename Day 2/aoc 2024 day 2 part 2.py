reports = []
safe = 0

with open('input.txt', 'r') as file:
    for line in file:
        reports.append(list(map(int, line.split())))

for report in reports:
    checkA = False
    for i in range(len(report)):
        copy = report.copy()
        copy.pop(i)
        checkB = False
        if copy == sorted(copy) or copy == sorted(copy, reverse=True):
            checkB = True
            for i in range(1, len(copy)):
                if abs(copy[i] - copy[i-1]) < 1 or abs(copy[i] - copy[i-1]) > 3:
                    checkB = False
        if checkB: checkA = True
    if checkA: safe += 1

print(safe)
