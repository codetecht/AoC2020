# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re

def main():
    f = open("input.txt", "r+")
    input_lines = f.readlines()
    file_lines = len(input_lines)
    width = len(input_lines[0])-1

    code_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    curr_pp = []

    passed = 0

    test_counter = 0
    line_counter = 0

    valid = True

    for line in input_lines:
        line_counter += 1
        
        curr_line = line.split()

        if line != "\n":
            for el in curr_line:
                curr_pp.append(el)
        else:
            code_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
            valid = True
            #print(curr_pp)
            for el in curr_pp:
                if el[0:3] == "byr":
                    #valid = (1920 <= int(el[4:]) <= 2002)
                    valid = ((int(el[4:]) >= 1920) and (int(el[4:]) <= 2002))
                if el[0:3] == "iyr":
                    valid = ((int(el[4:]) >= 2010) and (int(el[4:]) <= 2020))
                if el[0:3] == "eyr":
                    valid = ((int(el[4:]) >= 2020) and (int(el[4:]) <= 2030))
                if el[0:3] == "hgt":
                    if (el[-2:] == "cm"):
                        valid = ((int(el[4:-2]) >= 150) and (int(el[4:-2]) <= 193))
                    elif (el[-2:] == "in"):
                        valid = ((int(el[4:-2]) >= 59) and (int(el[4:-2]) <= 76))
                    else:
                        valid = False
                if el[0:3] == "hcl":
                    valid = (el[4] == "#") and (el[5:].isalnum())
                if el[0:3] == "ecl":
                    valid = el[4:].isalnum()
                if el[0:3] == "pid":
                    valid = (len(el[4:]) == 9) and el[4:].isnumeric()

                if not valid:
                    break
                if el[0:3] in code_list:
                    code_list.remove(el[0:3])


            if valid and len(code_list) == 0:
                passed += 1

            curr_pp = []

        #limits how many lines the program searches through
        #if test_counter > 100:
        #    break
        #else:
        #    test_counter += 1

    print(passed)


main()
