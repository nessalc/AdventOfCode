f=r'C:\Users\c41663\Documents\programming\advent2015\input14.txt'

def race(filename,time):
    f=open(filename)
    s=f.readlines()
    f.close()
    reindeer={}
    for reindeer_description in s:
        parse=reindeer_description.split()
        reindeer[parse[0]]=(int(parse[3]),int(parse[6]),int(parse[13]))
    max_distance=0
    for r,data in reindeer.items():
        distance=time//(data[1]+data[2])*data[1]*data[0]
        distance+=data[1]*data[0] if time%(data[1]+data[2])>=data[1] else time%(data[1]+data[2])*data[0]
        max_distance=max(max_distance,distance)
    return max_distance

def race_points(filename,time):
    f=open(filename)
    s=f.readlines()
    f.close()
    reindeer={}
    scoreboard={}
    for reindeer_description in s:
        parse=reindeer_description.split()
        reindeer[parse[0]]=(int(parse[3]),int(parse[6]),int(parse[13]))
        scoreboard[parse[0]]=0
    for t in range(1,time+1):
        tempdist={}
        max_distance=0
        for r,data in reindeer.items():
            tempdist[r]=t//(data[1]+data[2])*data[1]*data[0]
            tempdist[r]+=data[1]*data[0] if t%(data[1]+data[2])>=data[1] else t%(data[1]+data[2])*data[0]
            max_distance=max(max_distance,tempdist[r])
        for point in [k for k,v in tempdist.items() if v==max_distance]:
            scoreboard[point]+=1
    return scoreboard
