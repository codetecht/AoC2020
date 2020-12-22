# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re
import math
import functools

CUBE_SIZE = 10 
DIMENSION = range(-CUBE_SIZE, CUBE_SIZE+1)

f = open("17/input.txt", "r+")
data = f.readlines()

def getInput():
    input = list()
    for line in data:
        input.append(line.rstrip())

    sample = ['.#.', '..#', '###']
    return input #sample 

def initializeCube():
    input = getInput()
    cube = [[['.' for k in DIMENSION] 
                  for j in DIMENSION] 
                  for i in DIMENSION]
    for y, line in enumerate(input):
        for x, char in enumerate(line):
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
        if cube[x][y][z] == '#': cube[x][y][z] = '.'
        else: cube[x][y][z] = '#'

def countActive(cube):
    count = 0
    for x in cube:
        for y in x:
            for z in y:
                if z == '#':
                    count += 1
    return count

def printCube(cube, depth):
    for y in DIMENSION:
        print(f'{y:3} ', end = '')
        for x in DIMENSION:
            print(cube[x][y][depth], end = '')
        print()
    print()
        
def initialize4DCube():
    input = getInput()
    cube = [[[['.' for l in DIMENSION]
                   for k in DIMENSION] 
                   for j in DIMENSION] 
                   for i in DIMENSION]
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            cube[x][y][0][0] = char
    return cube

def neighbors4D(cube, coords):
    x, y, z, w = [n for n in coords]
    active = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    if (i,j,k,l) != coords:
                        if cube[i][j][k][l] == '#':
                            active += 1
    return active


def update4DCube(cube, changelist):
    for coords in changelist:
        x, y, z, w = [n for n in coords]
        if cube[x][y][z][w] == '#': cube[x][y][z][w] = '.'
        else: cube[x][y][z][w] = '#'

def countActive4D(cube):
    count = 0
    for x in cube:
        for y in x:
            for z in y:
                for w in z:
                    if w == '#':
                        count += 1
    return count

def part1():
    cube = initializeCube()
    changelist = []

    for i in range(6):
        for x in DIMENSION:
            for y in DIMENSION:
                for z in DIMENSION:
                    active_count = neighbors(cube, (x,y,z))
                    if (cube[x][y][z] == '#' and active_count not in range(2,4)) or \
                       (cube[x][y][z] == '.' and active_count == 3):
                        changelist.append((x,y,z))
        updateCube(cube, changelist)
        changelist = []
    
    print(countActive(cube))

def part2():
    cube = initialize4DCube()
    changelist = []

    for i in range(6):
        for x in DIMENSION:
            for y in DIMENSION:
                for z in DIMENSION:
                    for w in DIMENSION:
                        active_count = neighbors4D(cube, (x,y,z,w))
                        if (cube[x][y][z][w] == '#' and active_count not in range(2,4)) or \
                           (cube[x][y][z][w] == '.' and active_count == 3):
                            changelist.append((x,y,z,w))
        update4DCube(cube, changelist)
        changelist = []

    print(countActive4D(cube))
    
                    
    
def main():
    #part1()
    part2()

main()
