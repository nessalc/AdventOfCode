trees=list(map(str.strip,open('day3.txt').readlines()))

def check_slope(x,y):
    pos=-x
    encounters=0
    for row in trees[::y]:
        pos=(pos+x)%len(row)
        if row[pos]=='#':
            encounters+=1
    return encounters

print('Part 1:',
      check_slope(3,1))

print('Part 2:',
      check_slope(1,1)
      * check_slope(3,1)
      * check_slope(5,1)
      * check_slope(7,1)
      * check_slope(1,2))
