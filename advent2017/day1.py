#Advent of Code 2017
#Day 1: Inverse Captcha

def millisecond1(input_file):
    with open(input_file) as fp:
        instring=fp.readline().strip()
    print('Part 1:',captcha1(instring))
    print('Part 2:',captcha2(instring))

def captcha1(string):
    result=0
    l=len(string)
    for i in range(l):
        if string[i]==string[(i+1)%l]:
            result+=int(string[i])
    return result

def captcha2(string):
    result=0
    l=len(string)
    for i in range(l):
        if string[i]==string[(i+l//2)%l]:
            result+=int(string[i])
    return result
