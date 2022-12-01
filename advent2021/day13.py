# day13.py

import numpy as np
from PIL import Image

with open('input13.txt') as fp:
    coords = fp.readlines()


def vfold(arr: np.ndarray, n: int) -> np.ndarray:
    a, b = np.array_split(arr, 2, 0)
    # print(a.shape!= b.shape)
    if a.shape[0] != b.shape[0]:
        b = np.pad(b, [(0, 1), (0, 0)])
    elif a.shape[1] != b.shape[1]:
        b = np.pad(b, [(0, 0), (0, 1)])
    b = np.flipud(b)
    return (a | b)[:n, :]


def hfold(arr: np.ndarray, n: int) -> np.ndarray:
    a, b = np.array_split(arr, 2, 1)
    # print(a.shape != b.shape)
    if a.shape[0] != b.shape[0]:
        b = np.pad(b, [(0, 1), (0, 0)])
    elif a.shape[1] != b.shape[1]:
        b = np.pad(b, [(0, 0), (0, 1)])
    b = np.fliplr(b)
    return (a | b)[:, :n]


def nullfunc(x: object) -> object:
    return x


xs, ys = [], []
instructions = []
for c in coords:
    try:
        x, y = c.strip().split(',')
        xs.append(int(x))
        ys.append(int(y))
    except ValueError:
        c = c.strip()
        if c != '':
            func = nullfunc
            axis, num = c.split('=')
            if axis[-1] == 'x':
                func = hfold
            elif axis[-1] == 'y':
                func = vfold
            instructions.append((func, int(num)))
            print(c)

print(instructions)

transparency = np.zeros((max(ys)+1, max(xs)+1), dtype=bool)

for x, y in zip(xs, ys):
    transparency[y, x] = True

print(transparency.shape)


def print_r(arr: np.ndarray) -> None:
    for row in arr:
        for i in row:
            if i:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    return


for f, n in instructions:
    transparency = f(transparency, n)
    print(transparency.shape)
print_r(transparency)
# img=Image.fromarray(np.uint8(transparency*255),'L')
# img.show()
