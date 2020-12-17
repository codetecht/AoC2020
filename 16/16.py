# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re
import math
import functools
from dataclasses import dataclass

reField = re.compile('^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)')

f = open("16/input.txt", "r+")
data = f.readlines()

def getInput():
    input = list()
    for line in data:
        input.append(line.rstrip())
    return input

def part1(input):
    ticket_rules = {}
    valid_tickets = []
    section = 'rules'
    rule_end = 0
    while section == 'rules':
        for i, line in enumerate(input):
            if line == '':
                section = 'my ticket'
                rule_end = i
                break
            else:
                tokens = reField.findall(line)
                rule = tokens[0][0]
                ticket_rules[rule] = tokens[0][1:]

    my_ticket = input[rule_end+2]

    invalid = 0
    for line in input[rule_end+5:]:
        nums = line.split(',')
        for n in nums:
            valid = False
            n = int(n)
            for rule in ticket_rules:
                min1, max1 = int(ticket_rules[rule][0]), int(ticket_rules[rule][1])
                min2, max2 = int(ticket_rules[rule][2]), int(ticket_rules[rule][3])
                if min1 <= n <= max1 or min2 <= n <= max2:
                    valid = True
                    if line not in valid_tickets:
                        valid_tickets.append(line)
                    break
            if not valid:
                invalid += n

    valid_tickets.insert(0, my_ticket)

    print("# invalid: " + str(invalid))
    return(valid_tickets, ticket_rules)


def part2(valid_tickets, ticket_rules):
    bad_fields = {}
    for rule in ticket_rules:
        bad_fields[rule] = list(range(1, len(ticket_rules)+1))
    
    for i, num in enumerate(len(valid_tickets)):
        

    '''
    for ticket in valid_tickets[:3]:
        for i, n in enumerate(ticket.split(',')):
            n = int(n)
            for rule in ticket_rules:
                min1, max1 = int(ticket_rules[rule][0]), int(ticket_rules[rule][1])
                min2, max2 = int(ticket_rules[rule][2]), int(ticket_rules[rule][3])
                if not (min1 <= n <= max1 or min2 <= n <= max2):
                    print(rule + " invalid for " + str(i+1) + " because " + str(n) + " not between " + str(min1) + "-" + str(max1) + " or " + str(min2) + "-" + str(max2))
                    if i+1 in bad_fields[rule]:
                        bad_fields[rule].remove(i+1)

    '''

    for i, rule in enumerate(bad_fields):
        print(rule + ': ' + str(bad_fields[rule]))



def main():
    sample1 = ['class: 1-3 or 5-7',
              'row: 6-11 or 33-44',
              'seat: 13-40 or 45-50',
              '',
              'your ticket:',
              '7,1,14',
              '',
              'nearby tickets:',
              '7,3,47',
              '40,4,50',
              '55,2,20',
              '38,6,12']

    sample2 = ['class: 0-1 or 4-19',
               'row: 0-5 or 8-19',
               'seat: 0-13 or 16-19',                
               '',
               'your ticket:',
               '11,12,13',
               '',
               'nearby tickets:',
               '3,9,18',
               '15,1,5',
               '5,14,9']
    
    

    valid_tickets, ticket_rules = part1(getInput())
    part2(valid_tickets, ticket_rules)

main()
