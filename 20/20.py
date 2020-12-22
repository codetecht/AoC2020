# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re
from dataclasses import dataclass

f = open("20/sample1.txt", "r+")
data = f.readlines()

reNum = re.compile('(\d+)')

@dataclass
class tile:
    id: int
    top: str
    bot: str
    lft: str
    rht: str

def getInput():
    
    tileset = []
    for n, line in enumerate(data):
        if n%12 == 0:
            lft, rht = '', ''
            id = reNum.findall(line)[0]
            top = data[n+1].rstrip()
            bot = data[n+10].rstrip()
            for el in data[n+1:n+11]:
                lft += el[0]
                rht += el.rstrip()[-1]
            temp = tile(id, top, bot, lft, rht)
            tileset.append(temp)

    return tileset

def part1():
    tileset = getInput()

    for piece in tileset:
        attr = [val for field, val in piece.__dict__.items()]
        # For each side of each piece, iterate through all other sides of 
        # all other pieces and generate a record of what, if flipped or
        # rotated, could potentially fit that side. After a list of 
        # associations is built, create a separate function to brute force
        # them together. Or something.

def part2():
    bar = 'foo'
    
def main():
    part1()
    #part2()

main()
