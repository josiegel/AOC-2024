import time
from collections import Counter


def initialize_stones():
    with open('input.txt', 'r') as file:
        return list(map(int, file.read().strip().split()))

def morph_dict(stones, blinks):
    new_stones = Counter()
    for stone in stones:
        if stone == 0:
            new_stones[1] += stones[stone]
        elif len(str(stone)) % 2 == 0:
            st = str(stone)
            new_stones[int(st[:len(st)//2])] += stones[stone]
            new_stones[int(st[len(st)//2:])] += stones[stone]
        else:
            new_stones[2024*stone] += stones[stone]
    if blinks == 1:
        return new_stones
    else:
        return morph_dict(new_stones, blinks-1)

        
def initialize_stone_counter(stones):
    stone_counter = Counter()
    for stone in stones:
        stone_counter[stone] += 1
    return stone_counter

def main():
    stones = initialize_stones()
    stones = initialize_stone_counter(stones)
    stones = morph_dict(stones, 75)
    print(sum(stones.values()), " total stones")


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")
