# Advent of Code
# Day 5

# Read Input
import itertools
from collections import Counter

def read_input(filename:str='day05.txt'):
    with open(filename) as fp:
        lines=fp.read()
    ordering_rules_temp,updates_temp=lines.split('\n\n')
    ordering_rules,updates=[],[]
    for rule in ordering_rules_temp.split('\n'):
        a,b=rule.split('|')
        ordering_rules.append((int(a),int(b)))
    for update in updates_temp.split('\n'):
        if update!='':
            updates.append([int(x) for x in update.split(',')])
    return ordering_rules,updates

def test_input(part:int=1):
    ordering_rules_temp="""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""
    updates_temp="""75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    ordering_rules,updates=[],[]
    for rule in ordering_rules_temp.split('\n'):
        a,b=rule.split('|')
        ordering_rules.append((int(a),int(b)))
    for update in updates_temp.split('\n'):
        updates.append([int(x) for x in update.split(',')])
    return ordering_rules,updates

def find_applicable_rules(update,ordering_rules):
    rules=[]
    for page in update:
        rest=list(filter(lambda x:x!=page,update))
        try:
            rules+=filter(lambda x:x[0]==page and x[1] in rest or x[1]==page and x[0] in rest,ordering_rules)
        except TypeError:
            print(page,update,rest)
            raise
    rules=list(set(rules))
    return rules

def meets_rules(update,applicable_rules):
    return all([pair in applicable_rules for pair in itertools.pairwise(update)])

def sort_rules(applicable_rules):
    rules=Counter([x[0] for x in applicable_rules])
    rules=sorted(rules,key=rules.get,reverse=True)
    rules.append(list(filter(lambda x:x[0]==rules[-1],applicable_rules))[0][1])
    return rules

def solution():
    ordering_rules,updates=read_input()
    part1,part2=0,0
    for update in updates:
        applicable_rules=find_applicable_rules(update,ordering_rules)
        if meets_rules(update,applicable_rules):
            part1+=update[len(update)//2]
        else:
            updated=sort_rules(applicable_rules)
            part2+=updated[len(updated)//2]
    return part1,part2
    

if __name__=='__main__':
    part1,part2=solution()
    print(f'Solution to Part 1: {part1}\n'
          f'Solution to Part 2: {part2}\n')
