# day06.py

import collections

with open('input06.txt') as fp:
    lanternfish: list[int] = list(map(int, fp.readline().strip().split(',')))

print(f'After {0:3d} days ({len(lanternfish)}): {lanternfish}')
fish_factory = collections.Counter(lanternfish)
for i in range(9):
    if i not in fish_factory.keys():
        fish_factory[i] = 0
a, ff = zip(*sorted(fish_factory.items()))
ff = list(ff)
del(a)


def rotate_left(input_list: list, count: int) -> list:
    return input_list[count:]+input_list[:count]


for i in range(1, 302):
    ff = rotate_left(ff, 1)
    ff[6] += ff[8]
    print(f'Day {i:3d}: {sum(ff)} lanternfish')
