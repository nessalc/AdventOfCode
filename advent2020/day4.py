import re

def convert_to_dict(passport):
    kv=re.finditer('\\b([a-z]{3}):([\w#]+)',passport,flags=re.M | re.S)
    return dict([(match.group(1),match.group(2)) for match in kv])

passports=list(map(lambda x:convert_to_dict(x.replace('\n',' ')),open('day4.txt').read().split('\n\n')))
print(len(passports))
required_keys=['byr','iyr','eyr','hgt','hcl','ecl','pid']

valid=0
for passport in passports:
    if all([k in passport.keys() for k in required_keys]):
        valid+=1
print(valid)

valid=0
for passport in passports:
    if all([k in passport.keys() for k in required_keys]):
        validated=True
        for k,v in passport.items():
            if k=='byr' and not (v.isdecimal() and 1920<=int(v)<=2002):
                validated=False
                break
            elif k=='iyr' and not (v.isdecimal() and 2010<=int(v)<=2020):
                validated=False
                break
            elif k=='eyr' and not (v.isdecimal() and 2020<=int(v)<=2030):
                validated=False
                break
            elif k=='ecl' and v not in ['amb','blu','brn','gry','grn','hzl','oth']:
                validated=False
                break
            elif k=='pid' and not (v.isdecimal() and len(v)==9):
                validated=False
                break
            elif k=='hcl' and not re.search('#[a-f0-9]{6}',v):
                validated=False
                break
            elif k=='hgt' and v[-2:]=='cm' and not (v[:-2].isdecimal() and 150<=int(v[:-2])<=193):
                validated=False
                break
            elif k=='hgt' and v[-2:]=='in' and not (v[:-2].isdecimal() and 59<=int(v[:-2])<=76):
                validated=False
                break
            elif k=='hgt' and v[-2:] not in ['cm','in']:
                validated=False
                break
            #elif k in required_keys:
                #valid+=1
                #print(k,v)
        if validated:
            valid+=1
print(valid)
