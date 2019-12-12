import copy

#f=r'C:\users\c41663\Documents\programming\advent2015\input18test.txt'
f=r'C:\users\c41663\Documents\programming\advent2015\input18.txt'

def neighborcount(lights,coords):
    x,y=coords
    lightcount=0
    for tx in range(-1,2):
        for ty in range(-1,2):
            try:
                if (tx==0 and ty==0) or (x+tx)<0 or (y+ty)<0:
                    continue
                if lights[x+tx][y+ty]:
                    lightcount+=1
            except IndexError:
                pass
    return lightcount
def lightshow(filename,steps,stuck_coords=[],stuck_state=1):
    f=open(filename)
    s=f.readlines()
    f.close()
    xr,yr=range(len(s)),range(len(s[0])-1)
    lights=[[(1 if s[x][y]=='#' else 0) for y in yr] for x in xr]
    for sx,sy in stuck_coords:
        lights[sx][sy]=stuck_state
    nextlights=copy.deepcopy(lights)
    for n in range(steps):
        for x in xr:
            for y in yr:
                if lights[x][y]:
                    nextlights[x][y]=(1 if neighborcount(lights,(x,y)) in [2,3] else 0)
                else:
                    nextlights[x][y]=(1 if neighborcount(lights,(x,y))==3 else 0)
        for sx,sy in stuck_coords:
            nextlights[sx][sy]=stuck_state
        lights=copy.deepcopy(nextlights)
    return nextlights
def displaylights(lights):
    for x in range(len(lights)):
        for y in range(len(lights[x])):
            if lights[x][y]:
                print('#',end='')
            else:
                print('.',end='')
        print()
    return
def countlights(lights):
    return sum([sum(lights[x]) for x in range(len(lights))])
