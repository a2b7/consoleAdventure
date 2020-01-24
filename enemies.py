import random as r
import dicts as d


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    GREEN_BOLD = '\033[92;1m'


dict = d.Dicts


class Enemy:

    def __init__(self, enemies_killed, dict=dict):
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

    def print_stats(self):
        text = str(self.name) + ' having ' + str(self.current_health) + ' HP and ' + str(self.attack) + '-' + str(
            self.attack + self.tier) + ' attack power'
        print(Color.RED + text + Color.END)
