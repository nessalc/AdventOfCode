#Advent of Code
#Day 10: The Stars Align

import re
from PIL import Image, ImageSequence

class Point:
    def __init__(self,position,velocity):
        self.position=position
        self.velocity=velocity
    def move(self,steps=1):
        self.position=self.position[0]+self.velocity[0]*steps,\
                      self.position[1]+self.velocity[1]*steps

f=open('input10.txt')
points=[]
for line in f.readlines():
    px,py,vx,vy=map(int,re.findall(r'[\-0-9]+',line))
    points.append(Point((px,py),(vx,vy)))
f.close()

images=[]

def plot_all(points,offset):
    i=Image.new('1',(500,500))
    for p in points:
        pos=p.position
        try:
            i.putpixel((pos[0]+offset[0],pos[1]+offset[1]),1)
        except IndexError:
            pass
    return i

def move_all(points,steps=1):
    for p in points:
        p.move(steps)

def plot_time(points,offset,time):
    for t in range(time):
        images.append(plot_all(points,offset))
        move_all(points)
    images[0].save('day10.webp',append_images=images[1:],duration=500,save_all=True,loop=1)
    
bbox=(max(p.position[0] for p in points)-min(p.position[0] for p in points),\
      max(p.position[1] for p in points)-min(p.position[1] for p in points))
move_all(points,10000)
ticks=10000
while bbox[0]>200 and bbox[1]>200:
    move_all(points)
    ticks+=1
    bbox=(max(p.position[0] for p in points)-min(p.position[0] for p in points),\
          max(p.position[1] for p in points)-min(p.position[1] for p in points))
plot_time(points,(100,100),20)
ticks+=19
print(ticks)
