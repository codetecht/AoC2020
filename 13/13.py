# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re

f = open("13/input.txt", "r+")
data = f.readlines()

def getInput():
    input = list()
    for line in data:
        input.append(line.rstrip())
    return input


def part1(input):
    foo = 'bar'

    for line in input:
        foo = 'bar'
    
def part2():
    bar = 'foo'
    
def main():
    part1(getInput())
    #part2()

main()
