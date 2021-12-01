# day01.py

from collections import deque
from itertools import islice, tee
from typing import Iterable, Optional
import sys


def sliding_window(data: Iterable, window_size: int = 1) -> tuple:
    window = deque(islice(data, window_size), maxlen=window_size)
    if len(window) == window_size:
        yield tuple(window)
    for x in data:
        window.append(x)
        yield tuple(window)


def count_increases(data: Iterable[int], window_size: int = 1) -> int:
    count = -1
    last = -1
    for window in sliding_window(data, window_size):
        if sum(window) > last:
            count += 1
        last = sum(window)
    return count


if __name__ == '__main__':
    data: Optional[Iterable] = None
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = 'input01.txt'
    with open(filename) as infile:
        data = map(int, infile.readlines())
    data = tee(data)
    print(count_increases(data[0]))
    print(count_increases(data[1], 3))
