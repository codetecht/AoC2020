# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

def main():
    f = open("input.txt", "r+")

    file_lines = f.readlines()

    pw_correct = 0
    pt2_correct = 0


    for x in file_lines:
        
        # split string into sub-strings
        temp = x.split()

        # load min/max times, pattern, and pass into variables
        min = int((temp[0].split('-'))[0])
        max = int((temp[0].split('-'))[1])
        let = (temp[1])[0]
        pw = temp[2]
        count = 0

        # check pattern in password
        for letter in pw:
            if letter == let:
                count += 1

        if (count >= min) and (count <= max):
            pw_correct += 1

        ######################## PART 2 ########################################

        pos1 = min
        pos2 = max

        # check if the letter shows up at those positions
        if((pw[pos1-1] == let) != (pw[pos2-1] == let)):
            pt2_correct += 1


    print(str(pw_correct) + ", " + str(pt2_correct))

main()
