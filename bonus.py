import stats as s

# This made to help me with items and mob bonuses
# Strings are made of substrings
# Substrings have 2 parts : |<Name>|<value>|
# actually i think its better to use tables in this case but it is my first project so i want to make it simple

test_string = "|NAME|Huge|TYPE|BUFF|DESC|Big and Strong|HPM|*2|HPC|*2|APB|*2|"


def get_stats_from_string(input_string):
    string = input_string
    stats_dict = {}
    blocks = (string.count('|') - 1) / 2
    for i in (1, blocks):
        pos1 = string.find('|')
        pos2 = string.find('|', pos1)
        pos3 = string.find('|', pos2)
        name_string = string[pos1 + 1:pos2 - 1]
        value_string = string[pos2 + 1:pos3 - 1]
        stats_dict[name_string] = value_string
        string = string[pos3:]

    return stats_dict


def make_stats_sting(stats_dict):
    string = '|'
    for key in stats_dict:
        string = string + key + stats_dict[key] + '|'

    return string


def enemy_add_bonus(enemy, string):
    stats_dict = get_stats_from_string(string)
    for key in stats_dict:
        if key not in ('NAME', 'DESC', 'TYPE'):
            enemy[key] = calculate(enemy[key], stats_dict[key])


def player_add_bonus(player, string):
    stats_dict = get_stats_from_string(string)
    for key in stats_dict:
        if key not in ('NAME', 'DESC', 'TYPE'):
            player[key] = calculate(player[key], stats_dict[key])


def calculate(pre, string):
    if string[0] == '+':
        post = pre + int(string[1:])
    elif string[0] == '-':
        post = pre - int(string[1:])
    elif string[0] == '*':
        post = pre * int(string[1:])
    elif string[0] == '/':
        post = pre // int(string[1:])

    return post
