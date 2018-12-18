import re
from itertools import chain
from copy import deepcopy
step_list,requirements=[],{}
f=open('input07.txt')
for line in f.readlines():
    step_list.append(re.findall(r'\b[A-Z]\b',line))
f.close()
for n,k in step_list:
    if k in requirements.keys():
        requirements[k].append(n)
    else:
        requirements[k]=[n]
requirements2=deepcopy(requirements)
completed_steps=[]
to_delete=[]
all_steps=set(chain(*step_list))
dependent_steps=set(requirements.keys())
while dependent_steps:
    available_steps=all_steps-dependent_steps-set(completed_steps)
    current_step=sorted(list(available_steps))[0]
    completed_steps.append(current_step)
    for k,v in requirements.items():
        if current_step in v:
            v.remove(current_step)
        if not v:
            to_delete.append(k)
    if to_delete:
        for k in to_delete:
            del requirements[k]
        to_delete=[]
    dependent_steps=set(requirements.keys())
available_steps=all_steps-dependent_steps-set(completed_steps)
if available_steps:
    completed_steps+=sorted(list(available_steps))
print(''.join(completed_steps))
worker_count=5
offset=4
workers=[None]*worker_count
requirements=requirements2
dependent_steps=set(requirements.keys())
done=''
in_progress=['']*worker_count
t=0
available_steps=all_steps-dependent_steps-set(in_progress)-set(done)
while dependent_steps or available_steps or set(in_progress)!=set(['']):
    free_workers=workers.count(None)
    #give steps to workers:
    for f in sorted(list(available_steps))[:free_workers]:
        i=workers.index(None)
        workers[i]=[f,ord(f)-offset]
        in_progress[i]=f
    #print row:
    print(t,'\t'.join(map(lambda x:x[0] if x else '.',workers)),done,sep='\t')
    #tick:
    for w in range(worker_count):
        if workers[w]:
            workers[w][1]-=1
            if not workers[w][1]:
                done+=workers[w][0]
                workers[w]=None
                in_progress[w]=''
    t+=1
    for job in done:
        for k,v in requirements.items():
            if job in v:
                v.remove(job)
            if not v:
                to_delete.append(k)
    if to_delete:
        for k in to_delete:
            try:
                del requirements[k]
            except KeyError:
                pass
    dependent_steps=set(requirements.keys())
    available_steps=all_steps-dependent_steps-set(in_progress)-set(done)
print(t,'\t'.join(map(lambda x:x[0] if x else '.',workers)),done,sep='\t')
