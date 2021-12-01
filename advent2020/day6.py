anyone,everyone=0,0
for answer_group in open('day6.txt').read().split('\n\n'):
    anyone += len(set(answer_group.replace('\n','')))
    everyone += len(set.intersection(*map(set,answer_group.split())))
print(anyone)
print(everyone)
