import itertools

def pick_n_from_lists(*args):
    r=[]
    for i in range(0,len(args)//2*2,2):
        r.append(powerset_sub(args[i],args[i+1]))
    return itertools.product(*r)
def powerset_sub(iterable,srange):
    s=list(iterable)
    if isinstance(srange,tuple):
        low,high=srange[:2]
    elif isinstance(srange,int):
        low,high=0,srange
    high=min(len(s),high)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(low,high+1))
def rpg(my_hp,boss_hp,boss_damage,boss_defense):
    weapons={'Dagger':{'cost':8,'damage':4,'armor':0},
             'Shortsword':{'cost':10,'damage':5,'armor':0},
             'Warhammer':{'cost':25,'damage':6,'armor':0},
             'Longsword':{'cost':40,'damage':7,'armor':0},
             'Greataxe':{'cost':74,'damage':8,'armor':0}}
    armor={'Leather':{'cost':13,'damage':0,'armor':1},
           'Chainmail':{'cost':31,'damage':0,'armor':2},
           'Splintmail':{'cost':53,'damage':0,'armor':3},
           'Bandedmail':{'cost':75,'damage':0,'armor':4},
           'Platemail':{'cost':102,'damage':0,'armor':5}}
    rings={'Damage +1':{'cost':25,'damage':1,'armor':0},
           'Damage +2':{'cost':50,'damage':2,'armor':0},
           'Damage +3':{'cost':100,'damage':3,'armor':0},
           'Defense +1':{'cost':20,'damage':0,'armor':1},
           'Defense +2':{'cost':40,'damage':0,'armor':2},
           'Defense +3':{'cost':80,'damage':0,'armor':3}}
    my_cost,my_damage,my_defense=0,0,0
    tmy_hp,tboss_hp=my_hp,boss_hp
    min_cost_to_win,max_cost_to_lose=1000000,0
    for my_weapon,my_armor,my_rings in pick_n_from_lists(weapons,(1,1),armor,(0,1),rings,(0,2)):
        for x in my_weapon:
            my_cost+=weapons[x]['cost']
            my_damage+=weapons[x]['damage']
            my_defense+=weapons[x]['armor']
        for x in my_armor:
            my_cost+=armor[x]['cost']
            my_damage+=armor[x]['damage']
            my_defense+=armor[x]['armor']
        for x in my_rings:
            my_cost+=rings[x]['cost']
            my_damage+=rings[x]['damage']
            my_defense+=rings[x]['armor']
        #battle
        while tmy_hp>0 and tboss_hp>0:
            tboss_hp-=max((my_damage-boss_defense),1)
            if tboss_hp>0:
                tmy_hp-=max((boss_damage-my_defense),1)
        if tboss_hp<=0:
            min_cost_to_win=min(min_cost_to_win,my_cost)
        elif tmy_hp<=0:
            max_cost_to_lose=max(max_cost_to_lose,my_cost)
        my_cost,my_damage,my_defense=0,0,0
        tmy_hp,tboss_hp=my_hp,boss_hp
    return min_cost_to_win,max_cost_to_lose
