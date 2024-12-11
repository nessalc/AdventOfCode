from dataclasses import dataclass
import numpy as np
from typing import Self

with open('input10.txt', encoding='utf-8') as fp:
    all_input = fp.read()

example1 = """-L|F7.
7S-7|.
L|7||.
-L-J|.
L|-JF.
"""

example2 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other: Self) -> Self:
        return Point(self.x+other.x, self.y+other.y)

    def as_tuple(self) -> tuple[int, int]:
        return self.y, self.x


R = Point(1, 0)
U = Point(0, -1)
L = Point(-1, 0)
D = Point(0, 1)

pipe_map = all_input


def paint_path(pipe_map: np.ndarray, path: list[Point] = []):
    pipe_map_print_copy = pipe_map.copy()
    for c in path:
        pipe_map_print_copy[c.as_tuple()] = 'X'
    string_map = '\n'.join(x for x in [''.join(e)
                           for e in pipe_map_print_copy])
    translation_table = str.maketrans(
        '-|7JLFX', chr(0x2500)+chr(0x2502)+chr(0x2510)+chr(0x2518)+chr(0x2514)+chr(0x250c)+chr(0x2588))
    print(string_map.translate(translation_table))


pipe_map = np.asarray(list(map(list, pipe_map.strip().split('\n'))))

# paint_path(pipe_map)


def check_directions(pipe_map: np.ndarray, coords: Point) -> str:
    y, x = coords.as_tuple()
    ysize, xsize = pipe_map.shape
    directions = ''
    # check all
    # right
    # print(f'test: {x+1}, {y}, {pipe_map[y,x+1,]}')
    if x+1 < xsize and pipe_map[y, x] in 'SLF-' and pipe_map[y, x+1] in 'S7J-':
        directions += 'R'
    # left
    # print(f'test: {x-1}, {y}, {pipe_map[y,x-1]}')
    if x-1 >= 0 and pipe_map[y, x] in 'SJ7-' and pipe_map[y, x-1] in 'SFL-':
        directions += 'L'
    # up
    # print(f'test: {x}, {y-1}, {pipe_map[y-1,x]}')
    if y-1 >= 0 and pipe_map[y, x] in 'SLJ|' and pipe_map[y-1, x] in 'SF7|':
        directions += 'U'
    # down
    # print(f'test: {x}, {y+1}, {pipe_map[y+1,x]}')
    if y+1 < ysize and pipe_map[y, x] in 'SF7|' and pipe_map[y+1, x] in 'SJL|':
        directions += 'D'
    # print(f'check_directions: {directions}')
    return directions


def follow_path(pipe_map: np.ndarray, coords: Point):
    coord_list = []
    while coords not in coord_list:
        directions = check_directions(pipe_map, coords)
        coord_list.append(coords)
        if len(directions) <= 1:
            print('**', coord_list[-1], pipe_map[coord_list[-1].as_tuple()])
            raise IndexError
        if 'R' in directions and coords+R not in coord_list:
            coords += R
            # print(f'move right to {coords}, {pipe_map[coords.y,coords.x]}')
        elif 'U' in directions and coords+U not in coord_list:
            coords += U
            # print(f'move up to {coords}, {pipe_map[coords.y,coords.x]}')
        elif 'L' in directions and coords+L not in coord_list:
            coords += L
            # print(f'move left to {coords}, {pipe_map[coords.y,coords.x]}')
        elif 'D' in directions and coords+D not in coord_list:
            coords += D
            # print(f'move down to {coords}, {pipe_map[coords.y,coords.x]}')
        else:
            pass
            # print('back to the start?')
    # print(f'{coord_list=}')
    return coord_list


x, y = np.where(pipe_map == 'S')
start_coord = Point(*y, *x)
# print(start_coord)
# print(pipe_map[start_coord.as_tuple()])
path = follow_path(pipe_map, start_coord)
part1 = len(path)//2

print(f'{part1=}\n')

paint_path(pipe_map, path)
