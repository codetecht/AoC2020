# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

def main():
    temp = ""
    intArray = [];

    # Open the file
    f = open("numbers.txt", "r+")

    # Place each line of the file in an array index
    numberArray = f.readlines()

    # Remove newline whitespace at the end of each entry
    for x in numberArray:
        intArray.append(x.rstrip())

    for n in intArray:

        for m in intArray:

            # This part is for the extra second half
            for o in intArray:
                if (int(n) + int(m) + int(o) == 2020):
                    print(n + ", " + m + ", " + o)

main()
