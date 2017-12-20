#Advent of Code 2017
#Day 14: Disk Defragmentation

from day10 import algorithm, gethashstring

def knothash(msg):
    return gethashstring(algorithm(list(range(256)),([ord(c) for c in msg]+[17,31,73,47,23])*64)[0])

def countbits(hexstring):
    bitcount=[0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
    bits=0
    for c in hexstring:
        bits+=bitcount[int(c,16)]
    return bits

def used_squares(key):
    return sum([countbits(knothash(key+'-'+str(i))) for i in range(128)])


def countregions(key):
    pass
