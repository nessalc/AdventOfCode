from more_itertools import map_reduce,windowed,run_length
from functools import lru_cache,reduce
from operator import mul
import networkx as nx
import numpy as np

adapters=list(map(int,open('day10.txt').readlines()))
#adapters=[16,10,15,5,1,11,7,19,6,12,4]
#adapters=[28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
adapters+=[0,max(adapters)+3]
adapted=[b-a for a,b in windowed(sorted(adapters),2)]
diff_dict=map_reduce(adapted,keyfunc=lambda x:x,valuefunc=lambda x:1,reducefunc=sum)
print(diff_dict[1]*diff_dict[3])

ones_differences=map(lambda x:x[1],filter(lambda x:x[0]!=3,list(run_length.encode(adapted))))

@lru_cache
def tribonacci(n):
    if 0<=n<=1:
        return 0
    elif n==2:
        return 1
    else:
        return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)

print(reduce(mul,map(lambda x:tribonacci(x+2),ones_differences),1))

adapters.sort()

DG=nx.DiGraph()
DG.add_nodes_from(adapters)
for i in adapters:
    DG.add_edges_from(map(lambda x:(i,x),filter(lambda x:0<x-i<=3 and x!=i,adapters)))
adjacency_matrix=nx.to_numpy_array(DG)
identity_matrix=np.identity(adjacency_matrix.shape[0])
count_matrix=np.linalg.inv(identity_matrix-adjacency_matrix)

print(int(count_matrix[0][-1]))
