import logging
from functools import reduce
from operator import __mul__

logging.basicConfig(filename='day06.log',
                    format='[%(asctime)s] %(message)s', level=logging.INFO)

with open('input06.txt', encoding='utf-8') as fp:
    all = fp.read()

example = """Time:      7  15   30
Distance:  9  40  200
"""

races = all

race_document = races.split('\n')

_, *times = race_document[0].split()
_, *distances = race_document[1].split()
times_part1 = list(map(int, times))
distances_part1 = list(map(int, distances))
time_part2 = int(''.join(times))
distance_part2 = int(''.join(distances))

results = []
for time, distance in zip(times_part1, distances_part1):
    count = 0
    for t in range(time):
        if (time-t)*t > distance:
            count += 1
    results.append(count)

part1 = reduce(__mul__, results)
print(f'{part1=}')
logging.info(f'{part1=}')

part2 = 0
for t in range(time_part2):
    if (time_part2-t)*t > distance_part2:
        part2 += 1
print(f'{part2=}')
logging.info(f'{part2=}')
