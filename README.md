# City of Heroes / City of Villains Macro Generator
This is a short python script to create a set of macro files for players of City of Heroes / City of Villains (CoX). For more information on the game, check out [Homecoming](https://forums.homecomingservers.com/). CoX is limited to one auto-triggering power, but often players will have multiple powers you want to keep active. In addition end-game players can (usually) ignore all inspirations other than damage ones, and it's beneficial to quickly convert these. This script creates a series of binding files that will accomplish these tasks.

# Benefits
* Automatically converts inspirations to reds and uses them. 
* Creates a single target and multi target rotation if you want to use it.
* Cycles through a number of buffing powers you'd like to keep active.
* Easily lets you tweak a power or two and refresh all your binds.
* ~~Walks your dog for you. ~~(Work in Progress.)

# Definitions
* Single Target cycle: the powers you use on a single target.
* Multi Target cycle: the powers you use in Area of Effect situations.
* Buff cycle: the powers you use to buff your character, like Hasten or Build Up. 
* Inspiration cycle: the binds to automatically convert all inspirations to red skittles and eat them. Note: these macros assume you have turned off status and rez inspirations at the P2W vendor. 

# Usage
1. Install python on your machine if you don't have it. 
2. Download the script. (Optional: make a copy for each character you want to make binds for.)
3. Open the script using a text editor like Notepad++, Notepad, VS Code, etc. 
4. Edit the file:
  * Set the directory where you want your macros stored. Binds are limited to 255 characters each and we'll use this path in the binds, so the shorter the better.
  * Set the folder for output. Again, shorter is better. 
  * List the names (in order) for your single target, multi-target, and buff rotations. (If you don't know a power name, load your character in game and type "/powexecname <insert name>" until it triggers. Replace spaces with underscores ("_").
  * Save the file.
  * Execute the file using python. This is usually done at the command line (like "python coh_bind_generator.py"). 
5. Log into City of Heroes and load your character.
6. Type "/bindloadfile <path>\bind0.txt" (The binder function isn't working yet).

# Using the bindings
* Your single target binds will cycle on numpad1. Note: This will not trigger your buff cycling, so regularly use 1 through 0 to activate powers.
* Your multi target binds will cycle on numpad2. Same caveat as numpad1.
* Your buffs will cycle on using 1 through 0 to active powers. The power in 1 through 0 will activate first, and then the power you have cycled to - so give your command queue time to empty between button presses or your buffs will never activate. 
  
# Uninstallation
In game, type '/unbind <x>' where X is:
  * 0 - 9
  * w, s, a, and d
  * numpad 0, 1, 2, and decimal
 
 # Prior Art
 * These [examples](https://shipofheroes.com/forums/viewtopic.php?t=2424).
 * The macros Luka#8022 added to [Warlawk's Tanking Guide](https://forums.homecomingservers.com/topic/7594-farm-fresh-builds-farming-focused-builds-and-tips/).
 * The macros in the [G** D*** PB](https://forums.homecomingservers.com/topic/6824-youre-a-g-d-pb-guide/) guide. (note: I didn't add these macros but if you run a PB or WS you want them and they don't conflict with these scripts).
