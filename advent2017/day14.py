#Advent of Code 2017
#Day 14: Disk Defragmentation

from day10 import algorithm, gethashstring
from PIL import Image, ImageDraw, ImageMorph

def knot_hash(msg):
    return gethashstring(algorithm(list(range(256)),([ord(c) for c in msg]+[17,31,73,47,23])*64)[0])

def count_bits(hexstring):
    bitcount=[0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
    bits=0
    for c in hexstring:
        bits+=bitcount[int(c,16)]
    return bits

def get_data(key):
    return [knot_hash(key+'-'+str(i)) for i in range(128)]

def used_squares(key):
    return sum(map(count_bits,''.join(get_data(key))))

def draw_disk(key):
    s=''.join(get_data(key))
    b=bytes([int(s[i:i+2],16) for i in range(0,len(s),2)])
    return Image.frombytes('1',(128,128),b)

def count_regions(key):
    image=draw_disk(key)
    on_pixels=ImageMorph.MorphOp().get_on_pixels(image.convert('L'))
    image=image.convert('RGB')
    region_count=0
    for x,y in on_pixels:
        if image.getpixel((x,y))!=(0,0,0):
            ImageDraw.floodfill(image,(x,y),(0,0,0))
            region_count+=1
    return region_count

