# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re
from array import *

def main():
    f = open("5/input.txt", "r+")
    input_lines = f.readlines()
    file_lines = len(input_lines)
    width = len(input_lines[0])-1

    seatID_max = 0
    seatID_list = []

    for row in range(128):
        for col in range(8):
            seatID_list.append((row * 8) + col)

    # For debugging
    test_counter = 0

    for line in input_lines:
        r_max = 127
        r_min = 0
        c_max = 7
        c_min = 0

        curr_line = line.rstrip()

        for i in range(len(curr_line)):
            if curr_line[i] == "F":
                r_max -= pow(2, 6-i)
            elif curr_line[i] == "B":
                r_min += pow(2, 6-i)
            elif curr_line[i] == "L":
                c_max -= pow(2, 9-i)
            elif curr_line[i] == "R":
                c_min += pow(2, 9-i)

        if (r_max != r_min) or (c_max != c_min):
            print("Max/min mismatch for id", line.rstrip(), sep = " ")

        seatID = (r_max * 8) + c_max
        seatID_list.remove(seatID)
        seatID_max = max(seatID_max, seatID)

        # This part limits runtime for debugging
        #if test_counter > 3:
        #    break
        #else:
        #    test_counter += 1

    #print(seatID_max)
    print(seatID_list)



main()