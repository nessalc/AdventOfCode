#Advent of Code 2017
#Day 16: Permutation Promenade

def dance(dancers,move):
    if move[0]=='s':
        param=int(move[1:])
        return dancers[-param:]+dancers[:-param]
    elif move[0]=='x':
        pos1,pos2=tuple(map(int,move[1:].split('/')))
        dancers[pos1],dancers[pos2]=dancers[pos2],dancers[pos1]
        return dancers
    elif move[0]=='p':
        pos1,pos2=tuple(map(lambda x:dancers.index(x),move[1:].split('/')))
        dancers[pos1],dancers[pos2]=dancers[pos2],dancers[pos1]
        return dancers
    return dancers

if __name__=='__main__':
    move_list=open('input16.txt').readline().strip().split(',')
    dancers=list('abcdefghijklmnop')
    repetitions=1000000000
    s=[]
    for i in range(repetitions):
        state=''.join(dancers)
        if state in s:
            print('Part 2, Dance order: {}'.format(s[repetitions%i]))
            break
        if i==1:
            print('Part 1, Dance order: {}'.format(''.join(dancers)))
        s.append(state)
        for move in move_list:
            dancers=dance(dancers,move)
