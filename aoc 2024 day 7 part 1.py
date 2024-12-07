outputs = []
inputs = []

with open('input.txt', 'r') as file:
    for line in file:
        outputs.append(int(line.split(':')[0]))
        inputs.append(line.split(':')[1].split())

# fun with recursion
def possible_totals(ls):
    if len(ls) == 2:
        return [ls[0] + ls[1], ls[0] * ls[1]]
    else:
        ans = []
        tail = ls.pop()
        for num in possible_totals(ls):
            ans.append(tail * num)
            ans.append(tail + num)
        return ans

def test_line(output, nums):
    int_nums = list(map(int, nums))
    if output in possible_totals(int_nums):
        return output
    else:
        return 0

total = 0        
for i in range(len(outputs)):
    total += test_line(outputs[i], inputs[i])
print(total)
