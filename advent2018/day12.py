import re

f=open('input12.txt')
init=f.readline().strip()[15:]
f.readline()
##Naive solution, works for part 1, forget about part 2.
##gens=20
##rules={}
##for line in f.readlines():
##    a,b=re.findall('[#\.]+',line)
##    rules[a]=b
##print(rules)
##gen='.'*gens+init+'.'*gens
##def next_gen(prev_gen):
##    gen='..'
##    for i in range(2,len(prev_gen)-1):
##        pattern=prev_gen[i-2:i+3]
##        if pattern in rules.keys():
##            gen+=rules[pattern]
##        else: #for test/example
##            gen+='.'
##    gen+='..'
##    return gen
###print(gen)
##for i in range(gens):
##    if i%500000000==0:
##        print('.',end='')
##    prev_gen,gen=gen,next_gen(gen)
##    #print(gen)
##total=0
##for c in range(len(gen)):
##    if gen[c]=='#':
##        total+=c-gens
##print(total)

#parse rules
rules=[]
for line in f.readlines():
    a,b=re.findall('[#\.]+',line)
    if b=='#':
        rules.append(list(map(lambda c:c=='#',a)))
#initialize
current_gen=[]
for idx in range(len(init)):
    if init[idx]=='#':
        current_gen.append(idx)
min_pot,max_pot=current_gen[0],current_gen[-1]
gens=500 #should be enough for periodicity (143 for my input)
#print(''.join('#' if j in current_gen else '.' for j in range(current_gen[-1]+1)))
for i in range(gens):
    prev_gen,current_gen=current_gen,[]
    for j in range(min_pot-2,max_pot+2):
        for k in rules:
            if all((j+l-2 in prev_gen) if k[l] else (j+l-2 not in prev_gen) for l in range(5)):
                current_gen.append(j)
    #print(''.join('#' if j in current_gen else '.' for j in range(current_gen[-1]+1)))
    if i==19:
        print('After {} generations, the sum of the pots with plants is {}.'.format(i+1,sum(current_gen)))
    min_pot,max_pot=current_gen[0],current_gen[-1]
    #print(i,sum(current_gen)-sum(prev_gen)) #find out how long to get periodicity
period=sum(current_gen)-sum(prev_gen)
absurd=50000000000
print('After {} generations, the sum of the pots with plants is {}.'.format(absurd,sum(current_gen)+(absurd-gens)*period))
