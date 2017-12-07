#Advent of Code 2017
#Day 5: A Maze of Twisty Trampolines, All Alike

def millisecond5(input_file):
    with open(input_file) as fp:
        instructions1=list(map(lambda x:int(x.strip()),fp.readlines()))
        instructions2=instructions1[:]
    print('Part 1:',find_exit(instructions1))
    print('Part 2:',find_exit_2(instructions2))

def find_exit(instructions,decrease_threshhold=3):
    l=len(instructions)
    index=prev_index=count=0
    while 0<=index<l:
        prev_index=index
        index+=instructions[index]
        instructions[prev_index]+=1
        count+=1
    return count
def find_exit_2(instructions):
    l=len(instructions)
    index=prev_index=count=0
    while 0<=index<l:
        prev_index=index
        index+=instructions[index]
        if instructions[prev_index]>=3:
            instructions[prev_index]-=1
        else:
            instructions[prev_index]+=1
        count+=1
    return count
