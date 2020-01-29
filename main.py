import stats as s
import help as h
import battle as b
import enemies as e
import dicts as d
import random as r
import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


color = d.Color


adventure_ended = False
dict_class = d.Dicts
'''
---------------------------
--------start phase--------
------pick profession------  
---------------------------
'''
shop_interaction_count = 0
not_global_command = False
player_name = input(color.BOLD + "Hello, you name is?\n" + color.END)
print("Nice to meet you, " + str(player_name))
print("We have these classes to choose:")
for key, value in dict_class.profession.items():
    print(color.UNDERLINE + str(key) + color.END)
command = ''
player_class_name = ''
continue_flag = False
while not continue_flag:
    command = input(color.BOLD + "What class do you want to know about?\n" + color.END)
    try:
        print(dict_class.profession[command]["story"])
        player_class_name = command
        continue_flag = True
    except KeyError:
        print("There is no such command or class, lets try again")
        continue_flag = False

continue_flag = False
while not continue_flag and command != 'this':
    command = input(color.BOLD +
                    "If you want to be " + player_class_name + " write 'this', otherwise write class you want to know about\n" + color.END)
    try:
        print(dict_class.profession[command]["story"])
        player_class_name = command
        continue_flag = False
    except KeyError:
        if command != 'this':
            print("There is no such command or class, lets try again")
        continue_flag = False
player = s.Class(player_class_name)
print("Nice, these are you stats now")
player.print_stats()
print()

'''
---------------------------
---------tutorial----------
-------learn basics--------  
---------------------------
'''
h.start()

print('Do you know what to do? Neither do i. I think you should ask yourself who can help you')
continue_flag = False
while not continue_flag:
    command = input(color.BOLD + "Who do you think can help?\n" + color.END)
    if command == 'help':
        command = input(
            color.BOLD + "If you want to reread help, write 'yes', if you think it is something named 'help' can help you, write 'yes, of course', if it is just a typo, write anything to continue\n" + color.END)
        if command == 'yes':
            h.basics()
        elif command == 'yes, of course':
            helper_name = 'help'
            print("Okay, let's find something named " + helper_name +
                  ' to get help')
            continue_flag = True
    else:
        helper_name = command
        print("Okay, let's find " + helper_name + ' to get help')
        continue_flag = True

count = 0
zone_count = 1000
while count <= zone_count and not adventure_ended:
    count = count + 1
    command = input(color.BOLD + "So, where do you want to move your world?\n" + color.END)
    if command in ('south', 'west', 'east', 'north'):
        print('You moved your world ' + command)
        if r.randint(0, 100) >= 90:
            print("Now you're in special zone")
            print(color.RED_BOLD_UNDERLINE + 'reminder:make special zones' + color.END)
        else:
            print('Now you got to ' + r.sample(dict_class.zones, 1)[0])
            b.battle_flow(player.enemies_killed, player)
    elif command.lower() == 'help':
        h.zone()
        count = count - 1
    elif command.lower() == 'stats':
        player.print_stats()
    else:
        print('You can not do ' + command + ', try again please.')
        count = count - 1
