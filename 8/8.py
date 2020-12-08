# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re

def main():
    f = open("8/input.txt", "r+")
    data = f.readlines()

    # For debugging
    test_counter = 0

    for line in data:













        # This part limits runtime for debugging
        if test_counter > 3:
            break
        else:
            test_counter += 1

main()
