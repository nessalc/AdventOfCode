with open('input01.txt') as f:
    cals=[list(map(int,elf.split('\n'))) for elf in f.read().strip().split('\n\n')]

part1=max(map(sum,cals))
part2=sum(sorted(map(sum,cals))[-3:])
