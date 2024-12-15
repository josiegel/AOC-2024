import time
MAX_X = 101
MAX_Y = 103


def initialize_guards():
    guards = []
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip().split()
            guards.append([list(map(int, line[0][2:].split(","))),list(map(int, line[1][2:].split(",")))])
    return guards

def move(point, direction, times=1):
    point = [point[0] + (times * direction[0]), point[1] + (times * direction[1])]
    while point[0] < 0:
        point[0] += MAX_X
    while point[0] >= MAX_X:
        point[0] -= MAX_X
    while point[1] < 0:
        point[1] += MAX_Y
    while point[1] >= MAX_Y:
        point[1] -= MAX_Y
    return point

def safety_factor(guards):
    up_left = 0
    up_right = 0
    down_left = 0
    down_right = 0
    for guard in guards:
        if guard[0][0] < 50:
            if guard[0][1] < 51:
                up_left += 1
            elif guard[0][1] > 51:
                up_right += 1
        elif guard[0][0] > 50:
            if guard[0][1] < 51:
                down_left += 1
            elif guard[0][1] > 51:
                down_right += 1
    return up_left * up_right * down_left * down_right

def draw_guards(guards):
    print()
    print()
    print()
    output = []
    for i in range(103):
        output.append("")
        for j in range(101):
            output[i] += "."
    for guard in guards:
        output[guard[0][1]] = output[guard[0][1]][:guard[0][0]] + "X" + output[guard[0][1]][guard[0][0]+1:]
    for row in output:
        print(row)

def main():
    guards = initialize_guards()
    seconds = 0
    while True:
        seconds += 1
        for guard in guards:
            guard[0] = move(guard[0], guard[1])
        if (seconds - 25) % 103 == 0 or (seconds - 62) % 101 == 0:
            draw_guards(guards)
            print(seconds, " seconds.")
            input()
        

start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")


