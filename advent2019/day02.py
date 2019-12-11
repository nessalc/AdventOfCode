import os

import itertools


def run_code(intcode, ip):
    while intcode[ip] != 99:
        if intcode[ip] == 1:
            intcode[intcode[ip+3]] = intcode[intcode[ip+1]] + \
                intcode[intcode[ip+2]]
        elif intcode[ip] == 2:
            intcode[intcode[ip+3]] = intcode[intcode[ip+1]] * \
                intcode[intcode[ip+2]]
        ip += 4
    return intcode[0]


with open(os.path.join(os.curdir, 'advent2019', 'input02.txt')) as file:
    intcode = list(map(int, file.readline().split(',')))


def initialize(intcode, noun, verb):
    newcode = intcode[:]
    newcode[1], newcode[2] = noun, verb
    return newcode


print('Original Code:', intcode)
print('Part 1:', run_code(initialize(intcode, 12, 2), 0))
for noun, verb in itertools.combinations_with_replacement(range(100), 2):
    print(noun, verb)
    if run_code(initialize(intcode, noun, verb), 0) == 19690720:
        break
print('Part 2:', 100*noun+verb)
