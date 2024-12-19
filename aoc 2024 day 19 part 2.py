import time
filename = "input.txt"
recursion_layer = 0
design_dict = {"":1}

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

def score_design(design, patterns):
    global design_dict
    score = 0
    for pattern in patterns:
        if design.startswith(pattern):
            if design[len(pattern):] in design_dict:
                design_score = design_dict[design[len(pattern):]]
            else:
                design_score = (score_design(design[len(pattern):], patterns))
            design_dict[design[len(pattern):]] = design_score
            score += design_score
    return score

def main():
    patterns = get_patterns(filename)
    print(len(patterns))
    designs = get_designs(filename)
    total_score = 0
    patterns_analyzed = 0
    for design in designs:
        design_score = score_design(design,patterns)
        total_score += design_score
    print(len(design_dict))
    print(total_score)


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")