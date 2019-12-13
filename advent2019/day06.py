import os

with open(os.path.join(os.curdir, 'advent2019', 'input06.txt')) as file:
    orbits = dict([tuple(x.strip().split(')')[::-1])
                   for x in file.readlines()])


def count_orbits(item):
    if item == 'COM':
        return 0
    else:
        return 1+count_orbits(orbits[item])


def generate_path(item):
    if item == 'COM':
        return []
    else:
        return generate_path(orbits[item])+[orbits[item]]


checksum = 0
for k in orbits.keys():
    checksum += count_orbits(k)
print(checksum)
san_path = generate_path('SAN')
you_path = generate_path('YOU')
for k in set(san_path).intersection(set(you_path)):
    san_path.remove(k)
    you_path.remove(k)
orbit_transfers = len(san_path)+len(you_path)
print(orbit_transfers)
