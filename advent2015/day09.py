import itertools

ftest=r'C:\Users\c41663\Documents\programming\advent2015\input09test.txt'
f=r'C:\Users\c41663\Documents\programming\advent2015\input09.txt'

def shortest_distance(filename):
    f=open(filename)
    s=f.readlines()
    f.close()
    l=int((len(s)*2)**0.5)+1
    distances=[[None for x in range(l)] for x in range(l)]
    locations=[]
    for line in s:
        t=line.split()
        if t[0] not in locations:
            locations.append(t[0])
        if t[2] not in locations:
            locations.append(t[2])
        distances[locations.index(t[0])][locations.index(t[2])]=int(t[4])
    mindistance=1000000000000000
    for route in itertools.permutations(range(l)):
        distance=0
        for i in range(len(route)-1):
            city1,city2=route[i],route[i+1]
            try:
                distance+=distances[city1][city2]
            except TypeError:
                distance+=distances[city2][city1]
        mindistance=min(mindistance,distance)
    return mindistance

def longest_distance(filename):
    f=open(filename)
    s=f.readlines()
    f.close()
    l=int((len(s)*2)**0.5)+1
    distances=[[None for x in range(l)] for x in range(l)]
    locations=[]
    for line in s:
        t=line.split()
        if t[0] not in locations:
            locations.append(t[0])
        if t[2] not in locations:
            locations.append(t[2])
        distances[locations.index(t[0])][locations.index(t[2])]=int(t[4])
    maxdistance=0
    for route in itertools.permutations(range(l)):
        distance=0
        for i in range(len(route)-1):
            city1,city2=route[i],route[i+1]
            try:
                distance+=distances[city1][city2]
            except TypeError:
                distance+=distances[city2][city1]
        maxdistance=max(maxdistance,distance)
    return maxdistance
