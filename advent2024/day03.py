# Advent of Code
# Day 3

# Read Input
import re
import functools

def read_input(filename:str='day03.txt')->list[list[int]]:
    with open(filename) as fp:
        lines=fp.read()
    return lines

def get_instructions(memory:str,conditionals=False)->list[tuple[int,int]]:
    retval=[]
    enabled=True
    for instruction in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)",memory):
        match instruction.group(0)[:4]:
            case "mul(":
                if enabled:
                    retval.append((int(instruction.group(1)),int(instruction.group(2))))
            case "do()":
                if conditionals:
                    enabled=True
            case "don'":
                if conditionals:
                    enabled=False
    return retval

def solution():
    memory=read_input()
    instructions=get_instructions(memory)
    part1=sum([a*b for a,b in instructions])
    instructions=get_instructions(memory,True)
    part2=sum([a*b for a,b in instructions])
    print(f'Part 1 solution: {part1}\n'
          f'Part 2 solution: {part2}\n')
