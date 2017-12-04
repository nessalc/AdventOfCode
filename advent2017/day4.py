#Advent of Code 2017
#Day 4: High-Entropy Passphrases

def millisecond4(input_file):
    with open(input_file) as fp:
        passphrase_list=list(map(str.strip,fp.readlines()))
    print('Part 1:',valid_count(passphrase_list,False))
    print('Part 2:',valid_count(passphrase_list,True))

def valid_count(passphrase_list,anagrams=False):
    count=0
    for passphrase in passphrase_list:
        test=passphrase.split(' ')
        if anagrams:
            test=list(map(lambda x:''.join(sorted(x)),test))
        if len(test)==len(set(test)):
            count+=1
    return count
