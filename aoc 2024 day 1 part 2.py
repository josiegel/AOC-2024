list1 = []
list2 = []
simscore = 0

with open('input.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()
for i in list1:
    for j in list2:
        if i == j:
            simscore = simscore + i

print(simscore)
