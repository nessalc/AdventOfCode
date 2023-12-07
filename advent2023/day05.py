from dataclasses import dataclass
from typing import Self
from functools import reduce
from itertools import batched
from time import perf_counter
from math import inf
import logging

logging.basicConfig(filename='day05.log',
                    format='[%(asctime)s] %(message)s', level=logging.INFO)

with open('input05.txt', encoding='utf-8') as fp:
    all = fp.read()

example = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

almanac = all

info = almanac.split('\n\n')


@dataclass
class MapMap:
    dest_range_start: int
    source_range_start: int
    range_length: int


class Map:
    source: str
    dest: str
    _map_list: list[MapMap]
    _map_link: Self

    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        self._map_list = []

    def add_entry(self, dest_range_start, source_range_start, range_length):
        self._map_list.append(
            MapMap(dest_range_start, source_range_start, range_length))

    def transform(self, input) -> int:
        # print(f'searching {self.source} to {self.dest} map:')
        for m in self._map_list:
            # print(f'Is {input} between {m.source_range_start} and {m.source_range_start+m.range_length}?')
            if m.source_range_start <= input <= m.source_range_start+m.range_length:
                result = input-m.source_range_start+m.dest_range_start
                # print(f'compute answer and return ({result})')
                return result
        # print(f'return default answer ({input})')
        return input

    def transform_through(self, input):
        result = self.transform(input)
        if hasattr(self, '_map_link') and self._map_link:
            result = self._map_link.transform_through(result)
        return result


if __name__ == '__main__':
    seeds = info[0]
    map_list: list[Map] = []
    for maps in info[1:]:
        map_title, *map_data = maps.strip().split('\n')
        source, dest = map_title[:-5].split('-to-')
        m = Map(source, dest)
        for map_range in map_data:
            m.add_entry(*list(map(int, map_range.split())))
        map_list.append(m)
    for i in range(len(map_list)-1):
        if map_list[i].dest == map_list[i+1].source:
            map_list[i]._map_link = map_list[i+1]
    seed_list = list(map(int, seeds.split()[1:]))
    part1 = reduce(
        min, map(lambda x: map_list[0].transform_through(x), seed_list))

    print(f'{part1=}')

    logging.info(f'start part 2')
    start = perf_counter()
    s0, s1 = seed_list[0], seed_list[1]
    minimum = inf  # 15880237
    test = inf  # 15880237
    batches = batched(seed_list, 2)
    # skip = 5
    for seed_start, seed_count in batches:
        # if skip > 0:
        #     skip -= 1
        #     continue
        print(f'{seed_start} through {
              seed_start+seed_count} ({seed_count} seeds)')
        for s in range(seed_start, seed_start+seed_count):
            test = map_list[0].transform_through(s)
            if test < minimum:
                minimum = test
            if s % 100000 == 0:
                print('.', end='')
        print(f'\nlowest so far: {minimum}')
        logging.info(f'\nlowest so far: {minimum}')
        now = perf_counter()
        print(f'time elapsed: {now-start}s')
    part2 = minimum
    end = perf_counter()
    print(f'total time: {end-start}s')
    logging.info(f'total time: {end-start}s')

    print(f'{part2=}')
