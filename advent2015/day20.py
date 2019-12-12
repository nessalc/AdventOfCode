def lazy_elves(min_presents,present_multiplier=10,stop_after=None):
    limit=min_presents//present_multiplier
    house_present_count=[0]*limit
    for elf in range(1,limit+1):
        for i in range(elf,(stop_after*elf if stop_after else limit)+1,elf):
            try:
                house_present_count[i-1]+=elf*present_multiplier
            except IndexError:
                pass
    for house in house_present_count:
        if house>=min_presents:
            return house_present_count.index(house)+1
