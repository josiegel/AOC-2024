reports = []
safe = 0

with open('input.txt', 'r') as file:
    for line in file:
        reports.append(list(map(int, line.split())))

for report in reports:
    check = False
    if report == sorted(report) or report == sorted(report, reverse=True):
        check = True
        for i in range(1, len(report)):
            if abs(report[i] - report[i-1]) < 1 or abs(report[i] - report[i-1]) > 3:
                check = False
        if check: safe += 1

print(safe)
