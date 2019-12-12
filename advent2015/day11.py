import string
import re
import itertools

def int_to_base(number,base,digits=string.digits+string.ascii_lowercase+string.ascii_uppercase):
    #borrowed and modified from http://code.activestate.com/recipes/65212/#c8
    if base>len(digits):
        raise ValueError('Not enough digits for given base.')
    return ((number==0 and digits[0]) or (int_to_base(number//base,base,digits).lstrip(digits[0])+digits[number%base]))
def base_to_int(numberstring,base,digits=string.digits+string.ascii_lowercase+string.ascii_uppercase):
    if base>len(digits):
        raise ValueError('Not enough digits for given base.')
    i=0
    count=0
    for c in numberstring[::-1]:
        i+=digits.index(c)*base**count
        count+=1
    return i

def next_password(current_password):
    password=base_to_int(current_password,26,string.ascii_lowercase)
    valid=False
    while not valid:
        password+=1
        strpass=int_to_base(password,26,string.ascii_lowercase).rjust(8,'a')
        if strpass.find('i')>=0:
            strpass=strpass[:strpass.find('i')]+'j'+'a'*(7-strpass.find('i'))
        if strpass.find('l')>=0:
            strpass=strpass[:strpass.find('l')]+'m'+'a'*(7-strpass.find('l'))
        if strpass.find('o')>=0:
            strpass=strpass[:strpass.find('o')]+'p'+'a'*(7-strpass.find('o'))
        password=base_to_int(strpass,26,string.ascii_lowercase)
        valid=True
        #test length
        valid&=(len(strpass)==8)
        #test requirement 1
        straightfound=False
        for straight in map(lambda k:''.join(k),itertools.zip_longest(string.ascii_lowercase[:-2],string.ascii_lowercase[1:-1],string.ascii_lowercase[2:])):
            straightfound|=(strpass.find(straight)>=0)
        valid&=straightfound
        #test requirement 2
        #guaranteed from earlier code
        #test requirement 3
        pairs=re.findall('([a-z])\\1',strpass)
        valid&=(len(pairs)>=2)
        for t in itertools.combinations(pairs,2):
            valid&=(t[0]!=t[1])
    return strpass
