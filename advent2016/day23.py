# Author: BumpitySnook, with mod by Lains

file = open("example23.2.txt", "rb").read()
lines = file.strip().split("\n")


def is_a_num(s):
    try:
        int(s)
    except:
        return False

    return True


def get_value(regs, x):
    if is_a_num(x):
        return int(x)
    else:
        return regs[x]


def toggle(tgl_line):
    sp = tgl_line.split(" ")
    instr = sp[0]

    if instr == "inc":
        return " ".join(["dec"] + sp[1:])
    elif instr == "dec" or instr == "tgl":
        return " ".join(["inc"] + sp[1:])
    elif instr == "jnz":
        return " ".join(["cpy"] + sp[1:])
    elif instr == "cpy":
        return " ".join(["jnz"] + sp[1:])
    else:
        assert False


def assembunny_compile(lines, part2=False):
    index = 0
    regs = {"a": 7, "b": 0, "c": 0, "d": 0}

    if part2:
        regs["a"] = 12

    while True:
        if index >= len(lines):
            break

        line = lines[index]
        a, b = line.split(" ", 1)

        if a == "cpy":
            b, c = b.split(" ")
            b = get_value(regs, b)

            if c in regs:
                regs[c] = b
            else:
                print "invalid"

            index += 1

        elif a == "inc":
            if b in regs:
                #if index + 3 < len(lines) and index - 1 >= 0 and lines[index-1].startswith("cpy ") and \
                #        lines[index+1].startswith("dec") and lines[index+2].startswith("jnz") and \
                #        lines[index+3].startswith("dec") and lines[index+4].startswith("jnz"):
                #
                #    incop = b
                #    cpysrc, cpydest = lines[index-1].split(" ")[1:]
                #    dec1op = lines[index+1].split(" ")[1]
                #    jnz1cond, jnz1off = lines[index+2].split(" ")[1:]
                #    dec2op = lines[index+3].split(" ")[1]
                #    jnz2cond, jnz2off = lines[index+4].split(" ")[1:]
                #
                #    if cpydest == dec1op and dec1op == jnz1cond and \
                #        dec2op == jnz2cond and \
                #            jnz1off == "-2" and jnz2off == "-5":
                #            regs[incop] += (get_value(regs, cpysrc) * get_value(regs, dec2op))
                #            regs[dec1op] = 0
                #            regs[dec2op] = 0
                #            index += 5
                #
                #            continue
                #
                regs[b] += 1

            index += 1
        elif a == "dec":
            if b in regs:
                regs[b] -= 1

            index += 1
        elif a == "jnz":
            b, c = b.split(" ")
            b = get_value(regs, b)
            c = get_value(regs, c)

            if b != 0:
                index = index + int(c)
            else:
                index += 1
        elif a == "tgl":
            xr = b
            x = get_value(regs, xr)
            iidx = index + x

            if iidx >= 0 and iidx < len(lines):
                tgl_line = lines[iidx]
                lines[iidx] = toggle(tgl_line)
            index += 1
        else:
            assert False

    return regs["a"]


print "part 1:", assembunny_compile(lines[:])
print "part 2:", assembunny_compile(lines[:], part2=True)