in3=r'C:\Users\c41663\Documents\programming\advent2015\input3.txt'

#part 1
def santa_present_delivery(filename):
    f=open(filename)
    s=f.readline()
    f.close()
    x,y=0,0
    housecount=1
    coordlist=set([(x,y)])
    for direction in s:
        if direction=='>':
            x+=1
        elif direction=='^':
            y+=1
        elif direction=='<':
            x-=1
        elif direction=='v':
            y-=1
        coordlist.add((x,y))
    housecount=len(coordlist)
    return housecount

#part 2
def robosanta_present_delivery(filename):
    f=open(filename)
    s=f.readline()
    f.close()
    x,y=0,0
    housecount=1
    coordlist=[[(x,y)],[(x,y)]]
    for direction_number in range(len(s)):
        deliverer=direction_number%2
        x,y=coordlist[deliverer][-1]
        direction=s[direction_number]
        if direction=='>':
            x+=1
        elif direction=='^':
            y+=1
        elif direction=='<':
            x-=1
        elif direction=='v':
            y-=1
        coordlist[deliverer].append((x,y))
    housecount=len(set(coordlist[0]+coordlist[1]))
    return housecount
