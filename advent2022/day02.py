def score_1(play):
    # A, X is Rock
    # B, Y is Paper
    # C, Z is Scissors
    # Rock is 1, Paper is 2, Scissors is 3
    # Win is 6, Draw is 3, Lose is 0
    a,b=play
    if a=='A':
        if b=='X':
            return 1+3
        elif b=='Y':
            return 2+6
        elif b=='Z':
            return 3+0
    elif a=='B':
        if b=='X':
            return 1+0
        elif b=='Y':
            return 2+3
        elif b=='Z':
            return 3+6
    elif a=='C':
        if b=='X':
            return 1+6
        elif b=='Y':
            return 2+0
        elif b=='Z':
            return 3+3

def score_2(play):
    # A is Rock
    # B is Paper
    # C is Scissors
    # X is Lose
    # Y is Draw
    # Z is Win
    # Rock is 1, Paper is 2, Scissors is 3
    # Win is 6, Draw is 3, Lose is 0
    a,b=play
    if b=='X': # Lose
        if a=='A':
            return 0+3
        elif a=='B':
            return 0+1
        elif a=='C':
            return 0+2
    elif b=='Y': # Draw
        if a=='A':
            return 3+1
        elif a=='B':
            return 3+2
        elif a=='C':
            return 3+3
    elif b=='Z': # Win
        if a=='A':
            return 6+2
        elif a=='B':
            return 6+3
        elif a=='C':
            return 6+1
        

with open('input02.txt') as f:
    strategy_guide=[play.strip() for play in f.readlines()]

part1=sum(map(score_1,map(str.split,strategy_guide)))
part2=sum(map(score_2,map(str.split,strategy_guide)))

print(f'Part 1: {part1}\nPart 2: {part2}')
