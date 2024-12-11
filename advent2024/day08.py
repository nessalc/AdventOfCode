# Advent of Code
# Day 7

# Read Input
import numpy as np
import itertools
import time
from datetime import timedelta
from fractions import Fraction
from dataclasses import dataclass

def read_input(test:bool=False,filename:str='day08.txt'):
    if test:
        lines="""............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
    else:
        with open(filename) as fp:
            lines=fp.read()
    antenna_map=np.array([list(x) for x in lines.split('\n')[:-1]])
    return antenna_map

def calc_antinodes_part_1(point_a,point_b):
    distance=point_a-point_b
    return [point_a+distance,
            point_b-distance]

def calc_antinodes_part_2(point_a,point_b,count=50):
    distance=point_a-point_b
    retval=[]
    for i in range(-count,count):
        retval.append(point_a+i*distance)
    return retval

@dataclass
class Coords:
    x:float
    y:float
    def __init__(self,x,y):
        try:
            self.x=x.item()
            self.y=y.item()
        except AttributeError:
            self.x=x
            self.y=y
    def __add__(self,b):
        return Coords(self.x+b.x,
                      self.y+b.y)
    def __sub__(self,b):
        return Coords(self.x-b.x,
                      self.y-b.y)
    def __mul__(self,other):
        if type(other) in [int,float]:
            return Coords(other*self.x,
                          other*self.y)
        else:
            return NotImplementedError
    __rmul__=__mul__
    def reduce(self):
        temp=Fraction(self.x,self.y)
        self.x,self.y=temp.numerator,temp.denominator
    def __neg__(self):
        return -1*self
    def in_bounds(self,shape,allow_negative=False):
        if not allow_negative:
            low_x,low_y=0,0
        else:
            low_x,low_y=-shape[1]+1,-shape[0]+1
        return low_x<=self.x<shape[1] and \
               low_y<=self.y<shape[0]
    def __eq__(self,b):
        return b.x==self.x and b.y==self.y
    def __hash__(self):
        return hash(repr(self))
    def as_tuple(self):
        return self.x,self.y

def pmap(array):
    for row in array:
        print(''.join(row))
    print()

def solution(test=False,count=None):
    part1,part2=0,0
    antenna_map=read_input(test)
    unique_frequencies=set(np.ravel(antenna_map))
    unique_frequencies.remove('.')
    fdict=dict()
    antinodes=set()
    outside=0
    shape=antenna_map.shape
    start_time = time.monotonic()
    for freq in unique_frequencies:
        a,b=np.where(antenna_map==freq)
        fdict[freq.item()]=list(map(lambda x:Coords(x[0],x[1]),zip(a,b)))
    for freq,locations in fdict.items():
        for a,b in itertools.combinations(locations,2):
            antinodes|=set(calc_antinodes_part_1(a,b))
    antinodes=list(filter(lambda p:p.in_bounds(shape),antinodes))
    for antinode in antinodes:
        if antenna_map[antinode.as_tuple()]=='.':
            antenna_map[antinode.as_tuple()]='#'
    #pmap(antenna_map)
    part1=len(antinodes)
    part1_time = time.monotonic()
    print(timedelta(seconds=part1_time - start_time))
    antinodes=set()
    for freq,locations in fdict.items():
        for a,b in itertools.combinations(locations,2):
            antinodes|=set(filter(lambda p:p.in_bounds(shape),calc_antinodes_part_2(a,b)))
    for antinode in antinodes:
        if antenna_map[antinode.as_tuple()]=='.':
            antenna_map[antinode.as_tuple()]='#'
    #pmap(antenna_map)
    part2=len(antinodes)
    part2_time = time.monotonic()
    print(timedelta(seconds=part2_time - part1_time))    
    return part1,part2

if __name__=='__main__':
    part1,part2=solution(False)
    print(f'Solution to Part 1: {part1}\n'
          f'Solution to Part 2: {part2}\n')
