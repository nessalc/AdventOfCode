#parse map
f=open('input13.txt')
infile=f.readlines()
f.close()
size=len(infile)
track=[[' ' for x in range(size)] for y in range(size)]
carts=[]
directions='^>v<'
for y in range(size):
    for x in range(size):
        if infile[y][x] in '/\\+-|':
            track[y][x]=infile[y][x]
        elif infile[y][x] in '<>':
            track[y][x]='-'
            carts.append({'direction':infile[y][x],
                          'coords':(x,y),
                          'next_turn':-1,
                          'crashed':False})
        elif infile[y][x] in 'v^':
            track[y][x]='|'
            carts.append({'direction':infile[y][x],
                          'coords':(x,y),
                          'next_turn':-1,
                          'crashed':False})
#print('\n'.join(''.join(track[y][x] for x in range(size)) for y in range(size)))
def tick():
    global carts
    carts.sort(key=lambda x:(x['coords'][1],x['coords'][0]))
    crashed_coords=[]
    for cart in carts:
        if cart['crashed']:
            continue
        dir_=cart['direction']
        coords=cart['coords']
        next_turn=cart['next_turn']
        if dir_=='<':
            cart['coords']=coords[0]-1,coords[1]
        elif dir_=='>':
            cart['coords']=coords[0]+1,coords[1]
        elif dir_=='v':
            cart['coords']=coords[0],coords[1]+1
        elif dir_=='^':
            cart['coords']=coords[0],coords[1]-1
        crashes=list(filter(lambda c:c['coords']==cart['coords'],carts))
        if len(crashes)>1:
            print('Crash! At {}'.format(cart['coords']))
            for cart in crashes:
                cart['crashed']=True
            continue
        track_piece=track[cart['coords'][1]][cart['coords'][0]]
        if track_piece=='\\':
            if dir_=='v':
                cart['direction']='>'
            elif dir_=='^':
                cart['direction']='<'
            elif dir_=='>':
                cart['direction']='v'
            elif dir_=='<':
                cart['direction']='^'
        elif track_piece=='/':
            if dir_=='v':
                cart['direction']='<'
            elif dir_=='^':
                cart['direction']='>'
            elif dir_=='>':
                cart['direction']='^'
            elif dir_=='<':
                cart['direction']='v'
        elif track_piece=='+':
            cart['direction']=directions[(directions.index(dir_)+next_turn)%4]
            if next_turn<1:
                cart['next_turn']+=1
            else:
                cart['next_turn']=-1
    carts=list(filter(lambda c:c['crashed']==False,carts))
i=0
while len(carts)==17:
    tick()
    i+=1
    if i%100000==0:
        print('.',end='')
while len(carts)>1:
    tick()
    i+=1
    if i%100000==0:
        print('.',end='')
cart=list(filter(lambda c:c['crashed']==False,carts))[0]['coords']
print('Last cart remaining is at {}'.format(cart))
