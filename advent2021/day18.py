class SnailfishNumber:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __add__(self, a):
        return SnailfishNumber(self, a)

    def __radd__(self, a):
        return SnailfishNumber(a, self)

    def __iadd__(self, a):
        self.x=SnailfishNumber(self.x,self.y)
        self.y=a
        return self

    def __repr__(self):
        return f'[{self.x},{self.y}]'

    def depth(self):
        dleft,dright=0,0
        if isinstance(self.x,SnailfishNumber):
            dleft=self.x.depth()+1
        if isinstance(self.y,SnailfishNumber):
            dright=self.y.depth()+1
        return max(dleft,dright)

    def reduce(self):
        if self.depth()>=4:
            print('explode')
            #find node to blow up...
        pass

    def _explode(self):
        pass

    def _split(self):
        pass

    def magnitude(self):
        if isinstance(self.x,int) and isinstance(self.y,int):
            return 3*self.x+2*self.y
        elif isinstance(self.x,int):
            return 3*self.x+2*self.y.magnitude()
        elif isinstance(self.y,int):
            return 3*self.x.magnitude()+2*self.y
        return 3*self.x.magnitude()+2*self.y.magnitude()

SN = SnailfishNumber

t=SN(SN(1,2),SN(SN(3,4),5))
t.magnitude()
