from treelib import Tree
from dataclasses import dataclass

sample="""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

@dataclass
class Item:
    name:str
    type:str
    size:int

with open('input07.txt') as f:
    terminal_output=list(map(str.strip,f.readlines()))
#terminal_output=sample.split('\n')

tree=Tree()
tree.create_node('/',1,data=Item('/','dir',None))

def get_node_by_tag(tree,tag):
    nlist=list(filter(lambda node:node.tag==tag,tree.all_nodes()))
    if len(nlist)>1:
        raise IndexError("too many nodes with same tag")
    if len(nlist)<1:
        raise KeyError("tag not found")
    return nlist[0]

def get_child_by_tag(tree,node,tag):
    nlist=list(filter(lambda n:n.tag==tag,tree.children(node.identifier)))
    if len(nlist)>1:
        raise IndexError("too many nodes with same tag")
    if len(nlist)<1:
        raise KeyError("tag not found")
    return nlist[0]

cur_node=tree.get_node(1)
for line in terminal_output[1:]:
    if line[0]=="$":
        command=line[1:].strip()
        #print(f"command:\t{command}")
        if command[:2]=="cd" and command[2:].strip()=="..":
            cur_node=tree.parent(cur_node.identifier)
        elif command[:2]=="cd":
            cur_node=get_child_by_tag(tree,cur_node,command[2:].strip())
        elif command[:2]=="ls":
            pass
    elif line[:3]=="dir":
        directory=line[3:].strip()
        #print(f"directory:\t{directory}")
        tree.create_node(directory,parent=cur_node,data=Item(directory,'dir',None))
    else:
        size,name=line.split(' ')
        size=int(size)
        #print(f"file:\t{name} (size={size})")
        tree.create_node(name,parent=cur_node,data=Item(name,'file',size))

def get_dir_size(tree,node):
    return sum(map(lambda n:n.data.size,tree.leaves(node.identifier)))

f1=tree.filter_nodes(lambda n:n.data.type=='dir')
size_list=list(map(lambda n:get_dir_size(tree,n),f1))
part1=sum(filter(lambda i:i<=100000,size_list))

TOTAL_SPACE=70000000
REQD_SPACE=30000000

unused_space=TOTAL_SPACE-get_dir_size(tree,tree.get_node(tree.root))
print(REQD_SPACE-unused_space)

part2=min(filter(lambda n:n>REQD_SPACE-unused_space,size_list))

print(f'Part 1: {part1}\nPart 2: {part2}')
