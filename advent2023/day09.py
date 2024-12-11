from itertools import pairwise, accumulate
from operator import add
from typing import Iterable

with open('input09.txt', encoding='utf-8') as fp:
    all_input = fp.read()

example = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def condense(sequence: Iterable[int]) -> list[int]:
    return [b-a for a, b in pairwise(sequence)]


def extrapolate(sequence_list) -> int:
    new_elements = list(accumulate(
        map(lambda x: x[-1], sequence_list[::-1]), add))
    return new_elements[-1]


def backstrapolate(sequence_list) -> int:
    prev = 0
    for next in sequence_list[::-1]:
        value = next[0]-prev
        prev = value
    return prev


oasis_data = all_input

part1 = 0
part2 = 0
for history in oasis_data.strip().split('\n'):
    c = list(map(int, history.split()))
    sequence_list = [c]
    while any(c):
        c = condense(c)
        sequence_list.append(c)
    part1 += extrapolate(sequence_list)
    part2 += backstrapolate(sequence_list)

print(f'{part1=}')
print(f'{part2=}')
