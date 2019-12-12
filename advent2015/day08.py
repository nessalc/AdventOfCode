import re
f=r'C:\Users\c41663\Documents\programming\advent2015\input08.txt'
def encoded_less_characters(filename):
    f=open(filename)
    string_array=f.readlines()
    f.close()
    whitespace=re.compile('\s*')
    for i in range(len(string_array)):
        string_array[i]=whitespace.sub('',string_array[i])
    return sum(map(len,string_array))-sum(map(lambda s:len(eval(s)),string_array))
def reencoded_less_encoded(filename):
    f=open(filename)
    string_array=f.readlines()
    f.close()
    whitespace=re.compile('\s*')
    for i in range(len(string_array)):
        string_array[i]=whitespace.sub('',string_array[i])
    return sum(map(lambda s:len(re.escape(s))+2,string_array))-sum(map(len,string_array))
