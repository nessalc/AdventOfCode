f=open('input08.txt')
root=list(map(int,f.readline().split()))

## Quick & Dirty--works fine for part 1, but doesn't help for part 2
##metadata_sum=0
##while root:
##    #find index of first "only metadata" entry
##    i=root.index(0)
##    #find index of last item in "only metadata" entry
##    j=i+root[i+1]+2
##    node_data=root[i:j]
##    metadata_sum+=sum(node_data[2:])
##    root=root[:i]+root[j:]
##    if root:
##        root[i-2]-=1
##print(metadata_sum)

class Node:
    def __init__(self,data):
        self.metadata=data[-data[1]:]
        self.children=[]
        self.__parse_children(data[2:-data[1]])
    def __parse_children(self,data):
        if data:
            for i in data:
                self.children.append(Node(i))
    def value(self):
        if not self.children:
            return self.metadata_sum()
        else:
            r=0
            for i in self.metadata:
                try:
                    r+=self.children[i-1].value()
                except IndexError:
                    pass
            return r
        return 0
    def metadata_sum(self,all_children=False):
        if all_children:
            r=0
            for i in self.children:
                r+=i.metadata_sum(all_children)
            return r+sum(self.metadata)
        return sum(self.metadata)
    def __parse_raw(self,data):
        return
    def __str__(self):
        return '<Node ({}, {})>'.format(len(self.children),len(self.metadata))
    def __repr__(self):
        return self.__str__()
i=0
limit=max(root)
idx=root.index(i)
start_index=0
while i<=limit:
    try:
        idx=root[start_index:].index(i)+start_index
    except ValueError:
        i+=1
        start_index=0
        continue
    if i==0 or (idx+2<len(root) and not isinstance(root[idx+1],list) and isinstance(root[idx+2],list)):
        root=root[:idx]+[root[idx:idx+root[idx+1]+2+i]]+root[idx+root[idx+1]+2+i:]
    elif i!=0:
        start_index=idx+1
tree=root[0]
n=Node(tree)
print('License File Check #1: {}'.format(n.metadata_sum(all_children=True)))
print('License File Check #2: {}'.format(n.value()))
print('License Valid!')
