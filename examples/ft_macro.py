# ###################################################################
# COH BindFile                                                      # 
# Version 0                                                         #
# 10 Feb 2022                                                       #
# The War Doctor                                                    #
#                                                                   #
# Usage:                                                            #
# 1) Edit this file until you see the comment to stop, adding names #
# for the powers you want, where you want the files stored, etc.    #
# 2) In game, run /bindloadfile <path>\binder.txt                   #
# 3) In game, push numpad0 to turn binds on, numpad. to turn off    #
# ###################################################################

# Imports
import os

# Enter folder for macro home
parent_dir = "D:/cohmacro/"

# Enter folder for output (archetype, char name, etc.)
directory = "FT"

path = os.path.join (parent_dir, directory)

# Check whether the specified path exists or not
isExist = os.path.exists(path)

if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(path)

# Enter skill names for Single Target macro
sts = ["barb_swipe",
    "lunge",
    "barb_swipe",
    "barb_swipe",
    "lunge"
    ]

# Enter skill names for AOE macro
mts = ["cross_punch",
    "burn",
    "cross_punch",
    "spine_burst",
    "cross_punch"
    ]

# Enter skill names for buffs macro
buffs = ["hasten",
    "build_up",
    "fiery_embrace",
    "conserve_power",
    "ageless_partial_core_invocation"
    ]
    
# Stop editing here unless you know what you're doing. =)

# Commands for inspiration combination. These assume that status and
# rez inspirations are turned off at the P2W vendor.
## Yellows (Accuracy)
yel_insp_cmd = '$$inspcombine insight enrage$$inspcombine keen_insight focused_rage$$inspcombine uncanny_insight righteous_rage'
## Purples (Defense)
pur_insp_cmd = "$$inspcombine luck enrage$$inspcombine good_luck focused_rage$$inspcombine phenomenal_luck righteous_rage"
## Blues (Endurance)
blu_insp_cmd = "$$inspcombine catch_a_breath enrage$$inspcombine take_a_breather focused_rage$$inspcombine second_wind righteous_rage"
## Greens (Health)
grn_insp_cmd = "$$inspcombine respite enrage$$inspcombine dramatic_improvement focused_rage$$inspcombine resurgence righteous_rage"
## Oranges (Defense + TP protection)
org_insp_cmd = "$$inspcombine sturdy enrage$$inspcombine rugged focused_rage$$inspcombine robust righteous_rage"
## Reds (Damage)
red_insp_cmd = "$$insp_exec_name enrage$$insp_exec_name Focused_Rage$$insp_exec_name Righteous_Rage"
## Final Array
insp_cmds = [yel_insp_cmd,pur_insp_cmd,blu_insp_cmd,grn_insp_cmd,org_insp_cmd]

mvmts = ['w "+forward',
    's "+backward',
    'a "+left',
    'd "+right'
    ]

# Output Files Section
for i in range(5):
    if i == 4: 
        j = 0 
    else:
        j = i+1
    lines = []
    next_file = '$$bindloadfilesilent '+path+'/bind'+str(j)+'.txt"'+'\n'
    for k in range(10):
        lines.append(str(k) + ' "powexecslot ' + str(k) + '$$powexecauto ' + buffs[i] + next_file)
    loop_mvmt_cmd = insp_cmds[i] + red_insp_cmd + next_file
    for k in range(4):
        lines.append(mvmts[k] + loop_mvmt_cmd)
    lines.append('numpad1 "powexecname ' + sts[i] + next_file)
    lines.append('numpad2 "powexecname ' + mts[i] + next_file)
    output_file = open(path + '/bind' + str(i) + '.txt',"w")
    output_file.writelines(lines)
    output_file.close()
    
output_file = open(path + '/bind_off.txt',"w")
lines = []
for i in range(10):
    lines.append(str(i) + ' "powexecslot ' + str(i) + '"\n')
for i in range(4):
    lines.append(mvmts[i] + '"\n')
lines.append('numpad1 "TELL $name,<color blue><bgcolor yellow><scale 1.25>Binds are off."\n')
lines.append('numpad2 "TELL $name,<color blue><bgcolor yellow><scale 1.25>Binds are off."\n')
output_file.writelines(lines)
output_file.close()

output_file = open(path + '/binder.txt',"w")
output_file.writelines('numpad0 /bindloadfile' + path + '/bind0.txt\n')
output_file.writelines('decimal /bindloadfile' + path + '/bind_off.txt')
output_file.close()