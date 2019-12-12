import itertools

def seating_arrangement(filename,include_self=False):
    f=open(filename)
    s=f.readlines()
    f.close()
    happiness_pairs=[]
    happiness_value=[]
    people=set()
    for line in s:
        parse=line.split()
        people.add(parse[0])
        happiness_pairs.append((parse[0],parse[-1][:-1]))
        happiness_value.append((-1 if parse[2]=='lose' else 1)*int(parse[3]))
    if include_self:
        people.add('Me')
    num_people=len(people)
    max_happiness=0
    for arrangement in itertools.permutations(people):
        happiness=0
        for i in range(len(arrangement)):
            if include_self and (arrangement[i]=='Me' or arrangement[(i+1)%num_people]=='Me'):
                continue
            happiness+=happiness_value[happiness_pairs.index((arrangement[i],arrangement[(i+1)%num_people]))]
            happiness+=happiness_value[happiness_pairs.index((arrangement[(i+1)%num_people],arrangement[i]))]
        max_happiness=max(max_happiness,happiness)
    return max_happiness
