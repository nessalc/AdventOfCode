import re

def look_and_say(string,iterations):
    digits=re.compile('(?P<digit>\d)(?P=digit)*')
    for i in range(iterations):
        s=''
        for t in digits.finditer(string):
            s+=str(t.end()-t.start())+t.groups()[0]
        string=s
    return string
