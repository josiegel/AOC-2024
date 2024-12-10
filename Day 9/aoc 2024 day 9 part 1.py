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
                disk.append('')
        if writing_nums: file_id += 1
        writing_nums = not writing_nums
    return disk

# move the blocks per the amphipod's instructions    
def move_blocks(disk):
    i = 0
    while i < len(disk):
        if disk[i] == '':
                disk[i] = disk[-1]
                disk.pop()
        else:
            i += 1
    return disk

# run the checksum
def checksum(disk):
    total = 0
    for i in range(len(disk)):
        if disk[i] != '':
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
