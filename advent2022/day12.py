import numpy as np
import pandas as pd
from collections import deque

def flatten(nested_list):
    flat_list=[]
    for element in nested_list:
        if isinstance(element,list):
            flatten(element)
        else:
            flat_list.append(element)
    return flat_list

def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)

#elevation_map=pd.read_fwf('test12.txt',widths=[1]*8,header=None)
elevation_map=pd.read_fwf('input12.txt',widths=[1]*83,header=None)
elevation_map=elevation_map.to_numpy()
vord=np.vectorize(lambda x:ord(x)-96,otypes=[np.int16])
elevation_map=vord(elevation_map)
height,width=elevation_map.shape
end_idx=np.argmin(elevation_map)
end_y,end_x=end_idx//width,end_idx%width
elevation_map[end_y,end_x]=26
start_idx=np.argmin(elevation_map)
start_y,start_x=start_idx//width,start_idx%width
elevation_map[start_y,start_x]=1
graph={}
for idx in range(elevation_map.size):
    y,x=idx//width,idx%width
    value=elevation_map[y,x]
    graph[idx]=[]
    if y>0 and elevation_map[y-1,x]<=value+1:
        graph[idx].append(width*(y-1)+x)
    if y<height-1 and elevation_map[y+1,x]<=value+1:
        graph[idx].append(width*(y+1)+x)
    if x>0 and elevation_map[y,x-1]<=value+1:
        graph[idx].append(idx-1)
    if x<width-1 and elevation_map[y,x+1]<=value+1:
        graph[idx].append(idx+1)

path=find_shortest_path(graph,start_idx,end_idx)
path=list(pd.core.common.flatten(path))
part1=len(path)-1

part2=elevation_map.size
elevation_masked=np.ma.masked_not_equal(elevation_map,1)
for y,x in zip(*elevation_masked.nonzero()):
    start_idx=y*width+x
    path=find_shortest_path(graph,start_idx,end_idx)
    try:
        path=list(pd.core.common.flatten(path))
    except TypeError:
        continue
    pathlen=len(path)-1
    part2=min(pathlen,part2)

print(f'Part 1: {part1}\nPart 2: {part2}')
