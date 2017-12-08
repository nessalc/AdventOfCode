#Advent of Code 2017
#Day 8: I Heard You Like Registers

def millisecond8(filename):
    with open(filename) as fp:
        instructions=list(map(str.strip,fp.readlines()))
    r1,r2=parse_instructions(instructions)
    print('Part 1:',r1)
    print('Part 2:',r2)

def parse_instructions(instructions):
    registers=dict()
    memmax=-1000000
    for i in instructions:
        reg,inst,amt,cond,regcon,regcomp,regamt=i.split()
        if reg not in registers.keys():
            registers[reg]=0
        if regcon not in registers.keys():
            registers[regcon]=0
        stmt='registers[\''+regcon+'\']'+regcomp+regamt
        conditional=eval(stmt)
        if conditional:
            if inst=='inc':
                registers[reg]+=int(amt)
            else:
                registers[reg]-=int(amt)
        memmax=max(memmax,registers[reg])
    return max(registers.values()),memmax
