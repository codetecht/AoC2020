# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re
import math
import functools

CUBE_SIZE = 20

f = open("17/input.txt", "r+")
data = f.readlines()

def getInput():
    input = list()
    for line in data:
        input.append(line.rstrip())

    sample = ['.#.', '..#', '###']
    return sample #input

def initializeCube():
    input = getInput()
    cube = [[['.' for k in range(-CUBE_SIZE, CUBE_SIZE+1)] 
                  for j in range(-CUBE_SIZE, CUBE_SIZE+1)] 
                  for i in range(-CUBE_SIZE, CUBE_SIZE+1)]
    for x, line in enumerate(input):
        for y, char in enumerate(line):
            cube[x][y][0] = char
    return cube

def neighbors(cube, coords):
    x, y, z = [n for n in coords]
    active = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if (i,j,k) != coords:
                    if cube[i][j][k] == '#':
                        active += 1
    return active 

def updateCube(cube, changelist):
    for coords in changelist:
        x, y, z = [n for n in coords]
        if cube[x][y][z] == '#':
            cube[x][y][z] = '.'
        else:
            cube[x][y][z] = '#'

def countActive(cube):
    count = 0
    for x in cube:
        for y in x:
            for z in y:
                if z == '#':
                    count += 1
    return count

def part1():
    cube = initializeCube()
    changelist = []
    for i in range(6):
        for x in range(-CUBE_SIZE, CUBE_SIZE+1):
            for y in range(-CUBE_SIZE, CUBE_SIZE+1):
                for z in range(-CUBE_SIZE, CUBE_SIZE+1):
                    active = neighbors(cube, (x,y,z))
                    if (cube[x][y][z] == '#' and active not in range(2,4)) or \
                    (cube[x][y][z] == '.' and active == 3):
                        changelist.append((x,y,z))
        updateCube(cube, changelist)
    
    print(countActive(cube))


def part2(input):
    bar = 'foo'
    
def main():
    part1()
    #part2()

main()
