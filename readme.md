# Console Adventure

* Run 

You can run it by just typing: 

    python 'full path to main.py'

* Plot

  You are sleeping adventure whose dreaming mind created imaginary universe. 
  You main goal is to wake up. Thats all for now.

* Mechanics

  You can only interact with game by typing text commands, 
  they are usually printed to you when you should use them.

* Actual adventure

  * Professions
    
    At the start of your adventure you have to choose from **N** professions 
    which are listed for you at the start of the game

    Each profession has these attributes:
    
    * **name** - name of the profession
    * **story** - profession description (it should be story one day, but now its only short description)
    * **bonus_damage** - bonus damage you deal when hit 
    * **bonus_healing** - bonus healing you deal when heal
    * **max_health** - you maximum possible health
    * **current_health** - your current health (only valuable in combat)
    * **damage_resist** - damage you block when enemy hit you
    * **money** - you money
    * **life_elixir** - consumable autoused to be healed to full HP instead of dying when your HP drops to 0 
    * **invisibility_powder** consumable used to skip common enemy
    * **can_use_shop** - ability to use shop
    * **lifesteal** - healing on hit (0.0-1.0)
    * **critical_chance** - chance to deal double damage (0.0 - 1.0)
    * **enemies_killed** - count of enemies you killed, user to calculate enemy tier    

  * Zones
    
    You can 'move your world':
      
      1. North (while actually going south)
      2. South (while actually going north)
      3. East (while actually going west)
      4. West (while actually going east)
      
    And you can come to 3 types of zone:
        
      1. Common zone with 1 enemy to kill or skip
      2. Uncommon zone with problem to deal with
      3. Zone, which is important for story 

  * Enemies
     
    For now there is only 1 type of enemy - common enemy with:
    
     * Name
       * Name is made of State and Name. 
         You can check possible names by in dictionaries and states in dicts.py  
     * Message
     * HP
     
        Calculated at the start of combat, 
        depends on enemy tier, 
        you can check formula in battle.py 
     * Attack
     
        Calculated at the start of combat, 
        depends on enemy tier, 
        you can check formula in battle.py 
     * Speed (speed is relative so it doesnt have any km/h speed, 
     but it can be faster than you or slower (enemies with 1-4 grade can only be slower))
    
    they also drop money when killed (and may be would drop artifacts later)
    
* Rest

Most info contained in dicts.py and help.py.
Code is not commented at all for now, mostly because i am lazy and its simple af     