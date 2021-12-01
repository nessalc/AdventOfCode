import copy

board=list(map(lambda x:[c for c in x.strip()],open('day11.txt').readlines()))

def get_adjacent_only(row,col):
    adjacent=[(row-1,col-1),
              (row-1,col),
              (row-1,col+1),
              (row,col-1),
              (row,col+1),
              (row+1,col-1),
              (row+1,col),
              (row+1,col+1)]
    return list(filter(lambda x:0<=x[0]<len(board) and 0<=x[1]<len(board[0]),adjacent))

def find_seat(row,col,direction,search_distance=1):
    row+=direction[0]
    col+=direction[1]
    distance=1
    while 0<=row<len(board) and 0<=col<len(board[0]) and distance<search_distance:
        if floor(row,col):
            row+=direction[0]
            col+=direction[1]
            distance+=1
        else:
            break
    if 0<=row<len(board) and 0<=col<len(board[0]):
        return row,col
    return None

def get_adjacent(row,col,distance=1):
    if distance==1:
        return get_adjacent_only(row,col)
    if distance is None:
        distance=2**10
    adjacent=[]
    #North
    adjacent.append(find_seat(row,col,(-1,0),distance))
    #Northeast
    adjacent.append(find_seat(row,col,(-1,1),distance))
    #East
    adjacent.append(find_seat(row,col,(0,1),distance))
    #Southeast
    adjacent.append(find_seat(row,col,(1,1),distance))
    #South
    adjacent.append(find_seat(row,col,(1,0),distance))
    #Southwest
    adjacent.append(find_seat(row,col,(1,-1),distance))
    #West
    adjacent.append(find_seat(row,col,(0,-1),distance))
    #Northwest
    adjacent.append(find_seat(row,col,(-1,-1),distance))
    adjacent=list(filter(lambda x:x is not None,adjacent))
    return adjacent

def occupied(row,col):
    try:
        if board[row][col]=='#':
            return True
        return False
    except IndexError:
        print(row,col)
        raise

def floor(row,col):
    if board[row][col]=='.':
        return True
    return False

def empty_seat(row,col):
    if board[row][col]=='L':
        return True
    return False

def count_adjacent_occupied(row,col,visibility=False):
    return sum([occupied(*seat) for seat in get_adjacent(row,col,distance=(None if visibility else 1))])

def print_board(board):
    for r in board:
        print(''.join(r))
    print('-'*len(board[0]))

def iterate_board(board,visibility=False):
    new_board=copy.deepcopy(board)
    for r in range(len(board)):
        for c in range(len(board[0])):
            count=count_adjacent_occupied(r,c,visibility)
            if empty_seat(r,c) and count==0:
                new_board[r][c]='#'
            elif occupied(r,c) and count>=(5 if visibility else 4):
                new_board[r][c]='L'
    return new_board

def count_occupied(board):
    return ''.join([''.join(board[r]) for r in range(len(board))]).count('#')

def reset_board(board):
    new_board=copy.deepcopy(board)
    for r in range(len(board)):
        for c in range(len(board[0])):
            if not floor(r,c):
                new_board[r][c]='L'
    return new_board

count=0
prev=None
while prev!=board:
    count+=1
    prev,board=board,iterate_board(board)
    #print_board(board)
print(f'{count-1} iterations, {count_occupied(board)} seats occupied')

board=reset_board(board)

count=0
prev=None
while prev!=board:
    count+=1
    prev,board=board,iterate_board(board,True)
    #print_board(board)
print(f'{count-1} iterations, {count_occupied(board)} seats occupied')
