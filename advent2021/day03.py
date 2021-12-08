# day03.py

import numpy as np


with open('input03.txt') as fp:
    inputs: list[list[int]] = list(
        map(lambda x: list(map(int, x.strip())), fp.readlines()))

na: np.ndarray = np.array(inputs)

half: int = np.shape(na)[0]//2
gamma: int = int(''.join(map(lambda x: str(int(x > half)), np.sum(na, 0))), 2)
epsilon: int = int(
    ''.join(map(lambda x: str(int(x < half)), np.sum(na, 0))), 2)
power_consumption: int = gamma * epsilon
print(f'power consumption: {power_consumption}')
print()

nacopy = na.copy()

i: int = 0
while na.shape[0] > 1:
    pick: list[tuple[int, int]] = np.unique(na[:, i], return_counts=True)
    mask: np.ndarray = na[:, i] == max(zip(pick[1], pick[0]))[1]
    na: np.ndarray = na[mask, :]
    i += 1
o2_rating = int(''.join(map(str, na[0, :])), 2)

na = nacopy

i = 0
while na.shape[0] > 1:
    pick: list[tuple[int, int]] = np.unique(na[:, i], return_counts=True)
    mask: np.ndarray = na[:, i] == min(zip(pick[1], pick[0]))[1]
    na: np.ndarray = na[mask, :]
    i += 1
co2_rating = int(''.join(map(str, na[0, :])), 2)

life_support_rating = o2_rating*co2_rating

print(f'life support rating: {life_support_rating}')
