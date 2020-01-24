class Color:
    RED_BOLD_UNDERLINE = "\033[91;1;4m"
    GREEN_ITALIC_UNDERLINE = "\033[92;3;4m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
    GREEN_BOLD = "\033[92;1m"
    GREEN_ITALIC = "\033[92;3m"
    RED_ITALIC = "\033[91;3m"


class Dicts:
    names_grade1 = ["wolf puppy", "parrot", "squirrel", "rabbit", "mole", "crow", "tuna with pair of legs",
                    "walking dandelion", "blind bear puppy"]

    names_grade2 = ["nor child or adult but still wolf", "really huge rabbit", "tuna with 2 pairs of legs",
                    "flying dandelion", "blind old bear", "exhausted young geek at his first day outside",
                    "1 leg robber", "disarmed assassin (he has no arms, not even weapons)"]

    names_grade3 = ["adult wolf", "supersquirrel", "armed huge rabbit", "tuna with 2 pair of legs and 1 pair of arms",
                    "teleporting dandelion", "common bear", "young geek at his second day outside",
                    "robber with 3 legs (he's not used to have 3 legs actually so you have all chance to defeat him)",
                    "disarmed assassin (this one has arms but not weapon)"]
    names_grade4 = ["demon wolf", "demon-god squirrel", "demon rabbit",
                    "armed tuna with 2 pair of mechanized legs and 2 pair of mechanized arms", "demon bear",
                    "demon dandelion (demons are strong, ok?)", "young geek-robber with sci-fi weapons (they work)",
                    "common assassin", "your mom who tells you 'go to bed its almost nighttime'"]
    names_grade5 = ["", "", "", "", "", "", "", "", ""]
    names_grade6 = ["", "", "", "", "", "", "", "", ""]
    names_grade7 = [
        "something (you have no real enemy at that stage except yourself, but its so stupid to choose you as your last enemy)"]

    messages = ["OMFG YOU'VE MET %enemy% now you have to deal with it's %current_health% HP and %attack% damage",
                "Your dad once met your mom and you think you'l meet your soulmate one day but you only meet %enemy% atm, it doesnt have cute face or sharp mind, but it has %current_health% HP and %attack% damage",
                "It's a bird. It's a plane. No, lol, are you blind? It's %enemy% with %current_health% HP and %attack% damage",
                "Do you believe in life after love? Actually that doesn't matter because you see something and it is %enemy% with %current_health% HP and %attack% damage",
                "Oh wait, who's that pokemon? It is not pokemon at all, it is  %enemy% with %current_health% HP and %attack% damage",
                "What about child abuse? You come home, take off you coat, beat your child.. NO! Don't beat children, just beat this %enemy% with %current_health% HP and %attack% damage",
                "%enemy% with %current_health% HP and %attack% damage appears, do something",
                "(sings) Is this love? Or am i dreaming? Is this looove? No, it is %enemy% with %current_health% HP and %attack% damage",
                "Who would never give you up? Who would never let you down? It's Rick Astley but you could never meet him because of this %enemy% with %current_health% HP and %attack% damage",
                "I used to be adventurer like you, but then %enemy% with %current_health% HP and %attack% damage appeared",
                "There once was a maiden in Stonebury Hallow, she didn't talk much, but, boy, did she swallow. I have a nice lance that she sat upon. The maiden from Stonebury who was also %enemy% with %current_health% HP and %attack% damage",
                "You see dead body, who is that? Why did he die? So many questions, so little answers, may be %enemy% with %current_health% HP and %attack% damage can help you to find out what happened here?",
                "Some night you should just stop, take a deep breath with your eyes closed and then look up to the sky. What would you see? Moon and stars. Aren't they beautiful? Sure they are, but now you shouldn't think about them, you have %enemy% with %current_health% HP and %attack% damage to deal with"]

    states = ["natural", "biter", "powerful", "potential", "mortal", "infernal", "greatest", "dangerous", "deadly",
              "ancient", "secret", "spiritual", "undead", "deadliest", "imaginary", "violent", "violet", "fierce",
              "savage", "terrible", "wicked", "hated", "unseen", "relentless", "malicious"]

    zones = ["desert", "snow desert", "jungle", "forest", "taiga", "ocean beach", "abandoned mine", "spooky old house"]

    priest = {
        "name": "Priest",
        "story": "less dmg, bonus heal, get +1 life any combat (in combat{elixirLife++})",
        "bonusDmg": -1,
        "bonusHeal": 4,
        "maxHealth": 38,
        "dmgResist": 0,
        "money": 100,
        "elixirLife": 1,
        "powderInvisibility": 0,
        "shopUser": True,
        "lifesteal": 0,
        "criticalChance": 0.2
    }
    rogue = {
        "name": "Rogue",
        "story": "more dmg less health, sneaky bastard with bonus money, can evade any fight (has invis powder for any fight)",
        "bonusDmg": 3,
        "bonusHeal": 0,
        "maxHealth": 25,
        "dmgResist": 0,
        "money": 250,
        "elixirLife": 1,
        "powderInvisibility": 1000000,
        "shopUser": True,
        "lifesteal": 0,
        "criticalChance": 0.7
    }
    deathknight = {"name": "DeathKnight",
                   "story": "dead, cant use heal, but heals for half of dmg dealt (dmg//2 + dmg%2), cant die at all (boring op class for pussies), cant use shop",
                   "bonusDmg": 4,
                   "bonusHeal": -20,
                   "maxHealth": 60,
                   "dmgResist": 0,
                   "money": 100,
                   "elixirLife": 1000000,
                   "powderInvisibility": 0,
                   "shopUser": False,
                   "lifesteal": 0.5,
                   "criticalChance": 0.1}
    monk = {
        "name": "Monk",
        "story": "cant spend money and use potions, but get bonusDmg=money//100 and dmgResist=money//100",
        "bonusDmg": 1,
        "bonusHeal": 1,
        "maxHealth": 40,
        "dmgResist": 1,
        "money": 100,
        "elixirLife": 0,
        "powderInvisibility": 0,
        "shopUser": False,
        "lifesteal": 0,
        "criticalChance": 0.5
    }
    wizard = {
        "name": "Wizard",
        "story": "glass cannon can fake death once per fight (elixirLife=1), cant use shop",
        "bonusDmg": 15,
        "bonusHeal": 0,
        "maxHealth": 10,
        "dmgResist": 0,
        "money": 100,
        "elixirLife": 1,
        "powderInvisibility": 0,
        "shopUser": False,
        "lifesteal": 0,
        "criticalChance": 0.05
    }
    profession = {"priest": priest, "rogue": rogue, "deathknight": deathknight, "monk": monk, "wizard": wizard}
