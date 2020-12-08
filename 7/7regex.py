# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re

f = open("7/input.txt", "r+")
data = f.readlines()

reContainer = re.compile('^([\w ]*) bags contain')
reInside = re.compile('(\d+) ([\w ]*) bag')

bag_dict = {}

# For debugging
test_counter = 0

for line in data:
    if line != "\n":
        container = reContainer.findall(line)[0]
        bag_dict[container] = {}
        inside = reInside.findall(line)
        for bag in inside:
            bag_dict[container][bag[1]] = bag[0]
    







    # This part limits runtime for debugging
    #if test_counter > 3:
    #    break
    #else:
    #    test_counter += 1
        
def carries_gold(color):
    if 'shiny gold' in bag_dict[color]:
        return True
    else:
        for bag in bag_dict[color]:
            if carries_gold(bag):
                return True
    return False

def bags_inside(color):
    sum = 0
    for bag in bag_dict[color]:
        n = int(bag_dict[color][bag])
        sum += n*int(bags_inside(bag)) + n
        
    return sum

def part1():
    count = 0
    for bag in bag_dict:
        if carries_gold(bag):
            count += 1
    print(count)
    
def part2():
    print(bags_inside('shiny gold'))
    
    
    
    
part1()
part2()
        