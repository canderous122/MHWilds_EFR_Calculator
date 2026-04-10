from weapon_skills import *
from set_and_group_skills import *
from armour_skills import *

# Seperate Skills

#    'critical boost' : critical_boost ,
#    'punishing draw' : punishing_draw ,
#    'critical draw' : critical_draw ,
#    'synergy' : synergy ,
#    'burst' : burst ,
#    'ambush' : ambush ,

# skills that affect damage

d_skills = {
    'power stone' : power_stone ,
    'darkside' : darkside ,
    'fortifying pelt' : fortifying_pelt ,
    'lords soul' : lords_soul ,
    'lords fury' : lords_fury 
}

# skills that affect damage and need a level

d_l_skills = {
    'seregios tenacity' : seregios_tenacity ,
    'jin dahaads revolt' : jin_dahaads_revolt ,
    'heroics' : heroics ,
    'blagongas spirit' : blagongas_spirit ,
    'ebnony odogarons power' : ebony_odogarons_power ,
    'xu wus viqor' : xu_wus_vigor ,
    'resentment' : resentment ,
    'adrenaline rush' : adernaline_rush ,
    'peak performance' : peak_performance ,
    'counterstrike' : counterstrike ,
    'bludgeoner' : bludgeoner ,
    'attack boost' : attack_boost ,
    'offensive guard' : offensive_guard 
}

# skills that affect affinity

a_skills = {
    'grillmaster' : grillmaster ,
    'leviathans fury' : leviathans_fury
}

# skills that affect affinity and need a level

a_l_skills = {
    'critical eye' : critical_eye ,
    'slicked blade' : slicked_blade ,
    'antivirus' : antivirus ,
    'weakness exploit' : weakness_exploit ,
    'maximum might' : maximum_might ,
    'latent power' : latent_power 
}

#skills that affect damage and affinity and need a level

d_a_l_skills = {
    'omega resonance' : omega_resonance ,
    'gore magalas tyranny' : gore_magalas_tyranny ,
    'agitator' : agitator 
}


# list containing all skills for reference and lookup

all_skills = [
    'power stone' ,
    'darkside' ,
    'fortifying pelt' ,
    'lords soul' ,
    'lords fury' ,
    'seregios tenacity' ,
    'jin dahaads revolt' ,
    'heroics' ,
    'blagongas spirit' ,
    'ebony odogarons power' ,
    'xu wus vigor' ,
    'resentment' , 
    'adrenaline rush' ,
    'peak performance' ,
    'counterstrike',
    'bludgeoner' ,
    'ambush' ,
    'attack boost' ,
    'offensive gaurd' ,
    'grillmaster' ,
    'leviathans fury' ,
    'critical eye',
    'slicked blade' ,
    'antivirus' ,
    'weakness exploit' ,
    'maximum might' ,
    'latent power' ,
    'omega resonance' ,
    'gore magalas tyranny' ,
    'agitator' ,
    'critical boost',
    'punishing draw',
    'critical draw',
    'synergy',
    'burst',
    'rey daus voltage'
]