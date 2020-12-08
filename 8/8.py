# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re

f = open("8/input.txt", "r+")
data = f.readlines()

code = {}

for n, line in enumerate(data):
    code[n] = line.rstrip()

def part1():
    accum = 0
    line_num = 0
    executed = list()
    repeated = False
    
    while not repeated:
        if line_num in executed:
            print("Accum: " + str(accum))
            print(str(line_num) + ": " + code[line_num])
            repeated = True
            break
        
        executed.append(line_num)
        
        instr = code[line_num].split()[0]
        value = code[line_num].split()[1]
        
        if instr == 'nop':
            line_num += 1
        elif instr == 'jmp':
            line_num += int(value)
        elif instr == 'acc':
            accum += int(value)
            line_num += 1
    print(accum)
            
def part2():
    edit_line = 0
    
    while edit_line < 640:
        executed = list()
        repeated = False
        loop_lim = 0
        line_num = 0
        accum = 0
        
        while not repeated and loop_lim < 640:
            if line_num in executed or line_num > 640:
                if line_num > 640:
                    print("EoC reached")
                    print("Accum: " + str(accum))
                    print(str(line_num) + ": " + code[line_num])
                repeated = True
                break
            
            executed.append(line_num)
            
            instr = code[line_num].split()[0]
            value = code[line_num].split()[1]
            if line_num == edit_line:
                if instr == 'nop':
                    instr = 'jmp'
                elif instr == 'jmp':
                    instr = 'nop'
            
            if instr == 'nop':
                line_num += 1
            elif instr == 'jmp':
                line_num += int(value)
            elif instr == 'acc':
                accum += int(value)
                line_num += 1
                
        edit_line += 1

#part1()
#part2()
