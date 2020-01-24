import dicts as d

color = d.Color

dict = d.Dicts


class Profession:
    name = ""
    story = ""
    bonus_damage = 0
    bonus_healing = 0
    max_health = 0
    current_health = 0
    damage_resist = 0
    money = 0
    life_elixir = 0
    invisibility_powder = 0
    can_use_shop = False
    lifesteal = 0.0
    critical_chance = 0.0
    enemies_killed = 0

    def __init__(self, name, profession=dict.profession):
        self.name = profession.get(name)['name']
        self.story = profession.get(name)['story']
        self.bonus_damage = profession.get(name)['bonusDmg']
        self.bonus_healing = profession.get(name)['bonusHeal']
        self.max_health = profession.get(name)['maxHealth']
        self.current_health = profession.get(name)['maxHealth']
        self.damage_resist = profession.get(name)['dmgResist']
        self.money = profession.get(name)['money']
        self.life_elixir = profession.get(name)['elixirLife']
        self.invisibility_powder = profession.get(name)['powderInvisibility']
        self.can_use_shop = profession.get(name)['shopUser']
        self.lifesteal = profession.get(name)['lifesteal']
        self.critical_chance = profession.get(name)['criticalChance']
        self.enemies_killed = 0

    def get_info(self):
        return {
            "name": self.name,
            "story": self.story,
            "bonusDmg": self.bonus_damage,
            "bonusHeal": self.bonus_healing,
            "maxHealth": self.max_health,
            "dmgResist": self.damage_resist,
            "money": self.money,
            "elixirLife": self.life_elixir,
            "powderInvisibility": self.invisibility_powder,
            "shopUser": self.can_use_shop,
            "lifesteal": self.lifesteal,
            "criticalChance": self.critical_chance,
            "enemies killed": self.enemies_killed
        }

    def print_stats(self):
        text = "Your profession is " + self.name
        print(color.CYAN + text)

        text = "Your profession description is '" + self.story + "'"
        print(text)

        if self.bonus_damage > 0:
            text = "Your current attack bonus = +" + str(self.bonus_damage) + " damage each hit"
        elif self.bonus_damage == 0:
            text = "You don't have any active attack bonuses"
        else:
            text = "Your current attack bonus is negative so you deal " + str(
                abs(self.bonus_damage)) + " less damage each hit"
        print(text)

        if self.bonus_healing > 0:
            text = "Your current healing bonus = +" + str(self.bonus_healing) + " hp each time you heal"
        elif self.bonus_healing == 0:
            text = "You don't have any active healing bonuses"
        else:
            text = "Your current healing bonus is negative so you make " + str(
                abs(self.bonus_healing)) + " less hp each time you heal"
        print(text)

        text = "Your max heath is " + str(self.max_health)
        print(text)

        text = "Your current heath is " + str(self.current_health)
        print(text)

        text = "You block " + str(self.damage_resist) + " damage each time someone hits you"
        print(text)

        text = "You have " + str(self.money) + " money"
        print(text)

        if self.life_elixir == 1:
            text = "You have " + str(self.life_elixir) + " life"
        else:
            text = "You have " + str(self.life_elixir) + " lives"
        print(text)

        text = "You can get out of combat " + str(self.invisibility_powder) + " times"
        print(text)

        if self.can_use_shop:
            text = "You can buy goods from shop"
        else:
            text = "You can't buy goods from shop"
        print(text)

        text = "You heal for " + str(self.lifesteal * 100) + "% of damage dealt"
        print(text)

        text = "You have " + str(self.critical_chance * 100) + "% chance to deal double damage"
        print(text)

        text = "You have killed " + str(self.enemies_killed) + " enemies"
        print(text + color.END)

    def print_battle_stats(self):
        if self.bonus_damage > 0:
            text = "Your current attack bonus = +" + str(self.bonus_damage) + " damage each hit"
        elif self.bonus_damage == 0:
            text = "You don't have any active attack bonuses"
        else:
            text = "Your current attack bonus is negative so you deal " + str(
                self.bonus_damage) + " less damage each hit"
        print(color.CYAN + text)

        if self.bonus_healing > 0:
            text = "Your current healing bonus = +" + str(self.bonus_healing) + " hp each time you heal"
        elif self.bonus_healing == 0:
            text = "You don't have any active healing bonuses"
        else:
            text = "Your current healing bonus is negative so you make " + str(
                self.bonus_healing) + " less hp each time you heal"
        print(text)

        text = "Your max heath is " + str(self.max_health)
        print(text)

        text = "Your current heath is " + str(self.current_health)
        print(text)

        text = "You block " + str(self.damage_resist) + " damage each time someone hits you"
        print(text)

        if self.life_elixir == 1:
            text = "You have " + str(self.life_elixir) + " life"
        else:
            text = "You have " + str(self.life_elixir) + " lives"
        print(text)

        text = "You can get out of combat " + str(self.invisibility_powder) + " times"
        print(text)

        text = "You heal for " + str(self.lifesteal * 100) + "% of damage dealt"
        print(text)

        text = "You have " + str(self.critical_chance * 100) + "% chance to deal double damage"
        print(text + color.END)
