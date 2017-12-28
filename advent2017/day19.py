#Advent of Code 2017
#Day 19: A Series of Tubes

def collect_symbols(routing_diagram):
    entry_point=routing_diagram[0].index('|')
    x,y=entry_point,0
    xdir,ydir=0,1
    collection,steps='',1
    while 0<=x<len(routing_diagram[y]) and 0<=y<len(routing_diagram):
        try:
            x+=xdir
            y+=ydir
            sym=routing_diagram[y][x]
            if sym=='+':
                #direction change
                #if moving up or down
                if (xdir,abs(ydir))==(0,1):
                    #check left
                    if 0<=x-1<len(routing_diagram[y]) and routing_diagram[y][x-1] not in ' |':
                        #move left
                        xdir,ydir=-1,0
                    elif 0<=x+1<len(routing_diagram[y]) and routing_diagram[y][x+1] not in ' |':
                        #move right
                        xdir,ydir=1,0
                    else:
                        #oh no!
                        raise ValueError('can\'t go anywhere!')
                #if moving right or left
                elif (abs(xdir),ydir)==(1,0):
                    #check up
                    if 0<=y-1<len(routing_diagram) and routing_diagram[y-1][x] not in ' -':
                        #move up
                        xdir,ydir=0,-1
                    elif 0<=y+1<len(routing_diagram) and routing_diagram[y+1][x] not in ' -':
                        #move down
                        xdir,ydir=0,1
                    else:
                        #oh no!
                        raise ValueError('can\'t go anywhere!')
            elif sym in '-|':
                #keep going
                pass
            elif sym==' ':
                break
            else:
                collection+=sym
        except IndexError:
            return collection
        steps+=1
    return collection,steps

if __name__=='__main__':
    input_diagram=list(map(lambda x:x[:-1],open('input19.txt').readlines()))
    #find entrance
    routing_diagram=input_diagram
    print(collect_symbols(routing_diagram))
