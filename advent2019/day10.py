import os
import operator
from fractions import Fraction as F

os.chdir(r'D:\programming\AdventOfCode')

with open(os.path.join(os.curdir, 'advent2019', 'input10.txt')) as file:
    asteroid_field = list(map(str.strip, file.readlines()))
# asteroid_field = ['.#..#',
#                   '.....',
#                   '#####',
#                   '....#',
#                   '...##']
# asteroid_field = ['......#.#.',
#                   '#..#.#....',
#                   '..#######.',
#                   '.#.#.###..',
#                   '.#..#.....',
#                   '..#....#.#',
#                   '#..#....#.',
#                   '.##.#..###',
#                   '##...#..#.',
#                   '.#....####']
# asteroid_field = ['#.#...#.#.',
#                   '.###....#.',
#                   '.#....#...',
#                   '##.#.#.#.#',
#                   '....#.#.#.',
#                   '.##..###.#',
#                   '..#...##..',
#                   '..##....##',
#                   '......#...',
#                   '.####.###.']
# asteroid_field = ['.#..##.###...#######',
#                   '##.############..##.',
#                   '.#.######.########.#',
#                   '.###.#######.####.#.',
#                   '#####.##.#.##.###.##',
#                   '..#####..#.#########',
#                   '####################',
#                   '#.####....###.#.#.##',
#                   '##.#################',
#                   '#####.##.###..####..',
#                   '..######..##.#######',
#                   '####.##.####...##..#',
#                   '.#####..#.######.###',
#                   '##...#.##########...',
#                   '#.##########.#######',
#                   '.####.#.###.###.#.##',
#                   '....##.##.###..#####',
#                   '.#.#.###########.###',
#                   '#.#.#.#####.####.###',
#                   '###.##.####.##.#..##']


def fraction_iterator(max_denominator, include_reciprocals=False):
    """
This iterator will generate all fractions with a maximum denominator of
`max_denominator` in ascending value order. E.g., if `max_denominator` is 4,
the function will yield 1/4, 1/3, 1/2, 2/3, and 3/4.
    """
    # create fraction list:
    flist = []
    for d in range(max_denominator, 1, -1):
        for n in range(1, d):
            flist.append(F(n, d))
            if include_reciprocals:
                flist.append(F(d, n))
    flist = list(set(flist))  # remove duplicate elements
    if include_reciprocals:
        flist.append(F(1, 1))
    flist.sort()  # sort
    return iter(flist)  # return iterator


xsize = len(asteroid_field[0])
ysize = len(asteroid_field)
visible = dict()
for x in range(xsize):
    for y in range(ysize):
        if asteroid_field[y][x] == '#':
            count = 0
            # check up
            search = ''.join([asteroid_field[k][x] for k in range(0, y)])[::-1]
            if search.count('#'):
                # only add one, as one will block sight lines of others.
                # Reversing this isn't strictly necessary, but I'm leaving it
                # in in case it's needed for part 2.
                count += 1
            # check right
            search = ''.join([asteroid_field[y][k]
                              for k in range(x + 1, xsize)])
            if search.count('#'):
                # only add one, as one will block sight lines of others
                count += 1
            # check down
            search = ''.join([asteroid_field[k][x]
                              for k in range(y + 1, ysize)])
            if search.count('#'):
                # only add one, as one will block sight lines of others
                count += 1
            # check left
            search = ''.join([asteroid_field[y][k] for k in range(0, x)])[::-1]
            if search.count('#'):
                # only add one, as one will block sight lines of others.
                # Reversing this isn't strictly necessary, but I'm leaving it
                # in in case it's needed for part 2.
                count += 1
            # check diagonally between up and right
            blocked = {}
            for f in fraction_iterator(max(xsize, ysize)-1, True):
                blocked[f] = {'++': False, '+-': False,
                              '-+': False, '--': False}
                for s in range(1, max(xsize, ysize)):
                    xt, yt = s*f.numerator, s*f.denominator
                    try:
                        if x+xt >= 0 and y+yt >= 0 and \
                                asteroid_field[y+yt][x+xt] == '#' and \
                                not blocked[f]['++']:
                            count += 1
                            blocked[f]['++'] = True
                    except IndexError:
                        pass
                    # check diagonally between right and down
                    xt, yt = s*f.numerator, s*-f.denominator
                    try:
                        if x+xt >= 0 and y+yt >= 0 and \
                                asteroid_field[y+yt][x+xt] == '#' and \
                                not blocked[f]['+-']:
                            count += 1
                            blocked[f]['+-'] = True
                    except IndexError:
                        pass
                    # check diagonally between down and left
                    xt, yt = s*-f.numerator, s*f.denominator
                    try:
                        if x+xt >= 0 and y+yt >= 0 and \
                                asteroid_field[y+yt][x+xt] == '#' and \
                                not blocked[f]['-+']:
                            count += 1
                            blocked[f]['-+'] = True
                    except IndexError:
                        pass
                    # check diagonally between left and up
                    xt, yt = s*-f.numerator, s*-f.denominator
                    try:
                        if x+xt >= 0 and y+yt >= 0 and \
                                asteroid_field[y+yt][x+xt] == '#' and \
                                not blocked[f]['--']:
                            count += 1
                            blocked[f]['--'] = True
                    except IndexError:
                        pass
            visible[(x, y)] = count
print(max(visible.items(), key=operator.itemgetter(1)))

# .#..#
# .....
# X####
# ....#
# ...##
