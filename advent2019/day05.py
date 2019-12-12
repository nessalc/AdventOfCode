import os

with open(os.path.join(os.curdir, 'advent2019', 'input05.txt')) as file:
    intcode = list(map(int, file.readline().split(',')))


def run_code(intcode, diag_input, ip=0):
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
            intcode[intcode[ip+1]] = diag_input
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


print('Part 1:', run_code(intcode[:], 1))
print('Part 2:', run_code(intcode[:], 5))
