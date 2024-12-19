import time
input = "input.txt"

def get_patterns(input):
    with open(input, 'r') as file:
        patterns = file.readline().strip().split(", ")
    return patterns

def get_designs(input):
    designs = []
    with open(input, 'r') as file:
        file.readline()
        file.readline()
        for line in file:
            designs.append(line.strip())
    return designs

def works(design, patterns):
    for pattern in patterns:
        if design == pattern: return True
        if design[:len(pattern)] == pattern and works(design[len(pattern):], patterns):
            return True
    return False

def main():
    patterns = get_patterns(input)
    designs = get_designs(input)
    working_designs = 0
    for design in designs:
        if works(design, patterns):
            working_designs += 1
    print(working_designs)


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")