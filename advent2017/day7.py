#Advent of Code 2017
#Day 7: Recursive Circus

import re

def find_root(programs):
    global nodedict
    r=re.compile('(\\w+) \\((\d+)\)(?: -> ([\\w,\\s]+))?')
    nodedict=dict()
    for p in programs:
        t=list(r.match(p).groups())
        nodedict[t[0]]={'name':t[0],
                        'weight':int(t[1])}
        if t[2] is not None:
            nodedict[t[0]]['list']=list(map(str.strip,t[2].split(',')))
    #return nodedict

def nest(item):
    global nodedict
    for i in range(len(item['list'])):
        n=item['list'][i]
        if isinstance(n,str):
            item['list'][i]=nodedict.pop(n)
        if 'list' in item['list'][i].keys():
            nest(item['list'][i])

def weightsum(item):
    if 'list' in item.keys():
        return item['weight']+sum(map(weightsum,item['list']))
    return item['weight']    

def off_weight(node,parentdiff=0):
    weightlist=[weightsum(node['list'][i]) for i in range(len(node['list']))]
    a,b=max(weightlist),min(weightlist)
    if a==b:
        return node['name'],node['weight']-parentdiff
    elif len(weightlist)>2 and weightlist.count(a)==1:
        return off_weight(node['list'][weightlist.index(a)],a-b)
    elif len(weightlist)>2 and weightlist.count(b)==1:
        return off_weight(node['list'][weightlist.index(b)],b-a)
    elif len(weightlist)==2:
        raise NotImplementedError

if __name__=='__main__':
    with open('input7.txt') as fp:
        programs=list(map(str.strip,fp.readlines()))
    find_root(programs)
    keylist=list(nodedict.keys())
    for k in keylist:
        try:
            nest(nodedict[k])
        except KeyError:
            pass
    bottom=nodedict[list(nodedict.keys())[0]]
    print('Part 1: bottom program is',bottom['name'])
    a,b=off_weight(bottom)
    print('Part 2: {} should weigh {}'.format(a,b))
