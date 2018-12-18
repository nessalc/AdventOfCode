#Advent of Code
#Day 11: Chronal Charge

import numpy as np

def calc_power_level(coordinates,serial_number):
    x,y=coordinates
    #find rack id
    rack_id=x+10
    #initial power level
    power_level=rack_id*y
    #increase by serial number
    power_level+=serial_number
    #multiply by rack id
    power_level*=rack_id
    #extract hundreds digit
    power_level%=1000
    power_level//=100
    #subtract 5
    power_level-=5
    return power_level

serial_number=8199
#Create fuel cell
fuel_cell=np.ndarray((301,301),dtype=np.dtype(int))
#Create iterator
it=np.nditer(fuel_cell,flags=['multi_index'],op_flags=['writeonly'])
#Populate initial values
while not it.finished:
    it[0]=calc_power_level(it.multi_index,serial_number)
    it.iternext()

it=np.nditer(fuel_cell,flags=['multi_index'])
power_max=-500
while not it.finished:
    x,y=it.multi_index
    if x%3==0 and y==0:
        print('.',end='') #progress bar
    for s in range(1,min(301-x,301-y)): #will get faster as you move across the row and down the columns
        power=fuel_cell[x:x+s,y:y+s].sum()
        if power>power_max:
            maxx,maxy,maxs,power_max=x,y,s,power
            #print(x,y,s,power)
    it.iternext()
print(maxx,maxy,maxs,power_max)
