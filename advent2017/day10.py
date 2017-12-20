#Advent of Code 2017
#Day 10: Knot Hash

from operator import xor
from functools import reduce
import unittest

def rotate_list(twlist,position):
    return twlist[position:]+twlist[:position]

def twist_list(twlist,index,length):
    if index+length<=len(twlist):
        twlist[index:index+length]=reversed(twlist[index:index+length])
    else:
        templist=rotate_list(twlist,index)
        templist[:length]=reversed(templist[:length])
        twlist=rotate_list(templist,-index)
    return twlist

def algorithm(twlist,lengths,index=0,skip_size=0):
    for length in lengths:
        #reverse order of length elements in list
        twlist=twist_list(twlist,index,length)
        #increment index by length plus skip size
        index+=length+skip_size
        #modulo to fix index
        index%=len(twlist)
        #increment skip_size
        skip_size+=1
    return twlist,index,skip_size

def gethashstring(twlist):
    result=[reduce(xor,twlist[16*i:16*i+16]) for i in range(16)]
    hashstring=''
    for c in result:
        hashstring+='{:02x}'.format(c)
    return hashstring

class HashTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(gethashstring(full('')),'a2582a3a0e66e6e86e3812dcb672a272')
    def test_AoC(self):
        self.assertEqual(gethashstring(full('AoC 2017')),'33efeb34ea91902bb2f59c9920caa6cd')
    def test_123(self):
        self.assertEqual(gethashstring(full('1,2,3')),'3efbe78a8d82f29979031a4aa0b16a9d')
    def test_124(self):
        self.assertEqual(gethashstring(full('1,2,4')),'63960835bcdc130f0b66d7ff4f6a5a8e')

if __name__=='__main__':
    inputstring=open('input10.txt').readline().strip()
    #Part 1
    lengths=list(map(int,inputstring.split(',')))
    twlist,i,s=algorithm(list(range(256)),lengths)
    print('Check: {}'.format(twlist[0]*twlist[1]))
    #Part 2
    lengths=[ord(c) for c in inputstring]+[17,31,73,47,23]
    lengths*=64
    twlist,i,s=algorithm(list(range(256)),lengths)
    print('Knot Hash: {}'.format(gethashstring(twlist)))
    #unittest.main()
