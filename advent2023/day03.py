import regex
from dataclasses import dataclass
from itertools import combinations

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

with open('input03.txt', encoding='utf-8') as fp:
    all = fp.read()

schematic = all


@dataclass
class Part:
    part_number: int
    symbol: str
    symbol_location: tuple[int, int]


linelen = schematic.find('\n')+1
linecount = schematic.count('\n')
partNumbers: list[Part] = []
for y, line in enumerate(schematic.strip().split('\n')):
    for match in regex.finditer('\\d+', line):
        # does match have a symbol adjacent to it?
        for i in range(match.span()[0]-1, match.span()[1]+1):
            for j in range(y-1, y+2):
                try:
                    if i >= 0 and j >= 0 and schematic[i+j*linelen] not in '0123456789.\n':
                        symbol = schematic[i+j*linelen]
                        symbol_location = j, i
                        part_number = int(match.group(0))
                        partNumbers.append(
                            Part(part_number, symbol, symbol_location))
                except IndexError:
                    pass
print('part1:', sum(map(lambda x: x.part_number, partNumbers)))
gears = list(filter(lambda x: x.symbol == '*', partNumbers))
gear_ratio = []
for x, y in combinations(gears, 2):
    if x.symbol_location == y.symbol_location:
        gear_ratio.append(x.part_number*y.part_number)
print('part2:', sum(gear_ratio))
