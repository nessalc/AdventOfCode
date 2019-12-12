import re
import itertools

f=r'C:\Users\c41663\Documents\programming\advent2015\input15.txt'

def powerset(iterable):
    #from https://docs.python.org/3/library/itertools.html#itertools-recipes
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))
def total_weight(items,weight):
    start=weight if len(items)==1 else 0
    for i in range(start,weight+1):
        if len(items)==1:
            yield [(items[0],i)]
        else:
            for y in total_weight(items[1:],weight-i):
                yield [(items[0],i)]+y
def recipe(filename,calories=None):
    f=open(filename)
    s=f.readlines()
    f.close()
    ingredients=dict()
    for i in s:
        parse=re.split('[^-\w]+',i)
        ingredients[parse[0]]=dict(zip([x for x in parse[1::2]],map(int,[x for x in parse[2::2]])))
    max_total=0
    optimum_mixture={}
    for mixture in total_weight(list(ingredients.keys()),100):
        t=dict()
        for ingredient,amount in dict(mixture).items():
            for attribute,value in ingredients[ingredient].items():
                if attribute not in t.keys():
                    t[attribute]=0
                t[attribute]+=value*amount
        mix_value=1
        for attribute,value in t.items():
            if attribute!='calories':
                if value<0:
                    mix_value=0
                    break
                mix_value*=value
        if not calories and mix_value>max_total:
            max_total=mix_value
            optimum_mixture=mixture
        elif calories==t['calories'] and mix_value>max_total:
            max_total=mix_value
            optimum_mixture=mixture
    return optimum_mixture,max_total
