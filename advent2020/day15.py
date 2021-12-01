from collections.abc import Generator

starting=[15,5,1,4,7,0]

def memory_game_1():
    history=[]
    while True:
        try:
            i=(yield history[0])
        except IndexError:
            i=(yield None)
        if i is not None:
            history.insert(0,i)
        else:
            try:
                j=history.index(history[0],1)
                history.insert(0,j)
            except ValueError:
                history.insert(0,0)

def memory_game_2():
    history={}
    latest_num=None
    turn=0
    while True:
        turn+=1
        i=(yield latest_num)
        if i is not None:
            if latest_num is not None:
                history[latest_num]=turn-1
            latest_num=i
        else:
            if latest_num in history:
                history[latest_num],latest_num=turn-1,turn-history[latest_num]-1
            else:
                history[latest_num]=turn-1
                latest_num=0

mg1=memory_game_1
mg2=memory_game_2

def prime(game,starting_list):
    g=game
    k=0
    g.send(None)
    for i in starting_list:
        k=g.send(i)
    return k

def get_nth_term(game,starting_list,n):
    g=game()
    k=prime(g,starting_list)
    for i in range(n-len(starting_list)):
        k=next(g)
    return k

print(get_nth_term(memory_game_1,starting,2020))
print(get_nth_term(memory_game_2,starting,2020))
print(get_nth_term(memory_game_2,starting,30000000))
