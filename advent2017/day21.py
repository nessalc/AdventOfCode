from PIL import Image, ImageMorph
import numpy as np

if __name__=='__main__':
    pattern=bytes([0,255,0,
                   0,0,255,
                   255,255,255])
    i=Image.frombytes('L',(3,3),pattern)
    lb=ImageMorph.LutBuilder([#'4:(00 01)->110 100 000',
                              '4:(010 001 111)->1001 0000 0000 1001'])
    lut=lb.build_lut()
    ImageMorph.MorphOp(lut).apply(i)
