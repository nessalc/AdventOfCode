import re

f=r'C:\users\c41663\Documents\programming\advent2015\input16.txt'

def which_sue(filename):
    f=open(filename)
    s=f.readlines()
    f.close()
    sue_list=[]
    for sue in s:
        parse=re.split('[^\d\w]+',sue)
        sue_list.append(dict(zip(parse[2::2],map(int,parse[3::2]))))
    sue_data={'children':3,
              'cats':7,
              'samoyeds':2,
              'pomeranians':3,
              'akitas':0,
              'vizslas':0,
              'goldfish':5,
              'trees':3,
              'cars':2,
              'perfumes':1}
    for sue in range(len(sue_list)):
        for prop,val in sue_list[sue].items():
            if val!=sue_data[prop]:
                break
            if prop==list(sue_list[sue].keys())[-1]:
                actual_sue1=sue+1
    for sue in range(len(sue_list)):
        for prop,val in sue_list[sue].items():
            if (prop in ['cats','trees'] and val<=sue_data[prop]) or \
               (prop in ['pomeranians','goldfish'] and val>=sue_data[prop]) or \
               (prop not in ['cats','trees','pomeranians','goldfish'] and val!=sue_data[prop]):
                break
            if prop==list(sue_list[sue].keys())[-1]:
                actual_sue2=sue+1
    return actual_sue1,actual_sue2
