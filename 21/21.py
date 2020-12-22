# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

import re
from dataclasses import dataclass

f = open("21/input.txt", "r+")
data = f.readlines()

reAllergens = re.compile('\(contains (.*)\)')

@dataclass
class IngList():
    ingredients: list
    contains: list

def getInput():
    input = list()
    sample = ['mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
             'trh fvjkl sbzzf mxmxvkd (contains dairy)',
             'sqjhc fvjkl (contains soy)',
             'sqjhc mxmxvkd sbzzf (contains fish)']
    for line in data:
        input.append(line.rstrip())
    return input 

def part1():
    labels = getInput()
    all_foods = []
    all_allergens = {}
    for item in labels:
        ingredients = item[:item.index('(')-1]
        ingredients = ingredients.split()
        contains = [x for x in reAllergens.findall(item)[0].split(', ')]
        for el in contains:
            if el not in all_allergens:
                all_allergens[el] = list()
        temp = IngList(ingredients, contains)
        all_foods.append(temp)

    for allergen in all_allergens:
        common_ing = []
        for food in all_foods:
            if allergen in food.contains:
                if not common_ing:
                    common_ing.extend(food.ingredients)
                else:
                    remove = []
                    for ing in common_ing:
                        if ing not in food.ingredients:
                            remove.append(ing)
                    common_ing = [x for x in common_ing if x not in remove]
        all_allergens[allergen] = common_ing

    done = False
    while not done:
        done = True
        for allergen in all_allergens:
            if len(all_allergens[allergen]) > 1:
                done = False
            if len(all_allergens[allergen]) == 1:
                certainty = all_allergens[allergen][0]
                for other in all_allergens:
                    if allergen is not other:
                        if certainty in all_allergens[other]:
                            all_allergens[other].remove(certainty)


    verified = [x[0] for x in all_allergens.values()]
    not_allergens = 0
    for food in all_foods:
        for ing in food.ingredients:
            if ing not in verified:
                not_allergens += 1

    in_order = sorted(all_allergens.keys())
    for a in in_order:
        print(all_allergens[a][0], end = ',')


def part2():
    bar = 'foo'
    
def main():
    part1()
    #part2()

main()
