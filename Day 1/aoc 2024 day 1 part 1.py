list1 = []
list2 = []
distance = 0

with open('input.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()
for i in range(len(list1)):
    distance = distance + abs(list1[i] - list2[i])

print(distance)
