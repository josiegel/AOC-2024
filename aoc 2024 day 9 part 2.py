import time
import sys
sys.set_int_max_str_digits(19999)

# set the starting disk_map
def initialize_disk_map():
    with open('input.txt', 'r') as file:
        return file.read().strip()

# convert a disk_map to a disk
def unfold_disk(disk_map):
    disk = []
    writing_nums = True
    file_id = 0
    for digit in disk_map:
        for i in range(int(digit)):
            if writing_nums:
                disk.append(file_id)
            else:
                disk.append(-1)
        if writing_nums: file_id += 1
        writing_nums = not writing_nums
    return disk

# move the blocks per the amphipod's NEW instructions    
def move_blocks(disk):
    max_file_id = max(disk)
    for file_id in range(max_file_id, 1, -1):
        file_start = disk.index(file_id)
        file_size = disk.count(file_id)
        available_space = 0
        j = 0
        while disk[j] != file_id and available_space < file_size:
            j += 1
            if disk[j] == -1:
                available_space += 1
            else:
                available_space = 0
        if available_space == file_size:
            for k in range(file_size):
                disk[j-k], disk[file_start+k] = disk[file_start+k], disk[j-k]   
    return disk

# run the checksum
def checksum(disk):
    total = 0
    for i in range(len(disk)):
        if disk[i] != -1:
            total += i * disk[i]
    return total

    
def main():
    disk_map = initialize_disk_map()
    disk = unfold_disk(disk_map)
    updated_disk = move_blocks(disk)
    sum = checksum(updated_disk)
    print(sum)


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")
