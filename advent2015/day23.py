f=r'C:\Users\c41663\Documents\programming\advent2015\input23.txt'

def run_program(filename,a=0,b=0):
    f=open(filename)
    instructions=f.readlines()
    f.close()
    program_counter=0
    instruction=instructions[program_counter].strip()
    while instruction:
        parse=instruction.split()
        if parse[0]=='hlf':
            #exec('{}//=2'.format(parse[1]))
            if parse[1]=='a':
                a//=2
            elif parse[1]=='b':
                b//=2
            program_counter+=1
        elif parse[0]=='tpl':
            #exec('{}*=3'.format(parse[1]))
            if parse[1]=='a':
                a*=3
            elif parse[1]=='b':
                b*=3
            program_counter+=1
        elif parse[0]=='inc':
            #exec('{}+=1'.format(parse[1]))
            if parse[1]=='a':
                a+=1
            elif parse[1]=='b':
                b+=1
            program_counter+=1
        elif parse[0]=='jmp':
            program_counter+=int(parse[1])
        elif parse[0]=='jie':
            if eval(parse[1][:-1])%2==0:
                program_counter+=int(parse[2])
            else:
                program_counter+=1
        elif parse[0]=='jio':
            if eval(parse[1][:-1])==1:
                program_counter+=int(parse[2])
            else:
                program_counter+=1
        else:
            print('unknown instruction {}! exiting...'.format(parse[0]))
            break
        try:
            instruction=instructions[program_counter].strip()
        except IndexError:
            print('program end. exiting...')
            break
    return a,b
