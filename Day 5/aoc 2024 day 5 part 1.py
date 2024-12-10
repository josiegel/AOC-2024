rules = []
updates = []
sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        if '|' in line:
            rules.append(line.strip().split('|'))
        else:
            updates.append(line.strip().split(','))

updates.pop(0)

for update in updates:
    test = True
    for i in range(len(update)):
        for j in range(i, len(update)):
            for rule in rules:
                if rule[1] == update[i] and rule[0] == update[j]:
                    test = False
    if test: sum += int(update[len(update)//2])
    

print(sum)
