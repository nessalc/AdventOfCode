with open('input10.txt') as f:
    program=f.read()
program=program.splitlines()

cycle=0
X=1

significant_cycles=list(range(20,221,40))
sprite=[0,1,2]

signal_strength=0

for instruction in program:
    if instruction=='noop':
        cycle+=1
        if cycle in significant_cycles:
            signal_strength+=cycle*X
        if (cycle-1)%40 in sprite:
            print('#',end='')
        else:
            print(' ',end='')
        if cycle%40==0:
            print()
    else:
        _,V=instruction.split()
        cycle+=1
        if cycle in significant_cycles:
            signal_strength+=cycle*X
        if (cycle-1)%40 in sprite:
            print('#',end='')
        else:
            print(' ',end='')
        if cycle%40==0:
            print()
        cycle+=1
        if cycle in significant_cycles:
            signal_strength+=cycle*X
        if (cycle-1)%40 in sprite:
            print('#',end='')
        else:
            print(' ',end='')
        if cycle%40==0:
            print()
        X+=int(V)
        sprite=[X-1,X,X+1]
print()

part1=signal_strength
part2='read capital letters off screen above'

print(f'Part 1: {part1}\nPart 2: {part2}')
