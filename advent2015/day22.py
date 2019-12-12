import random

def rpg(my_hp,my_mana,boss_hp,boss_damage,hard=False,trials=1):
    spells={'Magic Missile':{'cost':53,
                             'damage':4,
                             'duration':1},
            'Drain':{'cost':73,
                     'damage':2,
                     'heal':2,
                     'duration':1},
            'Shield':{'cost':113,
                      'armor':7,
                      'duration':6},
            'Poison':{'cost':173,
                      'damage':3,
                      'duration':6},
            'Recharge':{'cost':229,
                        'mana':101,
                        'duration':5}}
    min_mana_to_win=1000000
    win_count=0
    for i in range(trials):
        tmy_hp,tmy_mana,tboss_hp=my_hp,my_mana,boss_hp
        my_defense,mana_spent=0,0
        spells_active=[]
        player=True
        sequence=[]
        while tmy_hp>0 and tboss_hp>0:
            if player:
                if hard:
                    tmy_hp-=1
                    if tmy_hp<=0:
                        break
            #apply spell effects
            my_defense=0
            for spell,duration in spells_active[:]:
                for k,v in spells[spell].items():
                    if k=='damage':
                        tboss_hp-=v
                    elif k=='heal':
                        tmy_hp+=v
                    elif k=='armor':
                        my_defense=v
                    elif k=='mana':
                        tmy_mana+=v
                spells_active.remove((spell,duration))
                duration-=1
                if duration>0:
                    spells_active.append((spell,duration))
            if player:
                #pick a spell to cast
                spell_list=list(spells.keys())
                for s in spell_list[:]:
                    if tmy_mana<spells[s]['cost'] or s in map(lambda x:x[0],spells_active):
                        spell_list.remove(s)
                if not spell_list:
                    #can't cast a spell, you lose
                    tboss_hp=1
                    break
                spell=random.choice(spell_list)
                #cast spell
                tmy_mana-=spells[spell]['cost']
                mana_spent+=spells[spell]['cost']
                if mana_spent>min_mana_to_win:
                    #already found a case where less mana is required, try again
                    break
                if spells[spell]['duration']==1:
                    for k,v in spells[spell].items():
                        if k=='damage':
                            tboss_hp-=v
                        elif k=='heal':
                            tmy_hp+=v
                else:
                    spells_active.append((spell,spells[spell]['duration']))
            if not player:
                #attack
                if tboss_hp>0:
                    tmy_hp-=max(boss_damage-my_defense,1)
            player=not player
        if tboss_hp<=0:
            min_mana_to_win=min(min_mana_to_win,mana_spent)
            win_count+=1
    return min_mana_to_win,win_count
