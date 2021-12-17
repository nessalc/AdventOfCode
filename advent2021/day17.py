# day17.py

from dataclasses import dataclass
import math


@dataclass
class Point:
    x: int
    y: int


class Rectangle:
    point1: Point
    point2: Point

    def __init__(self, point1: Point, point2: Point):
        self.point1 = Point(min(point1.x, point2.x), min(point1.y, point2.y))
        self.point2 = Point(max(point1.x, point2.x), max(point1.y, point2.y))


def step(point: Point, velocity: Point):
    point.x += velocity.x
    point.y += velocity.y
    if velocity.x != 0:
        velocity.x -= int(math.copysign(1, velocity.x))
    velocity.y -= 1


def inside(point: Point, rect: Rectangle):
    return rect.point1.x <= point.x <= rect.point2.x and rect.point1.y <= point.y <= rect.point2.y


def overshoot(point: Point, rect: Rectangle):
    return point.x > rect.point2.x or point.y < rect.point1.y

# test
# target=Rectangle(Point(20,-10),Point(30,-5))


# input
target = Rectangle(Point(150, -129), Point(171, -70))


def test_fire(velocity: Point) -> int | None:
    position: Point = Point(0, 0)
    max_height: int = 0
    step_count: int = 0
    while True:
        step(position, velocity)
        step_count += 1
        max_height = max(max_height, position.y)
        if inside(position, target):
            return max_height
        elif overshoot(position, target):
            return None


def find_valid_x_velocity(target: Rectangle) -> set[int]:
    x = 0
    valid = set()
    while x <= target.point2.x:
        if target.point1.x <= x*(x+1)//2 <= target.point2.x:
            valid.add(x)
        x += 1
    for j in range(1, target.point2.x+1):
        s = j
        k = j-1
        while s <= target.point2.x and k > 0:
            if target.point2.x >= s >= target.point1.x:
                valid.add(j)
                # break
            s += k
            k -= 1
    return valid


minx = 17


def height_after_steps(y_velocity: int, steps: int) -> int:
    return (-steps*steps+steps+2*steps*y_velocity)//2


valid_x = find_valid_x_velocity(target)

valid_y_values = []
for i in range(target.point1.y-1, 1000):
    done = False
    steps = 1
    while not done:
        height = height_after_steps(i, steps)
        if target.point1.y <= height <= target.point2.y:
            valid_y_values.append(i)
            done = True
        if height < target.point1.y:
            done = True
        steps += 1
myv = max(valid_y_values)
print(myv*(myv+1)//2)

count = 0
for x in valid_x:
    for y in range(target.point1.y-1, 1000):
        if test_fire(Point(x, y)) is not None:
            count += 1
    print('.', end='')
print(f'\n{count}')
