# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re

def main():
    f = open("7/input.txt", "r+")
    input_lines = f.readlines()
    file_lines = len(input_lines)-1
    width = len(input_lines[0])-1

    color_dict = []
    gold_holders = ["shiny gold"]
    in_gold = ["shiny gold"]
    bags_num = 0
    again = True

    # For debugging
    test_counter = 0

    for line in input_lines:
        if line != "\n":
            tokens = line.split()
            can_contain = ()

            for i in range(len(tokens)//4 - 1):
                can_contain += (tokens[4*(i+1)], 
                                str(tokens[4*(i+1)+1] + " " + tokens[4*(i+1)+2]))

            color_dict.append((str(tokens[0] + " " + tokens[1]), can_contain))

        # This part limits runtime for debugging
        #if test_counter > 600:
        #    break
        #else:
        #    test_counter += 1

    #while again:
    #    again = False
    #    for el in color_dict:
    #        for type in gold_holders:
    #            if type in el[1]:
    #                if el[0] not in gold_holders:
    #                    again = True
    #                    gold_holders.append(el[0])


    bags_num = bagLookup("shiny gold", color_dict)
    print(bags_num)
    

    #while len(in_gold) != 0:
    #    for bag in in_gold:



def bagLookup(color, color_dict):
    bags = []
    curr_bag_contains = ()
    sum = 0
    for n, hue in enumerate(color_dict):
        if hue[0] == color:
            curr_bag_contains = ((color_dict[n])[1])
  
    if len(curr_bag_contains) != 0:
        for i in range(len(curr_bag_contains)//2):
            sum += int(curr_bag_contains[2*i]) * bagLookup(curr_bag_contains[(2*i)+1], color_dict) + int(curr_bag_contains[2*i])

            #bags += (curr_bag_contains[2*i], curr_bag_contains[(2*i)+1])

    return sum
    
    
            

main()
