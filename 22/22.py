# Copyright 2020 Joseph Kularski
# Workspace for Advent of Code 2020
# Request permission before using or duplicating this code for any purpose

data = [line.rstrip() for line in open('22/input.txt', 'r+')]

def getInput():
    return [int(x) for x in data[1:26]], [int(x) for x in data[28:53]]

'''
Performs Recursive Combat on the input decks. Players take turns drawing cards
    from their own decks. If either player has fewer cards remaining in their
    deck than the value of the card they drew, the round is handled exactly as
    in Part 1. Otherwise, a sub-game is called with the cards remaining in the
    decks to decide the winner of the top-level game (even if their card is 
    lower in value).

args
    p1: player 1's deck of cards
    p2: player 2's deck of cards

returns:
    1 if player 1 won the current game
    2 if player 2 won
'''
def reCom(p1, p2):
    history = set()
    while p1 and p2:
        # Hash the current game scores (n, m) and check history by summing the
        # values of the cards in each deck multiplied by their position on the
        # "stack" of cards: [4, 6, 8] => 4*3 + 6*2 + 8*1
        id1, id2 = 0, 0
        for n, val in enumerate(reversed(p1)):
            id1 += (n+1) * val
        for n, val in enumerate(reversed(p2)):
            id2 += (n+1) * val
        if (id1, id2) in history: return 1
        else:
            history.add((id1, id2))
            a, b = p1.pop(0), p2.pop(0)

            # Check to see if a sub-game needs to be played
            if a > len(p1) or b > len(p2):
                if a > b: p1.extend([a,b])
                else: p2.extend([b,a])
            else:
                winner = reCom(p1[:a], p2[:b])
                if winner == 1: p1.extend([a,b])
                elif winner == 2: p2.extend([b,a])
    
    # Return the integer value of the winning player
    if not p1: return 2
    if not p2: return 1
    

def part2():
    p1, p2 = getInput()
    winner, score = reCom(p1, p2), 0
    if winner == 1:
        print(p1)
        for n, val in enumerate(reversed(p1)):
            score += (n+1) * val
    else: 
        print(p2)
        for n, val in enumerate(reversed(p2)):
            score += (n+1) * val

    print(score)
    
def part1():
    p1, p2 = getInput()
    while p1 and p2:
        a, b = p1.pop(0), p2.pop(0)
        if a > b: p1.extend([a, b])
        else: p2.extend([b, a])

    total = 0 
    for n, val in enumerate(reversed(max(p1, p2))):
        total += (n+1) * val

    return(total)


def main():
    part1()
    part2()

main()
