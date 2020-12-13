# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re
import math
from functools import reduce
# Do this again with Regex

f = open("13/input.txt", "r+")
data = f.readlines()

def getInput():
    input = list()
    for line in data:
        input.append(line.rstrip())
    return input

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a,b: a*b, n)
    for n_i, a_i in zip(n,a):
        p = prod/n_i 
        sum += a_i * mul_inv(p,n_i)*p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def part1(input):
    time_start = int(input[0])
    time_end = int(input[0])
    buses = [int(x) for x in input[1].split(',') if x.isdigit()]
    
    bus_found = False
    while not bus_found:
        for busID in buses:
            if time_end%busID == 0:
                bus_found = True
                print(busID)
                print((time_end - time_start) * busID)
                continue
        time_end += 1

def part2(input):
    n, a = [], []
    buses = [x for x in input[1].split(',')]
    for busID in sorted(buses):
        if busID.isdigit():
            n_val = int(busID)
            a_val = -1 * int(buses.index(busID))
            while a_val < 0:
                a_val += n_val
            n.append(n_val)
            a.append(a_val)

    print(n)
    print(a)
    #print(chinese_remainder(n,a))

    

    
def main():
    #part1(getInput())
    part2(getInput())

main()
