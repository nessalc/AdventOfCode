import re
from functools import reduce
from operator import mul

timestamp,buses=map(str.strip,open('day13.txt').readlines())
timestamp=int(timestamp)
buses=sorted(list(map(int,re.findall('\d+',buses))))
sched=dict()
for bus_id in buses:
    sched[bus_id]=(timestamp//bus_id+1)*bus_id
earliest=sorted(sched.items(),key=lambda x:x[1])[0]
print(earliest[0],earliest[1]-timestamp,earliest[0]*(earliest[1]-timestamp))

_,buses=map(str.strip,open('day13.txt').readlines())
buses=[int(b) if b!='x' else b for b in buses.split(',')]
buses=enumerate(buses)
sched=list(filter(lambda x:x[1]!='x',buses))
def test(sched,timestamp):
    return all([(timestamp+t)%b==0 for t,b in sched])
def eeuclid(a,b):
    r=[a,b]
    s=[1,0]
    t=[0,1]
    while r[-1]!=0:
        q=r[-2]//r[-1]
        r.append(r[-2]-q*r[-1])
        s.append(s[-2]-q*s[-1])
        t.append(t[-2]-q*t[-1])
    return r[-2],s[-2],t[-2]
size=len(sched)
a,n=map(list,zip(*sched))
a=[(n[i]-a[i])%n[i] for i in range(size)]
modulo=reduce(mul,n,1)
nbar=[modulo//x for x in n]
u=[eeuclid(nbar[i],n[i])[1] for i in range(size)]
s=sum([a[i]*nbar[i]*u[i] for i  in range(size)])
print(s%modulo)
