import pandas as pd
import numpy as np

def takeuntil(predicate,iterable):
    for x in iterable:
        yield x
        if not predicate(x):
            break

tree_map=pd.read_fwf('input08.txt',widths=[1]*99,dtype=np.uint8,header=None)
#tree_map=pd.DataFrame([[3,0,3,7,3],[2,5,5,1,2],[6,5,3,3,2],[3,3,5,4,9],[3,5,3,9,0]],dtype=np.uint8)
tree_map=tree_map.to_numpy()
tree_map_mask=np.zeros(tree_map.shape,dtype=bool)
scenery_score=np.zeros(tree_map.shape,dtype=int)

for coords, value in np.ndenumerate(tree_map):
    i,j=coords
    if tree_map[i,:j].size==0 or \
       tree_map[i,j+1:].size==0 or \
       tree_map[:i,j].size==0 or \
       tree_map[i+1:,j].size==0:
        #print(i,j)
        tree_map_mask[i,j]=True
    elif max(tree_map[i,:j])<value or \
         max(tree_map[i,j+1:])<value or \
         max(tree_map[:i,j])<value or \
         max(tree_map[i+1:,j])<value:
        #print(tree_map[i,:j],value,tree_map[i,j+1:])
        tree_map_mask[i,j]=True
    score=len(list(takeuntil(lambda x:x<tree_map[i,j],tree_map[i,:j][::-1])))
    score*=len(list(takeuntil(lambda x:x<tree_map[i,j],tree_map[i,j+1:])))
    score*=len(list(takeuntil(lambda x:x<tree_map[i,j],tree_map[:i,j][::-1])))
    score*=len(list(takeuntil(lambda x:x<tree_map[i,j],tree_map[i+1:,j])))
    scenery_score[i,j]=score

masked=np.ma.MaskedArray(tree_map,~tree_map_mask)

part1=masked.count()
part2=max(scenery_score.ravel())

print(f'Part 1: {part1}\nPart 2: {part2}')
