#Advent of Code 2017
#Day 17: Spinlock

from collections import deque

def fill_buffer(steps,iterations):
    buffer=deque([0])
    idx=0
    for i in range(1,iterations+1):
        buffer.rotate(-steps)
        buffer.append(i)
        if i%1000000==0:
            print('.',end='')
    return buffer

if __name__=='__main__':
    test17=3
    input17=370
    b=fill_buffer(input17,2017)
    print('Part 1: {}'.format(b[0]))
    b=fill_buffer(input17,50000000)
    print('Part 2: {}'.format(b[b.index(0)+1]))
