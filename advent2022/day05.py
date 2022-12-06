import pprint
import copy
pp=pprint.PrettyPrinter(indent=4,width=120)

with open('input05.txt') as f:
    infile=f.read()

crates,moves=infile.split('\n\n')
crateStacks=[[],[],[],[],[],[],[],[],[]]
crateConfig=crates.split('\n')[:-1][::-1]
for i in crateConfig:
    column=0
    row=i[1::4]
    for crate in row:
        if crate!=' ':
            crateStacks[column].append(crate)
        column+=1
#pp.pprint(crateStacks)

crateStacksCopy=copy.deepcopy(crateStacks)

for move in moves.split('\n'):
    if move.strip()=='':
        break
    count,stack1,stack2=[int(i) for i in move.split() if i.isdigit()]
    for c in range(count):
        crate=crateStacks[stack1-1].pop()
        crateStacks[stack2-1].append(crate)
#pp.pprint(crateStacks)
part1=''.join([crateStacks[i][-1] for i in range(len(crateStacks))])

crateStacks=crateStacksCopy

#pp.pprint(crateStacks)
for move in moves.split('\n'):
    if move.strip()=='':
        break
    count,stack1,stack2=[int(i) for i in move.split() if i.isdigit()]
    crates=crateStacks[stack1-1][-count:]
    crateStacks[stack1-1]=crateStacks[stack1-1][:-count]
    crateStacks[stack2-1]+=crates
#pp.pprint(crateStacks)
part2=''.join([crateStacks[i][-1] for i in range(len(crateStacks))])

print(f'Part 1: {part1}\nPart 2: {part2}')
