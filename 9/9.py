# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re

# Prep work
f = open("9/input.txt", "r+")
data = f.readlines()

# Checks if any two element in the queue sum to value
def checkQueue(value, queue):
    for i in queue:
        for j in queue:
            if i + j == value and queue.index(i) != queue.index(j):
                return True
    return False

def part1():
    queue = list()
    preamb = 0
    for line in data:

        if line != '\n':
            n = int(line.rstrip())

            # Populate the initial queue
            if preamb > 25:
                if checkQueue(n, queue) == False:
                    print(n)
                    return n
            else:
                preamb += 1
            
            # First-in-first-out queue kept at length of 25
            queue.insert(0, n)
            while len(queue) > 25:
                queue.pop()
    
def part2(broken_num):
    for n, line in enumerate(data): 
        if line != '\n':
            sum = 0
            val_list = list()

            # Check the list from the current number onward until sum >= broken_num
            for next_val in data[n:]:
                next_val = int(next_val)
                sum += next_val
                val_list.append(next_val)
                
                # Victory condition
                if sum == broken_num:
                    print(min(val_list) + max(val_list))
                elif sum > broken_num:
                    break

def main():
    broken_num = part1()
    part2(broken_num)

main()