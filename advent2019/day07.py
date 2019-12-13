import os
import itertools

with open(os.path.join(os.curdir, 'advent2019', 'input07.txt')) as file:
    intcode = list(map(int, file.readline().split(',')))
# intcode = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
# intcode = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1,
#            23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
# intcode = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
#            1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]
intcode = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
           27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]


def run_code(intcode, diag_input, ip=0):
    diag_index = 0
    if not isinstance(diag_input, (tuple, list)):
        diag_input = list(diag_input)
    while intcode[ip] != 99:
        instruction = f'{intcode[ip]:05d}'
        opcode = int(instruction[3:])
        mode1 = int(instruction[2])
        mode2 = int(instruction[1])
        mode3 = int(instruction[0])
        if opcode == 1:
            p1 = intcode[ip+1] if mode1 else intcode[intcode[ip+1]]
            p2 = intcode[ip+2] if mode2 else intcode[intcode[ip+2]]
            intcode[intcode[ip+3]] = p1+p2
            ip += 4
        elif opcode == 2:
            p1 = intcode[ip+1] if mode1 else intcode[intcode[ip+1]]
            p2 = intcode[ip+2] if mode2 else intcode[intcode[ip+2]]
            intcode[intcode[ip+3]] = p1*p2
            ip += 4
        elif opcode == 3:
            intcode[intcode[ip+1]] = diag_input[diag_index]
            diag_index += 1
            ip += 2
        elif opcode == 4:
            p1 = intcode[ip+1] if mode1 else intcode[intcode[ip+1]]
            output = p1
            ip += 2
        elif opcode == 5:
            p1 = intcode[ip+1] if mode1 else intcode[intcode[ip+1]]
            p2 = intcode[ip+2] if mode2 else intcode[intcode[ip+2]]
            if p1:
                ip = p2
            else:
                ip += 3
        elif opcode == 6:
            p1 = intcode[ip+1] if mode1 else intcode[intcode[ip+1]]
            p2 = intcode[ip+2] if mode2 else intcode[intcode[ip+2]]
            if not p1:
                ip = p2
            else:
                ip += 3
        elif opcode == 7:
            p1 = intcode[ip+1] if mode1 else intcode[intcode[ip+1]]
            p2 = intcode[ip+2] if mode2 else intcode[intcode[ip+2]]
            intcode[intcode[ip+3]] = (1 if p1 < p2 else 0)
            ip += 4
        elif opcode == 8:
            p1 = intcode[ip+1] if mode1 else intcode[intcode[ip+1]]
            p2 = intcode[ip+2] if mode2 else intcode[intcode[ip+2]]
            intcode[intcode[ip+3]] = (1 if p1 == p2 else 0)
            ip += 4
    return p1


all_outputs = []
for phase_setting in itertools.permutations(range(5), 5):
    output = 0
    for i in phase_setting:
        output = run_code(intcode[:], [i, output])
    all_outputs.append((phase_setting, output))
print(max(all_outputs, key=lambda x: x[1]))
all_outputs = []
for phase_setting in itertools.permutations(range(5, 10), 5):
    output = 0
    for i in phase_setting:
        output = run_code(intcode[:], [i, output])
    all_outputs.append((phase_setting, output))
print(max(all_outputs, key=lambda x: x[1]))
