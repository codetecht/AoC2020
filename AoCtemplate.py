# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re

def main():
    f = open("#/input.txt", "r+")
    input_lines = f.readlines()
    file_lines = len(input_lines)-1
    width = len(input_lines[0])-1

    # For debugging
    test_counter = 0

    for line in input_lines:













        # This part limits runtime for debugging
        if test_counter > 3:
            break
        else:
            test_counter += 1

main()
