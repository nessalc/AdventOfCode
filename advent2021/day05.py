# day05.py

import numpy as np
from PIL import Image

seafloor = np.zeros((1000, 1000), dtype=np.uint8)

with open('input05.txt') as fp:
    for line in fp.readlines():
        from_point, to_point = line.strip().split(' -> ')
        x_start, y_start = map(int, from_point.split(','))
        x_end, y_end = map(int, to_point.split(','))
        x_step, y_step = 1, 1
        if x_start > x_end:
            x_step = -1
        if y_start > y_end:
            y_step = -1
        x_len = abs(x_end-x_start)
        y_len = abs(y_end-y_start)
        if x_start == x_end and y_len != 0:
            for y in range(y_start, y_end+y_step, y_step):
                seafloor[y, x_start] += 1
        # comment out the next six lines for part 1
        elif y_start == y_end and x_len != 0:
            for x in range(x_start, x_end+x_step, x_step):
                seafloor[y_start, x] += 1
        elif abs(x_len) == abs(y_len):
            for i in range(x_len+1):
                seafloor[y_start+i*y_step, x_start+i*x_step] += 1

print(np.count_nonzero(seafloor >= 2))
# print(seafloor)

# Where's the most? (Personal curiosity)
seafloor_max = np.unravel_index(np.argmax(seafloor), seafloor.shape)
print(seafloor_max)
biggest = seafloor[seafloor_max]
print(biggest)

# # Make a pretty picture
# img = Image.fromarray(seafloor*(255//biggest), 'L')
# # img.save('temp.png')
# img.show()
