# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re

def main():
    f = open("6/input.txt", "r+")
    input_lines = f.readlines()
    file_lines = len(input_lines)-1
    width = len(input_lines[0])-1

    y_count = 0
    yes = []
    group_rem = []
    group_yes = []
    ng_flag = True

    # For debugging
    test_counter = 0

    for line in input_lines:
        if line != "\n":
            curr_line = line.rstrip()

            if ng_flag:
                group_yes = (list(curr_line))
                ng_flag = False

            else:
                for a in group_yes:
                    if a not in curr_line:
                        if a not in group_rem:
                            group_rem.append(a)
            #for a in curr_line:
                #if a not in yes:
                #    yes.append(a)

        else:
            for a in group_rem:
                group_yes.remove(a)
            y_count += len(group_yes)
            ng_flag = True
            print(y_count)
            yes = []
            group_yes = []
            group_rem = []





        # This part limits runtime for debugging
        #if test_counter > 15:
        #    break
        #else:
        #   test_counter += 1


main()
