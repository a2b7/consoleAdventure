import stats as p
import enemies as e
import random as r
import help as h
import dicts

color = dicts.Color

player = p.Class("priest")
enemy = e.Enemy(0)
battle_ended = False


def player_turn():
    command = 'battle_stats'
    while command not in ('hit', 'heal', 'run'):
        command = input(
            color.BOLD + "What do you want to do? You can 'hit', 'heal' or 'run' away (if you have invisibility powder)\n" + color.END)
        if command.lower() == 'help':
            h.battle()
            h.enemy()
        elif command == 'run':
            if player.invisibility_powder > 0:
                flee()
            else:
                print(
                    color.BOLD + "Sorry, but you can not run because you don't have any invisibility powder left and you lost your entire turn looking for chance to flee" + color.END)
        elif command == 'hit':
            hit()
        elif command == 'heal':
            heal()
        elif command.lower() == 'stats':
            player.print_stats()
        elif command.lower() == 'battle stats':
            player.print_battle_stats()
        else:
            print(color.BOLD + "Sorry i can't understand command '" + command + "', try again please" + color.END)


def battle_flow(enemies_killed, current_player):
    global battle_ended

    battle_ended = False
    get_enemy(enemies_killed)
    your_starting_stats(current_player)

    if enemy.first:
        print(
            color.BOLD + "Your enemy is extremely fast so you're the second one who can make move in battle round" + color.END)
    else:
        print(color.BOLD + "Your enemy is not fast enough so you make the first move each round" + color.END)

    while not battle_ended:
        if enemy.first:
            get_hitted()
            if player.current_health > 0:
                player_turn()
        else:
            player_turn()
            if enemy.current_health > 0:
                get_hitted()


def get_enemy(enemies_killed):
    global enemy

    enemy = e.Enemy(enemies_killed)
    print(color.RED + enemy.start_message + color.END)


def your_starting_stats(current_player):
    global player

    player = current_player
    player.current_health = player.max_health
    if player.name == 'Priest':
        player.life_elixir = player.life_elixir + 1
    elif player.name == 'Rogue':
        player.invisibility_powder = 1
    elif player.name == 'DeathKnight':
        player.life_elixir = 1000000
    elif player.name == 'Monk':
        player.bonus_damage = player.money // 100
        player.damage_resist = player.money // 100
    elif player.name == 'Wizard':
        player.life_elixir = 1

    player.print_battle_stats()


def hit():
    global player
    global enemy
    global battle_ended

    hit_power = r.randint(1, 6)
    actual_hit = hit_power + player.bonus_damage
    if actual_hit < 0:
        actual_hit = 0
    enemy.current_health = enemy.current_health - actual_hit
    print(color.GREEN_ITALIC + 'You hit enemy for ' + str(actual_hit) + '  (' + str(
        hit_power) + ' hit and ' + str(
        player.bonus_damage) + ' bonus ) damage' + color.END)
    if r.randint(1, 100) < (player.critical_chance * 100):
        enemy.current_health = enemy.current_health - actual_hit
        print(color.GREEN_ITALIC_UNDERLINE + 'Critical!' + color.END)
        print(color.GREEN_ITALIC + 'You hit enemy for ' + str(actual_hit) + '  (' + str(
            hit_power) + ' hit and ' + str(
            player.bonus_damage) + ' bonus ) damage' + color.END)
    if enemy.current_health <= 0:
        enemy.current_health = 0

    if player.current_health < player.max_health:
        lifesteal_value = round(actual_hit * player.lifesteal)
        print(color.GREEN_ITALIC + 'You got ' + str(lifesteal_value) + ' HP because of your lifesteal powers')
        player.current_health = player.current_health + lifesteal_value
        if player.current_health > player.max_health:
            player.current_health = player.max_health
            print(color.GREEN_ITALIC + "Your health can't exceed maximum so we adjusted values (^_^)" + color.END)
        print(color.GREEN_ITALIC + "You now have " + str(player.current_health) + " HP" + color.END)

    print(color.RED_ITALIC + 'Your enemy now have ' + str(enemy.current_health) + ' HP left' + color.END)

    if enemy.current_health == 0:
        win()


def get_hitted():
    global player
    global enemy
    global battle_ended

    hitted = r.randint(enemy.attack, enemy.attack + enemy.tier) - player.damage_resist
    if hitted > 0:
        player.current_health = player.current_health - hitted
        print(color.RED_ITALIC + 'Enemy hit you for ' + str(
            r.randint(enemy.attack, enemy.attack + enemy.tier)) + ' damage and you blocked ' + str(
            player.damage_resist) + ' damage' + color.END)
    else:
        player.current_health = player.current_health - 1
        print(color.RED_ITALIC + 'Enemy hit you for ' + str(enemy.attack) + ' damage and you blocked ' + str(
            player.damage_resist) + ' damage, but you can not completely avoid all damage from hit so you have been hitted for 1 damage' + color.END)

    if player.current_health <= 0:
        if player.life_elixir > 0:
            player.life_elixir = player.life_elixir - 1
            player.current_health = player.max_health
            print(color.RED_ITALIC + "You've lost 1 life and now have " + str(
                player.life_elixir) + ' lives left' + color.END)
        else:
            player.current_health = 0
            print(color.RED_ITALIC + "You don't have any more attempts" + color.END)
            battle_ended = True

    print(color.RED_ITALIC + 'You now have ' + str(player.current_health) + ' HP left' + color.END)


def heal():
    global player

    heal_power = r.randint(0, 6)
    player.current_health = player.current_health + heal_power + player.bonus_healing
    print(color.GREEN_ITALIC + 'You heal yourself for ' + str(heal_power) + ' HP + ' + str(
        player.bonus_healing) + ' HP from healing bonus you have' + color.END)
    if player.current_health > player.max_health:
        player.current_health = player.max_health
        print(
            color.GREEN_ITALIC + "Actually you're so good at healing your HP exceeded maximum HP so we had to lower your health to it's maximum" + color.END)
    print(color.GREEN_ITALIC + 'You now have ' + str(player.current_health) + ' HP left' + color.END)


def flee():
    global player
    global battle_ended

    player.current_health = player.max_health
    player.invisibility_powder = player.invisibility_powder - 1
    battle_ended = True


def win():
    global battle_ended

    player.current_health = player.max_health
    loot_money = (enemy.tier - 1) * 37 + r.randint(0, 36)
    player.money = player.money + loot_money
    player.enemies_killed = player.enemies_killed + 1
    print(color.GREEN + "You have won, nice, now you've killed " + str(player.enemies_killed) + ' enemies already' + color.END)
    print(color.YELLOW + 'You got ' + str(loot_money) + ' money from ' + enemy.name + ' corpse' + color.END)
    battle_ended = True
