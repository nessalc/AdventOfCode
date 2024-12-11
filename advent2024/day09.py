# Advent of Code
# Day 9

# Read Input
import numpy as np
import itertools
import time
from datetime import timedelta
from fractions import Fraction
from dataclasses import dataclass

def read_input(test:bool=False,filename:str='day09.txt'):
    if test:
        disk_map="""2333133121414131402"""
    else:
        with open(filename) as fp:
            disk_map=fp.readlines()[0].strip()
    return disk_map

def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks."
    # grouper('ABCDEFG', 3, fillvalue='x') → ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') → ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') → ABC DEF
    iterators = [iter(iterable)] * n
    match incomplete:
        case 'fill':
            return itertools.zip_longest(*iterators, fillvalue=fillvalue)
        case 'strict':
            return zip(*iterators, strict=True)
        case 'ignore':
            return zip(*iterators)
        case _:
            raise ValueError('Expected fill, strict, or ignore')

def compress_part_1(expanded):
    compressed=expanded
    index=compressed.find('.')
    while index>=0:
        compressed=compressed[:index]+compressed[-1]+compressed[index+1:-1]
        print(compressed)
        index=compressed.find('.')
    return compressed

def get_checksum(disk_map):
    checksum=0
    for idx,disk_block in enumerate(disk_map):
        if disk_block.isnumeric():
            checksum+=idx*int(disk_block)
    return checksum

def solution(test=False):
    part1,part2=0,0
    disk_map=read_input(test)
    expanded=''
    start_time = time.monotonic()
    for idx,disk_blocks in enumerate(grouper(disk_map,2,fillvalue='0')):
        expanded+=str(idx)*int(disk_blocks[0])
        expanded+='.'*int(disk_blocks[1])
    print(expanded)
    compressed=compress_part_1(expanded)
    checksum=get_checksum(compressed)
    print(checksum)
    part1_time = time.monotonic()
    print(timedelta(seconds=part1_time - start_time))
    
    part2_time = time.monotonic()
    print(timedelta(seconds=part2_time - part1_time))    
    return part1,part2

if __name__=='__main__':
    part1,part2=solution(True)
    print(f'Solution to Part 1: {part1}\n'
          f'Solution to Part 2: {part2}\n')
