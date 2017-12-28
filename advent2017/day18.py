#Advent of Code 2017
#Day 18: Duet

from collections import deque

class Program:
    def __init__(self,code,pid=0,part2=False):
        self.code=code
        self.part2=part2
        self.registers={'p':pid}
        self.message_queue=deque()
        self.pc=0
        self.send_count=0
    def set_partner(self,partner):
        self.partner=partner
    def get_val(self,arg):
        if arg.isalpha():
            return self.registers[arg]
        return int(arg)
    def run_one(self):
        if 0>=self.pc>len(self.code):
            return
        instruction=self.code[self.pc]
        argv=instruction.split()
        for i in argv[1:]:
            if i.isalpha() and i not in self.registers.keys():
                self.registers[i]=0
        if argv[0]=='snd':
            if self.part2:
                self.partner.message_queue.appendleft(self.get_val(argv[1]))
                self.send_count+=1
            else:
                self.registers['snd']=self.get_val(argv[1])
        elif argv[0]=='rcv':
            if self.part2:
                if len(self.message_queue)==0:
                    return
                self.registers[argv[1]]=self.message_queue.pop()
            else:
                if self.get_val(argv[1])!=0:
                    return self.registers['snd']
        elif argv[0]=='set':
            self.registers[argv[1]]=self.get_val(argv[2])
        elif argv[0]=='add':
            self.registers[argv[1]]+=self.get_val(argv[2])
        elif argv[0]=='mul':
            self.registers[argv[1]]*=self.get_val(argv[2])
        elif argv[0]=='mod':
            self.registers[argv[1]]%=self.get_val(argv[2])
        elif argv[0]=='jgz':
            if self.get_val(argv[1])>0:
                self.pc+=self.get_val(argv[2])
                return
        self.pc+=1
        return

test_code_1='''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2'''.split('\n')

test_code_2='''snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d'''.split('\n')

input_code=list(map(str.strip,open('input18.txt').readlines()))

if __name__=='__main__':
    p=Program(input_code)
    while True:
        a=p.run_one()
        if a:
            print(a)
            break
    del p
    input_code=test_code_2
    p1=Program(input_code,0,True)
    p2=Program(input_code,1,True)
    p1.set_partner(p2)
    p2.set_partner(p1)
    while True:
        pc1,pc2=p1.pc,p2.pc
        p1.run_one()
        p2.run_one()
        if p1.pc==pc1 and p2.pc==pc2: #deadlock or both out of range
            print(pc1,pc2)
            break
        
    print(p1.send_count) #correct answer is 7620? I get 7747...
