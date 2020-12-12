# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re

# Prep work
f = open("11/input.txt", "r+")
data = f.readlines()

width = len(data[0].rstrip()) # 92
seats = list()
seatmap = {}

# For debugging
test_counter = 0

for line in data:
    seats.append(line.rstrip())

    # This part limits runtime for debugging
    #if test_counter > 3:
    #    break
    #else:
    #    test_counter += 1

def populate(changelist):
    if len(seatmap) == 0:
        for i, row in enumerate(seats):
            for j, chair in enumerate(row):
                seatmap[(i,j)] = chair
    else:
        for seat in changelist:
            if seatmap[seat] == 'L':
                seatmap[seat] == '#'
            if seatmap[seat] == '#':
                seatmap[seat] == 'L'

def seatcheck(seat):
    occ = 0
    free = 0
    max_free = 8

    if seat[0] == 0:
        above = False
    else:
        above = True 
    if seat[0] == len(data)-1:
        below = False
    else:
        below = True
    if seat[1] == 0:
        left = False
    else:
        left = True
    if seat[1] == width-1:
        right = False
    else:
        right = True

    edge_case = above + below + right + left
    if edge_case == 3:
        max_free = 5
    if edge_case == 2:
        max_free = 3


    for row in range(seat[0]-int(above), seat[0]+int(below)+1):
        for chair in range(seat[1]-int(left), seat[1]+int(right)+1):
            if (row, chair) == seat:
                continue
            elif seatmap[(row, chair)] == '#':
                occ += 1
            elif seatmap[(row, chair)] == 'L' or '.':
                free += 1
    if seatmap[seat] == '#' and occ > 3:
        return True
    if seatmap[seat] == 'L' and free == max_free:
        return True

    return False


def part1():
    equilibrium = False
    changelist = list()
    populate(changelist)
    print(seatmap[(0,0)])
    test_counter = 0

    while not equilibrium and test_counter < 2:
        changelist = []

        for seat in seatmap:
            if seatcheck(seat):
                changelist.append(seat)

        if len(changelist) == 0:
            equilibrium = True
            print("Eq reached")
        else:
            test_counter += 1

        populate(changelist)
    
    print(seatmap[(0,0)])


def part2():
    bar = 'foo'
    
def main():
    part1()
    #part2()

main()