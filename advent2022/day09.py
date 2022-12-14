from dataclasses import dataclass
import numpy as np

@dataclass
class Point:
    x:int=0
    y:int=0
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    def distance(self,other):
        return (abs(other.x-self.x)*abs(other.x-self.x)+\
                abs(other.y-self.y)*abs(other.y-self.y))**0.5
    def normal(self,other):
        return abs(other.x-self.x)*abs(other.x-self.x)+\
               abs(other.y-self.y)*abs(other.y-self.y)

class Rope:
    def __init__(self,name='H',knot=None):
        self.H=Point()
        self.T=Point()
        self.tail_collection=set([(self.T.x,self.T.y)])
        self.name=name
        self.knot=knot
    def tail_follow(self):
        if self.H.y-self.T.y==1 and \
           self.H.x-self.T.x==2:
            self.T.x+=1
            self.T.y+=1
        elif self.T.y-self.H.y==1 and \
           self.H.x-self.T.x==2:
            self.T.x+=1
            self.T.y-=1
        elif self.H.y-self.T.y==1 and \
           self.T.x-self.H.x==2:
            self.T.x-=1
            self.T.y+=1
        elif self.T.y-self.H.y==1 and \
           self.T.x-self.H.x==2:
            self.T.x-=1
            self.T.y-=1
        elif self.H.x-self.T.x==1 and \
           self.H.y-self.T.y==2:
            self.T.x+=1
            self.T.y+=1
        elif self.T.x-self.H.x==1 and \
           self.H.y-self.T.y==2:
            self.T.x-=1
            self.T.y+=1
        elif self.H.x-self.T.x==1 and \
           self.T.y-self.H.y==2:
            self.T.x+=1
            self.T.y-=1
        elif self.T.x-self.H.x==1 and \
           self.T.y-self.H.y==2:
            self.T.x-=1
            self.T.y-=1
        elif self.H.x-self.T.x>1:
            self.T.x+=1
        elif self.T.x-self.H.x>1:
            self.T.x-=1
        elif self.H.y-self.T.y>1:
            self.T.y+=1
        elif self.T.y-self.H.y>1:
            self.T.y-=1
        self.tail_collection.add((self.T.x,self.T.y))
        if self.knot:
            self.knot.step_to_position(self.T.x,self.T.y)
    def step_right(self):
        self.H.x+=1
        self.tail_follow()
    def step_left(self):
        self.H.x-=1
        self.tail_follow()
    def step_up(self):
        self.H.y+=1
        self.tail_follow()
    def step_down(self):
        self.H.y-=1
        self.tail_follow()
    def __repr__(self):
        return f'<Rope name:{self.name} H:{self.H}, T:{self.T}>'
    def move_right(self,steps):
        for i in range(steps):
            self.step_right()
    def move_left(self,steps):
        for i in range(steps):
            self.step_left()
    def move_up(self,steps):
        for i in range(steps):
            self.step_up()
    def move_down(self,steps):
        for i in range(steps):
            self.step_down()
    def step_to_position(self,x,y):
        if x>self.H.x and y==self.H.y:
            print(self,'right')
            self.step_right()
        elif y>self.H.y and x==self.H.x:
            print(self,'up')
            self.step_up()
        elif x<self.H.x and y==self.H.y:
            print(self,'left')
            self.step_left()
        elif y<self.H.y and x==self.H.x:
            print(self,'down')
            self.step_down()
        elif x>self.H.x and y>self.H.y:
            print(self,'up/right')
            self.H.x+=1
            self.H.y+=1
            self.tail_follow()
        elif x>self.H.x and y<self.H.y:
            print(self,'down/right')
            self.H.x+=1
            self.H.y-=1
            self.tail_follow()
        elif x<self.H.x and y>self.H.y:
            print(self,'up/left')
            self.H.x-=1
            self.H.y+=1
            self.tail_follow()
        elif x<self.H.x and y<self.H.y:
            print(self,'down/left')
            self.H.x-=1
            self.H.y-=1
            self.tail_follow()

r=Rope('H')
with open('input09.txt') as f:
    directions=f.readlines()
for d,s in map(lambda x:x.strip().split(' '),directions):
    if d=='R':
        r.move_right(int(s))
    elif d=='D':
        r.move_down(int(s))
    elif d=='L':
        r.move_left(int(s))
    elif d=='U':
        r.move_up(int(s))
    else:
        raise ValueError('something is wrong with the input!')

part1=len(r.tail_collection)
part2=None

print(f'Part 1: {part1}\nPart 2: {part2}')
