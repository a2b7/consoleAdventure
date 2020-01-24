import dicts

color = dicts.Color


def start():
    print(color.GREEN_BOLD + "There are everything you need to know:" + color.END)
    print(color.GREEN + "You are always in the middle of your own world" + color.END)
    print(
        color.GREEN + "That means you can't be anywhere except at the middle, but you can rotate world around you" + color.END)
    print(
        color.GREEN + "There is merchant in any zone, he only needs your money and have infinite supply of life elixirs and invisibility powders" + color.END)
    print(color.GREEN + "There are enemies in most zones" + color.END)
    print()

    print(color.GREEN + "There are basic rules you can count on any time:" + color.END)
    basics()


def basics():
    zone()
    shop()
    battle()
    enemy()
    print(
        color.GREEN_BOLD + "Remember, you can try to get help by writing 'help', or check your stats by writing 'stats' in any situation" + color.END)
    print()


def zone():
    print(color.GREEN + "Write 'north' to slightly move your world south" + color.END)
    print(color.GREEN + "Write 'south' to slightly move your world north" + color.END)
    print(color.GREEN + "Write 'east' to slightly move your world west" + color.END)
    print(color.GREEN + "Write 'west' to slightly move your world east" + color.END)
    print(
        color.GREEN + "You can't go back, because world is always changing, so even if you use 'north' then 'south' you will come into new zone" + color.END)
    print()

    print(color.GREEN + "When you move, your zone changes so you have to face new enemy with new loot" + color.END)
    print(color.GREEN + "There are 3 types of zone:" + color.END)
    print(color.GREEN + "boring outside with monster and nothing else" + color.END)
    print(color.GREEN + "unusual outside with some kind of activity" + color.END)
    print(color.GREEN + "zone, important for story" + color.END)
    print()

    print(color.GREEN + "Write 'shop' when out of combat to enter shop" + color.END)
    print()


def shop():
    print(
        color.GREEN + "Write 'life' to buy life elixir which can be used to have 1 more chance to not fail your adventure" + color.END)
    print(color.GREEN + "Write 'invis' to buy invisibility powder which can be used to skip combat" + color.END)
    print(color.GREEN + "You can try to learn merchant story by politely asking him to 'tell' his 'story'" + color.END)
    print()


def battle():
    print(color.GREEN + "You start battle with your health points maxed" + color.END)
    print(color.GREEN + "Battle is turn based, each turn you hit or heal, your enemy hit" + color.END)
    print(
        color.GREEN + "It starts with your turn unless enemy is very fast (any mob faster than you is very fast, you're mob owner, remember?)" + color.END)
    print()

    print(color.GREEN + "Write 'hit' to hit your enemy" + color.END)
    print(color.GREEN + "You hit enemy for random amount from 1 to 6 plus your bonus damage" + color.END)
    print(color.GREEN + "Write 'heal' to heal your wounds" + color.END)
    print(color.GREEN + "You heal yourself for random amount from 1 to 6 plus your bonus healing" + color.END)
    print(color.GREEN + "Write 'run' to run from combat" + color.END)
    print(color.GREEN + "You lose 1 invisibility powder and your enemy disappear without dropping any loot" + color.END)
    print(color.GREEN + "Write 'suicide' to die and res with full hp is you have any backup lives" + color.END)
    print(color.GREEN + "You lose 1 life if you have any and are healed to full life" + color.END)
    print()

    print(color.GREEN + "You can get your battle stats by writing 'battle stats'" + color.END)

    print()


def enemy():
    print(
        color.GREEN + "Actually they enemies are pretty simple, you hit them until they have 0 health or less, they die, you get loot" + color.END)
    print(
        color.GREEN + "Current enemy has health, attack power and relative speed (slower or faster than you)" + color.END)
    print(
        color.GREEN + "Any other enemy doesnt have anything because most of NPCs only exist when you face them" + color.END)
    print()
