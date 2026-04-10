from weapon_classes import *
from skills_arr import *
from clear_func import clear


def calculation(w_type, dmg, aff):
    clear()
    # init text
    print("Now, its time to start adding skills.")
    print("")
    print("Im not going to take every skill into account. Im not accounting for elem damage or any skills that enhance that, the only skills I've decided to focus on are the ones that increase affinity and attack power. Handicraft isn't in there as to my knowledge in this game there aren't any weapons thats sharpness extend beyond their primary colour, although Im making this before g-rank releases. For Weakness Exploit, Im only counting the affinity increase on weak zones as well, as their uptime is far higher than for wounds.")
    print("")
    print("Im going to ask for the skill, one at a time, asking for the name without any punctuation, and the level of the skill : 1-3/5 for armour skills and 1 or 2 for the set and group bonus skills")
    ans1 = input("Press ENTER to continue >>")

    if ans1 != "":
        clear()
        print("Those are some funny extra keys that aren't ENTER hmmm....")
    else:
        clear()

    player_skills = {}
    print("")
    print("Input the skill below. You can type 'stop' once you're done or 'list' to list the skills I'm counting for this calculation. Additionally, you can type in 'mine' to view the skills you've currently put down. Type 'reset' to reset the list")

    # skill list config loop
    j = 1
    while j == 1:
        print("")
        input_skill = input("Input here:  ")

        if input_skill.lower() == 'stop':
            clear()
            break
        elif input_skill.lower() == "list":
            clear()
            print(all_skills)
            print("")

        elif input_skill.lower() == "mine":
            clear()
            print(player_skills)
            print("")

        elif input_skill.lower() == "reset":
            clear()
            print("RESETTING LIST")
            player_skills = []
            print("")

        elif input_skill.lower() not in all_skills:
            clear()
            print("Ah, don't need that one, lets do the next (could be a typo too)")
            print("")

        else:
            clear()
            skill_level = int(input("And the level of that skill please:  "))
            if skill_level > 5:
                clear()
                print("Ah, that level is bigger than 5. This aint World ya know, non of that here (yet).")
                print("")
            else:
                player_skills[input_skill] = skill_level
                clear() 

    # list initialized, now time to start calculating
    #d_skills loop
    for skill in d_skills:
        if skill in player_skills:
            dmg = d_skills[skill](dmg)

    #d_l_skills loop
    for skill in d_l_skills:
        if skill in player_skills:
            dmg = d_l_skills[skill](dmg, player_skills[skill])

    #a_skills loop
    for skill in a_skills:
        if skill in player_skills:
            aff = a_skills[skill](aff)

    #a_l_skills loop
    for skill in a_l_skills:
        if skill in player_skills:
            aff = a_l_skills[skill](aff, player_skills[skill])

    #d_a_l_skills loop
    for skill in d_a_l_skills:
        if skill in player_skills:
            dmg, aff = d_a_l_skills[skill](dmg,aff,player_skills[skill])


    #Now for the special cases
        #I'll init the draw and ambush vars
    
    draw_dmg = dmg
    draw_aff = aff
    ambush_dmg = draw_dmg
    #synergy
    if 'synergy' in player_skills:
        aff = synergy(aff, player_skills['omega resonance'] == 2)
    
    #critical draw
    if 'critical draw' in player_skills:
        draw_aff = critical_draw(aff, player_skills['critical draw'])

    #burst
    if 'burst' in player_skills:
        dmg = burst(weapon_type_id_inverse(w_type.lower()), dmg, player_skills['burst'])

    #punishing draw
    if 'punishing draw' in player_skills:
        draw_dmg = punishing_draw(dmg, player_skills['punishing draw'])

    #ambush
    if 'ambush' in player_skills:
        ambush_dmg = ambush(draw_dmg, player_skills['ambush'])

    #critical boost
    if 'critical boost' in player_skills:
        dmg = critical_boost(dmg , player_skills['critical boost'])
        draw_dmg = critical_boost(draw_dmg , player_skills['critical boost'])
        ambush_dmg = critical_boost(ambush_dmg , player_skills['critical boost'])

    return dmg, aff, draw_dmg, draw_aff, ambush_dmg





