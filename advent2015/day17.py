import itertools

f=r'C:\users\c41663\Documents\programming\advent2015\input17.txt'

def powerset(iterable):
    #from https://docs.python.org/3/library/itertools.html#itertools-recipes
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))
def egg_nog_containers(liters,filename,container_count=0):
    f=open(filename)
    s=f.readlines()
    f.close()
    containers=[]
    for c in s:
        containers.append(int(c))
    combinations=0
    min_container_count=10000
    for combination in powerset(containers):
        if sum(combination)==liters and (container_count==0 or len(combination)==container_count):
            min_container_count=min(min_container_count,len(combination))
            combinations+=1
    print(min_container_count)
    return combinations
