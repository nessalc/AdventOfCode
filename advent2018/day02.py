#Advent of Code 2018
#Day 2: Inventory Management System

import itertools

filename='input02.txt'
f=open(filename)
box_ids=list(map(str.strip,f.readlines()))
f.close()

checks={2:0,
        3:0}
for box_id in box_ids:
    counted_two,counted_three=False,False
    for l in set(box_id):
        if box_id.count(l)==2 and not counted_two:
            checks[2]+=1
            counted_two=True
        elif box_id.count(l)==3 and not counted_three:
            checks[3]+=1
            counted_three=True
print(checks)
print(checks[2]*checks[3])

for a,b in itertools.combinations(box_ids,2):
    if sum(c1!=c2 for c1,c2 in zip(a,b))==1:
        print(a)
        print(b)
        break
