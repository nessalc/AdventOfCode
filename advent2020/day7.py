import re

rules=open('day7.txt').readlines()
bag_dict={}

outer_exp=re.compile('^(.*?) bags contain')
inner_exp=re.compile(' (\d+) (.*?) bags?')

for rule in rules:
    bag_dict[outer_exp.findall(rule)[0]]=list(map(lambda x:(int(x[0]),x[1]),inner_exp.findall(rule)))

def find_containing_bags(color):
    return list(map(lambda z:z[0],filter(lambda y:color in map(lambda x:x[1],y[1]),bag_dict.items())))

def walk_containing_bags(color):
    if find_containing_bags(color)==[]:
        return [color]
    return [walk_containing_bags(c) for c in find_containing_bags(color)]+[color]

def find_contained_bags(color):
    return bag_dict[color]

def walk_contained_bags(color):
    if find_contained_bags(color)==[]:
        return 0
    return sum([x[0]+x[0]*walk_contained_bags(x[1]) for x in find_contained_bags(color)])

def flatten(non_flat):
    flat=[]
    while non_flat:
        e=non_flat.pop()
        if type(e)==list:
            non_flat.extend(e)
        else:
            flat.append(e)
    return flat

#part 1
print(len(set(flatten(walk_containing_bags('shiny gold'))))-1)
#part 2
print(walk_contained_bags('shiny gold'))
