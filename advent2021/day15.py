# day15.py

import numpy as np
import skimage.graph

cave = np.genfromtxt('input15.txt', delimiter=1, dtype=np.uint8)

start = 0, 0
end = cave.shape[0]-1, cave.shape[1]-1
path, weight = skimage.graph.route_through_array(
    cave, start, end, False, False)

print(int(weight-cave[start]))


def reduce_risk(x):
    if x > 9:
        return x-9
    return x


reduce_risk_v = np.vectorize(reduce_risk)

expanded_cave = np.concatenate([cave + i for i in range(5)], axis=1)
expanded_cave = np.concatenate([expanded_cave+i for i in range(5)], axis=0)
expanded_cave = reduce_risk_v(expanded_cave)

end = expanded_cave.shape[0]-1, expanded_cave.shape[1]-1

path, weight = skimage.graph.route_through_array(
    expanded_cave, start, end, False, False)

print(int(weight-expanded_cave[start]))
