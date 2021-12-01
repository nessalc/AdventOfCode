from itertools import chain,combinations
from more_itertools import windowed

XMAS_Code=list(map(int,open('day9.txt').readlines()))
#XMAS_Code=[35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,2,9,299,277,309,576]

def find_invalid(XMAS_Code,window_size):
    windows=zip(list(windowed(XMAS_Code,window_size)),XMAS_Code[window_size:])
    for x in windows:
        if x[1] not in map(sum,combinations(x[0],2)):
            invalid=x[1]
            break
    return invalid

def find_contiguous_sum(XMAS_Code,target):
    target_found=False
    result_list=[]
    for i in range(2,len(XMAS_Code)+1):
        for x in windowed(XMAS_Code,i):
            if sum(x)==target:
                target_found=True
                result_list=x
                break
        if target_found:
            break
    return result_list

invalid=find_invalid(XMAS_Code,25)
print(invalid)
contig_list=find_contiguous_sum(XMAS_Code,invalid)
print(min(contig_list)+max(contig_list))
