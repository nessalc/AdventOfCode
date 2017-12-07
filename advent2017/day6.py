#Advent of Code 2017
#Day 6: Memory Reallocation

def millisecond6(input_file):
    with open(input_file) as fp:
        memory_banks=list(map(lambda x:int(x.strip()),fp.readline().split('\t')))
    result1,result2=find_repeat(memory_banks)
    print('Part 1:',result1)
    print('Part 2:',result2)

def find_repeat(memory_banks):
    l=len(memory_banks)
    bank_state=[]
    while memory_banks not in bank_state:
        bank_state.append(memory_banks[:])
        blocks=max(memory_banks)
        index=memory_banks.index(blocks)
        memory_banks[index]=0
        index+=1
        for i in range(blocks):
            memory_banks[(index+i)%l]+=1
        #print(memory_banks)
    return len(bank_state),len(bank_state)-bank_state.index(memory_banks)

