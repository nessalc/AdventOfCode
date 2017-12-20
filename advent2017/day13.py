#Advent of Code 2017
#Day 13: Packet Scanners

class Scanner:
    position=0
    direction=1
    def __init__(self,depth):
        self.depth=depth
    def update(self,steps=1):
        for i in range(steps%((self.depth-1)*2)):
            self.position+=self.direction
            if self.position==self.depth-1 or self.position==0:
                self.direction*=-1
    def __str__(self):
        return '<Scanner: {}{}>'.format(self.position,'+' if self.direction>0 else '-')
    def __repr__(self):
        return '<Scanner: {}{}>'.format(self.position,'+' if self.direction>0 else '-')

class Firewall:
    layer=dict()
    packetpos=-1
    def __init__(self,layer_desc):
        for line in layer_desc:
            a,b=tuple(map(int,line.strip().split(':')))
            self.layer[a]=Scanner(b)
    def update_scanners(self,steps=1):
        for s in self.layer.keys():
            self.layer[s].update(steps)
    def move_packet(self):
        self.packetpos+=1
    def is_caught(self):
        return (self.packetpos in self.layer.keys() and self.layer[self.packetpos].position==0)
    def calculate_severity(self,delay,stop_once_caught=False):
        severity=caught_counter=0
        self.update_scanners(delay)
        for i in range(max(self.layer.keys())+1):
            self.move_packet()
            if self.packetpos>=0 and self.is_caught():
                severity+=self.packetpos*self.layer[self.packetpos].depth
                caught_counter+=1
                if stop_once_caught:
                    self.reset()
                    return severity,caught_counter
            self.update_scanners()
        self.reset()
        return severity,caught_counter
    def reset(self):
        self.packetpos=-1
        for s in self.layer.keys():
            self.layer[s].position=0
            self.layer[s].direction=1

if __name__=='__main__':
    firewall=Firewall(open('input13.txt').readlines())
    #firewall=Firewall(['0:3','1:2','4:4','6:4'])
    severity,caught_count=firewall.calculate_severity(0)
    print('Part 1: Severity of trip with no delay is {}'.format(severity))
    i=0
    while caught_count:
        i+=1
        severity,caught_count=firewall.calculate_severity(i,True)
        #if i%1000==0:
        #    print('.',end='')
    #print()
    print('Part 2: Delay {} picoseconds for a safe trip'.format(i))
