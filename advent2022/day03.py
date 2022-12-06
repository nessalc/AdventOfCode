import string

priority=' '+string.ascii_lowercase+string.ascii_uppercase

with open('input03.txt') as f:
    rucksacks=f.readlines()

prioritySum=0
for rucksack in rucksacks:
    sack=rucksack.strip()
    item=list(set(sack[:len(sack)//2])&set(sack[len(sack)//2:]))[0]
    prioritySum+=priority.find(item)

part1=prioritySum

prioritySum=0
for r in range(len(rucksacks)//3):
    item=list(set(rucksacks[3*r].strip())&set(rucksacks[3*r+1].strip())&set(rucksacks[3*r+2].strip()))[0]
    prioritySum+=priority.find(item)

part2=prioritySum

print(f'Part 1: {part1}\nPart 2: {part2}')
