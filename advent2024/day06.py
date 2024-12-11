# Advent of Code
# Day 6

# Read Input
import numpy as np
import time
from datetime import timedelta

def read_input(test=False,filename:str='day06.txt'):
    if test:
        lines="""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
    else:
        with open(filename) as fp:
            lines=fp.read()
    return np.array([list(x) for x in lines.split('\n')[:-1]])

def move_to_next_location(lab_map,location,direction,obstacle=None):
    match direction:
        case '^':
            test=location[0]-1,location[1]
            if lab_map[test]=='#' or test==obstacle:
                direction='>'
                test=location
            else:
                lab_map[location]='X'
                lab_map[test]='^'
        case '>':
            test=location[0],location[1]+1
            if lab_map[test]=='#' or test==obstacle:
                direction='v'
                test=location
            else:
                lab_map[location]='X'
                lab_map[test]='>'
        case 'v':
            test=location[0]+1,location[1]
            if lab_map[test]=='#' or test==obstacle:
                direction='<'
                test=location
            else:
                lab_map[location]='X'
                lab_map[test]='v'
        case '<':
            test=location[0],location[1]-1
            if lab_map[test]=='#' or test==obstacle:
                direction='^'
                test=location
            else:
                lab_map[location]='X'
                lab_map[test]='<'
    return lab_map,test,direction

def follow_full_path(lab_map,location,direction,limit=200,obstacle=None):
    turns=0
    locations=set()
    while turns<=limit and location[0]>0 and location[1]>0:
        try:
            prev_direction=direction
            lab_map,location,direction=move_to_next_location(lab_map,location,direction,obstacle)
            if prev_direction!=direction:
                turns+=1
        except IndexError:
            break
        locations.add(tuple(location))
    return locations,turns

def solution(test=False,count=None):
    global obstacle_locations
    a=read_input(test)
    i,j=np.where(a=='^')
    location=int(i[0]),int(j[0])
    direction='^'
    limit=2000
    options=set()
    part1,part2=0,0
    start_time = time.monotonic()
    locations,_=follow_full_path(a,location,direction,limit)
    part1_time = time.monotonic()
    print(timedelta(seconds=part1_time - start_time))
    for possibility in locations:
        locs,turns=follow_full_path(a,location,direction,limit,possibility)
        if turns>=limit:
            options.add(possibility)
    output=False
    if output:
        with open('output.txt','w') as fp:
            for line in [''.join(x) for x in a]:
                fp.write(line+'\n')
    part2_time = time.monotonic()
    print(timedelta(seconds=part2_time - part1_time))
    part1=len(locations)
    part2=len(options)
    return part1,part2

if __name__=='__main__':
    part1,part2=solution()
    print(f'Solution to Part 1: {part1}\n'
          f'Solution to Part 2: {part2}\n')
