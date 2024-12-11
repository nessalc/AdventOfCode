# Advent of Code
# Day 7

# Read Input
import itertools
import time
from datetime import timedelta

def read_input(test:bool=False,filename:str='day07.txt'):
    if test:
        lines="""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
    else:
        with open(filename) as fp:
            lines=fp.read()
    calibration_equations=[]
    for line in lines.split('\n')[:-1]:
        try:
            a,b=line.strip().split(':')
            calibration_equations.append(
                (int(a),
                 list(map(
                     lambda x:x.strip(),
                     b.strip().split(' ')))))
        except ValueError:
            print(line)
            print(a)
            print(b.split(' '))
            raise
    return calibration_equations

def round_robin(*iterables):
    "Visit input iterables in a cycle until each is exhausted."
    # roundrobin('ABC', 'D', 'EF') → A D E B F C
    # Algorithm credited to George Sakkis
    iterators = map(iter, iterables)
    for num_active in range(len(iterables), 0, -1):
        iterators = itertools.cycle(itertools.islice(iterators, num_active))
        yield from map(next, iterators)

def left_to_right(operands,operator_set):
    result,*rest=operands
    for idx,operator in enumerate(operator_set):
        match(operator):
            case '+':
                result+=rest[idx]
            case '*':
                result*=rest[idx]
            case '‖':
                result=int(str(result)+str(rest[idx]))
    return result

def solution(test=False,count=None):
    part1,part2=0,0
    part1_operators='+*'
    part2_operators='+*‖'
    calibration_equations=read_input(test)
    start_time = time.monotonic()
    for result,operands in calibration_equations:
        operator_count=len(operands)-1
        for operator_set in itertools.product(part1_operators,repeat=operator_count):
            eqn=''.join(round_robin(operands,operator_set))
            eval_result=left_to_right(map(int,operands),operator_set)
            if result==eval_result:
                part1+=result
                break
    part1_time = time.monotonic()
    print(timedelta(seconds=part1_time - start_time))
    for result,operands in calibration_equations:
        operator_count=len(operands)-1
        for operator_set in itertools.product(part2_operators,repeat=operator_count):
            eqn=''.join(round_robin(operands,operator_set))
            eval_result=left_to_right(map(int,operands),operator_set)
            if result==eval_result:
                part2+=result
                break
    part2_time = time.monotonic()
    print(timedelta(seconds=part2_time - part1_time))
    return part1,part2

if __name__=='__main__':
    part1,part2=solution()
    print(f'Solution to Part 1: {part1}\n'
          f'Solution to Part 2: {part2}\n')
