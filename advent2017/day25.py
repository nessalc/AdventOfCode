state='A'
steps=12481997
loc=0
tape={0:0}
for i in range(steps):
    try:
        tape[loc]
    except KeyError:
        tape[loc]=0
    if state=='A':
        if not tape[loc]:
            tape[loc],loc,state=1,loc+1,'B'
        else:
            tape[loc],loc,state=0,loc-1,'C'
    elif state=='B':
        if not tape[loc]:
            tape[loc],loc,state=1,loc-1,'A'
        else:
            tape[loc],loc,state=1,loc+1,'D'
    elif state=='C':
        if not tape[loc]:
            tape[loc],loc,state=0,loc-1,'B'
        else:
            tape[loc],loc,state=0,loc-1,'E'
    elif state=='D':
        if not tape[loc]:
            tape[loc],loc,state=1,loc+1,'A'
        else:
            tape[loc],loc,state=0,loc+1,'B'
    elif state=='E':
        if not tape[loc]:
            tape[loc],loc,state=1,loc-1,'F'
        else:
            tape[loc],loc,state=1,loc-1,'C'
    elif state=='F':
        if not tape[loc]:
            tape[loc],loc,state=1,loc+1,'D'
        else:
            tape[loc],loc,state=1,loc+1,'A'
    if i%(steps//100)==0:
        print('.',end='')
##    # test state machine
##    if state=='A':
##        if not tape[loc]:
##            tape[loc]=1
##            loc+=1
##            state='B'
##        else:
##            tape[loc]=0
##            loc-=1
##            state='B'
##    elif state=='B':
##        if not tape[loc]:
##            tape[loc]=1
##            loc-=1
##            state='A'
##        else:
##            tape[loc]=1
##            loc+=1
##            state='A'
print(sum(tape.values()))
