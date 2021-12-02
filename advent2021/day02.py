# day02.py

sub_x: int = 0
sub_y: int = 0

with open('input02.txt') as fp:
    for direction in fp.readlines():
        direction, distance = direction.split()
        distance = int(distance)
        match direction:
            case 'forward':
                sub_x += distance
            case 'up':
                sub_y -= distance
            case 'down':
                sub_y += distance

print(sub_x*sub_y)

sub_x: int = 0
sub_y: int = 0
sub_aim: int = 0

with open('input02.txt') as fp:
    for direction in fp.readlines():
        direction, distance = direction.split()
        distance = int(distance)
        match direction:
            case 'forward':
                sub_x += distance
                sub_y += distance*sub_aim
            case 'up':
                sub_aim -= distance
            case 'down':
                sub_aim += distance

print(sub_x*sub_y)
