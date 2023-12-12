import logging
from dataclasses import dataclass
from typing import Callable
from math import gcd
from functools import reduce

logging.basicConfig(filename='day08.log',
                    format='[%(asctime)s] %(message)s', level=logging.INFO)

with open('input08.txt', encoding='utf-8') as fp:
    all_input = fp.read()

example1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

example2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

example3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

desert_map = all_input

instructions, _, *node_list = desert_map.strip().split('\n')


@dataclass
class Node:
    left: str
    right: str


nodes = dict()
for node in node_list:
    nodes[node[0:3]] = Node(node[7:10], node[12:15])

current = 'AAA'
end = 'ZZZ'


def count_steps(current: str, instructions: str, endfn: Callable) -> int:
    steps = 0
    done = False
    steplen = len(instructions)
    while not done:
        direction = instructions[steps % steplen]
        steps += 1
        if direction == 'R':
            current = nodes[current].right
        elif direction == 'L':
            current = nodes[current].left
        done = endfn(current)
    return steps


part1 = count_steps(current, instructions, lambda x: x == 'ZZZ')
print(f'{part1=}')
logging.info(f'{part1=}')

starting_nodes = list(filter(lambda x: x[-1] == 'A', nodes.keys()))
step_count = [count_steps(current, instructions, lambda x: x[-1] == 'Z')
              for current in starting_nodes]
part2 = reduce(lambda a, b: a*b//gcd(a, b), step_count)

print(f'{part2=}')
logging.info(f'{part2=}')
