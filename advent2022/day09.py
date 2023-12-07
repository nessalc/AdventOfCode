from dataclasses import dataclass

@dataclass
class Point:
    x:int=0
    y:int=0

    @property
    def pos(self):
        return self.x,self.y

def sign(x):
    if x<0:
        return -1
    return 1

class Head(Point):
    def move(self,direction):
        match direction:
            case 'U':
                self.y+=1
            case 'D':
                self.y-=1
            case 'L':
                self.x-=1
            case 'R':
                self.x+=1

class Tail(Point):
    def __init__(self):
        super().__init__()
        self.history=set()
    def follow(self,pos):
        x,y=pos
        dist_x=x-self.x
        dist_y=y-self.y
        if abs(dist_x)==2 and dist_y==0:
            self.x+=sign(dist_x)
        elif abs(dist_y)==2 and dist_x==0:
            self.y+=sign(dist_y)
        elif (abs(dist_y)==2 and abs(dist_x)) or (abs(dist_x)==2 and abs(dist_y)):
            self.x+=sign(dist_x)
            self.y+=sign(dist_x)
        self.history.add(self.pos)

head=Head()
tail=Tail()

with open('input09.txt') as f:
    directions=f.read().splitlines()

for direction in directions:
    d,s=direction.split()
    #print(direction)
    for i in range(int(s)):
        head.move(d)
        tail.follow(head.pos)
        #print(head.pos,tail.pos)
part1=len(tail.history)
part2=None

print(f'Part 1: {part1}\nPart 2: {part2}')
