import os


def calculate_fuel(mass, recursive=False):
    fuel = mass//3-2
    if recursive:
        if fuel <= 0:
            return 0
        return fuel+calculate_fuel(fuel, recursive)
    return fuel


with open(os.path.join(os.curdir, 'advent2019', 'input01.txt')) as file:
    module_masses = list(map(int, file.readlines()))
print('Part 1:', sum(map(lambda x: calculate_fuel(x, False), module_masses)))
print('Part 2:', sum(map(lambda x: calculate_fuel(x, True), module_masses)))
