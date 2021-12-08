# day07.py

with open('input07.txt') as fp:
    crab_positions = list(map(int, fp.readline().strip().split(',')))

fuel_usage = []
for i in range(min(crab_positions), max(crab_positions)+1):
    fuel_usage.append(sum([abs(i-pos) for pos in crab_positions]))

print(min(fuel_usage))

fuel_usage = []
for i in range(min(crab_positions), max(crab_positions)+1):
    fuel_usage.append(
        sum([abs(i-pos)*(abs(i-pos)+1)//2 for pos in crab_positions]))

print(min(fuel_usage))
