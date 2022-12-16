from dataclasses import dataclass,field
from collections.abc import Callable
from typing import Self, Deque
from collections import deque

@dataclass
class Monkey:
    items:Deque[int]
    operation:Callable[[int],int]=field(repr=False)
    test:Callable[[int],bool]=field(repr=False)
    test_true:Self=field(default=None,repr=False)
    test_false:Self=field(default=None,repr=False)
    inspection_count:int=field(default=0,repr=False)

modulus=3*11*19*5*2*7*17*13
def reset_monkeys():
##    ## Example Input
##    monkeys=[
##        Monkey(deque([79,98]),
##               lambda x:x*19,
##               lambda x:x%23==0),
##        Monkey(deque([54,65,75,74]),
##               lambda x:x+6,
##               lambda x:x%19==0),
##        Monkey(deque([79,60,97]),
##               lambda x:x*x,
##               lambda x:x%13==0),
##        Monkey(deque([74]),
##               lambda x:x+3,
##               lambda x:x%17==0)]
##    monkeys[0].test_true=monkeys[2]
##    monkeys[0].test_false=monkeys[3]
##    monkeys[1].test_true=monkeys[2]
##    monkeys[1].test_false=monkeys[0]
##    monkeys[2].test_true=monkeys[1]
##    monkeys[2].test_false=monkeys[3]
##    monkeys[3].test_true=monkeys[0]
##    monkeys[3].test_false=monkeys[1]

    ## My input
    monkeys=[
        #Monkey 0
        Monkey(deque([76,88,96,97,58,61,67]),
               lambda x:x*19,
               lambda x:x%3==0),
        #Monkey 1
        Monkey(deque([93,71,79,83,69,70,94,98]),
               lambda x:x+8,
               lambda x:x%11==0),
        #Monkey 2
        Monkey(deque([50,74,67,92,61,76]),
               lambda x:x*13,
               lambda x:x%19==0),
        #Monkey 3
        Monkey(deque([76,92]),
               lambda x:x+6,
               lambda x:x%5==0),
        #Monkey 4
        Monkey(deque([74,94,55,87,62]),
               lambda x:x+5,
               lambda x:x%2==0),
        #Monkey 5
        Monkey(deque([59,62,53,62]),
               lambda x:x*x,
               lambda x:x%7==0),
        #Monkey 6
        Monkey(deque([62]),
               lambda x:x+2,
               lambda x:x%17==0),
        #Monkey 7
        Monkey(deque([85,54,53]),
               lambda x:x+3,
               lambda x:x%13==0)]
    monkeys[0].test_true=monkeys[2]
    monkeys[0].test_false=monkeys[3]
    monkeys[1].test_true=monkeys[5]
    monkeys[1].test_false=monkeys[6]
    monkeys[2].test_true=monkeys[3]
    monkeys[2].test_false=monkeys[1]
    monkeys[3].test_true=monkeys[1]
    monkeys[3].test_false=monkeys[6]
    monkeys[4].test_true=monkeys[2]
    monkeys[4].test_false=monkeys[0]
    monkeys[5].test_true=monkeys[4]
    monkeys[5].test_false=monkeys[7]
    monkeys[6].test_true=monkeys[5]
    monkeys[6].test_false=monkeys[7]
    monkeys[7].test_true=monkeys[4]
    monkeys[7].test_false=monkeys[0]

    return monkeys

monkeys=reset_monkeys()

for r in range(20):
    for monkey in monkeys:
        while monkey.items:
            item=monkey.items.popleft()
            item=monkey.operation(item)
            monkey.inspection_count+=1
            item//=3
            item%=modulus
            if monkey.test(item):
                monkey.test_true.items.append(item)
            else:
                monkey.test_false.items.append(item)
##for i,monkey in enumerate(monkeys):
##    print(f'Monkey {i} inspected items {monkey.inspection_count} times.')
##print()

counts=list(map(lambda x:x.inspection_count,monkeys))
top_two=sorted(counts,reverse=True)[:2]
part1=top_two[0]*top_two[1]

monkeys=reset_monkeys()

for r in range(10000):
    for i,monkey in enumerate(monkeys):
        while monkey.items:
            item=monkey.items.popleft()
            item=monkey.operation(item)
            monkey.inspection_count+=1
            item%=modulus
            if monkey.test(item):
                monkey.test_true.items.append(item)
            else:
                monkey.test_false.items.append(item)
##    if r+1 in [1,20] or (r+1)%1000==0:
##        print(f'After round {r+1}:')
##        for i,monkey in enumerate(monkeys):
##            print(f'Monkey {i} inspected items {monkey.inspection_count} times.')
##        print()

counts=list(map(lambda x:x.inspection_count,monkeys))
top_two=sorted(counts,reverse=True)[:2]
part2=top_two[0]*top_two[1]

print(f'Part 1: {part1}\nPart 2: {part2}')
