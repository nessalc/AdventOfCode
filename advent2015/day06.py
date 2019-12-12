
def follow_light_instructions(filename):
    lightgrid=[0 for x in range(1000000)]
    f=open(filename)
    s=f.readlines()
    f.close()
    for instruction in s:
        step=instruction.split()
        if step[0]=='turn':
            if step[1]=='on':
                action=1
            else:
                action=0
            coord1,coord2=tuple(map(int,step[2].split(','))),tuple(map(int,step[4].split(',')))
            for x in range(coord1[0],coord2[0]+1):
                for y in range(coord1[1],coord2[1]+1):
                    lightgrid[x+1000*y]=action
        if step[0]=='toggle':
            coord1,coord2=tuple(map(int,step[1].split(','))),tuple(map(int,step[3].split(',')))
            for x in range(coord1[0],coord2[0]+1):
                for y in range(coord1[1],coord2[1]+1):
                    lightgrid[x+1000*y]=not lightgrid[x+1000*y]
    return lightgrid.count(1)

def follow_translated_light_instructions(filename):
    lightgrid=[0 for x in range(1000000)]
    f=open(filename)
    s=f.readlines()
    f.close()
    for instruction in s:
        step=instruction.split()
        if step[0]=='turn':
            if step[1]=='on':
                action=1
            else:
                action=-1
            coord1,coord2=tuple(map(int,step[2].split(','))),tuple(map(int,step[4].split(',')))
        if step[0]=='toggle':
            action=2
            coord1,coord2=tuple(map(int,step[1].split(','))),tuple(map(int,step[3].split(',')))
        for x in range(coord1[0],coord2[0]+1):
            for y in range(coord1[1],coord2[1]+1):
                lightgrid[x+1000*y]=max(lightgrid[x+1000*y]+action,0)
    return sum(lightgrid)
