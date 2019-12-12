import re

f=r'C:\Users\c41663\Documents\programming\advent2015\input07.txt'
def find_signal(filename,signal_sought,override={}):
    #read file
    f=open(filename)
    string_array=f.readlines()
    f.close()
    #initialize data structure
    circuit=dict()
    #translate to code
    for string in string_array:
        string=string.replace('AND','&')
        string=string.replace('OR','|')
        string=string.replace('LSHIFT','<<')
        string=string.replace('RSHIFT','>>')
        string=string.replace('NOT','~')
        #prepend variable/signal names with underscore due to keywords
        string=re.sub('([a-z]+)','_\\1',string)
        #tokenize on spaces
        shuffle=string.split()
        #join to make statements
        circuit[shuffle[-1]]=''.join(shuffle[:-2])
    #prepend variable/signal name with underscore due to keywords
    signal_sought='_'+signal_sought
    #override (replace/insert value[s]) if desired/needed
    for k,v in override.items():
        circuit['_'+k]='{}'.format(str(v))
    #ensure desired signal is actually somewhere in the circuit
    if signal_sought not in circuit.keys():
        raise ValueError('Circuit does not contain signal "{}".'.format(signal_sought))
    #loop
    while True:
        for k,v in circuit.items():
            #try every circuit
            try:
                #if this evaluates, great! Assign result to ease next pass
                eval(v)
                exec('{}={}'.format(k,v))
                circuit[k]='{}'.format(eval(v))
                #if this is what we're looking for:
                if k==signal_sought:
                    #return it!
                    return '{}={}'.format(k[1:],eval(circuit[k]))
            #otherwise
            except:
                #loop again!
                pass
    #this return will never happen...
    return circuit
