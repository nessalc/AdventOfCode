from itertools import zip_longest
from functools import cmp_to_key

def compare(left:int|list,right:int|list)->bool:
    if isinstance(left,int) and isinstance(right,int):
        #print(f'int v int\n{left} v {right}')
        return -1 if left<right else 1
    elif isinstance(left,list) and isinstance(right,list):
        #print(f'list v list\n{left} v {right}')
        for a,b in zip_longest(left,right):
            if a==b:
                continue
            elif a==None:
                return -1
            elif b==None:
                return 1
            temp=compare(a,b)
            if temp is None:
                continue
            return temp
    elif isinstance(left,int) and isinstance(right,list):
        #print(f'int v list\n{left} v {right}')
        return compare([left],right)
    elif isinstance(left,list) and isinstance(right,int):
        #print(f'list v int\n{left} v {right}')
        return compare(left,[right])

with open('input13.txt') as f:
    pairs=[list(map(eval,x.splitlines())) for x in f.read().split('\n\n')]

part1=0

for i,pair in enumerate(pairs,1):
    if compare(*pair)<0:
        part1+=i

full_list=[]
for pair in pairs:
    full_list.extend(pair)
full_list.extend([[[2]]])
full_list.extend([[[6]]])
full_list.sort(key=cmp_to_key(compare))

part2=(full_list.index([[2]])+1)*(full_list.index([[6]])+1)

print(f'Part 1: {part1}\nPart 2: {part2}')
