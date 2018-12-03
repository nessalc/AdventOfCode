import re
from itertools import chain

filename='input21.txt'
iterations=18

init='.#./..#/###'

pattern_dict={}
f=open(filename)
for a,b,*rest in map(lambda s:re.split(r' => ',s),map(str.strip,f.readlines())):
    pattern_dict[a]=b
f.close()

def split(pattern):
    size=pattern.find('/')
    p=[]
    if size%2==0:
        S=2
    elif size%3==0:
        S=3
    else:
        raise ValueError('invalid pattern size')
    if size==S:
        return [pattern]
    else:
        s=size//S
        print(' (templist...)')
        pat=pattern.replace('/','')
        templist=[[pat[i*S:i*S+S] for i in range(j*s,(j+1)*s)] for j in range(size)]
        print(' (pattern list...)')
        pattern_list=[['/'.join(templist[k][l] for k in range(S*m,S*m+S)) for l in range(s)] for m in range(s)]
    while isinstance(pattern_list[0],list):
        pattern_list=list(chain(*pattern_list))
    return pattern_list

def print_pattern(pattern):
    for line in pattern.split('/'):
        print(line)

def match(pattern):
    for i in combinations(pattern):
        if i in pattern_dict.keys():
            return pattern_dict[i]
    else:
        raise Exception('pattern not in dictionary!')

def changeup(pattern,axis):
    if isinstance(axis,tuple) or isinstance(axis,list) and len(axis)>1:
        a,*rest=axis
        return changeup(changeup(pattern,a),rest)
    elif isinstance(axis,tuple) or isinstance(axis,list) and len(axis)==1:
        a=axis[0]
        return changeup(pattern,a)
    if axis==0:
        return pattern
    elif axis==1:
        return '/'.join(pattern.split('/')[::-1])
    elif axis==2:
        return '/'.join([x[::-1] for x in pattern.split('/')])
    elif axis==3:
        s=pattern.find('/')+1
        return '/'.join([pattern[n::s] for n in range(s-1)])
    elif axis==4:
        return pattern[::-1]

def combinations(pattern):
    combos=[0,
            3,
            2,
            (3,2),
            (4,3),
            (2,1),
            1,
            (3,1)]
    return map(lambda x:changeup(pattern,x),combos)

def recombine(pattern_list):
    size1=pattern_list[0].find('/')
    size2=int(len(pattern_list)**0.5)
    if size1<0:
        return pattern_list
    elif size2==1:
        return pattern_list[0]
    return '/'.join('/'.join(''.join(pattern_list[i].replace('/','')[j*size1:(j+1)*size1] for i in range(k*size2,(k+1)*size2)) for j in range(size1)) for k in range(size2))

pattern=init
print_pattern(pattern)
print('-'*pattern.find('/'))
for i in range(iterations):
    print(i) #progress indicator
    pl=split(pattern)
    p=[]
    for j in pl:
        p.append(match(j))
    pattern=recombine(p)
    #print_pattern(pattern)
    #print('-'*pattern.find('/'))
count=pattern.count('#')
print('{0} pixels are on after {1} iterations. The final size is {2}{3}{2} pixels.'.format(count,iterations,pattern.find('/'),chr(215)))
try:
    import pyperclip
    pyperclip.copy(count)
except ModuleNotFoundError:
    pass
