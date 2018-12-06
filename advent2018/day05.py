import string

aA=list(map(lambda x:''.join(x),zip(string.ascii_lowercase,string.ascii_uppercase)))

polymer=open('input05.txt').readline().strip()

def react(polymer,strip=None):
    if strip:
        polytemp=polymer.replace(strip[0],'')
        polytemp=polytemp.replace(strip[1],'')
    else:
        polytemp=polymer[:]
    while True:
        count=0
        for pair in aA:
            rev=pair[1]+pair[0]
            count+=polytemp.count(pair)
            count+=polytemp.count(rev)
            polytemp=polytemp.replace(pair,'')
            polytemp=polytemp.replace(rev,'')
        if count==0:
            break
    return len(polytemp)

print(react(polymer))
for c in aA:
    print(c,react(polymer,c),sep='\t')
