# day14.py

from collections import Counter

# %%

with open('input14.txt') as fp:
    polymer, rules = fp.read().split('\n\n')

print(polymer)

rule_dict = {}
for rule in rules.split('\n'):
    try:
        v, sub = rule.split(' -> ')
        rule_dict[v] = sub
    except ValueError:
        pass


def next_poly(polymer, rule_dict):
    new_poly = ''
    for i in range(len(polymer)-1):
        v = polymer[i:i+2]
        new_poly += v[0]+rule_dict[v]
    return new_poly+polymer[-1]


# for i in range(20):
#     polymer = next_poly(polymer, rule_dict)
#     c = Counter(polymer)
#     x, n = max(c.values()), min(c.values())
#     print(f'{i+1:2d}: {x:<7d} - {n:<7d} = {x-n:<7d}, {c.total():8d}')

def find_counts(polymer, rule_dict):
    c = Counter(rule_dict.keys())
    for pair in rule_dict.keys():
        if pair in polymer:
            count = polymer.count(pair)
        else:
            count = 0
        c[pair] = count
    return c


def update_counters(counter, rule_dict):
    next_counter = counter.copy()
    for k, c in (+counter).items():
        start, end = k
        insertion = rule_dict[k]
        start += insertion
        end = insertion+end
        next_counter[k] -= c
        next_counter[start] += c
        next_counter[end] += c
    return next_counter


# %%
pair_counter = find_counts(polymer, rule_dict)
last = polymer[-1]

# %%
for i in range(10):
    pair_counter = update_counters(pair_counter, rule_dict)

# %%
element_counter = Counter()
for k, c in pair_counter.items():
    element_counter[k[0]] += c
element_counter[last] += 1
commonality = element_counter.most_common()
most_common, least_common = commonality[0][1], commonality[-1][1]
print(f'{most_common} - {least_common} = {most_common - least_common}')

# %%
for i in range(30):
    pair_counter = update_counters(pair_counter, rule_dict)

# %%
element_counter = Counter()
for k, c in pair_counter.items():
    element_counter[k[0]] += c
element_counter[last] += 1
commonality = element_counter.most_common()
most_common, least_common = commonality[0][1], commonality[-1][1]
print(f'{most_common} - {least_common} = {most_common - least_common}')
# %%
