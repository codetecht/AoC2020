# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

'''
The ship and waypoint are represented as dictionaries with various details as
    key-value pairs.

For Part 1, the facing of the ship is reperesented as a digit as follows:
    0: East             3           
    1. South            |           Turn left by x: subtract x/90, %4
    2: West         2 -- -- 0
    3: North            |           Turn right by x: add x/90, %4
                        1
'''

# Prep work
f = open("12/input.txt", "r+")
data = f.readlines()

def takeAction(ship, action, amount):
    if action == 'L':
        ship['facing'] = (ship['facing'] - (int(amount)//90))%4
    elif action == 'R':
        ship['facing'] = (ship['facing'] + (int(amount)//90))%4
    elif action == 'F':
        if ship['facing'] == 0:         # East
            ship['EW'] += int(amount)
        if ship['facing'] == 1:         # South
            ship['NS'] -= int(amount)
        if ship['facing'] == 2:         # West
            ship['EW'] -= int(amount)
        if ship['facing'] == 3:         # North
            ship['NS'] += int(amount)
    elif action == 'E':                 # 0
        ship['EW'] += int(amount)
    elif action == 'S':                 # 1
        ship['NS'] -= int(amount)
    elif action == 'W':                 # 2
        ship['EW'] -= int(amount)
    elif action == 'N':                 # 3
        ship['NS'] += int(amount)

def takeAction2(ship, wp, action, amount):
    # Make a reference copy to change values which depend on each other
    ref_wp = wp.copy()

    # Rotation transformation equations:
    #     R90 or L270 : dy = -dx
    #                   dx =  dy
    #     R180 or L180: dy = -dy
    #                   dx = -dx
    #     R270 or L90 : dy =  dx
    #                   dx = -dy
    if action == 'L' or action == 'R':
        if amount == '180':
            wp['NS'] = -ref_wp['NS']
            wp['EW'] = -ref_wp['EW']
        elif action + amount == 'R90' or action + amount == 'L270':
            wp['NS'] = -ref_wp['EW']
            wp['EW'] = ref_wp['NS']
        elif action + amount == 'R270' or action + amount == 'L90':
            wp['NS'] = ref_wp['EW']
            wp['EW'] = -ref_wp['NS']
    elif action == 'F':
        for i in range(int(amount)):
            ship['NS'] += wp['NS']
            ship['EW'] += wp['EW']
    elif action == 'E':
        wp['EW'] += int(amount)
    elif action == 'S':
        wp['NS'] -= int(amount)
    elif action == 'W':
        wp['EW'] -= int(amount)
    elif action == 'N':
        wp['NS'] += int(amount)

def part1():
    ship = {}
    ship['facing'] = 0
    ship['NS'] = 0
    ship['EW'] = 0

    for line in data:
        action = line[0]
        amount = line[1:]
        takeAction(ship, action, amount)

    return abs(int(ship['EW'])) + abs(int(ship['NS']))

def part2():
    ship = {}
    ship['NS'] = 0 
    ship['EW'] = 0
    
    wp = {}
    wp['NS'] = 1 
    wp['EW'] = 10 
    for line in data:
        action = line[0]
        amount = line[1:].rstrip()
        takeAction2(ship, wp, action, amount)
    
    return abs(int(ship['EW'])) + abs(int(ship['NS']))
    
def main():
    print(part1())
    print(part2())

main()
