# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re
from functools import partial
from functools import reduce
from itertools import product 

# File IO
f = open("14/input.txt", "r+")
data = f.readlines()

# ReGex to extract numeric values from a string
reMem = re.compile('(\d+)')

# Convert a binary string to its base-10 value
# throws: ValueError if digits in string are not 0 or 1
#         TypeError if not supplied with string arg
binToDec = partial(int, base=2)

def getInput():
    input = list()
    for line in data:
        input.append(line.rstrip())
    return input

def part1(input):
    memory = {}
    mask = ''
    for line in input:
        line = line.split()
        if line[0] == 'mask':
            mask = line[2]
        else:
            # Extract the address to which we write
            addr = reMem.findall(line[0])[0]

            # Convert the integer value to be written to its binary equivalent
            # as a list for mutability
            bin_val = list(bin(int(line[2]))[2:])

            # Pad the length of the value such that its length equals the mask
            while len(bin_val) < len(mask):
                bin_val.insert(0, '0')

            # Apply the mask to the value:
            #     X: Bit unchanged
            #   0|1: Change value's bit to 0|1
            for i, bit in enumerate(mask):
                if bit != 'X':
                    bin_val[i] = bit

            memory[addr] = binToDec(''.join(bin_val))

    print(reduce(lambda x,y: x+y, memory.values()))

    
def part2(input):
    memory = {}
    mask = ''

    for line in input:
        line = line.split()
        if line[0] == 'mask':
            mask = line[2]
        else:
            # Extract the address to which we apply the mask
            addr = reMem.findall(line[0])[0]
            qbits = []

            # Convert the address to binary as a list for mutability
            bin_addr = list(bin(int(addr))[2:])
            value = int(line[2])
            
            # Pad the length of the address so that its length equals the mask
            while len(bin_addr) < len(mask):
                bin_addr.insert(0, '0')

            # Apply the mask to the address:
            #     0: Bit unchanged
            #   1|X: Change value's bit to 1|X
            for i, bit in enumerate(mask):
                if bit != '0':
                    bin_addr[i] = bit
                    if bit == 'X':
                        qbits.append(i)

            # Generate a list of all possible binary strings the same length
            # as the number of X's in bin_addr
            combos = list(product([0,1], repeat=len(qbits)))

            # Go through each combination, replacing the X's with each combo
            # of binary strings, thus generating all possible addresses
            for combo in combos:
                for i in range(len(combo)):
                    bin_addr[qbits[i]] = str(combo[i])
                new_addr = binToDec(''.join(bin_addr))
                memory[new_addr] = value

    print(reduce(lambda x,y: x+y, memory.values()))
        
def main():
    part1(getInput())
    part2(getInput())

main()
