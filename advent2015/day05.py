import re

def naughty_or_nice1(filename):
    f=open(filename)
    santas_list=f.readlines()
    f.close()
    nicecount=0
    for string in santas_list:
        test1=re.findall('[aeiou]',string)
        test2=re.findall('(?P<double>[a-z])(?P=double)',string)
        test3=re.findall('ab|cd|pq|xy',string)
        if len(test1)>=3 and len(test2)>=1 and len(test3)==0:
            nicecount+=1
    return nicecount

def naughty_or_nice2(filename):
    f=open(filename)
    santas_list=f.readlines()
    f.close()
    nicecount=0
    for string in santas_list:
        test1=re.findall('(?P<double>[a-z]{2}).*(?P=double)',string)
        test2=re.findall('(?P<middle>[a-z])[a-z](?P=middle)',string)
        if len(test1)>=1 and len(test2)>=1:
            nicecount+=1
    return nicecount
