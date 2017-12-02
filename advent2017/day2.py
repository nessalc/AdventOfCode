import itertools
def row_checksum(num_list):
    return max(num_list)-min(num_list)
def sheet_checksum(filename):
    with open(filename) as fp:
        sheet=fp.readlines()
    checksum=0
    for r in sheet:
        checksum+=row_checksum(list(map(int,r.strip().split('\t'))))
    return checksum
def row_divisibility(num_list):
    for a,b in itertools.combinations(num_list,2):
        if a>b and a//b==a/b:
            return a//b
        elif b>a and b//a==b/a:
            return b//a
        else:
            pass
def sheet_divisibility(filename):
    with open(filename) as fp:
        sheet=fp.readlines()
    total=0
    for r in sheet:
        total+=row_divisibility(list(map(int,r.strip().split('\t'))))
    return total
