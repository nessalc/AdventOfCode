import re
#from PIL import Image
import numpy as np

pat=re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
filename='input03.txt'
max_width,max_height=0,0
with open(filename) as f:
    claim_list=[]
    for r in f.readlines():
        r=pat.match(r.strip())
        claim=[int(d) for d in r.groups()]
        claim_list.append(claim)
        claim_id,left_offset,top_offset,width,height=claim
        max_width,max_height=max(max_width,left_offset+width),max(max_height,top_offset+height)
cloth=np.zeros((max_width,max_height),np.dtype(int))
for ident,left_offset,top_offset,width,height in claim_list:
    cloth[left_offset:left_offset+width,top_offset:top_offset+height]+=1
print('{} square inches of fabric have two or more claims on them.'.format(np.sum(cloth>1)))
#np.amax(cloth) #for fun
#cloth_im=Image.fromarray((cloth<2).astype(np.dtype(int))*255)
#cloth_im.show()
for ident,left_offset,top_offset,width,height in claim_list:
    if np.all(cloth[left_offset:left_offset+width,top_offset:top_offset+height]==1):
        print('#{} is the lone claim that doesn\'t overlap any others.'.format(ident))
        break
