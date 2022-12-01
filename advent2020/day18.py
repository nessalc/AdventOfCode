# day18.py

import re

from sqlalchemy import true

total_normal: int = 0
total_advanced: int = 0
k = re.compile(r'\([^\(\)]*\)')
plus = re.compile(r'(\d+)\s+\+\s(\d+)')


def evaluate_normal(equation: str):
    m: re.Match[str] | None = k.search(equation)
    while m is not None:
        equation = equation[:m.start(
        )]+str(evaluate_normal(m.group()[1:-1]))+equation[m.end():]
        m = k.search(equation)
    tokens = equation.split()
    nums = tokens[::2]
    ops = tokens[1::2]
    result = int(nums[0])
    for op, num in zip(ops, nums[1:], strict=True):
        n = int(num)
        match op:
            case '+':
                result += n
            case '*':
                result *= n
    return result


def evaluate_advanced(equation: str):
    # print(equation)
    m: re.Match[str] | None = k.search(equation)
    while m is not None:
        equation = equation[:m.start(
        )]+str(evaluate_advanced(m.group()[1:-1]))+equation[m.end():]
        m = k.search(equation)
    m = plus.search(equation)
    while m is not None:
        equation = equation[:m.start()]+str(int(m.groups()[0]) +
                                            int(m.groups()[1]))+equation[m.end():]
        m = plus.search(equation)
    tokens = equation.split()
    nums = tokens[::2]
    ops = tokens[1::2]
    result = int(nums[0])
    # print(ops)
    # print(nums[1:])
    for op, num in zip(ops, nums[1:], strict=True):
        n = int(num)
        match op:
            case '+':
                result += n
            case '*':
                result *= n
    # print(f'={result}')
    return result


with open('day18.txt') as fp:
    for equation in fp.readlines():
        total_normal += evaluate_normal(equation[::].strip())
        total_advanced += evaluate_advanced(equation[::].strip())

print(total_normal)
print(total_advanced)
