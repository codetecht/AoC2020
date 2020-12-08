# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

def main():
    f = open("3/input.txt", "r+")
    code_lines = f.readlines()
    width = len(code_lines[0]) - 1
    pos = 0
    trees = 0
    line_count = 1


    ################################ PART 2 ####################################
    #for i in range(0,len(code_lines)):
    #    if (i%2 == 1) or (i == 0):
    #        pos = (pos + 1)%width
    #        continue
    #    elif (code_lines[i])[pos] == '#':
    #        trees += 1
    #        print(str(i) + ", " + str(pos) + ";   " + code_lines[i])
    #    pos = (pos + 1)%width
        
        
    ################################ PART 1 ####################################
    for line in code_lines[0:]:
        if line[pos] == '#':
            print(str(line_count) + ", " + str(pos) + ";   " + line)
            trees += 1
        pos = (pos + 3)%width
        line_count += 1

    print(trees)

main()
