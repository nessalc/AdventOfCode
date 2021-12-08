# day08.py

import re
with open('input08.txt') as fp:
    lines: list[str] = fp.readlines()

count: int = 0
for line in lines:
    output_val: str = line.strip().split(' | ')[1]
    matches: list[re.Match] = re.findall(r'\b\w{2,4}\b|\b\w{7}\b', output_val)
    count += len(matches)

print(count)

total: int = 0
for line in lines:
    output_val_tokens: list[str] = line.strip().split(' | ')[1].split()
    all_tokens: list[str] = list(set([''.join(sorted(token))
                                     for token in line.split()])-set('|'))
    all_tokens.sort(key=len)
    digits: dict[int, str] = {8: 'abcdefg'}
    for token in all_tokens:
        if len(token) == 2:  # 1
            digits[1] = token
        elif len(token) == 3:  # 7
            digits[7] = token
        elif len(token) == 4:  # 4
            digits[4] = token
        elif len(token) == 5:  # 235
            if 1 in digits.keys() and len(set(token) & set(digits[1])) == 2:
                digits[3] = token
            elif 7 in digits.keys() and len(set(token) & set(digits[7])) == 3:
                digits[3] = token
            elif 4 in digits.keys() and len(set(token) & set(digits[4])) == 2:
                digits[2] = token
            elif 4 in digits.keys() and len(set(token) & set(digits[4])) == 3:
                digits[5] = token
        elif len(token) == 6:  # 690
            if 1 in digits.keys() and len(set(token) & set(digits[1])) == 1:
                digits[6] = token
            elif 7 in digits.keys() and len(set(token) & set(digits[7])) == 2:
                digits[6] = token
            elif 4 in digits.keys() and len(set(token) & set(digits[4])) == 4:
                digits[9] = token
            elif 3 in digits.keys() and len(set(token) & set(digits[3])) == 5:
                digits[9] = token
            elif 5 in digits.keys() and len(set(token) & set(digits[5])) == 4:
                digits[0] = token
        elif len(token) == 7:
            pass  # 8 is taken care of by initialization
    a: tuple[int | str]
    b: tuple[int | str]
    a, b = zip(*digits.items())
    rdigits = dict(zip(b, a))
    total += int(''.join(map(str,
                 [rdigits[''.join(sorted(token))] for token in output_val_tokens])))
print(total)
