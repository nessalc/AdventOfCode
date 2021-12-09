# day09.py

from threading import local
from scipy.ndimage import minimum_filter, label
from collections import Counter
from operator import mul
from functools import reduce
import numpy as np

heightmap: np.ndarray = np.genfromtxt(
    'input09.txt', delimiter=1, dtype=np.uint8)

neighbor_kernel: np.ndarray = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
local_lows: np.ndarray = minimum_filter(
    heightmap, footprint=neighbor_kernel, mode='constant', cval=10)
mask: np.ndarray = (heightmap == local_lows) & (heightmap < 9)
values: np.ndarray = heightmap[mask]
print(sum(values)+len(values))

areas = label(heightmap < 9, neighbor_kernel)[0]
largest: list[tuple[int, int]] = Counter(areas.flatten()).most_common(4)[1:]
print(reduce(mul, map(lambda x: x[1], largest)))
