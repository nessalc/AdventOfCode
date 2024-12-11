import regex as re

with open(r'C:\Users\c41663\Documents\programming\AdventOfCode\advent2024\day04.txt') as fp:
    word_search=fp.readlines()

count=0

word_search=list(map(str.strip,word_search))

# assume square:

size=len(word_search)

word_search_transpose=[]

for i in range(size):
    word_search_transpose.append(''.join([word_search[x][i] for x in range(size)]))

count=sum([line.count('XMAS')+line.count('SAMX') \
           for line \
           in word_search\
           +word_search_transpose\
           ])

xmas1=re.compile(f'X.{{{size+1}}}M.{{{size+1}}}A.{{{size+1}}}S',re.S)
xmas2=re.compile(f'S.{{{size+1}}}A.{{{size+1}}}M.{{{size+1}}}X',re.S)
xmas3=re.compile(f'X.{{{size-1}}}M.{{{size-1}}}A.{{{size-1}}}S',re.S)
xmas4=re.compile(f'S.{{{size-1}}}A.{{{size-1}}}M.{{{size-1}}}X',re.S)

count+=len(xmas1.findall('\n'.join(word_search),overlapped=True))
count+=len(xmas2.findall('\n'.join(word_search),overlapped=True))
count+=len(xmas3.findall('\n'.join(word_search),overlapped=True))
count+=len(xmas4.findall('\n'.join(word_search),overlapped=True))

part1=count

count=0

xmas1=re.compile(f'M.M.{{{size-1}}}A.{{{size-1}}}S.S',re.S)
xmas2=re.compile(f'M.S.{{{size-1}}}A.{{{size-1}}}M.S',re.S)
xmas3=re.compile(f'S.M.{{{size-1}}}A.{{{size-1}}}S.M',re.S)
xmas4=re.compile(f'S.S.{{{size-1}}}A.{{{size-1}}}M.M',re.S)

count+=len(xmas1.findall('\n'.join(word_search),overlapped=True))
count+=len(xmas2.findall('\n'.join(word_search),overlapped=True))
count+=len(xmas3.findall('\n'.join(word_search),overlapped=True))
count+=len(xmas4.findall('\n'.join(word_search),overlapped=True))

part2=count

print(f'Solution to Part 1: {part1}')
print(f'Solution to Part 2: {part2}')
