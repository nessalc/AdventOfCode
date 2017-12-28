#Advent of Code 2017
#Day 20: Particle Swarm

import re
import math
import copy

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __repr__(self):
        return '<{},{},{}>'.format(self.x,self.y,self.z)
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
    def __abs__(self):
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y and self.z==other.z
    def __getitem__(self,item):
        if item==0:
            return self.x
        elif item==1:
            return self.y
        elif item==2:
            return self.z
        else:
            raise IndexError('Index out of range')
    def __len__(self):
        return 3
    def mdist(self):
        return abs(self.x)+abs(self.y)+abs(self.z)

class Particle:
    def __init__(self,position,velocity,acceleration):
        self.position=Vector(*position)
        self.velocity=Vector(*velocity)
        self.acceleration=Vector(*acceleration)
    def __repr__(self):
        return '<Particle {}>'.format(self.position)
    def distance(self):
        return sum(self.position)
    def update(self):
        self.velocity+=self.acceleration
        self.position+=self.velocity
    def __eq__(self,other):
        return self.position==other.position

def Part1(iterations,particles):
    for i in range(iterations):
        for p in particles:
            p.update()
    ptemp=list(map(lambda x:x.position.mdist(),particles))
    return ptemp.index(min(ptemp))

def Part2(iterations,particles):
    for i in range(iterations):
        for p in particles:
            p.update()
        sps=set([tuple(p.position) for p in particles])
        if len(sps)!=len(particles):
            for sp in sps:
                spp=Particle(sp,(0,0,0),(0,0,0))
                if particles.count(spp)>1:
                    while particles.count(spp)>0:
                        del particles[particles.index(spp)]
    return len(particles)

if __name__=='__main__':
    #particles=[Particle((3,0,0),(2,0,0),(-1,0,0)),
    #           Particle((4,0,0),(0,0,0),(-2,0,0))]
    #particles=[Particle((-6,0,0),( 3,0,0),(0,0,0)),
    #           Particle((-4,0,0),( 2,0,0),(0,0,0)),
    #           Particle((-2,0,0),( 1,0,0),(0,0,0)),
    #           Particle(( 3,0,0),(-1,0,0),(0,0,0))]
    particles=[]
    pb=re.compile('p=< ?(?P<p>-?\d+,-?\d+,-?\d+)>,\s*v=< ?(?P<v>-?\d+,-?\d+,-?\d+)>,\s*a=< ?(?P<a>-?\d+,-?\d+,-?\d+)>')
    for particle in open('input20.txt').readlines():
        pd=pb.match(particle).groupdict()
        particles.append(Particle(eval(pd['p']),eval(pd['v']),eval(pd['a'])))
    print('Part 1: Particle {} will remain closest'.format(Part1(2000,copy.deepcopy(particles))))
    print('Part 2: Only {} particles will remain'.format(Part2(2000,copy.deepcopy(particles))))
