#Advent of Code
#Day 1:

filename='input01.txt'
f=open(filename)
freqlist=list(map(int,map(str.strip,f.readlines())))
f.close()
n=sum(freqlist)
print('Running diagnostics...')
print('One round of frequency changes, starting from 0, results in a frequency of {}.'.format(n))
i=0
n=freqlist[0]
caliblist=[]
l=len(freqlist)
print('Calibrating...')
print('Hang on, this could take a while...')
while n not in caliblist:
    caliblist.append(n)
    i=(i+1)%l
    n+=freqlist[i]
print('The first frequency reached twice is {}.'.format(n))
print('Calibration complete!')
