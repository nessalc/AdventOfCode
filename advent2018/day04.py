#Advent of Code
#Day 4: Repose Record

import re

filename='input04.txt'
f=open(filename)
pat=re.compile(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)')
guard_records=sorted(map(str.strip,f.readlines()))
f.close()
guard_data={}
guard_no,down,up=-1,-1,-1
for line in guard_records:
    m=pat.match(line)
    try:
        y,m,d,H,M,event=m.groups()
        if event[:5]=='Guard':
            guard_no=int(re.search(r'\d+',event).group())
        elif event[:5]=='falls':
            down=int(M)
        elif event[:5]=='wakes':
            up=int(M)
            if guard_no in guard_data.keys():
                guard_data[guard_no]['times'].append((down,up))
            else:
                guard_data[guard_no]={'times':[(down,up)]}
            try:
                guard_data[guard_no]['time_asleep']+=(up-down)
            except KeyError:
                guard_data[guard_no]['time_asleep']=(up-down)
    except AttributeError:
        pass
for k,v in guard_data.items():
    guard_data[k]['sleepiness']={}
    for i in range(60):
        guard_data[k]['sleepiness'][i]=0
    for down,up in guard_data[k]['times']:
        for i in range(down,up):
            guard_data[k]['sleepiness'][i]+=1
sleepiest=max(guard_data.items(),key=lambda x:x[1]['time_asleep'])
sleepy=sleepiest[0]
sleepys_minute=max(sleepiest[1]['sleepiness'].items(),key=lambda x:x[1])[0]
print('The sleepiest guard is #{}.'.format(sleepy))
print('He is asleep the most on minute {}.'.format(sleepys_minute))
print('(The applicable product for AoC is {})'.format(sleepy*sleepys_minute))
most_predictable=max(guard_data.items(),key=lambda x:max(x[1]['sleepiness'].items(),key=lambda x:x[1])[1])
dopey=most_predictable[0]
dopeys_minute=max(most_predictable[1]['sleepiness'].items(),key=lambda x:x[1])[0]
print('The most predictable guard is #{}.'.format(dopey))
print('He is asleep the most on minute {}.'.format(dopeys_minute))
print('(The applicable product for AoC is {})'.format(dopey*dopeys_minute))
