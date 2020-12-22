# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re
from functools import reduce
from dataclasses import dataclass

reField = re.compile('^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)')

f = open("16/input.txt", "r+")
data = f.readlines()

def getInput():
    input = [line for line in data]
    return input

def part1(input):
    ticket_rules = {}
    valid_tickets = []
    section = 'rules'
    rule_end = 0
    while section == 'rules':
        for i, line in enumerate(input):
            if line == '\n':
                section = 'my ticket'
                rule_end = i
                break
            else:
                tokens = reField.findall(line)
                rule = tokens[0][0]
                ticket_rules[rule] = [int(x) for x in tokens[0][1:]]

    my_ticket = input[rule_end+2]

    error = 0
    for line in input[rule_end+5:]:
        nums = line.split(',')
        valid_ticket = True
        for n in nums:
            n = int(n)
            valid_field = False
            for rule in ticket_rules:
                min1, max1 = ticket_rules[rule][0], ticket_rules[rule][1]
                min2, max2 = ticket_rules[rule][2], ticket_rules[rule][3]
                if min1 <= n <= max1 or min2 <= n <= max2:
                    valid_field = True

            if not valid_field:
                error += n
                valid_ticket = False

        if valid_ticket:
            valid_tickets.append(line)

    valid_tickets.insert(0, my_ticket)

    print("# invalid: " + str(error))
    return(valid_tickets, ticket_rules)


def part2(valid_tickets, ticket_rules):
    assign = {}
    fields_count = len(valid_tickets[0].split(','))
    for i in range(fields_count):
        assign[i] = list()

    for rule in ticket_rules:
        min1, max1 = ticket_rules[rule][0], ticket_rules[rule][1]
        min2, max2 = ticket_rules[rule][2], ticket_rules[rule][3]
        for i in range(fields_count):
            for num, ticket in enumerate(valid_tickets):
                val = int((ticket.split(','))[i])
                if min1 <= val <= max1 or min2 <= val <= max2:
                    if num+1 == len(valid_tickets):
                        assign[i].append(rule)
                else: break

    done = False
    while not done:
        done = True
        for field in assign:
            if len(assign[field]) != 1: done = False
            else: 
                for other in assign:
                    if other is not field:
                        if assign[field][0] in assign[other]:
                            assign[other].remove(assign[field][0])

    departures = [x for x in assign if 'departure' in assign[x][0]]
    answer = reduce(lambda a,b: int(a)*int(b), [valid_tickets[0].split(',')[x] for x in departures])
    print(answer)

def main():
    sample1 = ['class: 1-3 or 5-7',
              'row: 6-11 or 33-44',
              'seat: 13-40 or 45-50',
              '\n',
              'your ticket:',
              '7,1,14',
              '\n',
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
