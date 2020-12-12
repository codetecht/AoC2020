# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

f = open("11/input.txt", "r+")
data = f.readlines()

# Prep work
seatmap = list()
width = len(data[0].rstrip())
length = len(data)

for line in data:
    seatmap.append(list(line.rstrip()))

"""
Performs a check from the seat in seatmap at seat_loc in all directions in
[dirs]. If part == 1, a floor seat is considered unoccupied. If part == 2,
will recursively look until a non-floor space is returned (edge of seating
area is treated as unoccupied). 

args: seat_loc: ordered-pair tuple of seat coordinates (row, column)
          dirs: list of string IDs for directions to peek
          part: if part == 2, modifies the algorithm to search in sight-line;
                all other values of part look for adjacent seats
Returns: a [list] containing the status of each surrounding seat (adjacent 
         seats if part == 1, in-sight seats if part == 2)
"""
def dirCheck(seat_loc, dirs, part):
    adj = list()
    for dir in dirs:
        row = seat_loc[0]
        col = seat_loc[1]

        # Remove directions which don't apply to the current seat (if top left
        # corner, then none of the up or left directions will be checked)
        if 'u' in dir:
            row -= 1
        if 'd' in dir:
            row += 1
        if 'l' in dir:
            col -= 1
        if 'r' in dir:
            col += 1

        # If the seat is within the seating area, return its occupied status
        if 0 <= row <= length-1 and 0 <= col <= width-1:
            seat_peek = seatmap[row][col]
            if seat_peek == '.':
                if part == 2:
                    one_dir = [dir]
                    adj.append(dirCheck((row, col), one_dir, part)[0])
                else:
                    adj.append('.')
            else:
                adj.append(seat_peek)
        # If seat is outside the area, treat as unoccupied
        else:
            adj.append('L')

    return adj

"""
Performs a pass/fail check on whether or not the seat at seat_loc meets the
requirements to be changed from free to occupied (or vice-versa).

args: seat_loc: ordered-pair tuple of seat coordinates (row, column)
          dirs: list of string IDs for directions to peek
          part: if part == 2, modifies the algorithm to search in sight-line;
                all other values of part look for adjacent seats
returns: TRUE if either:
             The seat is occupied and >= 4 (>= 5 for part 2) surrounding seats are
             occupied, or
             The seat is occupied and all surrounding seats are free
         FALSE otherwise
"""
def seatCheck(seat_loc, part):
    if part == 2:
        tolerance = 5
    else:
        tolerance = 4

    dirs = ['u', 'd', 'l', 'r', 'ul', 'dl', 'ur', 'dr']
    if seat_loc[0] == 0:
        dirs = [str for str in dirs if 'u' not in str]
    if seat_loc[0] == length-1:
        dirs = [str for str in dirs if 'd' not in str]
    if seat_loc[1] == 0:
        dirs = [str for str in dirs if 'l' not in str]
    if seat_loc[1] == width-1:
        dirs = [str for str in dirs if 'r' not in str]

    adjacent = dirCheck(seat_loc, dirs, part)

    seat_status = seatmap[seat_loc[0]][seat_loc[1]]
    if seat_status == 'L' and '#' not in adjacent:
        return True
    elif seat_status == '#' and adjacent.count('#') >= tolerance: 
        return True
    else:
        return False

def updateSeatMap(changes):
    for seat in changes:
        status = seatmap[seat[0]][seat[1]]
        if status == '#':
            seatmap[seat[0]][seat[1]] = 'L'
        elif status == 'L':
            seatmap[seat[0]][seat[1]] = '#'

def equilibrate(part):
    at_equilibrium = False
    while not at_equilibrium:

        # Reset the change list and seatCheck all spots that aren't floor space
        change_list = list()
        for i, row in enumerate(seatmap):
            for j, seat in enumerate(row):
                if seat != '.' and seatCheck((i,j), part):
                    change_list.append((i,j))

        # If no changes are found, we've reached equilibrium
        if len(change_list) == 0:
            at_equilibrium = True
        else:
            updateSeatMap(change_list)

    occ = 0
    for row in seatmap:
        occ += row.count('#')
    return occ

def main():
    #TODO: figure out how to reset the seatmap between iterations so both parts
    #      can be run in sequence

    #print(equilibrate(1))
    print(equilibrate(2))

main()
