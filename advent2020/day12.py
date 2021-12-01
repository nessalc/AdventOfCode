import turtle

actions=list(map(str.strip,open('day12.txt').readlines()))
#actions=['F10','N3','F7','R90','F11']

def parse(direction,turtle,waypoint=None):
    d=direction[0]
    cmd=int(direction[1:])
    if waypoint is None:
        oldheading=turtle.heading()
        if d=='N':
            turtle.setheading(90)
        elif d=='W':
            turtle.setheading(180)
        elif d=='S':
            turtle.setheading(270)
        elif d=='E':
            turtle.setheading(0)
        elif d=='L':
            turtle.left(cmd)
        elif d=='R':
            turtle.right(cmd)
        if d in 'NSEWF':
            turtle.forward(cmd)
        if d in 'NSEW':
            turtle.setheading(oldheading)
    else:
        #print(direction,end=' ')
        if d=='N':
            waypoint.setheading(90)
        elif d=='W':
            waypoint.setheading(180)
        elif d=='S':
            waypoint.setheading(270)
        elif d=='E':
            waypoint.setheading(0)
        elif d=='R':
            waypoint.setheading(turtle.towards(waypoint)+90)
            waypoint.circle(waypoint.distance(turtle),-cmd)
            #print(waypoint.pos(),turtle.pos())
        elif d=='L':
            waypoint.setheading(turtle.towards(waypoint)+90)
            waypoint.circle(waypoint.distance(turtle),cmd)
            #print(waypoint.pos(),turtle.pos())
        if d in 'NSEW':
            waypoint.forward(cmd)
            x,y=waypoint.pos()-turtle.pos()
            #print(waypoint.pos(),turtle.pos())
        elif d=='F':
            x,y=waypoint.pos()-turtle.pos()
            turtle.setheading(turtle.towards(waypoint))
            turtle.forward(turtle.distance(waypoint)*cmd)
            #print(turtle.distance(waypoint)*cmd)
            waypoint.goto(turtle.pos()+(x,y))
    #print('.',end='')

t=turtle.Turtle()
t.speed(0)

t.screen.screensize(75000,75000)

w=turtle.Turtle(shape='circle')
w.ht()
w.pu()

for d in actions:
    parse(d,t)

pos=t.pos()
print(pos,round(abs(pos[0])+abs(pos[1])))

t.pu()
t.home()
t.pd()
t.color('blue')

w.goto(10,1)
w.st()
w.shapetransform(0.2,0,0,0.2)
w.speed(0)

for d in actions:
    parse(d,t,w)

pos=t.pos()
print(pos,round(abs(pos[0])+abs(pos[1])))
