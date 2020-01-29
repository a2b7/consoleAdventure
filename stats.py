import dicts as d
import random as r

# Stats now are:
# HPC - Health Points Current
# HPM - Health Points Max
# APB - Attack Power Bonus
# BLC - Block
# HLB - Healing Bonus
# VMP - Vampiric Effect
# CRT - Crit Chance
# EVN - Evasion
# ACC - Accuracy

color = d.Color

dict_class = d.Dicts


class Class:
    name = ""
    description = ""
    bonus_damage = 0
    bonus_healing = 0
    max_health = 0
    current_health = 0
    damage_resist = 0
    money = 0
    life_elixir = 0
    invisibility_powder = 0
    can_use_shop = False
    vampiric = 0.0
    critical_chance = 0.0
    enemies_killed = 0

    def __init__(self, name, profession=dict_class.profession):
        self.name = profession.get(name)['NAME']
        self.description = profession.get(name)['DESC']
        self.bonus_damage = profession.get(name)['APB']
        self.bonus_healing = profession.get(name)['HLB']
        self.max_health = profession.get(name)['HPM']
        self.current_health = profession.get(name)['HPM']
        self.damage_resist = profession.get(name)['BLC']
        self.money = profession.get(name)['money']
        self.life_elixir = profession.get(name)['elixirLife']
        self.invisibility_powder = profession.get(name)['powderInvisibility']
        self.can_use_shop = profession.get(name)['shopUser']
        self.vampiric = profession.get(name)['VMP']
        self.critical_chance = profession.get(name)['CRT']
        self.enemies_killed = 0

    def get_info(self):
        return {
            "NAME": self.name,
            "DESC": self.description,
            "APB": self.bonus_damage,
            "HLB": self.bonus_healing,
            "HPM": self.max_health,
            "BLC": self.damage_resist,
            "money": self.money,
            "elixirLife": self.life_elixir,
            "powderInvisibility": self.invisibility_powder,
            "shopUser": self.can_use_shop,
            "VMP": self.vampiric,
            "CRT": self.critical_chance,
            "enemies killed": self.enemies_killed
        }

    def print_stats(self):
        text = "Your profession is " + self.name
        print(color.CYAN + text)

        text = "Your profession description is '" + self.description + "'"
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

        text = "Your max health is " + str(self.max_health)
        print(text)

        text = "Your current health is " + str(self.current_health)
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

        text = "You heal for " + str(self.vampiric * 100) + "% of damage dealt"
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

        text = "Your max health is " + str(self.max_health)
        print(text)

        text = "Your current health is " + str(self.current_health)
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

        text = "You heal for " + str(self.vampiric * 100) + "% of damage dealt"
        print(text)

        text = "You have " + str(self.critical_chance * 100) + "% chance to deal double damage"
        print(text + color.END)


class Enemy:

    def __init__(self, enemies_killed, dict=dict_class):
        state = r.sample(dict.states, 1)[0]
        if enemies_killed <= 15:
            self.name = state + ' ' + r.sample(dict.names_grade1, 1)[0]
            tier = 1
        elif enemies_killed <= 30:
            self.name = state + ' ' + r.sample(dict.names_grade2, 1)[0]
            tier = 2
        elif enemies_killed <= 45:
            self.name = state + ' ' + r.sample(dict.names_grade3, 1)[0]
            tier = 3
        elif enemies_killed <= 60:
            self.name = state + ' ' + r.sample(dict.names_grade4, 1)[0]
            tier = 4
        elif enemies_killed <= 75:
            self.name = state + ' ' + r.sample(dict.names_grade5, 1)[0]
            tier = 5
        elif enemies_killed <= 90:
            self.name = state + ' ' + r.sample(dict.names_grade6, 1)[0]
            tier = 6
        else:
            self.name = state + ' ' + r.sample(dict.names_grade7, 1)[0]
            tier = 7
        self.max_health = r.randint(15 * (tier - 1) + 1, 15 * tier)
        self.current_health = self.max_health
        self.attack = r.randint(2 * tier - 1, 2 * tier)
        if tier <= 4:
            self.first = 0
        else:
            self.first = r.randint(0, 1)

        self.tier = tier

        text = str(r.sample(dict.messages, 1)[0].replace('%enemy%', self.name))
        text = text.replace('%current_health%', str(self.current_health))
        text = text.replace('%attack%', str(self.attack) + '-' + str(
            self.attack + self.tier))
        self.start_message = text
