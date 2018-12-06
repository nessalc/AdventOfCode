from PIL import Image,ImageDraw
import random
def voronoi(size,points,palette,distance_fn,draw_points=False,point_size=4):
    w,h=size
    image = Image.new("RGB", size)
    putpixel = image.putpixel
    count=len(points)
    for y in range(h):
        for x in range(w):
            dmin = distance_fn((0,0),(w-1,h-1))
            j = -1
            for i in range(len(points)):
                d = distance_fn(points[i],(x,y))
                if d < dmin:
                    dmin = d
                    j = i
                    putpixel((x, y), palette[j])
    if draw_points:
        draw=ImageDraw.Draw(image)
        point_size//=2
        for x,y in points:
            x0=x-point_size
            y0=y-point_size
            x1=x+point_size
            y1=y+point_size
            draw.ellipse([(x0,y0),(x1,y1)],(0,0,0))
    return image
def euclidean(p1,p2):
    return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5
def manhattan(p1,p2):
    return abs(p2[0]-p1[0])+abs(p2[1]-p1[1])
def chebyshev(p1,p2):
    return max(abs(p2[0]-p1[0]),abs(p2[1]-p1[1]))
def L_N_norm(p1,p2,N):
    return ((p2[0]-p1[0])**N+(p2[1]-p1[1])**N)**(1/N)
def rand_points(bbox,n):
    w,h=bbox
    return [(random.randrange(w),random.randrange(h)) for i in range(n)]
def rand_palette(n):
    colvals = [random.randrange(1,256) for s in range(n*3)]
    palette=list(zip(*[colvals[i::3] for i in range(3)]))
    return palette

if __name__=='__main__':
    size=500,500
    p=25
    points=rand_points(size,p)
    palette=rand_palette(p)
    i1=voronoi(size,points,palette,euclidean,True)
    i2=voronoi(size,points,palette,manhattan,True)
    i3=voronoi(size,points,palette,chebyshev,True)
    img=Image.new('RGB',(size[0]*3,size[1]))
    img.paste(i1,(size[0]*0,0))
    img.paste(i2,(size[0]*1,0))
    img.paste(i3,(size[0]*2,0))
    img.show()
