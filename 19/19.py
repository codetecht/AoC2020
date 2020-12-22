# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re
import math
import functools

reNums = re.compile('(\d+ \d+)')

f = open("19/input.txt", "r+")
data = f.readlines()

def getInput():
    raw_rules = []
    nonterminals = {}
    terminals = {}
    code = []

    for line in data:
        if line != '\n':
            if line[0] == 'a' or line[0] == 'b':
                code.append(line.rstrip())
            else:
                raw_rules.append(line.rstrip())

    for line in raw_rules:
        id, reqs = line.split(':')
        reqs = reqs.lstrip()
        if reqs[0] == '\"':
            terminals[id] = [a for a in reqs if a.isalpha()][0]
        else:
            if '|' in reqs: nonterminals[id] = reNums.findall(reqs)
            else: nonterminals[id] = reqs



    return terminals, nonterminals, code


    return input

def build(terms, nonterms):
    foo = 'bar'

def part1():
    terminals, nonterminals, code = getInput()
    string_set = build(terminals, nonterminals)
    #for line in code:




    
def part2():
    bar = 'foo'
    
def main():
    part1()
    #part2()

main()