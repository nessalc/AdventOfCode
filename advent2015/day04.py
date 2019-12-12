import hashlib

in4='ckczppom'

def find_advent_coin(secret_key,zeros_to_start=5):
    md5=hashlib.md5()
    key=bytes(secret_key,'ascii')
    md5.update(key)
    digest=md5.hexdigest()[:zeros_to_start]
    i=0
    most_zeros=0
    while digest!='0'*zeros_to_start:
        temp=md5.copy()
        i+=1
        temp.update(bytes(str(i),'ascii'))
        digest=temp.hexdigest()[:zeros_to_start]
    return i
