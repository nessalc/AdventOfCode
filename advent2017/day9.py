#Advent of Code 2017
#Day 9: Stream Processing

import re

def remove_garbage(data_stream):
    #remove cancelled characters first
    data_stream=re.sub('!.','',data_stream)
    return re.sub('<.*?(?<!!)>','',data_stream)

def is_balanced(data_stream):
    return data_stream.count('{')==data_stream.count('}')

def score(data_stream):
    s=total=0
    for c in data_stream:
        if c=='{':
            s+=1
        if c=='}':
            total+=s
            s-=1
    return total

def count_garbage(data_stream):
    #remove cancelled characters first
    data_stream=re.sub('!.','',data_stream)
    count=0
    for m in re.finditer('<.*?(?<!!)>',data_stream):
        span=m.span()
        count+=(span[1]-span[0]-2)
    return count
