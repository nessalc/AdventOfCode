import itertools
import functools
import sys


def find_combinations(input_filename: str,
                      number_of_items: int,
                      total: int) -> int:
    items = open(input_filename).readlines()
    for item_list in itertools.combinations(map(int, items), number_of_items):
        if sum(item_list) == total:
            return functools.reduce(lambda x, y: x * y, item_list)


if __name__ == '__main__':
    input_filename = sys.argv[1] if len(sys.argv) > 1 else 'day1.txt'
    number_of_items = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    total = int(sys.argv[3]) if len(sys.argv) > 3 else 2020
    print(find_combinations(input_filename, number_of_items, total))
