import itertools
import functools

def powerset(iterable):
    #from https://docs.python.org/3/library/itertools.html#itertools-recipes
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))
def balance_packages(filename,groups):
    weights=[int(line.strip()) for line in open(filename)]
    best_qe=100000000000000000000
    best_legroom=100000000000000000000
    weight_needed=sum(weights)//groups
    for s in powerset(weights):
        if sum(s)==weight_needed:
            legroom=len(s)
            if legroom<best_legroom:
                best_legroom=legroom
                qe=functools.reduce(lambda x,y:x*y,s)
                if qe<best_qe:
                    print('new best QE={} ({})'.format(qe,s))
                    best_qe=qe
    return best_qe
