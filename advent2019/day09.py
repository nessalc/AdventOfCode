import os

with open(os.path.join(os.curdir, 'advent2019', 'input09.txt')) as file:
    intcode = list(map(int, file.readline().split(',')))
# intcode = [109, 1, 204, -1, 1001, 100, 1,
#            100, 1008, 100, 16, 101, 1006, 101, 0, 99]
# intcode = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
# intcode = [104, 1125899906842624, 99]


def get_param(intcode, location, mode, rbase):
    if mode == 0:
        return intcode[intcode[location]]
    elif mode == 1:
        return intcode[location]
    elif mode == 2:
        return intcode[intcode[location]+rbase]


def run_code(intcode, diag_input, ip=0):
    rbase = 0
    while intcode[ip] != 99:
        instruction = f'{intcode[ip]:05d}'
        opcode = int(instruction[3:])
        mode1 = int(instruction[2])
        mode2 = int(instruction[1])
        mode3 = int(instruction[0])
        if opcode == 1:
            p1 = get_param(intcode, ip+1, mode1, rbase)
            p2 = get_param(intcode, ip+2, mode2, rbase)
            intcode[intcode[ip+3]] = p1+p2
            ip += 4
        elif opcode == 2:
            p1 = get_param(intcode, ip+1, mode1, rbase)
            p2 = get_param(intcode, ip+2, mode2, rbase)
            intcode[intcode[ip+3]] = p1*p2
            ip += 4
        elif opcode == 3:
            intcode[intcode[ip+1]] = diag_input
            ip += 2
        elif opcode == 4:
            p1 = get_param(intcode, ip+1, mode1, rbase)
            output = p1
            ip += 2
        elif opcode == 5:
            p1 = get_param(intcode, ip+1, mode1, rbase)
            p2 = get_param(intcode, ip+2, mode2, rbase)
            if p1:
                ip = p2
            else:
                ip += 3
        elif opcode == 6:
            p1 = get_param(intcode, ip+1, mode1, rbase)
            p2 = get_param(intcode, ip+2, mode2, rbase)
            if not p1:
                ip = p2
            else:
                ip += 3
        elif opcode == 7:
            p1 = get_param(intcode, ip+1, mode1, rbase)
            p2 = get_param(intcode, ip+2, mode2, rbase)
            intcode[intcode[ip+3]] = (1 if p1 < p2 else 0)
            ip += 4
        elif opcode == 8:
            p1 = get_param(intcode, ip+1, mode1, rbase)
            p2 = get_param(intcode, ip+2, mode2, rbase)
            intcode[intcode[ip+3]] = (1 if p1 == p2 else 0)
            ip += 4
        elif opcode == 9:
            p1 = get_param(intcode, ip+1, mode1, rbase)
            rbase += p1
            ip += 2
    return output


print('Part 1:', run_code(intcode[:]+[0]*1000, 1))
