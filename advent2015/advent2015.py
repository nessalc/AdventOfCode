#adventofcode

#day 1
#puzzle 1
def final_floor(filename):
    santas_directions=open(filename)
    s=santas_directions.readline()
    santas_directions.close()
    return s.count("(")-s.count(")")

#puzzle 2
def basement_direction(filename):
    santas_directions=open(filename)
    s=santas_directions.readline()
    santas_directions.close()
    f=0
    for i in range(len(s)):
        if s[i]=="(":
            f+=1
        elif s[i]==")":
            f-=1
        if f<0:
            return i+1
    return 'Not with this input'

#day 2
#puzzle 1
def wrapping_paper(filename):
    present_list=open(filename)
    paper_needed=0
    for present in present_list:
        length,width,height=map(int,present.split('x'))
        sides=[length*width,width*height,height*length]
        paper_needed+=2*sum(sides)+min(sides)
    present_list.close()
    return paper_needed

#puzzle 2
def ribbon(filename):
    present_list=open(filename)
    ribbon_needed=0
    for present in present_list:
        length,width,height=map(int,present.split('x'))
        bow=length*width*height
        wrap=2*min(length+width,width+height,height+length)
        ribbon_needed+=bow+wrap
    present_list.close()
    return ribbon_needed
