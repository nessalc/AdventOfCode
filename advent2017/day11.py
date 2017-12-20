#Advent of Code 2017
#Day 11: Hex Ed

import unittest
import itertools

class Part1Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(fewest_steps('ne,ne,ne'),3)
    def test2(self):
        self.assertEqual(fewest_steps('ne,ne,sw,sw'),0)
    def test3(self):
        self.assertEqual(fewest_steps('ne,ne,s,s'),2)
    def test4(self):
        self.assertEqual(fewest_steps('se,sw,se,sw,sw'),3)

def fewest_steps(path):
    if isinstance(path,str):
        path=path.split(',')
    path=reduce_path(path)
    return len(path)

def furthest(path):
    maxdist=0
    if isinstance(path,str):
        path=path.split(',')
    for i in range(len(path)):
        dist=len(reduce_path(path[:i+1]))
        if dist>maxdist:
            maxdist=dist
            print(maxdist,i/len(path))
    return maxdist

def reduce_path(path):
    replace=True
    def condense_walkback(a,b,path,repl=None):
        while a in path and b in path:
            del path[path.index(a)]
            del path[path.index(b)]
            if repl is not None:
                path.append(repl)
    while replace:
        l=len(path)
        condense_walkback('n','s',path)
        condense_walkback('ne','sw',path)
        condense_walkback('se','nw',path)
        condense_walkback('se','sw',path,'s')
        condense_walkback('ne','nw',path,'n')
        condense_walkback('ne','s',path,'se')
        condense_walkback('se','n',path,'ne')
        condense_walkback('nw','s',path,'sw')
        condense_walkback('sw','n',path,'nw')
        if len(path)==l:
            replace=False
    return path

if __name__=='__main__':
    #unittest.main()
    inputstring=open('input11.txt').readline().strip()
    print(fewest_steps(inputstring))
    print(furthest(inputstring))
