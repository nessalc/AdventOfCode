#Advent of Code 2017
#Day 12: Digital Plumber

import re

def trace(pid,program_list):
    path=set(program_list[pid])
    keep_going=True
    while keep_going:
        l=len(path)
        tl=list(path)
        for i in tl:
            for j in program_list[i]:
                path.add(j)
        if len(path)==l:
            keep_going=False
    return path

if __name__=='__main__':
    programs=[]
    for p in open('input12.txt').readlines():
        programs.append(list(map(int,re.sub('\d+\s<\->\s','',p.strip()).split(','))))
    #programs=[[2], [1], [0, 3, 4], [2, 4], [2, 3, 6], [6], [4, 5]]
    print('Part 1: {} programs in the group containing id 0'.format(len(trace(0,programs))))
    count=0
    bigset=set(range(len(programs)))
    while len(bigset):
        bigset-=trace(min(bigset),programs)
        count+=1
    print('Part 2: {} sets'.format(count))
