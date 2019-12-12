import os
from dataclasses import dataclass
import itertools

with open(os.path.join(os.curdir, 'advent2019', 'input03.txt')) as file:
    wires = file.readlines()
# wires = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
# wires = ['R75,D30,R83,U83,L12,D49,R71,U7,L72',
#          'U62,R66,U55,R34,D71,R55,D58,R83']
# wires = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
#          'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']


@dataclass
class Point:
    x: float
    y: float

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __abs__(self):
        if self.x == 0:
            return float('inf')
        return self.y/self.x


@dataclass
class LineSegment:
    p1: Point
    p2: Point

    def __abs__(self):
        t = self.p2-self.p1
        if t.x == 0:
            return abs(t.y)
        elif t.y == 0:
            return abs(t.x)
        return (t.x**2+t.y**2)**0.5

    def slope(self):
        return abs(self.p2-self.p1)

    def intersection(self, line):
        if self.slope() == line.slope():
            return None
        p1, p2, q1, q2 = self.p1, self.p2, line.p1, line.p2
        x1, x2, x3, x4, \
            y1, y2, y3, y4 = \
            p1.x, p2.x, q1.x, q2.x, \
            p1.y, p2.y, q1.y, q2.y
        tn = (x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)
        td = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        un = (x1-x2)*(y1-y3)-(y1-y2)*(x1-x3)
        ud = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        if td == 0 or ud == 0:
            return None
        elif 0 <= tn/td <= 1:
            return Point(x1+tn/td*(x2-x1), y1+tn/td*(y2-y1))
        elif 0 <= un/ud <= 1:
            return Point(x3+un/ud*(x4-x3), y3+un/ud*(y4-y3))


def create_path(path_definition):
    path_points = [Point(0, 0)]
    for segment in path_definition.strip().split(','):
        direction, distance = segment[0], int(segment[1:])
        if direction == 'U':
            path_points.append(
                Point(path_points[-1].x, path_points[-1].y+distance))
        elif direction == 'D':
            path_points.append(
                Point(path_points[-1].x, path_points[-1].y-distance))
        elif direction == 'R':
            path_points.append(
                Point(path_points[-1].x+distance, path_points[-1].y))
        elif direction == 'L':
            path_points.append(
                Point(path_points[-1].x-distance, path_points[-1].y))
    path = []
    for i in range(len(path_points)-1):
        path.append(LineSegment(path_points[i], path_points[i+1]))
    return path


def calculate_path_distance(path):
    return sum([abs(p) for p in path])


path1, path2 = create_path(wires[0]), create_path(wires[1])
intersections, steps = [], []
for i in range(len(path1)):
    for j in range(len(path2)):
        int1 = path1[i].intersection(path2[j])
        int2 = path2[j].intersection(path1[i])
        if int1 and int2 and int1 == int2 and int1 != Point(0, 0):
            intersections.append(int1)
            steps.append(
                calculate_path_distance(
                    path1[0:i]+[LineSegment(path1[i-1].p2, int1)]) +
                calculate_path_distance(
                    path2[0:j]+[LineSegment(path2[j-1].p2, int1)]))
mindistance = float('inf')
for point in intersections:
    distance = abs(point.x)+abs(point.y)
    if distance < mindistance:
        mindistance = distance

print('Part 1:', int(mindistance))
print('Part 2:', int(min(steps)))  # this is wrong

for i in range(2):
    wires[i] = [(x[0], int(x[1:])) for x in wires[i].strip().split(',')]

grid = {(0, 0): {'intersection': False,
                 'wire_id': '12',
                 'steps': {1: 0, 2: 0}}}
xdir = {'U': 0, 'D': 0, 'R': 1, 'L': -1}
ydir = {'U': 1, 'D': -1, 'R': 0, 'L': 0}
for wire in range(2):
    x, y = 0, 0
    steps = 0
    for direction, distance in wires[wire]:
        wire_id = wire+1
        for d in range(distance):
            x += xdir[direction]
            y += ydir[direction]
            steps += 1
            if (x, y) in grid.keys() and \
                    str(wire_id) not in grid[(x, y)]['wire_id']:
                grid[(x, y)]['wire_id'] += str(wire_id)
                grid[(x, y)]['intersection'] = True
                grid[(x, y)]['steps'][wire_id] = steps
            elif (x, y) not in grid.keys():
                grid[(x, y)] = {'intersection': False, 'wire_id': str(
                    wire_id), 'steps': {wire_id: steps}}

distances = []
for k, v in grid.items():
    if v['intersection']:
        distance = v['steps'][1]+v['steps'][2]
        distances.append(distance)

print('Part 2:', min(distances))

# part 1 correct answer for my input: 651
# part 2 correct answer for my input: 7534
