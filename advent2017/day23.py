#Advent of Code 2017
#Day 23: Coprocessor Conflagration

from collections import deque

class Program:
    def __init__(self,code):
        self.code=code
        self.registers={}
        self.pc=0
        self.mul_count=0
    def get_val(self,arg):
        if arg.isalpha():
            return self.registers[arg]
        return int(arg)
    def run_one(self):
        if not 0<=self.pc<len(self.code):
            return
        try:
            instruction=self.code[self.pc]
        except IndexError:
            print(self.pc)
            raise
        argv=instruction.split()
        for i in argv[1:]:
            if i.isalpha() and i not in self.registers.keys():
                self.registers[i]=0
        if argv[0]=='set':
            self.registers[argv[1]]=self.get_val(argv[2])
        elif argv[0]=='sub':
            self.registers[argv[1]]-=self.get_val(argv[2])
        elif argv[0]=='mul':
            self.registers[argv[1]]*=self.get_val(argv[2])
            self.mul_count+=1
        elif argv[0]=='jnz':
            if self.get_val(argv[1])!=0:
                self.pc+=self.get_val(argv[2])
                return
        self.pc+=1
        return

input_code=list(map(str.strip,open('input23.txt').readlines()))

if __name__=='__main__':
    p=Program(input_code)
    while p.pc<len(input_code):
        p.run_one()
    print('Part 1:',p.mul_count)
    #p=Program(input_code)
    #p.registers['a']=1
    #while p.pc<len(input_code):
    #    p.run_one()
    #print('Part 2:',p.registers['h'])
    # Part 2 in Pari/GP:
    # for(X=0,1000,if(!(isprime(100000+b*100+17*X)),x+=1);print(x))
