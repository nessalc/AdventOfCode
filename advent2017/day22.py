import operator
# Langton's Ant

#define tuple addition
def pos_add(a,b):
    return tuple(map(operator.add,a,b))

#import map
filename='input22.txt'
f=open(filename)
lines=f.readlines()
f.close()
#assume square
S=len(lines)//2
pos=(-S,S)
matrix={}
for line in map(str.strip,lines):
    for char in line:
        if char=='.':
            #this can be ignored--it is "off" and nonexistent items will be assumed to be off.
            pass
        elif char=='#':
            matrix[pos]='#'
        else:
            raise ValueError('invalid pattern character!')
        pos=pos_add(pos,(1,0)) #move "right" along x axis
    pos=pos_add(pos,(-S*2-1,-1)) #move "down" along y axis, and back to the beginning

#test matrix
#matrix={(-1, 0):'#',
#        ( 1, 1):'#',
#        (-4, 4):'.',
#        ( 4,-3):'.'}

def print_screen(matrix,pos=(0,0)):
    x,y=zip(*matrix.keys())
    minx,maxx,miny,maxy=min(x),max(x),min(y),max(y)
    for y in range(maxy,miny-1,-1):
        for x in range(minx,maxx+1):
            try:
                print((matrix[(x,y)] if (x,y)!=pos else 'X'),end='')
            except KeyError:
                print('.',end='')
        print()

x,y=zip(*matrix.keys())
minx,maxx,miny,maxy=min(x),max(x),min(y),max(y)
print(minx,maxx,miny,maxy)
print_screen(matrix)

ant_pos=(0,0)
direction=(0,1)
iterations=10000000
count=0
evolved=True
directions=[(0,1),(1,0),(0,-1),(-1,0)]
for i in range(iterations):
    try:
        m=matrix[ant_pos]
    except KeyError:
        m='.'
    d_index=directions.index(direction)
    if m=='.':
        direction=directions[(d_index-1)%4]
        m=('W' if evolved else '#')
        if not evolved:
            count+=1
    elif m=='W':
        m='#' #can't get here if not evolved
        count+=1
    elif m=='#':
        direction=directions[(d_index+1)%4]
        m=('F' if evolved else '.')
    elif m=='F':
        direction=directions[(d_index+2)%4]
        m='.' #can't get here if not evolved
    matrix[ant_pos]=m
    ant_pos=pos_add(ant_pos,direction)
    if i%100000==0:
        print('.',end='')

print(count)

# copy answer to clipboard
try:
    import pyperclip
    pyperclip.copy(count)
except ModuleNotFoundError:
    pass
