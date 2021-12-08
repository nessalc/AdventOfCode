# day04.py

fp = open('input04.txt')

numbers = map(int, fp.readline().split(','))

inputfile = fp.readlines()

boards = []

for i in range(len(inputfile)//6):
    boards.append(inputfile[i*6+1:i*6+6])

for board in boards:
    for i in range(5):
        board[i] = list(map(int, board[i].strip().split()))


def score(board, call):
    score_s = 0
    for i in [x for y in board for x in y]:
        if i != 'X':
            score_s += i
    return score_s*call


def check(board, call):
    for row in board:
        if all([j == 'X' for j in row]):
            s = score(board, call)
            print(f'Bingo H! {s}')
            return s
    for i in range(5):
        if all([board[j][i] == 'X' for j in range(5)]):
            s = score(board, call)
            print(f'Bingo V! {s}')
            return s
    return -1


ignore = set()
for count, call in enumerate(numbers):
    for k, board in enumerate(boards):
        if k not in ignore:
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c == call:
                        board[i][j] = 'X'
                        if check(board, call) >= 0:
                            ignore.add(k)
                        break
                else:
                    continue
                break
