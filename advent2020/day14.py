import more_itertools

program=list(map(str.strip,open('day14.txt').readlines()))
memory=dict()
ormask,andmask=0,2**36-1
for line in program:
    a,b=line.split(' = ')
    if a == 'mask':
        ormask,andmask=0,2**36-1
        maskstr=b[::-1]
        for c in range(36):
            if maskstr[c] == '1':
                ormask |= 2**c
            elif maskstr[c] == '0':
                andmask ^= 2**c
    else:
        b=int(b)
        b &= andmask
        b |= ormask
        a=int(a[4:-1])
        memory[a]=b
print(sum(memory.values()))
memory=dict()
for line in program:
    a,b=line.split(' = ')
    if a == 'mask':
        ormask,andmask=0,0
        maskstr=b[::-1]
        for c in range(36):
            if maskstr[c] == '1':
                ormask |= 2**c
            elif maskstr[c] == 'X':
                andmask ^= 2**c
    else:
        a=int(a[4:-1])
        a|=ormask
        a&=~andmask
        bitlist=[]
        for c in range(36):
            if maskstr[c] == 'X':
                bitlist.append(c)
        masks=[sum(map(lambda x:2**x,s)) for s in more_itertools.powerset(bitlist)]
        for addr in [a|mask for mask in masks]:
            memory[addr]=int(b)
print(sum(memory.values()))
