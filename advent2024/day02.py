# Advent of Code
# Day 2

# Read Input
import re
import itertools

def read_input(filename:str='day02.txt')->list[list[int]]:
    with open(filename) as fp:
        lines=fp.readlines()
    retval=[]
    for l in lines:
        try:
            retval.append([int(x) for x in re.split('\s+',l.strip())])
        except ValueError:
            print(l)
            raise
    return retval

def remove_n(report:list[int],count=1)->list[list[int]]:
    return [report[:idx]+report[idx+1:] for idx in range(len(report))]

def safe(report:list[int],dampener_level=0)->bool:
    testlist=[p[1]-p[0] for p in itertools.pairwise(report)]
    safe=(len(list(filter(lambda x:0<x<4,testlist))) == len(testlist) or \
          len(list(filter(lambda x:-4<x<0,testlist))) == len(testlist))
    if dampener_level>0:
        for testreport in remove_n(report,1):
            testlist=[p[1]-p[0] for p in itertools.pairwise(testreport)]
            safe|=(len(list(filter(lambda x:0<x<4,testlist))) == len(testlist) or \
                   len(list(filter(lambda x:-4<x<0,testlist))) == len(testlist))
            if safe:
                return safe
    return safe

def solution():
    reports=read_input()
    part1=len(list(filter(safe,reports)))
    part2=len(list(filter(lambda x:safe(x,1),reports)))
    print(f'Part 1 Solution: {part1}\n'
          f'Part 2 Solution: {part2}\n')
