def find_row(rowstr):
	low=0
	high=127
	for c in rowstr:
		if c=='F':
			high=(high-low+1)//2+low-1
		else:
			low=high-(high-low+1)//2+1
	if low==high:
		return low
	else:
		raise ValueError

def find_col(colstr):
    low=0
    high=7
    for c in colstr:
        if c=='L':
            high=(high-low+1)//2+low-1
        else:
            low=high-(high-low+1)//2+1
    if low==high:
        return low
    else:
        raise ValueError

def boarding_pass(bsp):
    row=find_row(bsp[:7])
    col=find_col(bsp[-3:])
    seat_id=row*8+col
    return row,col,seat_id

passes=list(map(str.strip,open('day5.txt').readlines()))
pass_list=list(map(boarding_pass,passes))
pass_list.sort(key=lambda x:x[2])
print(pass_list[-1])
all_seats=set(range(pass_list[0][2],pass_list[-1][2]+1))
used_seats=set(map(lambda x:x[2],pass_list))
print(all_seats-used_seats)
