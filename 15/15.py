# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

PART_ONE = 2020
PART_TWO = 30000000

def part1(input):
    spoken = input.copy()
    spoken.reverse()
    for i in range(len(input), PART_ONE):
        lastnum = spoken[0]
        if lastnum in spoken[1:]:
            spoken.insert(0, spoken.index(lastnum, 1))
        else:
            spoken.insert(0, 0)
    print(spoken[0])
    
def part2(input):
    spoken = {}
    for i, num in enumerate(input):
        spoken[num] = i+1

    nextnum = input[-1]
    for i in range(len(input), PART_TWO):
        if nextnum not in spoken:
            spoken[nextnum] = i
            nextnum = 0
        else:
            temp = spoken[nextnum]
            spoken[nextnum] = i
            nextnum = spoken[nextnum] - temp 
    print(nextnum)
    
def main():
    input = [8, 13, 1, 0, 18, 9]
    part1(input)
    part2(input)

main()
