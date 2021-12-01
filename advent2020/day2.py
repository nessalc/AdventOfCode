items = open('day2.txt').readlines()
valid = 0
for item in items:
    policy, password = item.strip().split(': ')
    crange, character = policy.split(' ')
    low, high = map(int, crange.split('-'))
    if low <= password.count(character) <= high:
        valid += 1
print(valid)
valid = 0
for item in items:
    policy, password = item.strip().split(': ')
    crange, character = policy.split(' ')
    low, high = map(int, crange.split('-'))
    if (password[low - 1] == character) ^ (password[high - 1] == character):
        valid += 1
print(valid)
