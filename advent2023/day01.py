import regex

with open('input01.txt', encoding='utf-8') as fp:
    all = fp.read()

# test input 1
test1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

# test input 2
test2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

digit = regex.compile('\\d')


def getTotal(input, debug=False):
    if debug:
        print('\nDEBUG OUTPUT:')
    total = 0
    for line in input.split('\n'):
        digits = digit.findall(line)
        try:
            if debug:
                print(line, int(digits[0]+digits[-1]), sep='\t')
            total += int(digits[0]+digits[-1])
        except IndexError:
            pass
    if debug:
        print('END DEBUG OUTPUT\n')
    return total


# part 1
part1input = all
print(f'part 1: {getTotal(part1input)}')

# part 2
part2input = all
digitmap = {'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'}
numbers = regex.compile('|'.join(digitmap.keys())+'|\\d')
s = ''
for line in part2input.split('\n'):
    numlist = list(numbers.findall(line, overlapped=True))
    for num in numlist:
        if str.isalpha(num):
            s += digitmap[num]
        else:
            s += num
    s += '\n'
print(f'part 2: {getTotal(s)}')
