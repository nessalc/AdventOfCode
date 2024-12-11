# Advent of Code
# Day 1

# Read Input
import re

def read_input(filename:str='day01.txt')->list[list[int]]:
    with open(filename) as fp:
        lines=fp.readlines()
    retval=[]
    for l in lines:
        l=l.strip()
        try:
            a,b=re.split('\s+',l)
            retval.append([int(a),int(b)])
        except ValueError:
            print(l)
            raise
    return retval

def distance_between_pairs(pair:list[int,int])->int:
    return abs(pair[1]-pair[0])

def similarity_score(item:int,other_list:list[int])->int:
    return item*other_list.count(item)

def solution():
    lista,listb=map(list,zip(*read_input()))
    lista.sort()
    listb.sort()
    part1=sum(map(distance_between_pairs,zip(lista,listb)))
    part2=sum(map(lambda x:similarity_score(x,listb),lista))
    print(f'Part 1 Solution: {part1}\n'
          f'Part 2 Solution: {part2}\n')
