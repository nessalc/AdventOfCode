import os
import itertools

with open(os.path.join(os.curdir, 'advent2019', 'input08.txt')) as file:
    sif = file.readline().strip()

image_dimensions = 25, 6
layer_size = image_dimensions[0]*image_dimensions[1]
layers = [sif[layer_size*n:layer_size*(n+1)]
          for n in range(len(sif)//layer_size)]
layer = min(layers, key=lambda x: x.count('0'))
print('Part 1:', layer.count('1')*layer.count('2'))
image = ''
for p in zip(*layers):
    image += next(i for i in p if i != '2')
image = image.replace('0', ' ')
image = image.replace('1', 'X')
print('Part 2:\n')
for i in range(image_dimensions[1]):
    print(image[image_dimensions[0]*i:image_dimensions[0]*(i+1)])
