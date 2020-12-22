# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re
import math
import functools

f = open("18/input.txt", "r+")
data = f.readlines()

reAdd = re.compile('(\d+\+\d+)')
reMul = re.compile('(\d+\*\d+)')
reSimp = re.compile('(\(\d+\))')
reDigit = re.compile('(\d+)')

def getInput():
    sample1 = ['1 + 2 * 3 + 4 * 5 + 6']
    sample2 = ['1 + (2 * 3) + (4 * (5 + 6))']
    sample4 = ['5 + (8 * 3 + 9 + 3 * 4 * 3)']
    sample5 = ['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))']
    sample6 = ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']
    input = list()
    for line in data:
        stripped = line.replace(' ', '')
        input.append(stripped)
    return [sample5[0].replace(' ', '')]

def closingParen(expr):
    unmatched = 1
    for n, char in enumerate(expr[1:]):
        if char == '(': unmatched += 1
        elif char == ')': unmatched -= 1
        if unmatched == 0: return n+1

def evaluate(expr):
    lhs, rhs = None, None
    operation = 'sum'
    while expr != '':
        char = expr[0]
        if char == '(':
            end = closingParen(expr)
            char = evaluate(expr[1:end])
            expr = expr[end:]
        if str(char).isdigit():
            if lhs is None: lhs = int(char)
            else: 
                rhs = int(char)
                if operation == 'sum': lhs += rhs
                elif operation == 'mul': lhs *= rhs
        elif char == '+': 
            operation = 'sum'
        elif char == '*': 
            operation = 'mul'
        if len(expr) > 0: expr = expr[1:]
        else: expr = ''
    return(lhs)

def part1(input):
    sum = 0
    for line in input:
        sum += evaluate(line)
    print(sum)

def part2(input):
    foo = 'bar'


def main():
    #part1(getInput())
    part2(getInput())

main()
