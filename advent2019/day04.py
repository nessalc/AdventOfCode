# my input: 138307-654504

import re


def check_valid_part_1(password):
    # check at least one double
    if not re.match(r'.*(.)\1.*', password):
        return False
    # check never decrease
    for x, y in zip(password[:-1], password[1:]):
        if int(x) > int(y):
            return False
    return True


def check_valid_part_2(password):
    # check double is not part of larger group
    matches = re.findall(r'(.)\1', password)
    if not any([password.count(match) <= 2 for match in matches]):
        return False
    return True


low, high = 138307, 654504
count_1, count_2 = 0, 0
for i in range(low, high+1):
    if check_valid_part_1(str(i)):
        count_1 += 1
        if check_valid_part_2(str(i)):
            count_2 += 1

print(count_1)
print(count_2)
