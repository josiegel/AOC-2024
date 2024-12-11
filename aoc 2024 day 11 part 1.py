import time

# set the starting disk_map
def initialize_stones():
    with open('input.txt', 'r') as file:
        return file.read().strip().split()

def morph_stones(stones, blinks):
    if blinks == 0:
        return stones
    else:
        mutated_stones = []
        for stone in stones:
            stone = str(int(stone))
            if stone == '0':
                mutated_stones.append('1')
            elif len(stone) % 2 == 0:
                mutated_stones.append(stone[:len(stone)//2])
                mutated_stones.append(stone[-len(stone)//2:])
            else:
                mutated_stones.append(str(2024*int(stone)))
        return morph_stones(mutated_stones, blinks-1)

        


def main():
    stones = initialize_stones()
    stones = morph_stones(stones, 25)
    print(len(stones))


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")
