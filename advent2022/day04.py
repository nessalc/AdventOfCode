with open('input04.txt') as f:
    cleaningAssignments=f.readlines()

fullContainment=0
for assignment in cleaningAssignments:
    a,b=assignment.strip().split(',')
    c,d=map(int,a.split('-'))
    e,f=map(int,b.split('-'))
    if c<=e and d>=f or c>=e and d<=f:
        fullContainment+=1

part1=fullContainment

partialContainment=0
for assignment in cleaningAssignments:
    a,b=assignment.strip().split(',')
    c,d=map(int,a.split('-'))
    e,f=map(int,b.split('-'))
    if e<=c<=f or e<=d<=f or c<=e<=d or c<=f<=d:
        partialContainment+=1

part2=partialContainment

print(f'Part 1: {part1}\nPart 2: {part2}')
