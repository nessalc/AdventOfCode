#Advent of Code 2017
#Day 15: Dueling Generators

def generator(seed,factor,picky_factor=None):
    value=seed
    while True:
        value=value*factor%2147483647
        if picky_factor is None or value%picky_factor==0:
            yield value

def judge(trials,seed_a,seed_b,picky_a=None,picky_b=None):
    genA=generator(seed_a,16807,picky_a)
    genB=generator(seed_b,48271,picky_b)
    count=0
    for i in range(trials):
        if (next(genA)&0xffff)==(next(genB)&0xffff):
            count+=1
    return count

