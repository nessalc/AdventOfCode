filename='input24.txt'
components=[]
f=open(filename)
for line in f.readlines():
    components.append(tuple(map(int,line.strip().split('/'))))
f.close()
components=set(components)
#can only start with 0
starters=set(filter(lambda x:x[0]==0 or x[1]==0,components))
#remove these
def can_connect(a,b):
    return a==b[0] or a==b[1]
bridges=[]
def build_chains(start,components,bridge_so_far=[]):
    valid=set(filter(lambda x:can_connect(start,x),components-set(bridge_so_far)))
    for c in valid:
        unused_end=(c[1] if c[0]==start else c[0])
        build_chains(unused_end,components,bridge_so_far+[c])
    else:
        bridges.append(bridge_so_far)
build_chains(0,components)
def calc_strength(bridge):
    s=0
    for b in bridge:
        s+=b[0]+b[1]
    return s
strength=list(map(calc_strength,bridges))
strongest=max(strength)
print(strongest)
def calc_length(bridge):
    return len(bridge)
length=list(map(calc_length,bridges))
longest=max(length)
print(longest)
print(list(filter(lambda x:x[0]==longest,zip(length,strength))))
