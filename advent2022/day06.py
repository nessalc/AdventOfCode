from collections import deque

with open('input06.txt') as f:
    data=f.read().strip()

def count_unique(in_list: list):
    return len(dict(zip(in_list,[in_list.count(i) for i in in_list])))

packet_length=4

d=deque(data[:3],maxlen=packet_length)
for i in range(3,len(data)):
    d.append(data[i])
    if count_unique(d)==packet_length:
        part1=i+1
        break

message_length=14

d=deque(data[:3],maxlen=message_length)
for i in range(3,len(data)):
    d.append(data[i])
    if count_unique(d)==message_length:
        part2=i+1
        break

print(f'Part 1: {part1}\nPart 2: {part2}')
