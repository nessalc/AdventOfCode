from PIL import Image
import random
import itertools
import re
nx,ny=[],[]
f=open('input06.txt')
for l in f.readlines():
    x,y=map(int,re.match('(\d+), (\d+)',l).groups())
    nx.append(x)
    ny.append(y)
f.close()
def dist(x,y):
    return abs(x)+abs(y)
def voronoi(w,h,nx,ny,distance_fn):
    image = Image.new("RGB", (w, h))
    putpixel = image.putpixel
    size=len(nx)
    nr = [random.randrange(1,256) for s in range(size)]
    ng = [random.randrange(1,256) for s in range(size)]
    nb = [random.randrange(1,256) for s in range(size)]
    colorcount={}
    for y in range(h):
        for x in range(w):
            dmin = distance_fn(w-1, h-1)
            j = -1
            for i in range(len(nx)):
                d = distance_fn(nx[i]-x, ny[i]-y)
                if d < dmin:
                    dmin = d
                    j = i
                    putpixel((x, y), (nr[j], ng[j], nb[j]))
                    try:
                        colorcount[(nr[j], ng[j], nb[j])]+=1
                    except KeyError:
                        colorcount[(nr[j], ng[j], nb[j])]=1
                elif d==dmin:
                    putpixel((x,y),(0,0,0))
    image.save("output.png", "PNG")
    #image.show()
    return image
maxx,maxy=max(nx),max(ny)
x_size,y_size=maxx*2,maxy*2
x_offset,y_offset=maxx//2,maxy//2
img=voronoi(x_size,y_size,list(map(lambda x:x_offset+x,nx)),list(map(lambda y:y_offset+y,ny)),dist)
img=img.quantize(len(nx)+1)
ib=img.tobytes()
edgecolors=set(ib[:img.width]+ib[::img.width]+ib[img.width-1::img.width]+ib[-img.width:])
for c in edgecolors:
    ib=ib.replace(bytes([c]),b'')
largest_area=max(ib.count(bytes([c])) for c in set(ib))
print(largest_area)
def distance_area(w,h,nx,ny,threshhold,distance_fn):
    coords=list(zip(nx,ny))
    area_size=0
    for y in range(h):
        for x in range(w):
            if sum(list(map(lambda x:distance_fn(x[0],x[1]),[(c[0]-x,c[1]-y) for c in coords])))<threshhold:
                area_size+=1
    return area_size
da=distance_area(x_size,y_size,list(map(lambda x:x_offset+x,nx)),list(map(lambda y:y_offset+y,ny)),10000,dist)
print(da)
