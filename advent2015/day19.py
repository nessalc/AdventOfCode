def calibrate(filename):
    f=open(filename)
    s=f.readlines()
    f.close()
    replacement_dict=dict()
    for line in s:
        line=line.strip()
        if line.find('=>')>0:
            t=line.split(' ')
            if t[0] not in replacement_dict.keys():
                replacement_dict[t[0]]=[]
            replacement_dict[t[0]].append(t[2])
        else:
            molecule=line
    molecule_set=set()
    for k,l in replacement_dict.items():
        for t in l:
            index=0
            i=0
            index=molecule[i:].find(k)
            i=index+i+len(k)
            while index>=0:
                molecule_set.add(molecule[:i-len(k)]+t+molecule[i:])
                index=molecule[i:].find(k)
                i=index+i+len(k)
    return len(molecule_set)
def make_medicine(filename):
    f=open(filename)
    s=f.readlines()
    f.close()
    replacement_dict=dict()
    for line in s:
        line=line.strip()
        if line.find('=>')>0:
            t=line.split(' ')
            if t[0] not in replacement_dict.keys():
                replacement_dict[t[0]]=[]
            replacement_dict[t[0]].append(t[2])
        else:
            molecule=line
    molecule_set=set()
    temp=molecule
    steps=0
    while temp!='e':
        for k,l in replacement_dict.items():
            for t in l:
                if t not in temp:
                    continue
                temp=temp.replace(t,k,1)
                steps+=1
    return steps
