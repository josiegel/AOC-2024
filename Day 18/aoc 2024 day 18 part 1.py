import time
input = 'input.txt'
drops = 1024
size = 71

def initialize_bytes(input):
    bytes = []
    with open(input, 'r') as file:
        for line in file:
            bytes.append(tuple(list(map(int,line.strip().split(",")))))
    return bytes

def get_next_node(queue,scores):
    next_node = queue[0]
    for node in queue:
        if node in scores and scores[node] < scores[next_node]:
            next_node = node
    return next_node

def get_steps(start, finish, walls):
    queue = []
    node_scores = {}
    for i in range(0,size):
        for j in range(0,size):
            if (i,j) not in walls:
                node_scores[(i,j)] = float('inf')
                queue.append((i,j))
    node_scores[start] = 0
    while queue:
        current = get_next_node(queue, node_scores)
        for point in [(current[0]+1, current[1]),(current[0]-1, current[1]),(current[0], current[1]+1),(current[0], current[1]-1)]:
            if point in node_scores and node_scores[point] > 1 + node_scores[current]:
                node_scores[point] = 1+node_scores[current]
        queue.remove(current)
    return node_scores[finish]


def main():
    start = (0,0)
    finish = (size-1, size-1)
    walls = initialize_bytes(input)[:drops]
    steps = get_steps(start, finish, walls)
    print(steps)

start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")
