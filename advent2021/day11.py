# day11.py

from pickle import ADDITEMS
import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import convolve

octopus_energy: np.ndarray = np.genfromtxt(
    'input11.txt', delimiter=1, dtype=np.int32)

neighbor_kernel: np.ndarray = np.array([[1, 1, 1],
                                        [1, 0, 1],
                                        [1, 1, 1]])
flash_count: int = 0
additional_energy: np.ndarray = np.zeros(octopus_energy.shape, dtype=np.int32)
step: int
print(f'step {0:3d}, flash count {flash_count:<5d}')
for step in range(1000):
    octopus_energy += 1
    flashed = np.zeros(octopus_energy.shape, dtype=bool)
    while np.any(flashing := octopus_energy > 9):
        flashed |= flashing
        octopus_energy += convolve2d(flashing, neighbor_kernel, mode='same')
        octopus_energy[flashed] = 0
    flash_count += np.count_nonzero(flashed)
    print(f'step {step+1:3d}, flash count {flash_count:<5d}' +
          (' all' if np.all(flashed) else ''))
    if np.all(flashed):
        break
